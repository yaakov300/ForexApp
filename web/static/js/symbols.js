function getListSymbols() {
	var symbols = JSON.parse(json/symbols.json);
    function myFunction(symbols) {
    var list = "";
    var i;
    for(i = 0; i < symbols.length; i++) {
        list +='<option>' + symbols[i].name + '</option>';
    }
}
    return list;
}