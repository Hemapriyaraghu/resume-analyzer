import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills import SKILLS


def find_skills(text):
    text = text.lower()
    found = set()
    for skill in SKILLS:
        pattern = r"(?<![a-z0-9+#])" + re.escape(skill) + r"(?![a-z0-9+#])"
        if re.search(pattern, text):
            found.add(skill)
    return found


def text_similarity(resume_text, jd_text):
    try:
        vectors = TfidfVectorizer(stop_words="english").fit_transform([resume_text, jd_text])
    except ValueError:
        return 0.0
    return float(cosine_similarity(vectors[0], vectors[1])[0][0])


def analyze_resume(resume_text, jd_text):
    resume_skills = find_skills(resume_text)
    jd_skills = find_skills(jd_text)

    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills

    similarity = text_similarity(resume_text, jd_text)
    skill_score = len(matched) / len(jd_skills) if jd_skills else 0

    score = round((0.6 * skill_score + 0.4 * similarity) * 100, 1)

    return {
        "match_score": score,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
    }