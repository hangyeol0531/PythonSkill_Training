const express = require('express');
const app = express();
var bodyParser = require('body-parser');
var mysql = require('mysql');
var sendperson, getperson, sendprice;
var db = mysql.createConnection({
    host: "localhost",
    database: "moodpayment",
    user: "root",
    password: "0000"
})
db.connect((error) =>{
    if(error){
        throw(error);
    }
    else{
        console.log("database connected");
    }
});

app.use(bodyParser.json())

app.post('/', (req, res) =>{
    var usermoney = 0;
    console.log("머기")
    console.log(req.body);
    console.log(typeof(req.body))
    sendperson = req.body.sendperson;
    console.log(sendperson);
    db.query(`SELECT money FROM user WHERE id = ${sendperson}`, function(err, docs){
        if(err){
            throw err;
        }
        if(JSON.stringify(docs) == '[]'){
            console.log(typeof(JSON.stringify(docs)));
            console.log("값이 없나?");
            db.query(`INSERT INTO user (id, money) VALUES(${sendperson}, 0)`, function(err, result, fields){
                if(err){
                    throw err;
                }
                console.log("삽입");
                res.send('0');
                db.end();
            });
        }
        else{
            console.log("돈확인:", docs);
            usermoney = docs[0].money;
            res.send(usermoney);
        }
        db.end();
    });      
});

app.post('/pay', (req, res) =>{
    console.log("머기중");
    console.log(req.body);
    console.log(typeof(req.body))
    sendperson = req.body.sendperson;
    getperson = req.body.getperson;
    sendprice = Number(req.body.sendprice);

    db.query(`INSERT INTO user (id, money) VALUES(${sendperson}, 0)`, function(err, docs){
        if(err){
            throw err;
        }
        console.log("보내는친구 돈가져올게");
        sendhavemoney = Number(docs[0].money);
        db.end();
    });

    db.query(`INSERT INTO user (id, money) VALUES(${getperson}, 0)`, function(err, docs){
        if(err){
            throw err;
        }
        sendhavemoney = Number(docs[0].money);   
        console.log("받는친구 돈가져올게");
        if(JSON.stringify(docs) == '[]'){
            console.log(typeof(JSON.stringify(docs)));
            console.log("친구가 없나?");
            res.end("친구 정보 없어여");
        }
    });

    if(sendhavemoney - sendprice) res.end("잔액 부족인디?");
    else{
        db.query(`UPDATE user SET money = ${sendhavemoney - sendprice} WHERE ${sendperson}`, function(err, docs){
            if(err){
                throw err;
            }
            console.log("주는 친구 돈 가져갈게");
            db.end();
        });

        db.query(`UPDATE user SET money = ${sendhavemoney + sendprice} WHERE ${getperson}`, function(err, docs){
            if(err){
                throw err;
            }
            console.log("받는 친구 돈 줄게");  
            db.end();
        });
    }
    console.log("처리 완료");
});

app.listen(3000, () =>{
    console.log("서버 포트 3000번으로 오픈했습니다");
});

// object.put("sendperson", sendperson);
// object.put("getperson", getperson );
// object.put("sendprice", sendprice);