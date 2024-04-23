
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
                a.textContent = data[livre].nom_oeuvre;
                b.imageContent = data[livre].image
                // Construire le lien avec les paramètres d'URL corrects
                a.href = `Branch_page.html?nom=${encodeURIComponent(data[livre].nom_oeuvre)}&description=${encodeURIComponent(data[livre].description)}&URL=${encodeURIComponent(data[livre].URL)}`;
                li.appendChild(a);
                book.appendChild(li);
            });
        })
        .catch(error => console.error('Erreur lors du chargement des livres:', error));
});



function rechercherEtSupprimerMots() {
    motRecherche = document.getElementById('searchbar').value
    var book = document.getElementById('book');
    var elements = book.getElementsByTagName('p');
    
    for (var i = 0; i < elements.length; i++) {
      var texte = elements[i].innerText;
      
      if (texte.includes(motRecherche)) {
        elements[i].style.display = 'block'; // Affiche l'élément s'il contient le mot recherché
      } else {
        elements[i].style.display = 'none'; // Masque l'élément s'il ne contient pas le mot recherché
      }
    }
  }



