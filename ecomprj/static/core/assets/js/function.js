
$('#add-to-cart-btn').on('click', function () {
    console.log('Ready');
    let this_val = $(this);
    let index = this_val.attr("data-index");

    let quantity = $('.product-quantity-' + index).val();
    let product_title = $('.product-title-' + index).val();
    let product_id = $('.product-id-' + index).val();
    let product_price = $('.current-product-price-' + index).val();
    let product_pid = $('.product-pid-' + index).val();
    let product_image = $('.product-image-' + index).val();


    $.ajax({
        url: '/add-to-cart',
        data: {
            'id': product_id,
            'pid': product_pid,
            'image': product_image,
            'qty': quantity,
            'title': product_title,
            'price': product_price,
        },
        dataType: 'json',
        beforeSend: function () {
            console.log('adding product is cart');
        },
        success: function (response) {
            this_val.html('✔️');
            $(".cart-item-count").text(response.total_cart_item);
            this_val.attr('disabled'.false);
            console.log('added product is cart');
        },
    });
});


$("#addToCartBtn").on('click', function () {
    console.log($(this));
})




$(document).ready(function () {
    // Listern for changes in chackboxes
    console.log($(this));

    $(".filter-checkbox").on("click", function () {
        // Get selected filters
        var selectedFilters = {
            category: [],
            vendor: [],
        };
        $(".filter-checkbox:checked").each(function () {
            let filterType = $(this).data("filter");
            let filterValue = $(this).val();
            selectedFilters[filterType].push(filterValue);
        });
        $.ajax({
            url: "/filter-products",
            method: "GET",
            data: selectedFilters,
            dataType: "json",
            success: function (response) {
                $("#filtered-product").html(response.data);
            },

            error: function (response) {
                console.error("Ajax request error", error);
            },
        });
    });
});


