from flask import Blueprint, render_template, request, url_for, redirect,session
import pymysql
from dbconnect import *
from flask_paginate import Pagination, get_page_args

db = pymysql.connect(host=HOST, user=USER, password=PASS, database=DATABASE)


Document_products = Blueprint('Document_products', __name__)


@Document_products.route("/Admin_index")
def Admin_index():
    if "username" not in session:
        return render_template('login.html')
    with db.cursor() as cur:
        sql = "SELECT * FROM requisition"
        try:
            cur.execute(sql)
            db.commit()
        except:
            return render_template('admin/index.html', datas=('nodata'))
        rows = cur.fetchall()
        user = list(range(len(rows)))
        total = len(user)
        page,per_page,offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
        pagination_user = user[offset:offset+10]
        pagination_date = pagination_user
        pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap5')
    return render_template('admin/index.html', datas=rows, page=page, per_page=per_page, Pagination=pagination, len=total, user=pagination_date)

@Document_products.route("/cresheradmin", methods=["POST"])
def cresheradmin():
    if request.method == "POST":
        dstart = request.form['dstart']
        with db.cursor() as cur:
            sql = "SELECT * FROM requisition WHERE re_pstatus = %s"
            try:
                cur.execute(sql, (dstart))
                db.commit()
            except:
                return render_template('admin/index.html', datas=('nodata'))
            rows = cur.fetchall()
            user = list(range(len(rows)))
            pagination_user = user
            pagination = Pagination(css_framework='bootstrap5')
        return render_template('admin/index.html', datas=rows, Pagination=pagination, user=pagination_user)

@Document_products.route("/Admin_edit", methods=["POST"])
def Admin_edit():
    if request.method == "POST":
        No = request.form['re_no']
        User_name = request.form['User_name']
        re_pstatus = request.form['re_pstatus']
        Product_type = request.form['Product_type']
        re_unit = request.form['re_unit']
        re_status = request.form['re_status']

        with db.cursor() as cur:
            sql = "UPDATE requisition SET User_name = %s, re_pstatus = %s ,Product_type = %s, re_unit = %s, re_date = CURRENT_TIME(), re_status = %s WHERE re_no = %s"
            try:
                cur.execute(sql, (User_name, re_pstatus, Product_type, re_unit, re_status, No))
                db.commit()
            except:
                return redirect(url_for('Document_products.Admin_index'))

            return redirect(url_for('Document_products.Admin_index'))

    return redirect(url_for('Document_products.Admin_index'))


@Document_products.route("/Admin_del", methods=["POST"])
def Admin_del():
    if request.method == "POST":
        No = request.form['re_no']
        with db.cursor() as cur:
            sql = "DELETE FROM requisition WHERE re_no = %s "
            try:
                cur.execute(sql,(No))
                db.commit()
            except:
                return redirect(url_for('Document_products.Admin_index'))

            return redirect(url_for('Document_products.Admin_index'))

    return redirect(url_for('Document_products.Admin_index'))
