<?php
$user = $_POST["username"];
$pass = $_POST["password"];
$data["dev"][] = array("username" =>$user,
"password" =>$pass);

$jsondata = json_encode($data);
$f = fopen("username.json", "w");
fwrite($f, $jsondata);
fclose($f);

exit();
?>
