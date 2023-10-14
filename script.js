async function submitForm() {
    const income = document.getElementById("income").value;
    const moneyToPutAway = document.getElementById("moneyToPutAway").value;
    const withdrawalDate = document.getElementById("withdrawalDate").value;
    const riskType = document.getElementById("riskType").value;

    const response = await fetch("/recommend", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            income,
            moneyToPutAway,
            withdrawalDate,
            riskType
        })
    });

    const data = await response.json();
    displayResults(data);
}

function displayResults(bonds) {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = '<h2>Recommended Bonds:</h2>';
    bonds.forEach(bond => {
        resultsDiv.innerHTML += `<p>${bond.name} (Change in price: ${bond.change_in_price})</p>`;
    });
}
