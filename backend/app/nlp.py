import re
from typing import List, Dict, Optional

from .skill_store import get_role_skills, get_all_skills


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def extract_skills_from_text(
    text: str,
    candidate_skills: Optional[List[str]] = None,
) -> List[str]:
    """
    Extract skills from text by matching against a catalog of skills.

    - candidate_skills: List of skills to search for (e.g., role-specific list).
      If None, we use union of all skills from skills_db.json.
    """
    norm_text = _normalize(text)

    if candidate_skills is None:
        candidate_skills = get_all_skills()

    found = set()
    for skill in candidate_skills:
        s = skill.lower().strip()
        if not s:
            continue
        # simple substring match; can be improved with fuzzy or regex
        if s in norm_text:
            found.add(s)

    return sorted(found)


def score_match(
    target_skills: List[str],
    resume_skills: List[str],
) -> Dict:
    """
    Compute match metrics:
    - target_skills: what the JD/role expects
    - resume_skills: what we detected in the resume
    """
    target = set(s.lower() for s in target_skills)
    res = set(s.lower() for s in resume_skills)

    matched = sorted(target & res)
    missing = sorted(target - res)
    extra = sorted(res - target)

    match_score = round((len(matched) / len(target) * 100), 2) if target else 0.0

    return {
        "match_score": match_score,
        "matched_keywords": matched,
        "missing_keywords": missing,
        "extra_keywords_in_resume": extra,
        "total_jd_keywords": len(target),
        "total_resume_keywords": len(res),
    }


def build_skill_targets_for_role_and_jd(role: str, jd_text: str) -> Dict[str, List[str]]:
    """
    Helper:
    - load skills for role from the DB (LLM-generated)
    - extract those skills that are explicitly mentioned in the JD
    - build combined target skill set = union of {role_skills, jd_explicit_skills}
    """
    role_skills = get_role_skills(role)
    # skills that appear in JD (filtered from role skills universe)
    jd_skills = extract_skills_from_text(jd_text, candidate_skills=role_skills or None)

    combined = sorted({*role_skills, *jd_skills})
    return {
        "role_skills": sorted(role_skills),
        "jd_skills": sorted(jd_skills),
        "combined_skills": combined,
    }
