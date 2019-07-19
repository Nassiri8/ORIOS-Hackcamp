<?php

$input = "2A4C10L30D";

function decodeString($input)
{
    $i = 0;
    $y = 0;
    $n = 0;
    preg_match_all('/\d+\D/', $input, $tab); 
    while($i < sizeof($tab))
    {
        while($y < sizeof($tab[$i]))
        {
            while($n< strlen($tab[$i][$y]))
            {
                if(is_numeric($tab[$i][$y][$n]))
                {
                    $compt = $tab[$i][$y][$n];
                }
                if(!is_numeric($tab[$i][$y][$n]))
                {
                    $letter = $tab[$i][$y][$n];
                }
                $final = str_repeat($letter, $compt);
                echo $final;
            $n++;
            }
            $y++;
            $n =0;
        }
        $i++;
    }
}

decodeString($input);