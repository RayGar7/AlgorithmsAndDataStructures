https.get('', (resp) => {
    let data = '';

    // A chunk of data has been recieved.
    resp.on('data', (chunk) => {
      data += chunk;
    });
  
    // The whole response has been received. Print out the result.
        resp.on('end', () => {
            // with the data retrived
            // for each country check if it's greater than p, if so add to the counter
            JSON.parse(data).data.forEach(country => {
                if (country.population > p) {
                    counter++;
                }
            });
            //console.log(counter);
        });
}).on("error", (err) => {
    console.log("Error: " + err.message);
});

//test case 12 = 8