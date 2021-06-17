const {Schema, model, ObjectId} = require('mongoose')

const place = new Schema({
  title: {type: String, required: true},
  address: {type: String, required: true},
  description: {type: String, required: true},
  bus_station: {type: String},
  rating: {type: Number, required: true},
  rates_count: {type: Number},
  sum_of_rating: {type: Number},
  tags: [String],
  photo: [String],
})

module.exports = model('place', place)
