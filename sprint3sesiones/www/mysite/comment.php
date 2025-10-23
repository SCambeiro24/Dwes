<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

$new_comment = $_POST['new_comment'];
$libro_id = $_POST['libro_id'];

$query = "INSERT INTO tComentarios (comentario, libro_id) VALUES ('$new_comment', $libro_id)";
mysqli_query($db, $query) or die('Error al insertar comentario');

$new_id = mysqli_insert_id($db);
echo "<p>Comentario añadido con ID: $new_id</p>";
echo "<a href='/detail.php?id=$libro_id'>Volver al libro</a>";

mysqli_close($db);
?>

