const Place = require('./models/place')
const siteUser = require('./models/siteUser')
const {validationResult} = require('express-validator')

Array.prototype.random = function (){
  return this[Math.floor(Math.random() * this.length)];
}

class GeneratorController {
  async addPlace(req, res) {
    try {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(400).json({message: "Game over"});
      }
      const {
        title,
        address,
        description,
        bus_station,
        rating,
        rates_count,
        sum_of_rating,
        tags,
        photo
      } = req.body;
      const place = new Place({
        title,
        address,
        description,
        bus_station,
        rating,
        rates_count,
        sum_of_rating,
        tags,
        photo
      });
      await place.save()
      return res.status(200).json({message: 'You are awesome!'})
    } catch (e) {
      console.log(e)
      res.status(400).json({message: 'Fuck you c:'})
    }
  }

  async getPlace(req, res) {
    const category = req.query.category
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      res.status(400).json({message: "You are invalid!"});
    }
    const place = await Place.find({tags: category});
    // const user = await siteUser.findOne({username: "bboomerang"});
    // user.save();
    if (!place) {
      res.status(400).json('Net mesta bro');
    }
    return res.status(200).send(place.random())
  }
}


module.exports = new GeneratorController()
