<?php
/**
 * register.php
 *
 * Recibe POST del formulario register.html, valida datos,
 * verifica que el email no exista, hashea la contraseña y
 * crea un nuevo usuario en tUsuarios. Redirige a main.php al éxito.
 *
 * Buenas prácticas empleadas:
 * - Sentencias preparadas (evitan SQL injection)
 * - password_hash para almacenar contraseñas
 * - Validaciones de campos vacíos y comprobación de coincidencia de contraseñas
 */

// ================================
// Configuración / Conexión a BD
// ================================
$db_host = 'localhost';
$db_user = 'root';
$db_pass = '1234';
$db_name = 'mysitedb';

$db = new mysqli($db_host, $db_user, $db_pass, $db_name);
if ($db->connect_errno) {
    // En producción no mostrar detalles, aquí se informa para el ejercicio
    die('Error de conexión a la base de datos: ' . $db->connect_errno);
}

// ================================
// Recuperar y sanitizar entrada
// ================================
$nombre   = isset($_POST['nombre'])   ? trim($_POST['nombre'])   : '';
$apellidos= isset($_POST['apellidos'])? trim($_POST['apellidos']): '';
$email    = isset($_POST['email'])    ? trim($_POST['email'])    : '';
$pass1    = isset($_POST['pass1'])    ? $_POST['pass1']          : '';
$pass2    = isset($_POST['pass2'])    ? $_POST['pass2']          : '';

// ================================
// Validaciones (lado servidor)
// ================================
if ($nombre === '' || $apellidos === '' || $email === '' || $pass1 === '' || $pass2 === '') {
    die('Error: Todos los campos son obligatorios.');
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    die('Error: El correo electrónico no tiene un formato válido.');
}

if ($pass1 !== $pass2) {
    die('Error: Las contraseñas no coinciden.');
}

// ================================
// Comprobar si el correo ya existe
// ================================
$stmt = $db->prepare("SELECT id FROM tUsuarios WHERE email = ?");
if (!$stmt) {
    die('Error en la preparación de la consulta.');
}
$stmt->bind_param("s", $email);
$stmt->execute();
$stmt->store_result();

if ($stmt->num_rows > 0) {
    // El correo ya está registrado
    $stmt->close();
    $db->close();
    die('Error: El correo ya está registrado.');
}
$stmt->close();

// ================================
// Insertar nuevo usuario (con password_hash)
// ================================
$password_hash = password_hash($pass1, PASSWORD_DEFAULT);

$stmt = $db->prepare("INSERT INTO tUsuarios (nombre, apellidos, email, contraseña) VALUES (?, ?, ?, ?)");
if (!$stmt) {
    die('Error en la preparación de la inserción.');
}
$stmt->bind_param("ssss", $nombre, $apellidos, $email, $password_hash);

if ($stmt->execute()) {
    $stmt->close();
    $db->close();
    // Registro correcto: redirigimos a main.php (puedes cambiar la ruta)
    header("Location: main.php");
    exit;
} else {
    // Error al insertar
    $err = $stmt->error;
    $stmt->close();
    $db->close();
    die('Error al registrar el usuario: ' . htmlspecialchars($err));
}
?>

