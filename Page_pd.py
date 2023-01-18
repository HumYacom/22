from flask import Blueprint, render_template, request, url_for, redirect,session,flash
import pymysql
from dbconnect import *
from flask_paginate import Pagination, get_page_args

db = pymysql.connect(host=HOST, user=USER, password=PASS, database=DATABASE)


PD = Blueprint('PD', __name__)

@PD.route("/pd")
def pd():
    with db.cursor() as cur:
        sql = "SELECT Products.Product_id, Products.Product_name, inventory.Product_category, Products.Product_manner, Products.Product_price,Products.Product_date,inventory.type_id,inventory.Product_status FROM Products INNER JOIN inventory ON Products.Product_type = inventory.Product_type;"
        try:
            cur.execute(sql)
            db.commit()
        except:
            return render_template('admin/menu_pd.html', datas=('nodata'))
        rows = cur.fetchall()

        return render_template('admin/menu_pd.html', datas=rows)

@PD.route("/PD_edit", methods=["POST"])
def PD_edit():
    if request.method == "POST":
        No = request.form['Product_id']
        User_name = request.form['Product_name']
        re_pstatus = request.form['re_pstatus']
        Product_type = request.form['Product_category']
        re_unit = request.form['Product_manner']
        re_status = request.form['Product_price']
        type_id = request.form['type_id']
        Product_status = request.form['Product_status']

        with db.cursor() as cur:
            sql = ""
            try:
                cur.execute(sql, (User_name, re_pstatus, Product_type, re_unit, re_status, No,type_id,Product_status))
                db.commit()
            except:
                return redirect(url_for('PD.pd'))

            return redirect(url_for('PD.pd'))

    return redirect(url_for('PD.pd'))


@PD.route("/PD_del", methods=["POST"])
def PD_del():
    if request.method == "POST":
        No = request.form['Product_id']
        with db.cursor() as cur:
            sql = "DELETE FROM requisition WHERE Product_id = %s "
            try:
                cur.execute(sql,(No))
                db.commit()
            except:
                return redirect(url_for('PD.pd'))

            return redirect(url_for('PD.pd'))

    return redirect(url_for('PD.pd'))

@PD.route("/PDadding")
def PDadding():
    return render_template("admin/PD_add.html")


@PD.route("/PDAdd", methods=["POST"])
def PDAdd():
    if request.method == "POST":
        runum = request.form['re_no']
        User_name = request.form['User_name']
        re_pstatus = request.form['re_pstatus']
        Product_type = request.form['Product_type']
        re_unit = request.form['re_unit']
        re_date = request.form['re_date']
        re_status = request.form['re_status']
        with db.cursor() as cur:
            sql = ""
            try:
                cur.execute(sql, (runum, User_name, re_pstatus,Product_type, re_unit, re_date, re_status))
                db.commit()
                flash(
                    "ได้ทำการส่งเรื่องขอวัสดุแล้วกำลังส่งข้อมูล...กรุณารอสักครู่ครับ")
            except:
                return redirect(url_for('PD.pd', status="wait"))

            return redirect(url_for('PD.pd', status="wait"))

    return render_template("admin/PD_add.html", status="wait")