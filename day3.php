<?php

$text = file_get_contents('input3.txt');

// Function to check if a coordinate is valid within the bounds of the engine schematic
function isValidCoordinate($x, $y, $width, $height) {
    return $x >= 0 && $x < $height && $y >= 0 && $y < $width;
}

// Function to parse the engine schematic and calculate the sum of part numbers adjacent to symbols
function calculatePartNumberSum($input) {
    // Split the input into lines
    $lines = explode("\n", $input);
    $height = count($lines);
    $width = strlen($lines[0])-1;
    $sum = 0;

    // Iterate through each cell in the engine schematic
    for ($x= 0; $x < $height; $x++) {
        for ($y= 0; $y < $width; $y++) {
            $char = $lines[$x][$y];
            // If the character is a digit, check if it is adjacent to a symbol
            if (ctype_digit($char)) {
                $number = $char;
                $adjacentToSymbol = false;
                // Check for multi-digit numbers
                while ($y + 1 < $width && ctype_digit($lines[$x][$y + 1])) {
                    $number .= $lines[$x][++$y];
                }
                // Check adjacent cells for symbols
                for ($dx = -1; $dx <= 1; $dx++) {
                    for ($dy =-strlen($number); $dy <= 1; $dy++) {
                        $nx = $x + $dx;
                        $ny = $y + $dy;
                        if (isValidCoordinate($nx, $ny, $width, $height) && $lines[$nx][$ny] !== '.' && !ctype_digit($lines[$nx][$ny])) {
                            $adjacentToSymbol = true;
                             echo " $number<br>";
                            break 2; // Exit both loops
                        }

                    }
                }
                if ($adjacentToSymbol) {
                   
                    $sum += intval($number);
                }
            }
        }
    }
    return $sum;
}

$sum = calculatePartNumberSum($text);
echo "Total Sum: $sum";

?>
