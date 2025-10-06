<!DOCTYPE html>
<head>
   <title>Calculadora  </title>
</head>
<body>
     <h1> Calculadora </h1>
    <form method="post">
        <input type="number" name="num1" step="any" required> 
        <select name="op">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type="number" name="num2" step="any" required>
        <input type="submit" value="Calcular">
    </form>

    <?php
    if ($_POST) {
        $a = $_POST['num1'];
        $b = $_POST['num2'];
        $op = $_POST['op'];

        if ($op == '/' && $b == 0) {
            echo "<p><strong>Error:</strong> No se puede dividir entre 0.</p>";
        } else {
            switch ($op) {
                case '+': $res = $a + $b; break;
                case '-': $res = $a - $b; break;
                case '*': $res = $a * $b; break;
                case '/': $res = $a / $b; break;
            }
            echo "<p>$a $op $b = " . round($res, 2) . "</p>";
        }
    }
    ?>
</body>
</html>

