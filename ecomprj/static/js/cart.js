let updateCartBtn = document.getElementsByClassName('update-cart');

for (let i = 0; i < updateCartBtn.length; i++) {
    updateCartBtn[i].addEventListener('click', function () {
        let productId = this.dataset.product;
        let action = this.dataset.action;
        console.log(user)

        if (user === 'AnonymousUser') {
            addCookieItem(productId, action)
        } else {
            updateUserOrder(productId, action)
        }

    });

}

function addCookieItem(productId, action) {
    if (action == 'add'){
        if (cart[productId] === undefined){
            cart[productId] = {'quantity': 1}
        } else {
            cart[productId]['quantity'] += 1;
        }
    }

    if (action == 'remove')  {
        cart[productId]['quantity'] -= 1;

        if (cart[productId]['quantity'] <= 0){
            delete cart[productId];
            console.log('remove Item');
        }
    }
    document.cookie = 'cart='+JSON.stringify(cart) + ";domain=;path=/";
    location.reload();
    console.log('cart', cart);
}



function updateUserOrder(productId, action) {
    let url = /update_item/;

    fetch(
        url,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({'productId': productId, 'action': action})
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data', data)
            location.reload()
        })
}