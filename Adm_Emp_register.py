#!C:\Users\Personal\AppData\Local\Programs\Python\Python310\python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb, os

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = conn.cursor()
q1="select max(Id) from empregister"
cur.execute(q1)
r=cur.fetchone()
if r[0]!=None:
    n=r[0]
else:
    n=0
z=""
if n<=9:
    z="000"
elif n>=10 and n<=99:
    z="00"
elif n>=100 and n<=999:
    z="0"
EmpID="Emp55"+z+str(n+1)




print("""<!DOCTYPE html>
<html lang="en">

<head>
    <title>empregister</title>
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

        .form-control,
        .col-md-6 {
            border-radius: 20px;
        }

        .btoggle {
            margin-left: 260px;
            margin-top: -30px;
        }

        form {
            width: 300px;
            height: 300px;
        }

        .a {
            color: black;
            font-size: 15px;
            margin-left: -180px;
        }

        .aa {
            color: black;
            font-size: 15px;
        }

        #color {
            opacity: 0.9;
            background-color: ghostwhite;

        }

        form {
            width: 100%;
        }
         input:hover {
            background-color: rgb(71, 249, 252);
        }

        select:hover {
            background-color: rgb(72, 249, 249);
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
    <form action="" method="post"  enctype="multipart/form-data">

        <div class="content">
            <div class="col-md-3"></div>
            <div class="form">
                <center>
                    <h1
                        style="text-shadow: 2px 3px 2px aqua;font-family:fantasy;color: rgb(13, 108, 108);letter-spacing: 1px;">
                        <i class="fa fa-user fa-lg"></i> Employee
                        Registration
                    </h1>
                </center>
                <br>
                <div class="form-content">
                    <div class="row">
                        <div class="col-md-3"></div>
                        <div class="col-md-4">""")
print("""       <div class="form-group">
                <input type="text" class="form-control" placeholder="ID Number" name="id" value="%s" readonly>
                </div>""" %EmpID)
print("""   <div class="form-group">
                                <input type="text" class="form-control" placeholder="Name" required name="name">
                            </div>
                            <div class="form-group">
                                <input type="email" class="form-control" placeholder="Email Id" required id="email"
                                    onchange="changeuser()" autocomplete="off" name="email">
                            </div>
                            <div class="form-group">
                                <input type="text" class="form-control" onfocus="(this.type='date')"
                                    placeholder="Date-Of-Birth" name="dob">
                            </div>
                            <div class="form-group">
                                <input type="text" class="form-control" placeholder="Date-Of-Joining"
                                    onfocus="(this.type='date')" name="doj">
                            </div>
                            <div class="form-group">
                                <select class="form-control" name="marital">
                                    <option>Marital Status</option>
                                    <option>Married</option>
                                    <option>Unmarried</option>
                                </select>
                            </div>""")
