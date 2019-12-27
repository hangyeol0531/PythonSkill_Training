   var app = require("express")();
   var http = require('http').Server(app);
   var bodyParser = require('body-parser');
   var msg;
   let users;
   //////////////////////
    app.use(bodyParser.json())
    app.post('/',function(req,res){
        msg=req.body.msg;
        console.log("python: " + msg);
        console.log(typeof(msg));
        users = {
                message : msg
        }
        res.end(users);
    });

     http.listen(8080, function(){
     console.log('listening...');
     });

     app.get('/msg', function(req,res){
        console.log("파일 줄게요 : ", msg);
        res.json(users);
     });
     //////////////////////

     

     