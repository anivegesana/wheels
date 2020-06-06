import sys, os

names = [f'<li><a href="{file}">{file}</a></li>\n' for file in os.listdir(sys.argv[1]) if file != 'index.html']
with open(os.path.join(sys.argv[1], 'index.html'), 'w') as index:
    index.write("""<!DOCTYPE html>
<html>
<body>
<ul>
""")
    index.writelines(names)
    index.write("""</ul>
</body>
</html>""")
