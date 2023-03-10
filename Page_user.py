from flask import Blueprint, render_template, request, url_for, redirect, session, flash
import pymysql
from dbconnect import *
from flask_paginate import Pagination, get_page_args

db = pymysql.connect(host=HOST, user=USER, password=PASS, database=DATABASE)


Pageuse = Blueprint('Pageuse', __name__)


@Pageuse.route("/userindex")
def userindex():
    with db.cursor() as cur:
        sql = "SELECT * FROM products "
        try:
            cur.execute(sql)
            db.commit()
        except:
            return render_template('user/index_user.html', datas=('nodata'))
        rows = cur.fetchall()
        user = list(range(len(rows)))
        total = len(user)
        page, per_page, offset = get_page_args(
            page_parameter='page', per_page_parameter='per_page')
        pagination_user = user[offset:offset+10]
        pagination_date = pagination_user
        pagination = Pagination(
            page=page, per_page=per_page, total=total, css_framework='bootstrap5')
    return render_template('user/index_user.html', datas=rows, page=page, per_page=per_page, Pagination=pagination, len=total, user=pagination_date)

#Document borrow adding
@Pageuse.route("/Useradding")
def useradding():
    with db.cursor() as cur:
        sql = "SELECT * FROM products_type"
        try:
            cur.execute(sql)
            db.commit
        except:
            return render_template("user/Add_user.html", datas=('nodata'))
        rows = cur.fetchall()
            
    return render_template("user/Add_user.html", datas=rows)


@Pageuse.route("/userAdd", methods=["POST"])
def userAdd():
    if request.method == "POST":
        runum = request.form['re_no']
        User_name = request.form['User_name']
        re_pstatus = request.form['re_pstatus']
        Product_type = request.form['Product_type']
        re_unit = request.form['re_unit']
        re_date = request.form['re_date']
        re_status = request.form['re_status']
        comment = request.form['comment']
        with db.cursor() as cur:
            sql = "INSERT INTO record (re_no,User_name,re_pstatus,Product_type,Product_export,re_date,re_status,comment) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            sql2 = "UPDATE record SET Product_export = Product_export - %s  WHERE re_no = %s;"
            sql3 = "SELECT Product_quantity, Product_id FROM products WHERE Product_type = %s"
            sql4 = "INSERT INTO borrow (borrow_no,Product_type,borrow_date,borrow_unit,User_name,re_pstatus,borrow_status) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            try:
                
                cur.execute(sql,(runum, User_name, re_pstatus, Product_type, re_unit, re_date, re_status, comment))
                db.commit()
                cur.execute(sql2,(re_unit, runum))
                db.commit()
                cur.execute(sql3,(Product_type))
                db.commit()
                

                rows = cur.fetchall()
                sql5 = "UPDATE products SET Product_date = %s ,Product_quantity = Product_quantity - %s WHERE Product_id = %s"
                cur.execute(sql5,(re_date,re_unit, rows[0][1]))
                db.commit()
                cur.execute(sql4,(runum,Product_type,re_date,re_unit,User_name,re_pstatus,re_status))
                db.commit()
                

                flash("???????????????????????????????????????????????????????????????????????????????????????????????????????????????....????????????????????????????????????????????????????????????????????????")
            except:
                return redirect(url_for('Pageuse.Borrowuser', status="wait"))

            return redirect(url_for('Pageuse.Borrowuser', status="wait"))

    return render_template("user/Add_user.html", status="wait",datas=rows)

#contact admin
@Pageuse.route("/contact")
def contact():
    return render_template("user/contact_admin.html")

@Pageuse.route("/contactadmin", methods = ["POST"])
def contactadmin():
    if request.method == "POST":
        no = request.form["TextID"]
        fname = request.form["Name"]
        idphone = request.form["phone"]
        sos = request.form["sos"]
        with db.cursor() as cur:
            sql = "INSERT INTO sos (ID,fname,phone,notify) VALUES (%s,%s,%s,%s)"
            try:
                cur.execute(sql,(no,fname,idphone,sos))
                db.commit()
                flash("??????????????????????????????????????????????????????????????????????????????????????????....????????????????????????????????????????????????????????????")
            except:
                return redirect(url_for('Pageuse.userindex', status="wait"))

            return redirect(url_for('Pageuse.userindex', status="wait"))

    return render_template("user/contact_admin.html", status="wait")

#borrow user
@Pageuse.route("/Borrowuser")
def Borrowuser():
    with db.cursor() as cur:
        sql = "SELECT * FROM borrow ORDER BY borrow_no DESC"
        try:
            cur.execute(sql)
            db.commit()
        except:
            return render_template('user/borrow_user.html', datas=('nodata'))
        rows = cur.fetchall()
        user = list(range(len(rows)))
        total = len(user)
        page, per_page, offset = get_page_args(
            page_parameter='page', per_page_parameter='per_page')
        pagination_user = user[offset:offset+10]
        pagination_date = pagination_user
        pagination = Pagination(
            page=page, per_page=per_page, total=total, css_framework='bootstrap5')
    return render_template('user/borrow_user.html', datas=rows, page=page, per_page=per_page, Pagination=pagination, len=total, user=pagination_date)

@Pageuse.route("/sss")
def sss():
    with db.cursor() as cur:
        sql = "SELECT * FROM products_type"
        try:
            cur.execute(sql)
            db.commit
        except:
            return render_template("user/Add_user.html", datas=('nodata'))
        rows = cur.fetchall()
            

    return render_template("user/Add_user.html", datas=rows)