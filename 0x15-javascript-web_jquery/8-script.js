$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('#list_movies').append(data.results.map((movie) => {
    return `<li>${movie.title}</li>`;
  }));
});
