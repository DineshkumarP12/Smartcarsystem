#!C:\Users\Personal\AppData\Local\Programs\Python\Python310\python.exe
print("content-type:text/html \r\n\r\n")



import pymysql
import cgi, cgitb,os

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = conn.cursor()
form=cgi.FieldStorage()
idvalue=form.getvalue("id")
print("""<!DOCTYPE html>
<html lang="en">

<head>
    <title>emppage</title>
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
            background-image: linear-gradient(rgb(253, 9, 50), rgb(162, 4, 4), rgb(243, 3, 3));
            position: fixed;
            top: 0px;
            width: 220px;
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

        }

        .nav-side-menu ul .active,
        .nav-side-menu li .active {
            border-left: 3px solid #d19b3d;

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
            border-bottom: 3px solid white;
        }

        .nav-side-menu li a {
            text-decoration: none;
            color: #e1ffff;
            padding: 5px;
            font-size: 15px;

        }

        .nav-side-menu li:hover {
            border-left: 3px solid #d19b3d;
            background-color: deeppink;
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
         #file {
            display: none;
        }

        #file1 {
            position: absolute;
            height: 30px;
            width: 30px;
            padding: 6px 6px;
            border-radius: 50%;
            cursor: pointer;
            color: white;
            background-color: lightslategrey;
            box-shadow: 3px 3px 3px black;
            transform: translateX(-90%);
            margin-top: 130px;
        }

        .modal-dialog {
            width: 400px;
            border-color: white;
            background: #fff;
            /* padding: 20px 0; */
            border-radius: 60px;
            /* margin: 30px 0; */
            box-shadow: 2px 2px 5px 2px rgba(0, 0, 0, 0.25);
        }

        .aa {
            color: white;
           
        }
    </style>
</head>

<body>
    <div class="nav-side-menu">
        <div class="brand">
            <h3>User Page</h3>

        </div>
        <hr>
        <i class="fa fa-bars fa-2x toggle-btn" data-toggle="collapse" data-target="#menu-content"></i>

        <div class="menu-list">

            <ul id="menu-content" class="menu-content collapse out">""")
print("""
                <li>
                    <a href="./User_profile.py?id=%s"><i class="fa fa-user fa-lg"></i> Profile
                    </a>
                </li>"""%idvalue)
print("""

                <li data-toggle="collapse" data-target="#new" class="collapsed">
                    <a href="#"><i class="fa fa-car fa-lg"></i> Buy A Car<span class="arrow"></span></a>
                </li>
                <ul class="sub-menu collapse" id="new">
                    <li><a href="./User_buy_page.py?id=%s">Buy cars</a></li>
                    <li><a href="./User_buy_status.py?id=%s">Status</a></li>
                    <li><a href="./user_buy_user_testdrive.py?id=%s">buy Testdrive</a></li>
                </ul>"""%(idvalue,idvalue,idvalue))
print("""
                <li data-toggle="collapse" data-target="#new1" class="collapsed">
                    <a href="#"><i class="fa fa-car fa-lg"></i> Sale A Car<span class="arrow"></span></a>
                </li>
                <ul class="sub-menu collapse" id="new1">
                    <li><a href="./User_sale_page.py?id=%s">Register Cars</a></li>
                    <li><a href="./User_sale_status.py?id=%s">Status</a></li>
                    <li><a href="./user_sale_testdrive.py?id=%s">Sale Testdrive</a></li>
                </ul>"""%(idvalue,idvalue,idvalue))
print("""
                <li>
                    <a href="./Index_page.py">
                        <i class="fa fa-sign-out fa-lg"></i> Logout
                    </a>
                </li>
            </ul>
        </div>
    </div>


</body>

</html>""")
q = """select * from  uregister where id=%s """ % (idvalue)
cur.execute(q)
rec = cur.fetchall()
for i in rec:
    fn = "userphoto/" + i[10]
    print(""" 
    <div class="content">
        <div class="col-md-3"></div>
        <div class="col-md-8">
            <br><br><br>
            <center>
                <div class="profile-pic">
                    <img src='%s' alt="emp" class="rounded-circle"
                        width="150" id="img">

                    <label for="file" id="file1" data-toggle="modal" data-target="#Profile">
                        <i class="fa fa-camera"></i>
                    </label>
                </div>

                
                <h3>name:%s</h3>
                <h3>Location: %s</h3>
                <input data-toggle="modal" data-target="#mymodal" class="btn-primary" value="Change Password">
            </center>
        </div>
    </div>""" % (fn, i[1], i[15]))
print("""
<style>
 .modal-dialog {
            width: 400px;
            border-color: white;
            background: #fff;
            border-radius: 60px;
            box-shadow: 2px 2px 5px 2px rgba(0, 0, 0, 0.25);
        }
</style>
<center>
        <div class="modal" id="Profile">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                        <h3 class="modal-title">
                            <center><span class="fa fa-arrow-left"></span> Change Profile</center>
                        </h3>
                        <br><br>
                        <form action=""method="post" enctype="multipart/form-data" >
                            <div>
                               <br>
                                <input type="file" name="images">
                                <br>
                                <input type="submit" class="btn btn-success" name="update" value="Update">
                                <br><br>

                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </center>

""")

update = form.getvalue("update")
if update != None:
    if len(form) != 0:
        profile = form['images']
        if profile.filename:
            fn = os.path.basename(profile.filename)
            open("userphoto/" + fn, "wb").write(profile.file.read())
            q3 = """update uregister set upload_photo="%s" where id="%s" """ % (fn, idvalue)
            cur.execute(q3)

print("""<center>
        <div class="col-md-8"></div>
        <div class="col-md-3">

            <div class="modal" id="mymodal">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h3 class="modal-title">
                                <center><span class="fa fa-arrow-left"></span> Change Password</center>
                            </h3>
                            <br><br>
                            <form action="" autocomplete="off" method="post" enctype="multipart/form-data">
                                <div>
                                    <input type="text" class="form-control" id="oldpass" placeholder="Old Password" name="oldpass"><br>
                                    <input type="text" class="form-control" id="name" placeholder="New Password" name="newpass">
                                    <br>
                                    <input type="text" class="form-control" id="password"
                                        placeholder="Confirm Password" name="password">
                                    <br>
                                    <input type="submit" class="btn btn-success" class="aa" value="Save" name="changepass">
                                    <br><br>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </center>""")
opass = form.getvalue("oldpass")
npass = form.getvalue("newpass")
cpass = form.getvalue("password")
Changepass = form.getvalue("changepass")
if Changepass != None:
    if npass == cpass:
        q4 = """update uregister set password="%s" where id="%s" """ % (cpass, idvalue)
        cur.execute(q4)
        print("""<script>alert("password changed successfully");</script>""")

conn.commit()
conn.close()

