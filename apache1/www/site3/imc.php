<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Cálculo del IMC</title>
</head>
<body>
    <h1>Calculadora de IMC</h1>
    <?php
    function calcular_imc($peso, $altura) {
        if ($altura <= 0) {
            return null;
        }
        return $peso / ($altura * $altura);
    }

    if (isset($_GET['peso']) && isset($_GET['altura'])) {
        $peso = floatval($_GET['peso']);
        $altura = floatval($_GET['altura']);
        $imc = calcular_imc($peso, $altura);

        if ($imc !== null) {
            echo "<p>Peso: {$peso} kg</p>";
            echo "<p>Altura: {$altura} m</p>";
            echo "<p>IMC: " . number_format($imc, 2) . "</p>";

            if ($imc < 18.5) {
                echo "<p><strong>Resultado:</strong> Bajo peso</p>";
            } elseif ($imc < 25) {
                echo "<p><strong>Resultado:</strong> Normal</p>";
            } else {
                echo "<p><strong>Resultado:</strong> Sobrepeso</p>";
            }
        } else {
            echo "<p>Error: altura no válida.</p>";
        }
    } else {
        echo "<p>Por favor, proporciona los parámetros <code>peso</code> y <code>altura</code> en la URL.</p>";
        echo "<p>Ejemplo: <a href='imc.php?peso=70&altura=1.75'>imc.php?peso=70&altura=1.75</a></p>";
    }
    ?>
</body>
</html>
