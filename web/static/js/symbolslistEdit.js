var my_json_obj;
var global_select="minSP";

$.getJSON('static/json/symbols.json', function(data) {
    var out="<select name='symbol' id='selectSymbol' onchange='selectChange()' >";
    var i;
    my_json_obj = data;

    var nameSelected=document.getElementById("edit").className;
    var optionSelect="";
    global_select=nameSelected;

    //out += "<option value='"+document.getElementById("edit").className+"'>"+document.getElementById("edit").className+"</option>";
    for(i = 0; i <data.symbol.length; i++)
    {
        if (data.symbol[i].name==nameSelected)
            optionSelect="selected";

        out += "<option value='"+data.symbol[i].name+"'"+ optionSelect+">"+data.symbol[i].name +"</option>";
        optionSelect="";
    }

    out+="</select>";
    document.getElementById("edit").innerHTML = out;
});
function selectChange()
{
    global_select= document.getElementById("selectSymbol").value;
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