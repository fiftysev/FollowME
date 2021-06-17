const express = require('express')
const path = require('path');
const mongoose = require('mongoose')
const authRouter = require('./authRouter')
const generatorRouter = require('./generatorRouter')
const cors = require('cors')
const PORT = process.env.PORT || 3000;

const app = express();

app.use(express.json());
app.use(cors())

app.use('/auth', authRouter)
app.use('/generator', generatorRouter)

let CATEGORIES = [
    {id: 1, value: "Бары", text: "Бары"},
    {id: 2, value: "Кафе", text: "Кафе"},
    {id: 3, value: "Места для прогулок", text: "Места для прогулок"},
    {id: 4, value: "Спортивные площадки", text: "Спортивные площадки"},
    {id: 5, value: "Кинотеатры", text: "Кинотеатры"},
    {id: 6, value: "Развлечения", text: "Развлечения"},
];

app.get('/api/categories', (req, res) => {
        res.status(200).json(CATEGORIES);
});

app.use('/', express.static(path.resolve(__dirname, '../dist')));

app.get('*', (req, res) => {
    res.send(path.resolve(__dirname, '../dist', 'index.html'))
})

const start = async () => {
    try {
        await mongoose.connect(`mongodb+srv://dbEgor:qwerty123@forexample.qzsin.mongodb.net/testdbfollowme?retryWrites=true&w=majority`);
        app.listen(PORT, () => {
            console.log(`===================== \n  Start on port ${PORT} \n=====================`);
        })
    } catch (e){
        console.log(e);
    }
}

start().then(r => console.log('+++'));
