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
    pageId = 'Welcome'
    description = '''  <p style = "margin-top: 40px;">안녕하세요 <strong>정현우</strong>가 만든 <u>Web</u> 페이지입니다.
      저는 숭실대 AI융합학부에 재학 중입니다.</p> <p style = "margin-top: 40px;">저는 머신러닝과 데이터 분석에 관해 흥미를 가지고 있습니다.
      이를 위해 지금 GDSC에서 활동하고 있습니다. 이 사이트는 제가 취미로써 만드는 것입니다.
      때문에 그렇게까지 퀄리티가 높을 것이라고 생각하지 않습니다.</p>
      <p style = "margin-top: 40px;">또 저는 취미로 그림을 그리고 있습니다. 그림도 그다지 잘 그리지는 않습니다만 열심히 그리는 타입입니다.
      중학생 시절에 만화를 너무 좋아해서 그 만화에 나오는 캐릭터들을 그리고 싶어서 그림을 그리기 시작했습니다.
      중학교 3학년에는 하루종일 그림을 그려서 졸라맨만 그리던 제가 사람을 그리게 되었습니다. 고등학생 때는 잠깐
      그림을 멈추고 올해 들어서 그림을 다시 그리고 있습니다. </p>
      <img src="image.jpeg" width="30%">
      <h4>방학 중에 내가 해야 할 것들</h4>
      <p>프로그래머들은 방학에 놀면 안 됩니다. 꾸준히 공부해야 하고 새로운 것을 계속해서 알아가야 합니다.
      때문에 프로그래머들에게 있어서 계획이라고 하는 것은 중요하다고 생각합니다. 따라서 저는 아래에 제가 방학 중에 해야
      할 것들의 목록을 써 보겠습니다.</p>
      <ul>
        <li>데이터 분석 공부</li>
          <ul>
            <li>시립대에서 해주는 교육 꾸준히 참석하기</li>
            <li>배운 내용 복습하고 깃허브에 꾸준히 올리기</li>
          </ul>
        <li>머신러닝 공부</li>
          <ul>
            <li>알고리즘 추천 프로그램 만들어보기</li>
            <li>앤드류 응 교수의 강의 학습 및 복습하기</li>
          </ul>
        <li>웹 공부</li>
          <ul>
            <li>생활코딩 사이트 하루에 하나의 인덱스씩 공부하기</li>
          </ul>
      </ul>
      <p>또 저는 블로그를 운영하고 있습니다. 블로그에는 주로 알로리즘을 어떻게 푸는지에 관한 내용을 올리고 있습니다.
      학교를 다니게 되면서 블로그를 쉬었고 보는 사람도 없어서 의욕도 떨어졌지만 많은 사람이 보고 공부할 수 있는 블로그를
      만드는 것도 저의 목표 중 하나입니다. 다음은 제 블로그의 링크 입니다.
      <a href="https://jung0228.tistory.com/" target="_blank" title="html5 specification">정현우의 코딩블로그</a></p>'''




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
</body>
</html>""".format(title=pageId, desc = description, listStr=listStr))
