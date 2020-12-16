// Complete the sockMerchant function below.
function sockMerchant(n, ar) {
    let pairs = 0;
    let sockObj = [];
    for (let i = 0; i < n; i++ ) {
        sockObj.push({
            sock: ar[i],
            checked: false
        });
    }

    //console.log('sockObj', sockObj);

    for (let i = 0; i < sockObj.length; i++) {
        for (let j = i + 1; j < sockObj.length; j++) {
            if (sockObj[i].sock === sockObj[j].sock && !sockObj[i].checked && !sockObj[j].checked) {
                sockObj[i].checked = true;
                sockObj[j].checked = true;
                pairs++;
                break;
            }
        }
    }

    /*
    for (let i = 0; i < sockObj.length; i++) {

    }
    
    */

    return pairs;

}


console.log(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]));  // expected 3