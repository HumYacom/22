from flask import Blueprint, render_template, request, url_for, redirect,session
import pymysql
from dbconnect import *

db = pymysql.connect(host=HOST, user=USER, password=PASS, database=DATABASE)


Document_products = Blueprint('Document_products', __name__)


@Document_products.route("/Admin_index")
def Admin_index():
    if "username" not in session:
        return render_template('login.html')
    with db.cursor() as cur:
        sql = "SELECT * FROM products"
        try:
            cur.execute(sql)
            db.commit()
        except:
            return render_template('admin/index.html', datas=('nodata'))
        rows = cur.fetchall()
    return render_template('admin/index.html', datas=rows)

@Document_products.route("/petition")
def petition():
    if "username" not in session:
        return render_template('login.html')
    with db.cursor() as cur:
        sql = "SELECT * FROM requisition"
        try:
            cur.execute(sql)
            db.commit()
        except:
            return render_template('admin/petition.html', datas=('nodata'))
        rows = cur.fetchall()
    return render_template('admin/petition.html', datas=rows)

@Document_products.route("/Borrow")
def Borrow():
    if "username" not in session:
        return render_template('login.html')
    with db.cursor() as cur:
        sql = "SELECT * FROM requisition"
        try:
            cur.execute(sql)
            db.commit()
        except:
            return render_template('admin/Borrow.html', datas=('nodata'))
        rows = cur.fetchall()
    return render_template('admin/Borrow.html', datas=rows)

@Document_products.route("/Admin_edit", methods=["POST"])
def Admin_edit():
    if request.method == "POST":
        No = request.form['No']
        Product_name = request.form['Product_name']
        Product_type = request.form['Product_type']
        Product_manner = request.form['Product_manner']
        Product_price = request.form['Product_price']
        with db.cursor() as cur:
            sql = "UPDATE products SET Product_name = %s, Product_type = %s ,Product_manner = %s, Product_price = %s, Product_date = CURRENT_TIME() WHERE Product_id = %s"
            try:
                cur.execute(sql, (Product_name, Product_type,Product_manner,Product_price, No))
                db.commit()
            except:
                return redirect(url_for('Document_products.Admin_index'))

            return redirect(url_for('Document_products.Admin_index'))

    return redirect(url_for('Document_products.Admin_index'))


@Document_products.route("/Admin_del", methods=["POST"])
def Admin_del():
    if request.method == "POST":
        No = request.form['No']
        with db.cursor() as cur:
            sql = "DELETE FROM products WHERE Product_id = %s "
            try:
                cur.execute(sql,(No))
                db.commit()
            except:
                return redirect(url_for('Document_products.Admin_index'))

            return redirect(url_for('Document_products.Admin_index'))

    return redirect(url_for('Document_products.Admin_index'))


@Document_products.route("/Adding")
def Adding():
    if "username" not in session:
        return render_template('login/login.html')
    return render_template("admin/Add.html")


@Document_products.route("/Admin_add", methods=["POST"])
def Admin_add():
    if request.method == "POST":
        Product_name = request.form['Product_name']
        Product_type = request.form['Product_type']
        Product_manner = request.form['Product_manner']
        Product_price = request.form['Product_price']
        with db.cursor() as cur:
            sql = "INSERT INTO products (Product_name,Product_type,Product_manner,Product_price) VALUES (%s,%s,%s,%s)"
            try:
                cur.execute(sql, (Product_name, Product_type,Product_manner,Product_price))
                db.commit()
            except:
                return redirect(url_for('Document_products.Admin_index'))

            return redirect(url_for('Document_products.Admin_index'))

    return render_template("admin/Add.html")

@Document_products.route("/petitionedit", methods=["POST"])
def petitionedit():
    if request.method == "POST":
        Num = request.form['No']
        Name = request.form['Nameuser']
        status = request.form['re_pstatus']
        type = request.form['Product_type']
        unit = request.form['re_unit']
        st = request.form['st']
        with db.cursor() as cur:
            sql = "UPDATE requisition SET User_name = %s, re_pstatus = %s ,Product_type = %s, re_unit = %s, re_date = CURRENT_TIME(), re_status = %s WHERE re_no = %s"
            try:
                cur.execute(sql, (Name,status,type,unit,st, Num))
                db.commit()
            except:
                return redirect(url_for('Document_products.petition'))

            return redirect(url_for('Document_products.petition'))

    return redirect(url_for('Document_products.petition'))

@Document_products.route("/Del", methods=["POST"])
def Del():
    if request.method == "POST":
        No = request.form['No']
        with db.cursor() as cur:
            sql = "DELETE FROM requisition WHERE re_no = %s "
            try:
                cur.execute(sql, (No))
                db.commit()
            except:
                return redirect(url_for('Document_products.petition'))

            return redirect(url_for('Document_products.petition'))

    return redirect(url_for('Document_products.petition'))

@Document_products.route("/Sending")
def Sending():
    if "username" not in session:
        return render_template('login/login.html')

    return render_template("admin/Borrow.html")

@Document_products.route("/Borrowedit", methods=["POST"])
def Borrowedit():
    if request.method == "POST":
        Num = request.form['No']
        Name = request.form['Nameuser']
        status = request.form['re_pstatus']
        type = request.form['Product_type']
        unit = request.form['re_unit']
        st = request.form['st']
        with db.cursor() as cur:
            sql = "UPDATE requisition SET User_name = %s, re_pstatus = %s ,Product_type = %s, re_unit = %s, re_date = CURRENT_TIME(), re_status = %s WHERE re_no = %s"
            try:
                cur.execute(sql, (Name,status,type,unit,st, Num))
                db.commit()
            except:
                return redirect(url_for('Document_products.Borrow'))

            return redirect(url_for('Document_products.Borrow'))

    return redirect(url_for('Document_products.Borrow'))

@Document_products.route("/BorrowDel", methods=["POST"])
def BorrowDel():
    if request.method == "POST":
        No = request.form['No']
        with db.cursor() as cur:
            sql = "DELETE FROM requisition WHERE re_no = %s "
            try:
                cur.execute(sql, (No))
                db.commit()
            except:
                return redirect(url_for('Document_products.Borrow'))

            return redirect(url_for('Document_products.Borrow'))

    return redirect(url_for('Document_products.Borrow'))