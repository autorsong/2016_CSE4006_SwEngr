/**
 * Created by Mini on 2016-11-17.
 */


<!-- end button Function-->
function finalbutton(){


    //Best way for getting EURail Ticket (1. Section Ticket 2. Eurail Pass 3. Using Both)
    var sr = "<div style='font-size: 14pt;margin-top:15px;color:mediumseagreen'> 총 금액 </div><div style='margin:5px;color:black'>  "+total_price+"(구간권만 샀을때보다 "+(-save_price)+" EUR 절약)</div>";

    //3. Using Both (EURail Pass Part)
    sr += "<div style='font-size: 14pt;color:mediumseagreen;margin-top:15px'>****유레일 패스를 사야하는구간****</div>";

    for(var i=0;i<num;i++) {
        if (pass_train[i] != undefined) {
            sr += "<div style='color:black'>" + (i + 1) + " 날짜 : " + pass_train[i].month+"월 "+ pass_train[i].day + "일 / 출발지 : " + pass_train[i].src_city + " 도착지 : " + pass_train[i].dst_city + "</div>";
        }
    }

    sr += "<div style='margin-top:15px;color:mediumseagreen'> 패스 구입 총 가격</div><div style='margin:5px;color:black'>  [ "+pass_name+" ]구매 / 가격은 : "+pass_price+"(EUR)</div>";

    //3. Using Both (Section Part)
    sr += "<div style='font-size: 14pt;color:mediumseagreen;margin-top:15px'>****구간권을 사야하는구간****</div>";
    for(var i=0;i<num;i++) {
        if (gugan_train[i] != undefined) {
            sr += "<div style='color:black'>" + (i + 1) + " 날짜 : " + gugan_train[i].month + "월 "+gugan_train[i].day+"일 / 출발지 : " + gugan_train[i].src_city + " 도착지 : " + gugan_train[i].dst_city + "</div>";
        }
    }

    sr +="<div style='margin-top:15px;color:mediumseagreen'>  구간권 구입 총가격 </div><div style='margin-top:5px;color:black'> "+gugan_price+ "(EUR) </div>";



    //Print by Modal
    $('div.modal').modal();
    $("#ticketch").html(sr);


    //reset array
    pass_train= new Array();
    gugan_train= new Array();
}