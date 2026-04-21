document.addEventListener("DOMContentLoaded", function () {

    let cards = document.querySelectorAll(".product-card");
    let loadBtn = document.getElementById("loadMoreBtn");

    let visible = 5;

    // 🔥 STEP 1: Hide all cards first
    cards.forEach((card, index) => {
        if (index >= visible) {
            card.style.display = "none";
        }
    });

    // 🔥 STEP 2: Load More logic
    if (loadBtn) {
        loadBtn.addEventListener("click", function () {

            let hiddenCards = Array.from(cards).filter(card => card.style.display === "none");

            hiddenCards.slice(0, 5).forEach(card => {
                card.style.display = "block";
            });

            if (hiddenCards.length <= 5) {
                loadBtn.style.display = "none";
            }
        });
    }

});