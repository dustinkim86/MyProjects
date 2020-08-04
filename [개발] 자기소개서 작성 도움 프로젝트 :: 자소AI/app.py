from flask import Flask, render_template, request, redirect, session, url_for
import os
import datetime
import re
from flaskext.mysql import MySQL
from flask_restful import Resource, Api, reqparse
from oauth2client.contrib.flask_util import UserOAuth2
from oauth2client.client import OAuth2Credentials
import simplejson as json
from jupyter_generator import main

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['GOOGLE_OAUTH2_CLIENT_ID'] = 'client_id'
app.config['GOOGLE_OAUTH2_CLIENT_SECRET'] = 'client_secret'
oauth2 = UserOAuth2(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'heroku_db'
app.config['MYSQL_DATABASE_HOST'] = 'host'
mysql.init_app(app)
app.secret_key = 'secret_keys'


@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('user_id'):
        return render_template('landing.html')
    else:
        return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
@oauth2.required
def login():
    email = oauth2.email
    user_id = oauth2.user_id
    session['user_id'] = user_id
    session['user_email'] = email
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute('select user_id from user_tb')
    chk_user_id_tuple = cur.fetchall()
    chk_user_id = sum([list(i) for i in chk_user_id_tuple],[])
    if user_id in chk_user_id:
        cur.execute(f'select major from user_tb where user_id="{user_id}"')
        chk_empty = cur.fetchone()[0]
        if chk_empty is None:
            return redirect('/signup')
        return redirect(url_for('writeResume'))
    else:
        cur.execute(f'insert into user_tb (email, user_id) values ("{email}","{user_id}")')
        conn.commit()
        return redirect('/signup')


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    user_id = session['user_id']
    conn = mysql.connect()
    cur = conn.cursor()

    if request.method == 'GET':
        return render_template('signup.html')
    else:
        birthdate = request.form.get('birthdate')
        birthday = birthdate[6:] +'-'+ birthdate[3:5] +'-'+ birthdate[:2]
        gender = request.form.get('gender')
        classes = request.form.get('classes')
        cur.execute(f'''update user_tb set birthdate="{birthday}", gender="{gender}",
            major="{classes}" where user_id="{user_id}"''')
        conn.commit()
        return redirect(url_for('writeResume'))


@app.route('/writeResume', methods=['GET', 'POST'])
def writeResume():
    if not session.get('user_id'):
        return render_template('error.html', msg="로그인 후 이용해 주세요.")
    if request.method == 'GET':
        if not session.get("texts") is None:
            sentences = session['texts']
            return render_template('writeResume.html', sentences=sentences)
        else:
            session['texts'] = "문장 생성을 위해 자기소개서를 작성해 주세요"
            return redirect(url_for('writeResume'))
    else:
        texts = request.form.get('DOC_TEXT')
        session['texts'] = texts
        return redirect(url_for('resumeGen'))


@app.route('/resumeGen', methods=['GET', 'POST'])
def resumeGen():
    if not session.get('user_id'):
        return render_template('error.html', msg="로그인 후 이용해 주세요.")
    if request.method == 'GET':
        if not session.get("texts") is None:
            texts = session['texts']
            if len(texts) > 100:
                return render_template('error.html', msg='입력 문장을 조금 더 짧게 조정해주세요.')
            ctx= 'cpu'
            cachedir='~/kogpt2/'
            load_path = './checkpoint/KoGPT2_checkpoint_277500.tar'
            loops = 6
            sent_dict = main(temperature=1.1, tmp_sent = texts, text_size = len(texts)/2+40, loops = loops, load_path = load_path)
            for key, value in sent_dict.items():
                lst = value.split('.')
                lst_delete_last = lst[:-1]
                lst_to_str = ".".join(lst_delete_last) + "."
                sent_dict[key] = lst_to_str
            return render_template('resumeGen.html', msg=sent_dict)
    else:
        sentences = request.form.get('sentences')
        session['texts'] = sentences        
        return redirect(url_for('writeResume'))


@app.route('/myresume', methods=['GET'])
def myresume():
    if not session.get('user_id'):
        return render_template('error.html', msg="로그인 후 이용해 주세요.")
    conn = mysql.connect()
    cur = conn.cursor()
    email = session['user_email']
    if request.method == 'GET':
        cur.execute(f'select email from resume_tb')
        db_email_tuple = cur.fetchall()
        chk_email = sum([list(i) for i in db_email_tuple],[])
        if email in chk_email:
            cur.execute(f'select title, texts from resume_tb where email="{email}" and actDeact="1"')
            user_data = cur.fetchall()
            return render_template('myresume.html', user_data=user_data, length=len(user_data))
        else:
            return render_template('error.html', msg="자소서 작성 후 이용해 주세요.")



@app.route('/insert', methods=['POST'])
def insert():
    conn = mysql.connect()
    cur = conn.cursor()
    email = session['user_email']
    user_title = request.form.get('user_title')
    user_text = request.form.get('user_text')
    
    cur.execute(f'select title from resume_tb where email="{email}" and actDeact="1"')
    title_tuple = cur.fetchall()
    chk_title = sum([list(i) for i in title_tuple],[])
    if user_title in chk_title:
        return render_template('error.html', msg="동일한 이름의 자소서 제목이 있습니다. 다른 이름으로 작성해주세요.")

    cur.execute(f'select idx from resume_tb where email="{email}" and actDeact="1"')
    resume_count_tuple = cur.fetchall()
    chk_resume_count = sum([list(i) for i in resume_count_tuple],[])
    if len(chk_resume_count) >= 6:
        return render_template('error.html', msg="저장 가능한 자소서 수를 넘었습니다.(최대6개)")

    cur.execute(f'insert into resume_tb (email, title, texts) values ("{email}", "{user_title}", "{user_text}")')
    conn.commit()
    return redirect(url_for('myresume'))


@app.route('/update', methods=['POST'])
def update():
    if not session.get('user_id'):
        return render_template('error.html', msg="로그인 후 이용해 주세요.")
    else:
        conn = mysql.connect()
        cur = conn.cursor()
        email = session['user_email']
        user_title = request.form.get('user_title')
        user_text = request.form.get('user_text')

        cur.execute(f'update resume_tb set texts="{user_text}" where email="{email}" and actDeact = "1" and title="{user_title}"')
        conn.commit()
        return redirect(url_for('myresume'))


@app.route('/delete', methods=['POST'])
def delete():
    if not session.get('user_id'):
        return render_template('error.html', msg="로그인 후 이용해 주세요.")
    else:
        conn = mysql.connect()
        cur = conn.cursor()
        email = session['user_email']
        user_title = request.form.get('deact').split(' 삭제')[0]

        cur.execute(f'update resume_tb set actDeact="0" where title="{user_title}" and email="{email}"')
        conn.commit()
        return redirect(url_for('myresume'))



if __name__ == '__main__':
    app.run(debug=True)
