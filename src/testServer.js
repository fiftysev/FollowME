/* eslint-disable */
const express = require('express')
const path = require('path');

const app = express();

app.use(express.json());

let CATEGORIES = [
  {id: 1, value: "bar", text: "Бары"},
  {id: 2, value: "cafe", text: "Кафе"},
  {id: 3, value: "places", text: "Места для прогулок"},
  {id: 4, value: "sport", text: "Спортивные площадки"},
  {id: 5, value: "cinema", text: "Кинотеатры"},
  {id: 6, value: "enjoy_places", text: "Развлечения"},
];

let place = {
  title: 'KFC',
  address: 'ул. Калинина, 8',
  description: 'Место, где скорее всего придется работать, если не удастся защитить курсач на отлично',
  bus_station: 'Калина Молл',
  rating: 4.8,
  //Изменил формат массива tags
  tags: [{'tag': 'lounge', 'color': '#00CF91'}, {'tag': 'cafe', 'color': '#1771F1'}],
  image: 'https://static.vl.ru/catalog/1482713713154_big_vlru.jpg'
}

app.get('/api/categories', (req, res) => {
  res.status(200).json(CATEGORIES);
});

app.get('/place/:category', (req, res) => {
  setTimeout(() =>
      res.status(200).json(place),
    3000)
});

app.use('/', express.static(path.resolve(__dirname, '../dist')));

app.get('*', (req, res) => {
  res.send(path.resolve(__dirname, '../dist', 'index.html'))
})

app.listen(8081, () => {
  console.log("Server started at port 8081...")
});
