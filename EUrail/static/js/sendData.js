/**
 * Created by Mini on 2016-11-17.
 */


//Data transfer function
function finishButton(){


    //Input cost of each section to costList
    for(var i=0;i<num;i++)
    {
        var tmp=$("#cost"+i).val();
        costList.push(parseInt(tmp));
        //console.log(parseInt(tmp));
    }



    //Making JSON Array (src_nation, src_city, dest_nation, dest_city, year, month, day, price)
    var result = [];

    for (var i = 0; i < num; i++) {
        var testList = new Object();

        var tmp = 7 * i;

        testList.id = i;

        testList.src_nation = nationCH[list[tmp]];
        //console.log(nationCH[list[tmp]]);

        testList.src_city = cityCH[list[tmp]][list[tmp + 1]];
        //console.log(cityCH[list[tmp]][list[tmp + 1]]);

        testList.dst_nation = nationCH[list[tmp + 2]];
        //console.log(nationCH[list[tmp + 2]]);

        testList.dst_city = cityCH[list[tmp + 2]][list[tmp + 3]];
        //console.log(cityCH[list[tmp + 2]][list[tmp + 3]]);

        testList.year = list[tmp + 4];
        //console.log(list[tmp + 4]);

        testList.month = list[tmp + 5];
        //console.log(list[tmp + 5]);

        testList.day = list[tmp + 6];
        //console.log(list[tmp + 6]);

        testList.price = costList[i];
        //console.log(costList[i]);


        var json_data = JSON.stringify(testList);
        //console.log(json_data);

        // Using JSON.parse for eliminate ""
        result.push(JSON.parse(json_data));





    }

    //console.log(result);
    var send_data = JSON.stringify(result);
    //console.log(send_data);





    //data transfer
    var url = "http://127.0.0.1:8080/send";
    var request = $.ajax({

        type:'POST',
	beforesend: function (request) {
		request.setRequestHeader("Access-Control-Allow-Origin", "*")
	},
        url:url,
        crossDomain : true,
        data:send_data,
        dataType:"json",
        success: function(responseData, textStatus, jqXHR) {

            var value = responseData;

            //Save ResponseData
            gugan_price=value.gugan_price;
            pass_name = value.pass_name;
            pass_price= value.pass_price;
            save_price = value.save_price;
            total_price = value.total_price;
            for(var i=0;i<num;i++)
            {
                if(value.pass_train[i]!=undefined)
                {
                    pass_train.push(value.pass_train[i]);
                }
                if(value.gugan_train[i]!=undefined)
                {
                    gugan_train.push(value.gugan_train[i]);
                }
            }
            console.log(responseData);
            //console.log(textStatus);

            //alert('Input Success');

            // Show the Advice when data transfer success
            finalbutton();
        },
        // Data transfer failed
        error: function (responseData, textStatus, errorThrown) {
            //console.log(responseData);
            //console.log(textStatus);

            alert('Error!!!.');
        }

    });



}
