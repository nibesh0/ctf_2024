const express = require('express');
const sqlite3 = require('sqlite3');
const crypto = require('crypto')


const app = express();
app.use(express.urlencoded({extended: true}));
app.use(express.static('./public'));
app.set('view engine', 'ejs');

const db = new sqlite3.Database(':memory:');

const flag = "ctf{sql_is_g00d_but__}";

db.run("CREATE table IF NOT EXISTS users (username text, password text)", () => {
    db.all("SELECT * FROM users WHERE username='admin'", (err, rows) => {
        if (err) {
            throw err;
        } else if (rows.length == 0) {
            crypto.randomBytes(32, (err, buf) => {
                if (err) {
                    throw err;
                }
                db.all("INSERT INTO users VALUES ('admin', $1)", [buf.toString('hex')]);
                console.log("Admin password: " + buf.toString('hex'));
            });
        }
    })
});


app.get('/', (req, res) => {
    return res.render("index.ejs", {"alert": req.query.alert});
})

app.post('/flag', (req, res) => {
    db.all("SELECT * FROM users WHERE username='" + req.body.username + "' AND password='" + req.body.password + "'", (err, rows) => {
        console.log(rows);
        try {
            if (rows.length == 0) {
                res.redirect("/?alert=" + encodeURIComponent("you are not admin :("));
            } else if(rows[0].username === "admin") {
                res.redirect("/?alert=" + encodeURIComponent(flag));
            } else {
                res.redirect("/?alert=" + encodeURIComponent("you are not admin :("));
            }
        } catch (e) {
            res.status(500).end();
        }
    })
})

app.listen(1200, () => console.log('Site listening on port 80'));