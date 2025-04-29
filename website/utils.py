import os
import re

def title_from_slug(slug):
    match = re.search(r'(\d+)', slug)
    if match:
        return f"Lesson {match.group(1)}"
    return slug.replace("_", " ").title()

def categorize_lessons(app):
    lesson_dir = os.path.join(app.root_path, "templates", "lessons")
    categories = {}
    
    # Map folder names to display names
    folder_map = {
        "python": "Python",
        "music": "Music Theory",
        "pixel_art": "Pixel Art",
        "precal": "Precalculus",
        "bash": "Bash",
        "networking": "Networking"
    }

    for folder, display_name in folder_map.items():
        category_path = os.path.join(lesson_dir, folder)
        if os.path.exists(category_path):
            lessons = []
            for file in sorted(os.listdir(category_path)):
                if file.endswith(".html"):
                    slug = file[:-5]  # Remove .html
                    title = " ".join([word.capitalize() for word in slug.split("_")])
                    lessons.append({
                        "slug": slug,
                        "title": title,
                        "path": f"lessons/{folder}/{file}"
                    })
            if lessons:
                categories[display_name] = lessons
                
    return categories
