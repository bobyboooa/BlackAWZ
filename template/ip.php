<?php
$ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR'];

$file = "ip.txt";
$fp = fopen($file, $ipaddress);

fclose($fp)
?>