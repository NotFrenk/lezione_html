const express = require('express');
const cors = require('cors')
const app = express();
app.use(cors());
var iPortaTcp = 4201;
var sIpAddress = "127.0.0.1"
app.listen(iPortaTcp,sIpAddress, () => console.log('API is running on http://' + sIpAddress +
':' + iPortaTcp));

const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
//pagina di invio della form
app.get('/formRegistrazione', (req, res) => {
    console.log("Mi hai chiesto la form di registrazione");
    res.sendFile("formSemplice.html", { root: './htdoc' });
    });

//pagina dinvio della forme 
app.get('/sendFile', (req, res) => {
	console.log("Mi hai chiesto la form di invio del file");
	res.sendFile("sendfile.html", { root: './htdoc' });
	});

app.post('/mansendfile', (req, res) => {
    console.log(req.body.password)
    pass_ricevuta = req.body.password;
    if(pass_ricevuta=="paperino"){
        res.send("<html>Bravo " + req.body.email + ' sono pronto a ricevere il file<html>')
    }else{
        res.send('<html> Attenzione ' + req.body.email + ' password essata</html>')
    }
});
    

//pagina di gestione dei dati della form se il metodo è GET
app.get('/gestisciDatiForm', (req, res) => {
console.log(req.query.fname);
res.send("<html>Buona serata " + req.query.fname + ' ' + req.query.fcognome + " </html>");
});
