import os
import glob
import yaml
import json

# Set the path to ../modules/ relative to the location of the script
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "modules")

# Define the role to slug mapping
role_mapping = {
    "Investigator": "investigator",
    "Research Leaders": "research-leader",
    "Informaticist": "informaticist",
    "Software Engineer": "software-engineer",
    "Clinician Scientist/Trainee": "clinician-scientist"
}

# Define the role module map
role_module_map = []

# Load data from _quarto.yml sidebar
#sidebar = None;
#with open(os.path.join(path, '..', '_quarto.yml'), 'r') as f:
#    quarto_data = yaml.safe_load(f.read().strip());
#    sidebar = quarto_data['website']['sidebar']

#print(str(quarto_data['website']['sidebar'][0]))

# Extract data
#for item in sidebar:
#    if isinstance(item, str): # direct link item
#        pass # save order, extract title from frontmatter
#    elif isinstance(item, dict) and item.has_key?('text'):
#        pass # save order and title
#    elif isinstance(item, dict) and item.has_key?('contents'):
#        pass # recurse
#    else:
#        pass


# Loop through each Markdown file in the path
for filename in glob.glob(os.path.join(path, "*.qmd")):
    with open(filename, "r") as f:
        # Read the file content
        content = f.read()

        # Parse the YAML frontmatter
        _, frontmatter, markdown = content.split("---", 2)
        frontmatter = yaml.safe_load(frontmatter.strip())

        # Extract the roles from the frontmatter
        roles = frontmatter.get("roles")

        # If the roles exist, add the filename to the corresponding role in the role module map
        if roles:
            for role in roles:
                role_slug = role_mapping.get(role)
                if role_slug:
                    existing_role = next(
                        (r for r in role_module_map if r["role"] == role_slug),
                        None)
                    if existing_role:
                        existing_role["modules"].append(os.path.splitext(os.path.basename(filename))[0])
                    else:
                        role_module_map.append({
                            "role":
                            role_slug,
                            "modules":
                            [os.path.splitext(os.path.basename(filename))[0]]
                        })

# Sort the role module map by role
role_module_map = sorted(role_module_map, key=lambda r: r["role"])


# Convert the role module map to a JavaScript variable
js_var = "const role_module_map = " + json.dumps(role_module_map, indent=2) + ";"

# Write the JavaScript variable to mappings.js
with open(os.path.join(path, "mappings.js"), "w") as f:
    f.write(js_var)
