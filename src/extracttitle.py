

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line[:2] == "# ":
            return line[2:].strip()
    raise Exception("no h1 header found")
    
