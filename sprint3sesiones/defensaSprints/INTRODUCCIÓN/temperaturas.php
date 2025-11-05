
<html>
  <body>
    <h1>Conversión de temperaturas</h1>
    <?php
    /* Arregla el código para que convierta las temperaturas */
    if (isset($_POST["cantidad"]) && isset($_POST["conversion"])) {
        $cantidad = $_POST["cantidad"];
        $conversion = $_POST["conversion"];

        if (empty($cantidad)) {
          echo "Debes introducir una cantidad.<br>";
        } elseif (empty($conversion)) {
          echo "Debes seleccionar una conversión.<br>";
        } else {
           if ($conversion == "aF") {
            $resultado = $cantidad * 9/5 + 32;
            echo $cantidad . " ºC = " . round($resultado, 2) . " ºF";
          } elseif ($conversion == "aC") {
            $resultado = ($cantidad - 32) * 5/9;
            echo $cantidad . " ºF = " . round($resultado, 2) . " ºC";
          } else {
            echo "Opción no válida.";
          }
        }
      }
    ?>

    <form action="/temperaturas.php" method="post">
      <label for="cantidad">Cantidad:</label><br>
      <input type="text" id="cantidad" name="cantidad" ><br>

      <input type="radio" id="aF" name="conversion" value="aF">
      <label for="aF">Celsius → Fahrenheit</label><br>

      <input type="radio" id="aC" name="conversion" value="aC">
      <label for="aC">Fahrenheit → Celsius</label><br><br>

      <input type="submit" value="Convertir">
    </form>
  </body>
</html>
