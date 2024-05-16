
document.addEventListener("DOMContentLoaded", function() {
    const book = document.getElementById('book');

    // Charger le fichier JSON des livres
    fetch('Main_Data.json')

        .then(response => {
            if (!response.ok) {
                throw new Error('Erreur lors du chargement du fichier JSON');
            }
            return response.json();
        })
        .then(data => {
            // Vérifier si des données ont été chargées
            if (!data || Object.keys(data).length === 0) {
                throw new Error('Aucune donnée de livre trouvée dans le fichier JSON');
            }

            // Pour chaque livre, créer un élément de liste avec un lien
            Object.keys(data).forEach(livre => {
                const li = document.createElement('li');
                const a = document.createElement('a');
                const imagejavascript = document.createElement("img");
                a.textContent = data[livre].nom_oeuvre;
                imagejavascript.src = data[livre].image
                // Construire le lien avec les paramètres d'URL corrects
                a.href = `Branch_page.html?nom=${encodeURIComponent(data[livre].nom_oeuvre)}&description=${encodeURIComponent(data[livre].description)}&URL=${encodeURIComponent(data[livre].URL)}`;
                li.appendChild(a);
                li.appendChild(imagejavascript);
                book.appendChild(li);
            });
        })
        .catch(error => console.error('Erreur lors du chargement des livres:', error));
});



function rechercherEtSupprimerMots() {
  var motRecherche = document.getElementById('searchbar').value.toLowerCase();
  var book = document.getElementById('book');
  var elements = book.getElementsByTagName('li');

  for (var i = 0; i < elements.length; i++) {
    var texte = elements[i].textContent.toLowerCase();

    if (texte.includes(motRecherche)) {
      elements[i].style.display = 'block'; // Affiche l'élément s'il contient le mot recherché
    } else {
      elements[i].style.display = 'none'; // Masque l'élément s'il ne contient pas le mot recherché
    }
  }
}

function rechercheMot_coche() {
  // Récupérer le mot depuis le bouton sur la page
  const mot = document.getElementById('coche').value.toLowerCase();;
  const a = document.createElement('a');
  var elements = book.getElementsByTagName('li');
  a.textContent = data[livre].genre;


function CocheMots() {
  fetch('Main_Data.json')
  .then(response => {
    if (!response.ok) {
        throw new Error('Erreur lors du chargement du fichier JSON');
    }
    return response.json();
})
.then(data => {
    // Vérifier si des données ont été chargées
    if (!data || Object.keys(data).length === 0) {
        throw new Error('Aucune donnée de livre trouvée dans le fichier JSON');
    }

  var motRecherche = document.getElementById('coche').value;
  Object.keys(data).forEach(livre => {
    const a = document.createElement('a');
    a.textContent = data[livre].genre;
    var book = document.getElementById('book');
    var elements = book.getElementsByTagName('li');
    var i = 0 
    for (var i = 0; i < a.length; i++) {
      var texte = a[i].textContent.toLowerCase();
      if (texte.includes(motRecherche)){
        elements[i].style.display = 'block';
      } else{
        elements[i].style.display = 'none';
      }
    }
  })
