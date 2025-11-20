import json
from pathlib import Path
from typing import Dict, List

# skills_db.json lives in backend/skills_db.json
DB_PATH = Path(__file__).resolve().parent.parent / "skills_db.json"


def _load_db() -> Dict[str, List[str]]:
    if not DB_PATH.exists():
        return {}
    with DB_PATH.open("r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def _save_db(db: Dict[str, List[str]]) -> None:
    with DB_PATH.open("w") as f:
        json.dump(db, f, indent=4)


def _role_key(role: str) -> str:
    return role.strip().lower().replace(" ", "_")


def get_role_skills(role: str) -> List[str]:
    """Return skills list for a given role, or empty list."""
    db = _load_db()
    return db.get(_role_key(role), [])


def set_role_skills(role: str, skills: List[str]) -> None:
    """Overwrite / create skills for a role."""
    db = _load_db()
    key = _role_key(role)
    # normalize skills
    norm = sorted({s.strip().lower() for s in skills if s.strip()})
    db[key] = norm
    _save_db(db)


def get_all_skills() -> List[str]:
    """Union of all skills across all roles."""
    db = _load_db()
    all_skills = set()
    for skills in db.values():
        all_skills.update(s.strip().lower() for s in skills)
    return sorted(all_skills)
