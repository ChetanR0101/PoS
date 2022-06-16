odoo.define("PoS.dropdown", function (require) {
    "use strict";
    // alert("js running"); // used for debugging

    $(document).ready(function() {
        // $("#solTitle a").click(function() {
        //     //Do stuff when clicked
        // });
        
        console.log("Loaded... now"); // used for debugging
        setTimeout(MenuClick,10000);
        // setTimeout(NewTestFun,7000);
        // setTimeout(NewTestFun1,5000);

    });


    function MenuClick() {

        console.log("Menu Clicked called"); // used for debugging
        $(".dropdown-item.o_nav_entry").click(function(){
            console.log("Menu... Clicked"); // used for debugging
            setTimeout(NewTestFun,5000);
            setTimeout(NewTestFun1,5000);
    })};
    function NewTestFun() {

        console.log("New Funtion called"); // used for debugging
        $(".o_field_x2many_list_row_add a").click(function(){
            console.log("Clicked... Add"); // used for debugging
            setTimeout(checkContainer,3000);
    })};

    function NewTestFun1() {

        console.log("New Funtion1 called"); // used for debugging
        $(".btn.btn-primary.o_list_button_add").click(function(){
            console.log("Clicked... Create"); // used for debugging
            setTimeout(checkContainer,3000);
            setTimeout(NewTestFun,3000);
    })};
        

    function checkContainer() {
        console.log("checkContainer running..."); // used for debugging
            $("select.o_input.o_field_widget.o_quick_editable").select2({
               
                formatResult: formatState,
                formatSelection: formatState,
                
                minimumInputLength: 1,
                allowClear: true,
                placeholder:'select here',
            });
    
    }

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

return;
});
