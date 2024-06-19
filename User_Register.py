#!C:\Users\Personal\AppData\Local\Programs\Python\Python310\python.exe
print("content-type:text/html \r\n\r\n")

print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>uregister</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <style>
        .n {
            background-color: slategrey;
            text-align: center;
            margin-left: -15px;
            margin-right: -15px;
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
        #form{
        width:100%;
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
 <form action="" method="post"  enctype="multipart/form-data" id="form">
    <div class="container">
        <div class="form">
            <div class="navbar navbar-default n">
                <h1><span class="glyphicon glyphicon-user"></span> User Registration</h1>
            </div>
            <div class="form-content">
                <div class="row">
                    <div class="col-md-6">
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Name" name="name" required>
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
                            <input type="text" class="form-control" placeholder="UserName" id="pass" name="uname">
                        </div>
                        <div class="form-group">
                            <input type="password" class="form-control" placeholder="Password" name="password">
                        </div>
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Contact Number" name="cno" required>
                        </div>
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Phone Number" name="pno">
                        </div>
                    </div>

                    <div class="col-md-6">
                        <div class="form-group" >
                            <select class="form-control" name="id proof">
                                <option>ID Proof</option>
                                <option>Aadhaar Card</option>
                                <option>Pan Card</option>
                                <option>Voter Id</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <input type="text" class="form-control" onfocus="(this.type='file')"
                                placeholder="Upload ID Proof" required name="id photo">
                        </div>
                        <div class="form-group">
                            <input type="text" class="form-control" onfocus="(this.type='file')"
                                placeholder="Upload photo" name="up photo" required>
                        </div>
                        <div class="form-group" style="color:black; font-size: 25px;">
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
                            <select class="col-md-6" style="height: 30px;" name="state" id="stateSel">
                                <option selected="selected">Select State</option>

                            </select>


                            <select class="col-md-6" style="height: 30px;" name="district" id="districtSel">
                                <option selected="selected">Select District</option>

                            </select>
                            <br><br>
                            <select class="form-control" name="city" id="citySel" size="1">
                                <option selected="selected">Select City</option>

                            </select>
                        </div><br><br>

                    </div>
                    <center>
                        <input  type="submit" name="submit" class="btn-success" 
                             style="font-size: 20px;"><br><br>
                        <button>
                            <a href="#" data-toggle="modal" data-target="#mymodal"> Existing
                                User Click Here to Login</a>
                        </button>
                    </center>

                    <br><br>
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
    <center>
        <div class="modal" id="mymodal">
            <div class="modal-dialog">
                <div class="modal-content" id="color">
                    <div class="modal-header">
                        <a href="./Index_page.py"> <button type="button" class="close">&times;</button></a>
                        <h3 class="modal-title" id="log">
                            <center><span class="glyphicon glyphicon-user"></span> User Login</center>
                        </h3>
                        <br><br><br>
                        <form action="" autocomplete="off">
                            <div>
                                <input type="text" class="form-control" id="name1" placeholder="UserName" name="user">
                                <br>
                                <input type="password" class="form-control" id="password1" placeholder="Password"
                                    name="ps">
                                <div class="btoggle"> <button type="button" class="toggle" id="btoggle"><span
                                            class="glyphicon glyphicon-eye-open" id="eyeicon"></span></button></div><br>
                                <a href="#" class="a" data-toggle="modal" data-target="#forgot">Forgot
                                    password?</a><br><br><br>

                                <input type="submit" class="btn btn-success" name="login" value="Submit">
                                <br><br><br>
                                <center><a href="#" class="aa">New user click here to Register</a>
                                </center>
                            </div>
                    </div>
                </div>
            </div>
        </div>
    </center>
    <center>
        <div class="modal" id="forgot" style="height: 450px;">
            <div class="modal-dialog">
                <div class="modal-content" style="background-color: white;">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                        <center><br><br>
                            <h1 class="modal-title"> Forget Password ?
                            </h1><br>
                            <div style="color: black; font-size: 15px; margin-left: -10px;">Enter your email to reset
                                your
                                password.</div>
                            <br><br><br>
                            <form action="" autocomplete="off">
                                <div id="center">
                                    <input type="email" class="form-control" id="email" placeholder="Email@id" name="email1">
                                    <br><br>
                                    <button type="submit" onclick="forgot()" class="btn btn-success" value="submit" name="submit1" >Submit</button>
                                </div>
                            </form>
                        </center>
                    </div>
                </div>
            </div>
        </div>
    </center>

    <script>
        let passwordInput = document.getElementById('password'),
            toggle = document.getElementById('btoggle')
        icon = document.getElementById('eyeicon');
        function togglePassword() {
            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                icon.classList.add("glyphicon-eye-close");

            } else {
                passwordInput.type = "password";
                icon.classList.remove("glyphicon-eye-close")

            }
        }
        function checkInput() {

        }
        toggle.addEventListener('click', togglePassword, false);
        passwordInput.addEventListener('keyup', checkInput, false);

    </script>
    <script>
        function changeuser() {
            val = document.getElementById("email").value;
            document.getElementById("pass").value = val;

        }
         </script>
