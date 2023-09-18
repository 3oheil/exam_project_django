// function SendArticleCommends(articleId) {
//     var comment = $('#CommendText').val();
//
//     $.get('article/add-article-comments', {
//         article_commend: comment,
//         article_id: articleId,
//         parent_id: null
//
//     }).then(res => {
//         console.log(res);
//     });
// }
// function SendArticleCommends() {
//     // console.log('this is custom js ')
//     var comment = $("#CommendText").val();
//     // console.log(comment);
//
//     $.get('/article/add-article-comment', {
//         article_comment: comment,
//         article_id : 23,
//         parent_id : null
//     }).then(res => {
//         console.log(res);
//     });
// }


function SendArticleCommends(articleId) {
    var comment = $('#CommendText').val();
    var parentId = $('#parent_id').val()
    $.get('/article/add_article_commend', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId

    }).then(res => {
        console.log(res);
        // location.reload();
        $('#comment_area').html(res);

        if (parentId !== null && parentId !== '') {
            document.getElementById('single_comments_box_' + parentId).scrollIntoView({behavior: 'smooth'});
        } else {
            document.getElementById('comment_area').scrollIntoView({behavior: "smooth"});
        }
    });
}

function FillParentId(parentId) {
    $('#parent_id').val(parentId)
    document.getElementById('comment_form').scrollIntoView({behavior: 'smooth'});
}

// function AddProductToOrder(productId) {
//     $.get('order/add-to-order?product_id=' + productId).then(res => {
//         console.log(res);
//     });
// }

// function AddProductToOrder(productId) {
//     $.get('order/add-to-order?product_id='+ productId + '$count=' + 10).then(res => {
//         console.log(res)
//     });
// }


function AddProductToOrder(productId) {
    const productCount = $('#product_count').val();
    $.get('/order/add-order?product_id=' + productId + '&count=' + productCount).then(res => {
        console.log(res);
    });
}
