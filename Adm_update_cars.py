#!C:\Users\Personal\AppData\Local\Programs\Python\Python310\python.exe
print("content-type:text/html \r\n\r\n")
print("""<!DOCTYPE html>
<html lang="en">

<head>
    <title>adminpage</title>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <script src="//netdna.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="./media/logoonly.png">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">

    <style>
        .nav-side-menu {
            overflow: auto;
            font-family: verdana;
            font-size: 15 px;
            font-weight: 200;
            /* background-image: linear-gradient(to top, rgb(56, 78, 186), rgb(220, 15, 176)); */
            /* background-color: rgb(196, 5, 107); */

            background-image: linear-gradient(rgb(105, 3, 57), rgb(188, 13, 106), rgb(234, 96, 170));
            position: fixed;
            top: 0px;
            /* width: 350px; */
            width: 280px;
            height: 100%;
            color: #e1ffff;

        }

        .nav-side-menu .brand {
            line-height: 50px;
            display: block;
            text-align: center;
            font-size: 14px;
            padding: 15px;
        }

        .nav-side-menu .toggle-btn {
            display: none;
        }

        .nav-side-menu ul,
        .nav-side-menu li {
            list-style: none;
            padding: 0px;
            margin: 0px;
            line-height: 35px;
            cursor: pointer;

        }

        .nav-side-menu ul :not(collapsed) .arrow:before,
        .nav-side-menu li :not(collapsed) .arrow:before {
            font-family: FontAwesome;
            content: "\f078";
            display: inline-block;
            padding-left: 10px;
            padding-right: 10px;
            vertical-align: middle;
            /* float: right; */
        }

        .nav-side-menu ul .active,
        .nav-side-menu li .active {
            border-left: 3px solid #d19b3d;
            background-color: #7e4eee;
            /* background-color: darkgray; */
        }

        /* .nav-side-menu ul .sub-menu li.active,
        .nav-side-menu li .sub-menu li.active {
            background-color: #ecc9ed;
            color: #090909;
        } */

        /* .nav-side-menu ul .sub-menu li.active a,
        .nav-side-menu li .sub-menu li.active a {
            color: #050505;
        } */

        .nav-side-menu ul .sub-menu li,
        .nav-side-menu li .sub-menu li {
            background-color: rgb(18, 82, 107);
            border: none;
            line-height: 28px;
            border-bottom: 1px solid #23282e;
            margin-left: 0px;
        }

        .nav-side-menu ul .sub-menu li:hover,
        .nav-side-menu li .sub-menu li:hover {
            background-color: rgb(153, 5, 5);
        }

        .nav-side-menu ul .sub-menu li:before,
        .nav-side-menu li .sub-menu li:before {
            font-family: FontAwesome;
            content: "\f105";
            display: inline-block;
            padding-left: 10px;
            padding-right: 10px;
            vertical-align: middle;
        }

        .nav-side-menu li {
            padding-left: 0px;
            border-left: 3px solid #2e353d;
            border-bottom: 1px solid #23282e;
        }

        .nav-side-menu li a {
            text-decoration: none;
            color: #e1ffff;
        }

        .nav-side-menu li a i {
            padding-left: 10px;
            width: 20px;
            padding-right: 20px;
        }

        .nav-side-menu li:hover {
            border-left: 3px solid #d19b3d;
            background-color: rgb(208, 63, 140);
            color: white;
            -webkit-transition: all 1s ease;
            -moz-transition: all 1s ease;
            -o-transition: all 1s ease;
            -ms-transition: all 1s ease;
            transition: all 1s ease;
        }

        @media (max-width: 767px) {
            .nav-side-menu {
                position: relative;
                width: 100%;
                margin-bottom: 10px;
            }

            .nav-side-menu .toggle-btn {
                display: block;
                cursor: pointer;
                position: absolute;
                right: 10px;
                top: 10px;
                z-index: 10 !important;
                padding: 3px;
                background-color: #ffffff;
                color: black;
                width: 40px;
                text-align: center;
            }

            .brand {
                padding-left: 5px;
                height: 100px;
            }
        }

        @media (min-width: 767px) {
            .nav-side-menu .menu-list .menu-content {
                display: block;
            }
        }

        body {
            margin: 0px;
            padding: 0px;
        }

        hr {
            color: #23282e;
            width: 120px;
        }
        input:hover {
            background-color: rgb(55, 253, 253);
        }

        select:hover {
            background-color: rgb(55, 253, 253);
        }



        .cc {
            background-image: linear-gradient(aqua, rgb(146, 244, 244), rgb(3, 120, 120));
            padding: 20px;
            color: deeppink;
            text-shadow: 2px 3px 2px rgb(37, 37, 245);
            font-family: fantasy;
        }
    </style>
</head>

<body>
    <div class="nav-side-menu">
        <div class="brand">
            <h1>Admin Page</h1>
        </div>
        <hr>
        <i class="fa fa-bars fa-2x toggle-btn" data-toggle="collapse" data-target="#menu-content"></i>

        <div class="menu-list">

            <ul id="menu-content" class="menu-content collapse out">
                <li data-toggle="collapse" data-target="#products" class="collapsed">
                    <a href="#"><i class="fa fa-user fa-lg"></i>Employee Details <span class="arrow"></span></a>
                </li>
               <ul class="sub-menu collapse" id="products">
                    <li class="active"><a href="./Adm_Emp_register.py">Add Employee Details</a></li>
                    <li><a href="./Adm_emp_view.py">View Employee Details</a></li>
                    <li><a href="./Adm_emp_leave_report.py">Leave Report</a></li>
                    <li><a href="./Adm_emp_leave_request.py">Leave Request</a></li>
                    <li><a href="./Adm_emp_password_request.py">Password Request</a></li>
                </ul>


                <li data-toggle="collapse" data-target="#service" class="collapsed">
                    <a href="#"><i class="fa fa-user fa-lg"></i> Buy User Request<span class="arrow"></span></a>
                </li>
                <ul class="sub-menu collapse" id="service">
                    <li><a href="./Adm_new_user_buy.py">New User</a></li>
                    <li><a href="./Adm_buy_status.py">buy complete process</a></li>
                    <li><a href="./Adm_user_password_request.py">Password Request</a></li>


                </ul>
                <li data-toggle="collapse" data-target="#service2" class="collapsed">
                    <a href="#"><i class="fa fa-user fa-lg"></i> Sale User Request<span class="arrow"></span></a>
                </li>
                <ul class="sub-menu collapse" id="service2">
                    <li><a href="./Adm_sale_user.py">New User</a></li>
                     <li><a href="./Adm_sale_status.py">sale complete process</a></li>
                    <li><a href="./Adm_user_password_request.py">Password Request</a></li>


                </ul>



                <li data-toggle="collapse" data-target="#new" class="collapsed">
                    <a href="#"><i class="fa fa-car fa-lg"></i> Cars<span class="arrow"></span></a>
                </li>
                <ul class="sub-menu collapse" id="new">
                    <li><a href="./Adm_add_Car.py">Add Cars</a></li>
                    <li><a href="./Adm_Car_view.py">Existing Cars</a></li>
                      <li><a href="./Adm_new_cars.py">New Cars</a></li>
                       
                </ul>

                <li>
                    <a href="./Index_page.py">
                        <i class="fa fa-sign-out fa-lg"></i> Logout
                    </a>
                </li>
            </ul>
        </div>
    </div>
<script type="text/javascript">
        window.history.forward();
        function noBack() {
            window.history.forward();
        }

    </script>
    
</body>

</html>""")
import pymysql
import cgi, cgitb,os

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = conn.cursor()
form=cgi.FieldStorage()
pid = form.getvalue("id")
q2= """select * from empaddedcar where id=%s """ %(pid)
cur.execute(q2)
res=cur.fetchall()
for i in res:
    print("""<form action="" method="post" enctype="multipart/form-data">
        <div class="container">
            <div class="content">
                <div class="col-md-3"></div>
                <div class="col-md-8">
                    <center>
                        <h1 class="cc"> <i class="fa fa-car fa-lg"></i> Car
                            Registration
                        </h1>
                    </center>
                    <br><br>
                    <div class="form-content">
                        <div class="row">

                            <div class="col-md-6">
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="ID Number" name="id1" value="%s">
                                </div>
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="make" name="make" value="%s">
                                </div>
                                <div class="form-group">
                                     <input type="text" class="form-control" placeholder="model" name="model" value="%s">
                                </div>
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="transmission" name="trm" value="%s">
                                </div>
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="year" name="year" value="%s">
                                </div>
                                <div class="form-group">
                                     <input type="text" class="form-control" placeholder="mileage" name="mileage" value="%s">
                                </div>
                                <div class="form-group">
                                     <input type="text" class="form-control" placeholder="body type" name="bt" value="%s">
                                </div>
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="color" name="color" value="%s">
                                </div>
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="kilometer driven" name="kd" value="%s">
                                </div>
                            </div>
                            <div class="col-md-6">

                                <div class="form-group">
                                     <input type="text" class="form-control" placeholder="car owner" name="co" value="%s">
                                </div>
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="fuel type" name="ft" value="%s">
                                </div>

                                <div class="form-group">
                                     <input type="text" class="form-control" placeholder="seating type" name="st" value="%s">
                                </div>
                                <div class="form-group">
                                     <input type="text" class="form-control" placeholder="photo 1" name="p1" value="%s">
                                </div>
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="photo 2" name="p2" value="%s">
                                </div>
                                <div class="form-group">
                                     <input type="text" class="form-control" placeholder="photo 3" name="p3" value="%s">
                                </div>
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="photo 4" name="p4" value="%s">
                                </div>
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="rc book" name="rc" value="%s">
                                </div>
                                 <div class="form-group">
                                    <input type="text" class="form-control" placeholder="Car Pricer" name="price">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>
        <center><input type="submit" value="submit" class="btn-success" name="update">
            
        </center>
    </form>
    """%(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17]))

update=form.getvalue("update")
if update!=None:
    if len(form) != 0:
        id1 = form.getvalue("id1")
        make = form.getvalue("make")
        model = form.getvalue("model")
        trm = form.getvalue("trm")
        year = form.getvalue("year")
        mileage = form.getvalue("mileage")
        body = form.getvalue("bt")
        color = form.getvalue("color")
        kilometer = form.getvalue("kd")
        owner = form.getvalue("co")
        fuel = form.getvalue("ft")
        seating = form.getvalue("st")
        photo1 =form.getvalue("p1")
        photo2 = form.getvalue("p2")
        photo3 = form.getvalue("p3")
        photo4 = form.getvalue("p4")
        rc = form.getvalue("rc")
        price=form.getvalue("price")
        q = """insert into addcars(id_no,make,model,transmission,year,mileage,body_type,color,kilometer_driven,car_owner,fuel_type,price,seating_type,car1_photo,car2_photo,car3_photo,car4_photo,rc_book_photo)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (id1, make, model, trm, year, mileage, body, color, kilometer, owner, fuel, price, seating, photo1, photo2, photo3, photo4, rc)
        cur.execute(q)
        conn.commit()
        print("""<script>alert("car added successfully")</script>""")


conn.close()
