const {Schema, model} = require('mongoose');


const siteUser = new Schema({
  firstname: {type: String, required: true},
  lastname: {type: String, required: true},
  username: {type: String, unique: true, required: true},
  password: {type: String, required: true}
})
// моделька может легко обновляться, слава богу для монго не нужно писать каждый раз миграции базы

module.exports = model('siteUser', siteUser);
