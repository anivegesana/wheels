import glob, hashlib, sys, os

def sha256(filename):
    # https://www.quickprogrammingtips.com/python/how-to-calculate-sha256-hash-of-a-file-in-python.html
    # Python program to find SHA256 hash string of a file
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def hash(file):
    if os.path.isdir(file):
        return ""
    else:
        return f"#sha256={sha256(file)}"

for folder in glob.glob('**/', recursive=True):
    names = [f'<li><a href="{file}{hash(os.path.join(folder, file))}">{file}</a></li>\n' for file in os.listdir(folder) if file != 'index.html']
    with open(os.path.join(folder, 'index.html'), 'w') as index:
        index.write("""<!DOCTYPE html>
<html>
<body>
<ul>
""")
        index.writelines(names)
        index.write("""</ul>
</body>
</html>""")
