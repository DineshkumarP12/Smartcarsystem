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
    <div class="content">
        <div class="col-md-3"></div>


        <div class="col-md-8">
            <br><br><br><br>
            <center>
                 
                <img src="./media/avatar7.png" alt="Admin" class="rounded-circle"
                    width="150">
                <h1 class="my-3">Admin</h1>
            </center>


        </div>
    </div>
</body>

</html>""")