from flask import Blueprint, render_template, request, url_for, redirect, session
import pymysql
from dbconnect import *

db = pymysql.connect(host=HOST, user=USER, password=PASS, database=DATABASE)


Pageuse = Blueprint('Pageuse', __name__)


@Pageuse.route("/Userindex")
def userindex():
    if "username" not in session:
        return render_template('login/login.html')
    with db.cursor() as cur:
        sql = "SELECT * FROM products"
        try:
            cur.execute(sql)
            db.commit()
        except:
            return render_template('user/index_user.html', datas=('nodata'))
        rows = cur.fetchall()
    return render_template('user/index_user.html', datas=rows)


@Pageuse.route("/userRe")
def userRe():
    if "username" not in session:
        return render_template('login/login.html')
    with db.cursor() as cur:
        sql = sql = "SELECT * FROM requisition"
        try:
            cur.execute(sql)
            db.commit()
        except:
            return render_template('user/requisition.html', datas=('nodata'))
        rows = cur.fetchall()
    return render_template('user/requisition.html', datas=rows)

@Pageuse.route("/Useradding")
def useradding():
    if "username" not in session:
        return render_template('login/login.html')
    return render_template("user/Add_user.html")


@Pageuse.route("/userDel", methods=["POST"])
def userDel():
    if request.method == "POST":
        No = request.form['No']
        with db.cursor() as cur:
            sql = "DELETE FROM requisition WHERE re_no = %s "
            try:
                cur.execute(sql, (No))
                db.commit()
            except:
                return redirect(url_for('Pageuse.userRe'))

            return redirect(url_for('Pageuse.userRe'))

    return redirect(url_for('Pageuse.userRe'))


@Pageuse.route("/userAdd", methods=["POST"])
def userAdd():
    if request.method == "POST":
        runum = request.form['re_no']
        re_pstatus = request.form['re_pstatus']
        Product_type = request.form['Product_type']
        re_unit = request.form['re_unit']
        re_date = request.form['re_date']
        with db.cursor() as cur:
            sql = "INSERT INTO requisition (re_no,re_pstatus,Product_type,re_unit,re_date) VALUES (%s,%s,%s,%s,%s)"
            try:
                cur.execute(sql, (runum,re_pstatus,Product_type, re_unit, re_date))
                db.commit()
            except:
                return redirect(url_for('Pageuse.userRe'))

            return redirect(url_for('Pageuse.userRe'))

    return render_template("user/Add_user.html")

@Pageuse.route("/useredit", methods=["POST"])
def useredit():
    if request.method == "POST":
        No = request.form['No']
        Name = request.form['Nameuser']
        status = request.form['re_pstatus']
        type = request.form['Product_type']
        unit = request.form['re_unit']
        st = request.form['st']
        with db.cursor() as cur:
            sql = "UPDATE requisition SET User_name = %s, re_pstatus = %s ,Product_type = %s, re_unit = %s, re_date = CURRENT_TIME(), re_status = %s WHERE re_no = %s"
            try:
                cur.execute(sql, (Name,status,type,unit,st, No))
                db.commit()
            except:
                return redirect(url_for('Pageuse.userRe'))

            return redirect(url_for('Pageuse.userRe'))

    return redirect(url_for('Pageuse.userRe'))