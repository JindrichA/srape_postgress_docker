function loadJsonAndRender() {
  // Make a request to the Flask endpoint to get the JSON data
  fetch('/get_json_data')
    .then(response => response.json())
    .then(jsonData => {
      // Get the HTML element where we'll render the list
      const listContainer = document.getElementById('list-container');

      // Create a new unordered list element to hold the titles, URLs, and images
      const listElement = document.createElement('ul');

      // Loop through each item in the JSON data and add it to the list
      jsonData.forEach(item => {
        // Create a new list item element
        const listItem = document.createElement('li');

        // Create a new anchor element with the URL and title
        const linkElement = document.createElement('a');
        linkElement.href = item.url;
        linkElement.innerHTML = item.title;

        // Create a new image element with the image URL and alt text
        const imageElement = document.createElement('img');
        imageElement.src = item.image;
        imageElement.alt = item.title;

        // Add the anchor and image elements to the list item
        listItem.appendChild(linkElement);
        listItem.appendChild(imageElement);

        // Add the list item to the list
        listElement.appendChild(listItem);
      });

      // Add the list to the HTML element
      listContainer.appendChild(listElement);
    })
    .catch(error => {
      console.error('Error loading JSON data:', error);
    });
}

      loadJsonAndRender();