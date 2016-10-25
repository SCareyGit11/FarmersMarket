function findMarkets(zip) {
    console.log(zip);
    $.get("http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=" + zip, function(response){getMarketData(response);}, "json");
    function getMarketData(response) {
        marketArr = [];
        mapArr = [];
        for(var i = 0; i < response["results"].length; i++) {
            marketArr.push(response["results"][i]["id"]);
        }
        for(j = 0; j < marketArr.length; j++) {
            $.get("http://search.ams.usda.gov/farmersmarkets/v1/data.svc/mktDetail?id=" + marketArr[j], function(response){getMapData(response);}, "json");
        }
        function getMapData(response) {
            mapArr.push(response["marketdetails"]["GoogleLink"]);
        }
        console.log(mapArr);
    }
}

function enterZip() {
    var zip = $("input[name='zip']").val();
    findMarkets(zip);
}
