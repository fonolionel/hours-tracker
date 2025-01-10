// main.js
fetch('http://127.0.0.1:5000/api/data')
  .then(response => response.json())
  .then(data => {
      console.log(data);
      document.getElementById('data').innerText = `Name: ${data.name}, Role: ${data.role}`;
  })
  .catch(error => console.error('Error fetching data:', error));
