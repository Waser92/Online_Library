
document.addEventListener("DOMContentLoaded", function() {
    fetch('Main_Data.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Erreur lors du chargement du fichier JSON');
            }
            return response.json();
        })
        .then(data => {
            if (!data || Object.keys(data).length === 0) {
                throw new Error('Aucune donnée de livre trouvée dans le fichier JSON');
            }
            createCheckboxes(data, 'genre', 'genres-container');
            createCheckboxes(data, 'auteur', 'auteurs-container');
            createCheckboxes(data, 'siècle', 'siecles-container');
            displayBooks(data);
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

function createCheckboxes(data, key, containerId) {
    const container = document.getElementById(containerId);
    const uniqueValues = new Set();
    
    Object.keys(data).forEach(livre => {
        uniqueValues.add(data[livre][key]);
    });

    uniqueValues.forEach(value => {
        const label = document.createElement('label');
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.name = key;
        checkbox.value = value;
        checkbox.onchange = filterBooks;

        label.appendChild(checkbox);
        label.appendChild(document.createTextNode(value));
        container.appendChild(label);
        container.appendChild(document.createElement('br'));
    });
}

function displayBooks(data) {
    const book = document.getElementById('book');
    const sortedBooks = Object.keys(data).sort((a, b) => {
        return data[a].nom_oeuvre.localeCompare(data[b].nom_oeuvre);
    });

    sortedBooks.forEach(livre => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        const br = document.createElement('br');
        const imagejavascript = document.createElement("img");

        a.textContent = data[livre].nom_oeuvre;
        imagejavascript.src = data[livre].image;
        imagejavascript.width = 80;
        imagejavascript.height = 120;

        a.href = `Branch_page.html?nom=${encodeURIComponent(data[livre].nom_oeuvre)}&description=${encodeURIComponent(data[livre].description)}&URL=${encodeURIComponent(data[livre].URL)}`;

        const imageLink = document.createElement('a');
        imageLink.href = a.href;
        imageLink.appendChild(imagejavascript);

        li.appendChild(a);
        li.appendChild(br);
        li.appendChild(imageLink);
        book.appendChild(li);
    });
}

function filterBooks() {
    fetch('Main_Data.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Erreur lors du chargement du fichier JSON');
            }
            return response.json();
        })
        .then(data => {
            if (!data || Object.keys(data).length === 0) {
                throw new Error('Aucune donnée de livre trouvée dans le fichier JSON');
            }

            const book = document.getElementById('book');
            const elements = book.getElementsByTagName('li');
            const selectedGenres = getSelectedValues('genre');
            const selectedAuteurs = getSelectedValues('auteur');
            const selectedSiecles = getSelectedValues('siècle');

            if (selectedGenres.length === 0 && selectedAuteurs.length === 0 && selectedSiecles.length === 0) {
                Array.from(elements).forEach(li => {
                    li.style.display = 'block';
                });
                return;
            }

            Object.keys(data).forEach((livre, index) => {
                const genre = data[livre].genre;
                const auteur = data[livre].auteur;
                const siecle = data[livre].siècle;
                const li = elements[index];

                const genreMatch = selectedGenres.length === 0 || selectedGenres.includes(genre);
                const auteurMatch = selectedAuteurs.length === 0 || selectedAuteurs.includes(auteur);
                const siecleMatch = selectedSiecles.length === 0 || selectedSiecles.includes(siecle);

                if (genreMatch && auteurMatch && siecleMatch) {
                    li.style.display = 'block';
                } else {
                    li.style.display = 'none';
                }
            });
        })
        .catch(error => console.error('Erreur lors du filtrage des livres:', error));
}

function getSelectedValues(name) {
    const checkboxes = document.querySelectorAll(`input[name="${name}"]:checked`);
    return Array.from(checkboxes).map(cb => cb.value);
}