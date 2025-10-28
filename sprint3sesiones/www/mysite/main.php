<?php
session_start();
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

$query = 'SELECT * FROM tLibros';
$result = mysqli_query($db, $query) or die('Query error');
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Catálogo de libros</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
        }

        h1 {
            color: #333;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        li {
            background: white;
            margin: 15px auto;
            padding: 20px;
            width: 300px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.4s ease, box-shadow 0.4s ease, opacity 0.4s ease;
            opacity: 0.9;
        }

        li:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            opacity: 1;
        }

        img {
            border-radius: 8px;
            transition: opacity 0.4s ease;
        }

        img:hover {
            opacity: 0.8;
        }

        a {
            text-decoration: none;
            color: #1a73e8;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Catálogo de libros</h1>

    <?php
    if (isset($_SESSION['user_id'])) {
        echo "<p>Usuario conectado | <a href='logout.php'>Cerrar sesión</a></p>";
    } else {
        echo "<p><a href='login.html'>Iniciar sesión</a> | <a href='register.html'>Registrarse</a></p>";
    }
    ?>

    <ul>
        <?php
        while ($row = mysqli_fetch_array($result)) {
            echo "<li>";
            echo "<img src='".$row['url_imagen']."' width='120'><br>";
            echo "<strong>".$row['nombre']."</strong> (".$row['año'].")<br>";
            echo $row['autor']."<br>";
            echo "<a href='detail.php?id=".$row['id']."'>Ver detalles</a>";
            echo "</li>";
        }
        ?>
    </ul>
</body>
</html>
<?php
mysqli_close($db);
?>

