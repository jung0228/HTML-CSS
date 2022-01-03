#!/Users/jhw/opt/anaconda3/bin/python3
print("content-type:text/html; charset=UTF-8\n")
print()

import cgi, os

files = os.listdir("data")
listStr = ""
for item in files:
    listStr = listStr + '<li><a href="index.py?id={Name}">{Name}</a></li>'.format(Name=item)


form = cgi.FieldStorage()
if "id" in form:
    pageId = form.getvalue("id")
    description = open('data/'+pageId, 'r').read()
else:
    pageId = "Create"
    description = ""




print("""<!doctype html>
<html>
<head>
  <title>WEB 1일차</title>
  <meta charset="utf-8">
  <!-- <h2>소개</h2> -->
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">create</a>
  <h2>{title}</h2>
  <p>{desc}</p>
  <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="제목을 입력하세요!"></p>
      <p><textarea rows="4" name="description"placeholder="설명을 해주세요!"></textarea></p>
      <p><input type="submit"></p>
  </form>
</body>
</html>""".format(title=pageId, desc = description, listStr=listStr))
