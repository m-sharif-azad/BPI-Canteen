document.addEventListener("DOMContentLoaded", function () {
    const deliveryFee = {{ delivery_fee}}; // Get the delivery fee from the server
    let baseTotalPrice = {{ total_food_price }}; // Get the base total price from the server
    const totalPriceElement = document.getElementById('total-price');
    const deliveryMessage = document.getElementById('delivery-message');
    const deliveryMessage2 = document.getElementById('delivery-message2');
    const deliveryRadio = document.querySelector('input[name="delivery_method"][value="delivery"]');
    const selfCollectionRadio = document.querySelector('input[name="delivery_method"][value="self_collection"]');

    // Function to update the total price based on selected delivery method
    function updateTotalPrice() {
        let totalPrice = baseTotalPrice;

        if (deliveryRadio.checked) {
            totalPrice += deliveryFee;
            deliveryMessage2.style.display = 'block'; // Show delivery message
        } else {
            deliveryMessage2.style.display = 'none'; // Hide delivery message
        }
        if (selfCollectionRadio.checked) {
            deliveryMessage.style.display = 'block'; // Show delivery message
        } else {
            deliveryMessage.style.display = 'none'; // Hide delivery message
        }

        // Update the total price on the page
        totalPriceElement.textContent = `Total Price: ${totalPrice.toFixed(2)} €`;
    }

    // Add event listeners for both radio buttons
    deliveryRadio.addEventListener('change', updateTotalPrice);
    selfCollectionRadio.addEventListener('change', updateTotalPrice);
});