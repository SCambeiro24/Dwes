<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

if (!isset($_GET['id'])) {
    die('No se ha especificado un libro');
}

$id = $_GET['id'];
$query = 'SELECT * FROM tLibros WHERE id='.$id;
$result = mysqli_query($db, $query) or die('Query error');
$only_row = mysqli_fetch_array($result);

echo "<h1>".$only_row['nombre']."</h1>";
echo "<img src='".$only_row['url_imagen']."' width='200'><br>";
echo "<h2>".$only_row['autor']."</h2>";
echo "<h3>".$only_row['año']."</h3>";

echo "<h3>Comentarios:</h3>";
echo "<ul>";

$query2 = 'SELECT * FROM tComentarios WHERE libro_id='.$id;
$result2 = mysqli_query($db, $query2) or die('Query error');
while ($row = mysqli_fetch_array($result2)) {
    echo "<li>".$row['comentario']."</li>";
}
echo "</ul>";

mysqli_close($db);
?>
