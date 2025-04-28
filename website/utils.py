import os
import re

def title_from_slug(slug):
    match = re.search(r'(\d+)', slug)
    if match:
        return f"Lesson {match.group(1)}"
    return slug.replace("_", " ").title()

def categorize_lessons(app):
    folder = os.path.join(app.root_path, "templates", "lessons")
    files = [f for f in os.listdir(folder) if f.endswith(".html")]

    categories = {
        "py": "Python",
        "bash": "Bash",
        "networking": "Networking"
    }

    lesson_data = {}

    for file in files:
        slug = file[:-5]  # remove .html
        prefix = slug.split("_")[0]

        category = categories.get(prefix, "Other")
        if category not in lesson_data:
            lesson_data[category] = []

        lesson_data[category].append({
            "slug": slug,
            "title": title_from_slug(slug)
        })

    for lessons in lesson_data.values():
        lessons.sort(key=lambda l: int(re.search(r'\d+', l["slug"]).group()))

    return lesson_data
