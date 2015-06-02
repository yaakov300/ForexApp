
function calculateRisk() {
    var selectSymbol= document.getElementById("selectSymbol").value;
    var enterPrice = parseFloat(document.getElementById("enterPrice").value);
    var stopLose = parseFloat(document.getElementById("stopPrice").value);
    var volume = parseFloat(document.getElementById("volume").value);
    var price;
    var risk;
    var i;

   for (i=0; i<my_json_obj.symbol.length; i++)
   {
       if (my_json_obj.symbol[i].name==selectSymbol)
       {
           price=my_json_obj.symbol[i].price;
       }
   }

    if(document.getElementById("long").checked == true)
        risk = enterPrice-stopLose;
    else
        risk = stopLose-enterPrice;
    risk = risk*volume*price;
    risk=parseFloat(risk).toFixed(2);

    document.getElementById("resultRisk").value =risk +" $";
}

function getCurrentPrice()
{
    var symbol=document.getElementById("selectSymbol").value;
    var type;
    var symbolName;

    for (i=0; i<my_json_obj.symbol.length; i++)
   {
       if (my_json_obj.symbol[i].name==symbol)
       {
           type=my_json_obj.symbol[i].type;
           symbolName=my_json_obj.symbol[i].symbolName;
       }
   }

    if (type==1)//Currency
    {
        getCurrency(symbolName);
    }
    else//Commodities
    {
        getCommodities(symbolName);
    }
}

function getCurrency(symbolName)
{
    console.log(symbolName);
    var xmlhttp = new XMLHttpRequest();
    var url ="https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22"+symbolName+
        "%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=";

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var myArr = JSON.parse(xmlhttp.responseText);
            document.getElementById("enterPrice").value =myArr.query.results.rate.Rate;
        }
    }
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function getCommodities(symbolName)
{
    var xmlhttp = new XMLHttpRequest();
    var url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22"+symbolName+"%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=";

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var myArr = JSON.parse(xmlhttp.responseText);
            document.getElementById("enterPrice").value =myArr.query.results.quote.Ask;
        }
    }
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

