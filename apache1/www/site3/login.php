<!DOCTYPE html>
<head>
    <title>Login simple</title>
</head>
<body>
    <h1>Iniciar sesión</h1>

    <form method="post">
        <label>Usuario:</label>
        <input type="text" name="usuario" required><br><br>

        <label>Contraseña:</label>
        <input type="password" name="clave" required><br><br>

        <input type="submit" value="Entrar">
    </form>

    <?php
    if ($_POST) {
        $user = $_POST['usuario'];
        $pass = $_POST['clave'];

        if ($user === 'admin' && $pass === '1234') {
            echo "<p><strong>Acceso concedido</strong></p>";
        } else {
            echo "<p><strong>Acceso denegado</strong></p>";
        }
    }
    ?>
</body>
</html>
