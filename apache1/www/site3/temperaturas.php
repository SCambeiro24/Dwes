<!DOCTYPE html>
<head>
    <title>Conversor de Temperaturas</title>
</head>
<body>
    <h1>Conversor de Temperaturas</h1>
    <form method="post">
        <label for="cantidad">Temperatura:</label>
        <input type="number" step="0.1" name="cantidad" id="cantidad" required>
        <p>
            <label><input type="radio" name="conversion" value="CtoF" required> Celsius → Fahrenheit</label><br>
            <label><input type="radio" name="conversion" value="FtoC"> Fahrenheit → Celsius</label>
        </p>
        <input type="submit" value="Convertir">
    </form>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $cantidad = floatval($_POST["cantidad"]);
        $conversion = $_POST["conversion"];

        if ($conversion == "CtoF") {
            $resultado = ($cantidad * 9/5) + 32;
            echo "<p>$cantidad ºC = " . round($resultado, 2) . " ºF</p>";
        } else {
            $resultado = ($cantidad - 32) * 5/9;
            echo "<p>$cantidad ºF = " . round($resultado, 2) . " ºC</p>";
        }
    }
    ?>
</body>
</html>
