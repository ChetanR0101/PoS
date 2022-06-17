odoo.define("PoS.dropdown", function (require) {
  "use strict";
  // alert("js running"); // used for debugging
  var checkinVisible = true
  function formatState(opt) {
      // alert("Select2 running"); // used for debugging
      var imurl;
      if (!opt.id || (opt.id == 'false')) {
          return opt.text.toUpperCase();
      }else{
          console.log(opt.id);
          imurl = window.location.origin + '/web/image/pos.products/' + opt.id + '/avatar_128';
      }
      //get attr data-image from option to show image
      //var optimage = $(opt.element).attr('data-image');
      console.log(imurl);
      if (!imurl) {
          return opt.text.toUpperCase();
      } else {
          var $opt = $(
              '<span style="width:60px;"><img class="imgth_' + opt.id + '" src="' + imurl + '" style="max-width:60px;max-height:60px;" alt="icon" loading="lazy" /> ' + opt.text.toUpperCase() + '</span>'
          );
          return $opt;
      }
  }
  function select2dropdown() {
      $("select.o_input.o_field_widget.o_quick_editable").select2({
          formatResult: formatState,
          formatSelection: formatState,
          minimumInputLength: 1,
          allowClear: true,
          placeholder:'select here',
      });
  }
  function checkContainer() {
      console.log("checkContainer running..."); // used for debugging
      if(checkinVisible){
          return
      }
      if ($('.modal-content').is(':visible')){ 
          console.log("checkContainer is visible..."); // used for debugging
          select2dropdown();
          $('button').click(function(){
              // console.log("Clicked... now") // used for debugging
              setTimeout(checkContainer, 10)
          });
      }
      else{
          setTimeout(checkContainer, 1000); //wait 50 ms, then try again
      }
  }
  function checkinCreate() {
      setTimeout(select2dropdown, 10);
  }
  function CheckinClick() {
      console.log("CheckinClick called"); // used for debugging
      $(".btn.btn-primary.o_list_button_add").click(function(){
          console.log("Clicked... Create"); // used for debugging
          setTimeout(checkinCreate,3000);
      });
  }
  function MenuClick() {
      console.log("Menu Clicked called"); // used for debugging
      // setTimeout(CheckoutClick,5000);
      // setTimeout(CheckinClick,5000);
      $(".dropdown-item.o_nav_entry[data-menu-xmlid='PoS.pos_checkin_menu']").click(function(){
          console.log("checkin... Clicked"); // used for debugging
          checkinVisible = true;
          setTimeout(CheckinClick,5000);
      });
      $(".dropdown-item.o_nav_entry[data-menu-xmlid='PoS.pos_checkout_menu']").click(function(){
          console.log("checkout... Clicked"); // used for debugging
          checkinVisible = false;
          setTimeout(checkContainer, 500);
      });
  }
  console.log('before event');
  // $('.modal-content').click(function (){
  //     console.log('inside event');
  //     setTimeout(checkContainer, 500);
  // });
  $(document).ready(function() {
      console.log("Loaded... now"); // used for debugging
      $('.modal-content').ready(function (){
          console.log('inside event');
          setTimeout(MenuClick,8000);
          setTimeout(checkContainer, 500);
      });
  });
  console.log('after event');
return;
});