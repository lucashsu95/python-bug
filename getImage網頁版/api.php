<?php
$data = json_decode(file_get_contents('php://input'), true);
$value = urldecode($data['value']);
$result = exec("python getImage.py $value");
$result_array = json_decode($result, true);
echo json_encode($result_array);
?>

