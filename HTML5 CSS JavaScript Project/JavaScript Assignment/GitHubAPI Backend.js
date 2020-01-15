function onAPICall() {
    var request = new XMLHttpRequest();
    request.open('GET', 'https://api.github.com/users/sandeshsuvarna7', false);
    //request.setRequestHeader("Content-Type", "application/json");
    //request.send(JSON.stringify(----- JSON-----));
    request.send();
    console.log('response head: ' + request.responseText.substring(0, 15) + '...');
    console.log('Output is: ' + request.responseText.toString());

    var obj = JSON.parse(request.responseText);

    var tablearea = document.getElementById('CreateTableDynamic'),
        table = document.createElement('table');
    for (key in obj) {
            var tr = document.createElement('tr');

            tr.appendChild(document.createElement('td'));
            tr.appendChild(document.createElement('td'));

            tr.cells[0].appendChild(document.createTextNode(key))
            tr.cells[1].appendChild(document.createTextNode(obj[key]));

            table.appendChild(tr);

        tablearea.appendChild(table);
    }
}