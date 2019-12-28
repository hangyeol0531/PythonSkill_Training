const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mysql = require('mysql');
const mysqlsync = require('sync-mysql');
var sendperson, getperson, sendprice, gethavemoney;
var sendhavemoney, sendprice;
var db = mysql.createConnection({
    host: "localhost",
    database: "moodpayment",
    user: "root",
    password: "0000"
})

var syncdb = new mysqlsync({
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
            });
        }
        else{
            console.log("돈확인:", docs);
            usermoney = docs[0].money;
            res.send(usermoney);
        }
    });      
});

app.post('/pay', (req, res) =>{
    console.log("머기중");
    console.log(req.body);
    console.log(typeof(req.body))
    sendperson = req.body.sendperson;
    getperson = req.body.getperson;
    sendprice = Number(req.body.sendprice);
    
    // db.query(`SELECT money From user Where id = ${sendperson}`, function(err, docs){
    //     if(err){
    //         throw err;
    //     }
    //     sendhavemoney = Number(docs[0].money);
    //     console.log("보내는친구 돈가져올게 :", sendhavemoney );
    // });

    let docs = syncdb.query(`SELECT money From user Where id = ${sendperson}`);
    console.log("테스트:", docs);
    sendhavemoney = Number(docs[0].money);
    console.log("보내는친구 돈가져올게 :", sendhavemoney );

    
    // db.query(`SELECT money From user Where id =  ${getperson}`, function(err, docs){
    //     if(err){
    //         throw err;
    //     }
    //     gethavemoney = Number(docs[0].money);   
    //     console.log("받는친구 돈가져올게 : ", gethavemoney);
    //     console.log(typeof(gethavemoney))
    //     if(JSON.stringify(docs) == '[]'){
    //         console.log(typeof(JSON.stringify(docs)));
    //         console.log("친구가 없나?");
    //         res.end("친구 정보 없어여");
    //     }
    // });

    docs = syncdb.query(`SELECT money From user Where id = ${getperson}`);
    console.log("docs : ", docs);
    if(JSON.stringify(docs) == '[]'){
        console.log(typeof(JSON.stringify(docs)));
        console.log("친구가 없나?");
        res.end("친구 정보 없어여");
        return ;    
    }else{
        gethavemoney = Number(docs[0].money);   
        console.log("받는친구 돈가져올게 : ", gethavemoney);
        console.log(typeof(gethavemoney))
    }

    if(sendhavemoney - sendprice < 0) res.end("잔액 부족인디?");
    else{
        console.log("확인");
        console.log("sendhavemoney :", sendhavemoney);
        console.log("gethavemoney : ", gethavemoney);
        console.log("sendprice: ", sendprice);

        db.query(`UPDATE user SET money = ${gethavemoney + sendprice} WHERE id = ${getperson}`, function(err, docs){
            if(err){
                throw err;
            }
            console.log("받는 친구 돈 줄게");  
        });

        db.query(`UPDATE user SET money = ${sendhavemoney - sendprice} WHERE id = ${sendperson}`, function(err, docs){
            if(err){
                throw err;
            }
            console.log("주는 친구 돈 가져갈게");
        });
        res.end(`${sendhavemoney - sendprice}`);
    }
    console.log("처리 완료");
    
});

app.listen(3000, () =>{
    console.log("서버 포트 3000번으로 오픈했습니다");
});

// object.put("sendperson", sendperson);
// object.put("getperson", getperson );
// object.put("sendprice", sendprice);