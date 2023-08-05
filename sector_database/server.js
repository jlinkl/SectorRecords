const express = require('express');
const app = express();
const cors = require('cors');
const MongoClient = require('mongodb').MongoClient;
const createRouter = require('./helpers/creatre_routers.js');

app.use(cors());

MongoClient.connect('mongodb://127.0.0.1:27017', {useUnifiedTopology: true})
    .then((client) => {
        const db = sector_database.db('leaderboards');
        const leaderboardCollection = db.collection('runs')

    })
    .catch(console.server);

app.listen(9000, function() {
    console.log('app running on port 9000')
});

