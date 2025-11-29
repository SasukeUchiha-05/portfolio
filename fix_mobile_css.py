
import os

file_path = 'c:/Users/91996/Desktop/portfolio/style.css'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# We need to find the @media (max-width: 480px) block and update the .cta-buttons and .hero styles inside it.
# Or append them if they don't exist fully.

# Let's construct the new content for the 480px media query.
media_query_start = "@media (max-width: 480px) {"
new_media_content = """@media (max-width: 480px) {
    .name {
        font-size: 2rem;
    }

    .title {
        font-size: 1.2rem;
    }

    .hero {
        align-items: center;
        text-align: center;
        padding: 0 5%;
    }

    .btn {
        padding: 0.8rem 2rem;
        width: 100%;
        text-align: center;
    }

    .cta-buttons {
        flex-direction: column;
        width: 100%;
        gap: 1rem;
    }
}
"""

# Find where the media query starts
start_idx = -1
for i, line in enumerate(lines):
    if media_query_start in line:
        start_idx = i
        break

if start_idx != -1:
    # Replace from start_idx to the end of the file (assuming it's the last block)
    # This is a bit risky if there's content after, but usually it's at the end.
    # Let's check if there are closing braces.
    # A safer way is to just replace the whole block if we can identify the end.
    # Given the previous view, it was at the end.
    lines = lines[:start_idx] + [new_media_content]
else:
    # Append if not found (unlikely)
    lines.append("\n" + new_media_content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Mobile CSS updated.")
