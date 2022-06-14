odoo.define("PoS.dropdown", function (require) {
    "use strict";
    // alert("js running"); // used for debugging

    jQuery('.modal-content').ready(checkContainer);
    

    function checkContainer() {
        // console.log("checkContainer running..."); // used for debugging
        if ($('.modal-content').is(':visible')){ 
            //if the container is visible on the page
            $("select.o_input.o_field_widget.o_quick_editable").select2({
               
                formatResult: formatState,
                formatSelection: formatState,
                
                minimumInputLength: 1,
                allowClear: true,
                placeholder:'select here',
                // templateResult: formatState,
                // templateSelection: formatState,
                
            });
            
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

            $('button').click(function(){
                // console.log("Clicked... now") // used for debugging
                setTimeout(checkContainer, 500);
            });
              
        } 
        
        else {
            setTimeout(checkContainer, 500); //wait 50 ms, then try again
        }
    }

return;
});
