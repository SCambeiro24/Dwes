<!DOCTYPE html>
<head>
    <title>Carrito de la compra</title>
</head>
<body>
    <h1>Carrito de la compra</h1>
    <?php
        $carrito = array(
            "Manzana" => 0.50,
            "Pan" => 1.20,
            "Leche" => 1.10
        );

        $total = 0;

        echo "<table border='1'>";
        echo "<tr><th>Producto</th><th>Precio (€)</th></tr>";

        foreach ($carrito as $producto => $precio) {
            echo "<tr><td>$producto</td><td>$precio €</td></tr>";
            $total += $precio;
        }

        echo "<tr><td><strong>TOTAL</strong></td><td><strong>$total €</strong></td></tr>";
        echo "</table>";
    ?>
</body>
</html>
