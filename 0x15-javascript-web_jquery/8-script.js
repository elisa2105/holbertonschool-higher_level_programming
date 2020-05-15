$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const result = data.results;
  result.forEach(movie => {
    const m = movie.title;
    const list = '<li>' + m + '</li>';
    $('#list_movies').append(list);
  });
});
