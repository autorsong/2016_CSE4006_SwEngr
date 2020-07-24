/**
 * Created by Mini on 2016-11-17.
 */

//Input Cost of each section by MODAL
function checkCost() {

    //Open Modal Screen
    $('div.modal').modal();

    // Connect to reailway by button
    var bodyCheck = "<div style='margin-top:20px; color:mediumseagreen'> Find your Ticker from here </div> <button type='button' id='spain' onclick='spainbutton()' style='font-size:10pt;background:#5cb85c;color:white'> Spain </button> <button type='button' id='france' onclick='francebutton()'style='font-size:10pt;background:#5cb85c;color:white'> France </button>"+
                        "<button type='button' id='switzerland' onclick='switzerlandbutton()'style='font-size:10pt;background:#5cb85c;color:white'> Switzerland </button> <button type='button' id='germany' onclick='germanybutton()'style='font-size:10pt;background:#5cb85c;color:white'> Germany </button> <button type='button' id='italy' onclick='italybutton()'style='font-size:10pt;background:#5cb85c;color:white'> Italy </button> <button type='button' id='austria' onclick='austriabutton()'style='font-size:10pt;background:#5cb85c;color:white'> Austria </button>";
    $("#ticketch").html(bodyCheck);



    var sr="<div style='margin-top:20px'></div>";
    $("#ticketch").append(sr);


    //number box
    for (var j = 0; j < num; j++) {
        var sr = "";
        var tmp=7*j;
        var named="<div style='color:mediumseagreen'>"+nationCH[parseInt(list[tmp])]+"<a style='color:red'>["+cityCH[parseInt(list[tmp])][parseInt(list[tmp+1])]+"]</a> to "+nationCH[parseInt(list[tmp+2])]+"<a style='color:red'>["+cityCH[parseInt(list[tmp+2])][parseInt(list[tmp+3])]+"]</a>"+"<span>&nbsp;&nbsp;</span></div>";


        var sr2="";
        //Only Input Number
        sr2="<div><input  type='number'  id= 'cost"+j+"' style='color:black'><span style='color:black;margin-left: 20px'>(EUR)</span></div>";

        var hh = "<div><span>&nbsp;&nbsp;</span>"+named+sr2+"</div>";

        $("#ticketch").append(hh);

    }

    //send data(JSON) by finishButton
    var sr1="<div><div><div><button type='button' id='plus' onclick='finishButton()'style='font-size:10pt;color:black;margin-top:50px;margin-bottom: 20px' > FINISH </button></div></div></div>";
    $("#ticketch").append(sr1);
}















