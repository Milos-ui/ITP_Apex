var http = require('http');
var url = require('url');
daten = []

http.createServer(function (req, res) {
    const headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "OPTIONS, POST, GET",
        "Access-Control-Max-Age": 2592000,
        'Content-Type': 'text/json'
      };
    res.writeHead(200, headers);

    var u = url.parse(req.url, true)
    var q = u.query
    console.log(q)
    var path = u.pathname
    console.log(path)
    //add?sportDrop=1&timeInvest=2&goal=3&weight=4&height=5&age=6&gender=7&fitLevel=8
    if(path == '/post'){
        daten.add(Daten(q.sportDrop, q.timeInvest, q.goal, q.weight, q.height, q.age, q.gender, q.fitLevel));
    }
    //get
    else if(path == '/get'){
    }
    res.end(JSON.stringify(daten));
  }).listen(8080);

function Daten(sportDrop, timeInvest, goal, weight, height, age, gender, fitLevel){
    this.sportDrop = sportDrop;
    this.timeInvest = timeInvest;
    this.goal = goal;
    this.weight = weight;
    this.height = height;
    this.age = age;
    this.gender = gender;
    this.fitLevel = fitLevel;
}