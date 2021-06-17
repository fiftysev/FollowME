const {Schema, model, ObjectId} = require('mongoose')

const place = new Schema({
  title: {type: String, required: true},
  address: {type: String, required: true},
  description: {type: String, required: true},
  bus_station: {type: String},
  rating: {type: Number, required: true},
  tags: [String],
  photo: [String]
})

module.exports = model('place', place)