print("""                           <div class="form-group">
                                <select class="form-control" name="des">
                                    <option>Destination</option>
                                    <option>Sales Executive</option>
                                    <option>Mechanical</option>
                                </select>

                            </div>

                            <div class="form-group">
                                <input type="text" class="form-control" placeholder="Contact Number" required name="cno">
                            </div>
                            <div class="form-group">
                                <input type="text" class="form-control" placeholder="Phone Number" name="pno">
                            </div>
                        </div>
                        <div class="col-md-3"></div>
                        <div class="col-md-4">
                            <div class="form-group">
                                <select class="form-control" name="idproof">
                                    <option>ID Proof</option>
                                    <option>Aadhaar Card</option>
                                    <option>Pan Card</option>
                                    <option>Voter Id</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <input type="text" class="form-control" onfocus="(this.type='file')"
                                    placeholder="Upload ID Proof" required name="uidproof">
                            </div>
                            <div class="form-group">
                                <input type="text" class="form-control" onfocus="(this.type='file')"
                                    placeholder="Upload photo" required name="uphoto">
                            </div>
                            <div class="form-group" style="color:black; font-size: 20px;">
                                <p name="gender">Gender
                                    <input type="radio" class="form-control1" value="Female" name="gender">
                                    <label>Female</label>
                                    <input type="radio" class="form-control1" value="Male" name="gender">
                                    <label>Male</label>
                                </p>
                            </div>

                            <div class="form-group">
                                <input type="text" placeholder="Address" class="form-control" required name="address">
                                <br>
                                <select class="col-md-6" style="height: 30px;" name="state" id="stateSel" size="1" name="state">
                                    <option selected="selected">Select State</option>

                                </select>
                                <select class="col-md-6" style="height: 30px;"  id="districtSel"
                                    size="1" name="district">
                                    <option selected="selected">Select District</option>

                                </select>
                                <br><br>
                                <select class="form-control" name="city" id="citySel">
                                    <option selected="selected" name="city">Select City</option>

                                </select>
                            </div>
                            <div class="form-group">
                                <input type="text" class="form-control" placeholder="Salary" name="salary">
                            </div>
                            <div class="form-group">
                                <select class="form-control" name="qua">
                                    <option>Qualification</option>
                                    <option>Arts</option>
                                    <option>Science</option>
                                    <option>Engineering</option>
                                </select>
                            </div><br>
                            <center>

                                <input type="submit" class="btn-success" style="font-size: 20px;">
                                <input type="reset" class="btn-success" style="font-size: 20px;">
                               
                            </center><br>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </form>
  
    <script>

        var stateObject = {
            "TamilNadu": {
                "Chennai": ["Ambattur", "Guindy", "Chennai"],
                "Coimbatore": ["Pollachi", "Annur", "Coimbatore"],
                "Sivagangai": ["Sivagangai", "Karaikudi", "Tiruppattur"],
                "Thanjavur": ["Thanjavur", "Kumbakonam", "Pattukkotai"],
                "Pudukkottai": ["Thirumayam", "Aranthangi", "Pudukkottai"],

            },
            "Kerala": {
                "Munnar": ["Palakkad", "Malappuram", "Thrissur", "Wayanad", "Kollam", "Kannur"],
                "Kochi": ["Palakkad", "Malappuram", "Thrissur", "Wayanad", "Kollam", "Kannur"],
                "Varkala": ["Palakkad", "Malappuram", "Thrissur", "Wayanad", "Kollam", "Kannur"],
                "Thiruvananthapuram": ["Palakkad", "Malappuram", "Thrissur", "Wayanad", "Kollam", "Kannur"],
                "Kannur": ["Palakkad", "Malappuram", "Thrissur", "Wayanad", "Kollam", "Kannur"],
            },
            "Karnataka": {
                "Bangaluru": ["Udupi", "Ballary", "Belagavi", "Yadgiri", "Vijayanagara"],
                "Mysore": ["Udupi", "Ballary", "Belagavi", "Yadgiri", "Vijayanagara"],
                "Gokarna": ["Udupi", "Ballary", "Belagavi", "Yadgiri", "Vijayanagara"],
                "Belgaum": ["Udupi", "Ballary", "Belagavi", "Yadgiri", "Vijayanagara"],
                "Mangalore": ["Udupi", "Ballary", "Belagavi", "Yadgiri", "Vijayanagara"],
            },
            "Goa": {
                "Panaji": ["North Goa", "South Goa"],
                "Mormugao": ["North Goa", "South Goa"],
                "Mapusa": ["North Goa", "South Goa"],
                "Bichalim": ["North Goa", "South Goa"],
                "Canacona": ["North Goa", "South Goa"],
            },
            "Bihar": {
                "Patna": ["Arwal", "Banka", "Bhojpur", "Araria", "Munger"],
                "Bhagalpur": ["Arwal", "Banka", "Bhojpur", "Araria", "Munger"],
                "Gaya": ["Arwal", "Banka", "Bhojpur", "Araria", "Munger"],
                "Muzaffarpur": ["Arwal", "Banka", "Bhojpur", "Araria", "Munger"],
                "Arrah": ["Arwal", "Banka", "Bhojpur", "Araria", "Munger"],
            },
        }
        window.onload = function () {
            var stateSel = document.getElementById("stateSel"),
                districtSel = document.getElementById("districtSel"),
                citySel = document.getElementById("citySel");
            for (var state in stateObject) {
                stateSel.options[stateSel.options.length] = new Option(state, state);
            }
            stateSel.onchange = function () {
                districtSel.length = 1;
                citySel.length = 1;
                if (this.selectedIndex < 1) return;
                for (var district in stateObject[this.value]) {
                    districtSel.options[districtSel.options.length] = new Option(district, district);
                }
            }
            stateSel.onchange();
            districtSel.onchange = function () {
                citySel.length = 1;
                if (this.selectedIndex < 1) return;
                var city = stateObject[stateSel.value][this.value];
                for (var i = 0; i < city.length; i++) {
                    citySel.options[citySel.options.length] = new Option(city[i], city[i]);
                }
            }
        }
    </script>
    <script type="text/javascript">
        window.history.forward();
        function noBack() {
            window.history.forward();
        }

    </script>

</body>

</html>""")

# q="""create database project"""
# q = """create table empregister(id int(50) Auto_increment primary key,id_number varchar(50),name varchar(50),email varchar(50),date_of_birth varchar(50),date_of_joining varchar(50),marital_status varchar(50),destination varchar(50),contact_no varchar(50),phone_no varchar(50),id_proof varchar(50),upload_id_proof varchar(50),upload_photo varchar(50),gender varchar(50),address varchar(50),state varchar(50),district varchar(50),city varchar(50),salary varchar(50),qualification varchar(50))"""
# cur.execute(q)
f = cgi.FieldStorage()
if len(f) != 0:
    id1=f.getvalue("id")
    name = f.getvalue("name")
    email = f.getvalue("email")
    dob = f.getvalue("dob")
    doj = f.getvalue("doj")
    marital = f.getvalue("marital")
    des=f.getvalue("des")
    cno = f.getvalue("cno")
    pno = f.getvalue("pno")
    idproof = f.getvalue("idproof")
    idimage = f['uidproof']
    upphotoo = f['uphoto']
    gender = f.getvalue("gender")
    address = f.getvalue("address")
    state = f.getvalue("state")
    district = f.getvalue("district")
    city = f.getvalue("city")
    salary=f.getvalue("salary")
    qua=f.getvalue("qua")
    uname="0000"
    upass="0000"
    active="Active"


    if idimage.filename:
        img = os.path.basename(idimage.filename)
        photo = os.path.basename(upphotoo.filename)
        open("empphoto/" + img, "wb").write(idimage.file.read())
        open("empphoto/" + photo, "wb").write(upphotoo.file.read())
        q = """insert into empregister(id_number,name,email,date_of_birth,date_of_joining,marital_status,destination,contact_no,phone_no,id_proof,upload_id_proof,upload_photo,gender,address,state,district,city,salary,qualification,username,password,status)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (id1,name, email, dob, doj, marital,des, cno, pno, idproof, img, photo, gender, address, state, district, city,salary,qua,uname,upass,active)
        cur.execute(q)
        print("""<script>alert("Register successfully")</script>""")
conn.commit()
conn.close()




