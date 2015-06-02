var my_json_obj;
var global_select="minSP";

$.getJSON('static/json/symbols.json', function(data) {
    var out="<select name='symbol' id='selectSymbol' onchange='selectChange()' >";
    var i;

    my_json_obj = data;

    for(i = 0; i <data.symbol.length; i++)
    {
        out += "<option value='"+data.symbol[i].name+"'>"+data.symbol[i].name +"</option>";
    }

    out+="</select>";
    document.getElementById("demo").innerHTML = out;
});

function selectChange()
{
    global_select= document.getElementById("selectSymbol").value;
    document.getElementById("enterPrice").value ="";
    document.getElementById("stopPrice").value ="";
}

function getStep(inputID)
{
    var selectSymbol= global_select;
    var step;

    for (i=0; i<my_json_obj.symbol.length; i++)
    {
        if (my_json_obj.symbol[i].name==selectSymbol)
        {
            step=my_json_obj.symbol[i].step;
        }
    }
    document.getElementById(inputID).step = step;
}