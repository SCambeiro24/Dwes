<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

$email = $_POST['email'];
$nueva_password = $_POST['nueva_password'];
$confirmar_password = $_POST['confirmar_password'];

if (empty($email) || empty($nueva_password) || empty($confirmar_password)) {
    die('Por favor, completa todos los campos.');
}

if ($nueva_password !== $confirmar_password) {
    die('Las contraseñas no coinciden.');
}

$query = "SELECT * FROM tUsuarios WHERE email='$email'";
$result = mysqli_query($db, $query);

if (mysqli_num_rows($result) == 0) {
    die('No existe ninguna cuenta con ese correo.');
}

$hashed_new = password_hash($nueva_password, PASSWORD_DEFAULT);
$update = "UPDATE tUsuarios SET password='$hashed_new' WHERE email='$email'";
mysqli_query($db, $update) or die('Error al actualizar la contraseña.');

echo "Contraseña actualizada correctamente. <a href='login.html'>Iniciar sesión</a>";

mysqli_close($db);
?>

