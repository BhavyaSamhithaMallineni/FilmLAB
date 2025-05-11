import re

def is_scene_heading(line):
    return re.match(r"^(INT\.|EXT\.).*", line.strip().upper()) is not None

def is_character_name(line):
    return re.match(r"^[A-Z ]{3,30}$", line.strip()) is not None and not line.strip().startswith(("INT", "EXT"))

def is_parenthetical(line):
    return re.match(r"^\(.*\)$", line.strip()) is not None

def is_dialogue(line):
    return len(line.strip()) > 0 and not is_scene_heading(line) and not is_character_name(line) and not is_parenthetical(line)

def run_format_checker(lines):
    issues = []
    for i, line in enumerate(lines):
        # Scene Heading issues
        if is_scene_heading(line):
            if line != line.upper():
                issues.append((i+1, "Scene heading should be in ALL CAPS."))
            if not line.startswith(("INT.", "EXT.")):
                issues.append((i+1, "Scene heading should start with 'INT.' or 'EXT.'"))

        # Character name formatting
        if is_character_name(line):
            if line != line.upper():
                issues.append((i+1, "Character name should be in ALL CAPS."))
        
        # Detect all caps but not scene heading or character name
        if line.isupper() and not is_scene_heading(line) and not is_character_name(line):
            if len(line.split()) > 4:
                issues.append((i+1, "Possible shouting or misformatted action block in ALL CAPS."))

        # Long action lines
        if not is_scene_heading(line) and not is_character_name(line):
            if len(line) > 120:
                issues.append((i+1, "Action line is too long. Consider splitting."))
                
    return issues