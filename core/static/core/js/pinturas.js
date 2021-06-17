var apiKey = "f89cdebf-0238-4872-bcbe-48decb727676"
// Find all of the objects that are paintings and have the word "rabbit" in the title
var apiEndpointBaseURL = "https://api.harvardartmuseums.org/object";
var queryString = $.param({
    apikey: apiKey,
    title: "",
    classification: "",
});

$.getJSON(apiEndpointBaseURL + "?" + queryString, function (data) {
    // var dict=[];
    let padit = document.querySelector('.padre-items')
    for (var key in data) {
        var dictionary = data[key];
        padit.innerHTML = '';
        for (let index = 0; index < dictionary.length; index++) {
            let item = dictionary[index]
            console.log(item)
            padit.innerHTML += `<h5>Clasificación: ${item.classification}</h5>`
        }
    } 
});




















































































































































































