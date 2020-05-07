function update_eventbox(){
	$('.eventbox_body').load('/dashboard/ecg-eventbox',function(){
            
    });
}

function update_eventbox_interval(){
	// refresh the page in every second
	setInterval(update_eventbox, 1000);
}

$('.openBtn').on('click',update_eventbox);
$('document').ready(update_eventbox);