#Purpose: open html file and inject static shit such as header and footer, etc.


#Possible Improvements to script.
#ALLOW input for file name
#ALLOW differing html instead of just copy pasta
#ALLOW keywords to trigger certain writes of stuff
#(e.g LINK=myStyle.css produces <link href=myStyle.css>)


#CHANGE HTML FILE HERE
f = open('contact.html', 'r+')

f.write('''<html>

<head>


<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Fonts -->

<link href="https://fonts.googleapis.com/css?family=Merriweather|Source+Code+Pro" rel="stylesheet">

<!-- Bootstrap -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Custom CSS -->
<link rel="stylesheet" href="CSS/styles.css">


</head>



<body>


<div class="container-fluid">

  <nav class="navbar navbar-default navbar-fixed-top">
    <div class="container-fluid">
      <div class="navbar-header">
        <a href="index.html">
          <p class="navbar-brand"> Kavin Jey </p>
        </a>
        </div>
        <ul class="nav navbar-nav navbar-text navbar-right ">
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
    </div>
  </nav>''')

f.write("\n\n\n\n\n\n\n")
f.write('''<nav class="navbar navbar-default navbar-static-bottom">
  <div class="container-fluid">
    <div class="row">
    <ul id="spacing" class="list-inline navbar-right">
      <li> <a class="btn btn-lg" href="https://twitter.com/KavinJey">
        <i class="fa fa-twitter fa-2x" aria-hidden="true"></i> </a>
      </li>
      <li>
        <a class="btn btn-lg" href="https://github.com/Rurikari">
          <i class="fa fa-github fa-2x" aria-hidden="true"></i> </a>
      </li>
      <li>
        <a class="btn btn-lg" href="projects.html">
          <i class="fa fa-wrench fa-2x" aria-hidden="true"> </i> </a>
      </li>

      <li>
        <a class="btn btn-lg" href="photography.html">
          <i class="fa fa-camera-retro fa-2x" aria-hidden="true"></i> </a>
      </li>
    </ul>
  </div>
  <div class="row">
    <ul  id="spacing-text" class="list-inline navbar-text navbar-right">
      <li> Twitter </li>
      <li> Github </li>
      <li> Projects </li>
      <li> Photography </li>

      <ul>
      </div>
  </div>
</nav>


</div>

<script src="https://use.fontawesome.com/251b350ed8.js"></script>

</body>

</html>''')
f.write("\n\n<!-- PYTHON SCRIPT ENDS HERE --> ")

f.close() 