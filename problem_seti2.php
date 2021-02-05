index.php



<html>

  <head> 

   <title>Perfect Number in PHP </title>

  </head>

  <body> 

      <style type="text/css">
  

      body {

        font-family: arial;

            size: 12px;

      };
        </style>

    <?php
    
    $num_values = $_POST['num_val'];

    function CheckPerfect($num) {

  $i = 1;

  $total = 0;



  for($i=1; $i<$num; $i++)

  {

  if($num % $i == 0)

      $total += $i;

} 


  if($total == $num)

    $message = "$num is a perfect number.";

  else

    $message = "$num is not a perfect number.";

     return $message;

    }

   if(isset($_POST['submit'])) {
                

      $results= CheckPerfect($num_values);
      

      }


 if(isset($_POST['clear'])) {

      $num_values = "";

      $results = "";

    }

?>



  <h2> Perfect Number in PHP </h2>

  <p> Mr. Jake Rodriguez Pomperada,MAED-IT, MIT </p>

<form method="post">

   <p>Give a Number <input 

    type="numeric" name="num_val"

     value="<?php echo $num_values; ?>" autofocus required /></p>

      

<input type="submit" name="submit" 

   title="Click here to compute the cube root. "

   value="Submit" />

   

    &nbsp;&nbsp;&nbsp;

    <input type="submit" name="clear" 

    title="Click here to clear the textbox."

    value="Clear" />

</form>



<?php

   echo $results;

?>

</body>

</html>
