/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
  base: {
    color: "#000",
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};
var card = elements.create("card", {
  style: style
});
card.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener("change", function (event) {
  var errorDiv = document.getElementById("card-errors");
  if (event.error) {
    var html = `
            <p class="icon" role="alert">
            <i class="fa-solid fa-circle-xmark"></i>
            </p>
            <p>${event.error.message}</p>
        `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = "";
  }
});


var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
  ev.preventDefault();
  // If the client secret was rendered server-side as a data-secret attribute
  // on the <form> element, you can retrieve it here by calling `form.dataset.secret`
  card.update({
    'disabled': true
  });
  $('#submit-button').attr('disabled', true);
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
  }).then(function (result) {
    if (result.error) {
      var errorDiv = document.getElementById("card-errors");
      // Show error to your customer (for example, insufficient funds)
      var html = `
            <p class="icon" role="alert">
            <i class="fa-solid fa-circle-xmark"></i>
            </p>
            <p>${result.error.message}</p>
        `;
      $(errorDiv).html(html);
      card.update({
        'disabled': false
      });
      $('#submit-button').attr('disabled', false);
    } else {
      // The payment has been processed!
      if (result.paymentIntent.status === 'succeeded') {
        form.onsubmit();
        // Show a success message to your customer
        // There's a risk of the customer closing the window before callback
        // execution. Set up a webhook or plugin to listen for the
        // payment_intent.succeeded event that handles any business critical
        // post-payment actions.
      }
    }
  });
});