</body>
</html>
   """)
import pymysql
import cgi, cgitb, os

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = conn.cursor()
# q="""create database project"""
# q = """create table uregister(id int(50) Auto_increment primary key,name varchar(50),email varchar(50),date_of_birth varchar(50),username varchar(50),password varchar(50),contact_no varchar(50),phone_no varchar(50),id_proof varchar(50),upload_id_proof varchar(50),upload_photo varchar(50),gender varchar(50),address varchar(50),state varchar(50),district varchar(50),city varchar(50))"""
# cur.execute(q)
f = cgi.FieldStorage()
Reg=f.getvalue("submit")
if Reg!=None:
    if len(f) != 0:
        name = f.getvalue("name")
        email = f.getvalue("email")
        dob = f.getvalue("dob")
        uname = f.getvalue("uname")
        password = f.getvalue("password")
        cno = f.getvalue("cno")
        pno = f.getvalue("pno")
        idproof = f.getvalue("id proof")
        idphoto = f['id photo']
        upphoto = f['up photo']
        gender = f.getvalue("gender")
        address = f.getvalue("address")
        state = f.getvalue("state")
        district = f.getvalue("district")
        city = f.getvalue("city")


        if idphoto.filename:
            fn = os.path.basename(idphoto.filename)
            gn = os.path.basename(upphoto.filename)
            open("userphoto/" + fn, "wb").write(idphoto.file.read())
            open("userphoto/" + gn, "wb").write(upphoto.file.read())
            q = """insert into uregister(name,email,date_of_birth,username,password,contact_no,phone_no,id_proof,upload_id_proof,upload_photo,gender,address,state,district,city)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (name, email, dob, uname, password, cno, pno, idproof, fn, gn, gender, address, state, district, city)
            cur.execute(q)
            print("""<script>alert("Register successfully")</script>""")



name=f.getvalue("user")
password=f.getvalue("ps")
submit=f.getvalue("login")
if submit != None:
    q1 = """select * from uregister where username='%s' and password='%s' """ % (name,password)
    cur.execute(q1)
    print("""<script>
    alert("login successfully");
    </script>""")


uemail1=f.getvalue("email1")
submit1=f.getvalue("submit1")
if submit1 != None:
    q1="""select Id from uregister where email='%s' """ %(uemail1)
    cur.execute(q1)
    idvalue=cur.fetchone()
    q2="""select * from uregister where id=%s """ %(idvalue)
    cur.execute(q2)
    rec=cur.fetchall()
    for i in rec:
        Name = i[1]
        email4 = i[2]
        username2 = i[4]
        password2 = i[5]
        contact = i[6]
        photo = i[10]
        status="New"

        # print(Name)
        q4="""insert into userforget(name,email,username,password,contact_no,upload_photo,status)values('%s','%s','%s','%s','%s','%s','%s')""" % (Name,email4,username2,password2,contact,photo,status)
        cur.execute(q4)
        print("""<script>alert("request submit success");</script>""")
    else:
        print("""<script>alert("Enter your valid data");</script>""")



conn.commit()
conn.close()




