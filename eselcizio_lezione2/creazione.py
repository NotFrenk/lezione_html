pag11 = """
<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>totti</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<link rel="icon" href="img/images.jpg">
     <link rel="icon" href=".png">

  </head>
  <body>
    <style>
        

        main{
        margin-top: 20px;
        margin-right: 20px;
        margin-left: 20px;
        font-family: sans-serif;
        }

        .container-fluid {background-color: rgb(91, 229, 67);
    list-style-type: none;
    padding: 10px;
    margin: 0px;
    overflow: hidden;}


    </style>

  <nav class="navbar bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand">ER PUPONE</a>

  </div>
</nav>
<main>
    <center>
      <div class="container text-center">
        <div class="row">
"""

pag12 = """
          <div class="col-md-4">
            <div class="card" style="width: 18rem;">
              <img src="img/ditone.jpg" class="card-img-top" alt="..." width="175px" height="180px">
              <div class="card-body">
                <h5 class="card-title">CHI E'?</h5>
                <p class="card-text">Francesco Totti è un ex calciatore italiano, considerato uno dei più grandi giocatori nella storia del calcio italiano. Nato il 27 settembre 1976 a Roma, ha trascorso tutta la sua carriera professionistica con la squadra della Roma, diventando una leggenda del club.</p>
                <button class="btn btn-primary"><a href="#" class="text-white">CONOSCILO MEGLIO</a></button>
              </div>
            </div>
          </div>
"""

pag13 = """
        </div>
      </div>
    </center>
    </main>
  </body>
</html>
"""

n = int(input("inserisci il numero da moltiplicare: "))
pag = pag11 + (n * pag12) + pag13

with open("risultato.html", "w") as file:
    file.write(pag)