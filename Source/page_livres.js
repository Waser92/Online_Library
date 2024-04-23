function envoyerMail() {
    var email = document.getElementById("email").value;
    var subject = "Sujet de l'e-mail";
    var body = "Contenu de l'e-mail";

    var mailto_link = 'mailto:' + email + '?subject=' + subject + '&body=' + body;
    win = window.open(mailto_link, 'emailWindow');
    if (win && win.open && !win.closed) win.close();
}