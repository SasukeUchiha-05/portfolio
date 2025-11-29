
import os

file_path = 'c:/Users/91996/Desktop/portfolio/style.css'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Helper to replace a block
def replace_block(lines, start_marker, end_marker, new_content):
    try:
        start_idx = -1
        for i, line in enumerate(lines):
            if start_marker in line:
                start_idx = i
                break
        
        if start_idx == -1:
            print(f"Could not find start marker: {start_marker}")
            return lines

        end_idx = -1
        for i in range(start_idx, len(lines)):
            if end_marker in lines[i]:
                end_idx = i
                break
        
        if end_idx == -1:
            print(f"Could not find end marker: {end_marker}")
            return lines

        # Replace lines
        return lines[:start_idx] + [new_content] + lines[end_idx+1:]
    except Exception as e:
        print(f"Error replacing block: {e}")
        return lines

# 1. Update Hero
hero_new = """/* Hero Section */
.hero {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    text-align: left;
    padding: 0 10%;
    position: relative;
}
"""
# Find .hero { and the closing }
# We'll search for the exact lines to be safe
new_lines = []
skip = False
for line in lines:
    if ".hero {" in line and "height: 100vh;" in lines[lines.index(line)+1]:
        new_lines.append(hero_new)
        skip = True
    elif skip and "}" in line and line.strip() == "}":
        skip = False
    elif not skip:
        new_lines.append(line)

lines = new_lines

# 2. Update CTA Buttons
# We can just replace the .cta-buttons block similarly
cta_new = """.cta-buttons {
    display: flex;
    gap: 3rem;
    animation: fadeInUp 1s ease 0.8s backwards;
}
"""
new_lines = []
skip = False
for line in lines:
    if ".cta-buttons {" in line:
        new_lines.append(cta_new)
        skip = True
    elif skip and "}" in line and line.strip() == "}":
        skip = False
    elif not skip:
        new_lines.append(line)

lines = new_lines

# 3. Update Highlight
highlight_new = """.highlight {
    background: linear-gradient(to right, var(--primary-color), var(--accent-color), var(--primary-color));
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 3s linear infinite;
}

@keyframes shimmer {
    to {
        background-position: 200% center;
    }
}
"""
new_lines = []
skip = False
for line in lines:
    if ".highlight {" in line:
        new_lines.append(highlight_new)
        skip = True
    elif skip and "}" in line and line.strip() == "}":
        skip = False
    elif not skip:
        new_lines.append(line)

lines = new_lines

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("CSS updated successfully.")
