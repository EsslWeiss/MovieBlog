  $(".modal-btn").on("click", function (e) {
    e.preventDefault();
    $(".overlay").addClass("active");
    $(".modal").addClass("active");
  });

  $(".modal")
    .find(".close")
    .click(function () {
      $(".modal").removeClass("active");
      $(".overlay").removeClass("active");
    });

  $(".overlay").click(function () {
    $(".modal").removeClass("active");
    $(".overlay").removeClass("active");
  });

  $(".modal .options a").on("click", function (e) {
    if (!$(this).hasClass("active")) {
      $(this).parent().find("a.active").removeClass("active");
      $(this).addClass("active");
      $(this).parents(".modal").find(".wrapper").toggleClass("switch");
    }
  });
