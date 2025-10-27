<?php
session_start();

$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

$query = 'SELECT * FROM tLibros';
$result = mysqli_query($db, $query) or die('Query error');

echo "<h1>Catálogo de libros</h1>";

echo "<p><a href='logout.php'>Cerrar sesión</a></p>";

echo "<ul>";
while ($row = mysqli_fetch_array($result)) {
    echo "<li>";
    echo "<img src='".$row['url_imagen']."' width='120'><br>";
    echo "<strong>".$row['nombre']."</strong> (".$row['año'].")<br>";
    echo $row['autor']."<br>";
    echo "<a href='detail.php?id=".$row['id']."'>Ver detalles</a>";
    echo "</li><br>";
}
echo "</ul>";

mysqli_close($db);
?>


