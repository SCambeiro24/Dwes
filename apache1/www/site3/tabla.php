<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>Tabla de multiplicar del 7</title>
    <style>
        table { border-collapse: collapse; margin: 20px; }
        th, td { border: 1px solid #333; padding: 8px 12px; text-align: center; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Tabla de multiplicar del 7</h1>
    <table>
        <tr>
            <th>Operación</th>
            <th>Resultado</th>
        </tr>
        <?php
            for ($i = 1; $i <= 10; $i++) {
                echo "<tr><td>7 x $i</td><td>" . (7 * $i) . "</td></tr>";
            }
        ?>
    </table>
</body>
</html>
