const Router = require('express')
const router = new Router()
const controller = require('./generatorController')


router.post('/add', controller.addPlace);
router.get('/getplace', controller.getPlace);


module.exports = router
