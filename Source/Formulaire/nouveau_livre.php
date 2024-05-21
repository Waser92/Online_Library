<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Récupération et traitement des données du formulaire
    $titre = htmlspecialchars($_POST['Titre']);
    $auteur = htmlspecialchars($_POST['auteur']);
    $url = htmlspecialchars($_POST['url']);
    $description = htmlspecialchars($_POST['Description']);
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);

    // Adresse e-mail de destination
    $to = 'votre-email@exemple.com';

    // Sujet de l'e-mail
    $subject = 'Nouvelle proposition de livre';

    // Corps de l'e-mail
    $message = "
    <html>
    <head>
      <title>Nouvelle proposition de livre</title>
    </head>
    <body>
      <h2>Nouvelle proposition de livre</h2>
      <p><strong>Titre de l'oeuvre:</strong> $titre</p>
      <p><strong>Nom de l'auteur:</strong> $auteur</p>
      <p><strong>URL de la couverture:</strong> <a href='$url'>$url</a></p>
      <p><strong>Description:</strong> $description</p>
      <p><strong>E-mail de l'utilisateur:</strong> $email</p>
    </body>
    </html>
    ";

    // En-têtes de l'e-mail
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
    $headers .= "From: <$email>" . "\r\n";

    // Envoi de l'e-mail
    if (mail($to, $subject, $message, $headers)) {
        echo "L'e-mail a été envoyé avec succès.";
    } else {
        echo "Une erreur s'est produite lors de l'envoi de l'e-mail.";
    }
} else {
    echo "Méthode de requête non autorisée.";
}
?>
