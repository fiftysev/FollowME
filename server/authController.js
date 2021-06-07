const User = require('./models/user');
const Role = require('./models/roles');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const {validationResult} = require('express-validator');
const {secret} = require('./config');

const generateToken = (id) => {
    const payload = {
        id
    }
    return jwt.sign(payload, secret, {expiresIn: "24h"});
}

class authController{
    async registration(req, res) {
        try {
            const errors = validationResult(req);
            if (!errors.isEmpty()){
                return res.status(400).json({message: 'invalid data', errors});
            }
            const {username, password} = req.body;
            const candidate = await User.findOne({username});
            console.log(username, password)
            if (candidate) {
                return res.status(400).json({message: 'Username is already exists'});
            }
            const passwordHash = bcrypt.hashSync(password, 5);
            const user = new User({username, password: passwordHash});
            await user.save();
            return res.json({message: 'Register success'});
        }catch(e) {
            console.log(e);
            res.status(400).json({message: 'Reg error , check data'});
        }
    }

    async login(req, res) {
        try {
            const {username, password} = req.body;
            const user = await User.findOne({username});
            if (!user) {
                return res.status(400).json({message: `user ${username} is doesn't exist`});
            }
            const validPassword = bcrypt.compareSync(password, user.password);
            if (!validPassword) {
                return res.status(400).json({message: 'invalid password'});
            }
            const token = generateToken(user._id);
            return res.json({token});
        }catch(e) {
            console.log(e);
            res.status(400).json({message: "Login error , check data"});
        }
    }

    async usersGetter(req, res) {
        try {
            const users = await User.find();
            res.json(users);
        }catch(e) {
            console.log(e);
            res.status(400).json({message: 'GG WP'});
        }
    }
}

module.exports = new authController();
