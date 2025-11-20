import json
import os
from typing import List
from openai import OpenAI

from .skill_store import set_role_skills

# Initialize client using env variable OPENAI_API_KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_skills_for_role(role: str) -> List[str]:
    """
    Use an LLM to generate a list of core skills for a given role.
    Example roles: 'Software Engineer', 'Database Administrator'.
    """

    prompt = f"""
    Generate a list of 40 to 60 essential skills for the job role: "{role}".
    Include:
    - core technical skills
    - languages and frameworks
    - cloud / infra skills
    - system design or architecture skills
    - tools / platforms
    - relevant soft skills

    Return ONLY a valid JSON array like:
    ["skill1", "skill2", ...]
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    content = response.choices[0].message.content

    # Try parsing JSON
    try:
        skills = json.loads(content)
    except Exception:
        # fallback: parse lines
        skills = [
            line.strip(" -•\t").lower()
            for line in content.splitlines()
            if len(line.strip()) > 2
        ]

    # Clean duplicates + normalize
    skills = [s.lower().strip() for s in skills if s.strip()]
    unique_skills = sorted(list(set(skills)))

    return unique_skills


def build_role_skills(role: str) -> List[str]:
    """
    High-level function:
    - Generate skills using LLM
    - Store them into skills_db.json
    - Return the list
    """
    skills = generate_skills_for_role(role)
    set_role_skills(role, skills)
    return skills
