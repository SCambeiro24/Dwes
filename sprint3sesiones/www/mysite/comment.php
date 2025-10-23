<?php
session_start();

$db = new mysqli('localhost', 'root', '1234', 'mysitedb');
if ($db->connect_errno) {
    die('Error de conexión');
}

$email = isset($_POST['email']) ? trim($_POST['email']) : '';
$password = isset($_POST['password']) ? $_POST['password'] : '';

if ($email === '' || $password === '') {
    die('Error: completa todos los campos.');
}

$stmt = $db->prepare("SELECT id, contraseña FROM tUsuarios WHERE email = ?");
$stmt->bind_param("s", $email);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows === 0) {
    echo "<p style='color:red;'>No existe ningún usuario con ese correo.</p>";
    echo "<p><a href='login.html'>Volver</a></p>";
    exit;
}

$user = $result->fetch_assoc();

if (password_verify($password, $user['contraseña'])) {
    $_SESSION['user_id'] = $user['id'];
    header("Location: main.php");
    exit;
} else {
    echo "<p style='color:red;'>Contraseña incorrecta.</p>";
    echo "<p><a href='login.html'>Volver</a></p>";
}

$stmt->close();
$db->close();
?>

