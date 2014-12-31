

var mailto = "gregersen.dylan@gmail.com";
var subject_template = "[] {name} {title}";

string_span_challenge_validator = function(spam_input) {
    return spam_input.toLowerCase() == "i am human";
};

spam_challenge_validator = string_span_challenge_validator;

function email_to (form) {
    var message = "email: "+form.email.value+"\n"+form.message.value;   
    if ( form.hasOwnProperty('name') ){ 
        form.name.value;
    }
    // if ( form.hasOwnProperty('phone') ){ 
    //     form.phone.value;
    // }
    if ( form.hasOwnProperty('spam_check') ){
        if ( not spam_challenge_validator(form.spam_check.value) ) {
            consol.log("you're a computer?!");
        }
    }
    var link = "mailto:"+mailto+"?"
             + "&suject=" + escape(form.email.value)
             + "&body=" + escape(message)
             ;
    window.location.href = link;
};
