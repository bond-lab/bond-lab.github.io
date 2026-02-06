function toggle(myid) {
    if(document.getElementById(myid).style.display == 'none'){
	document.getElementById(myid).style.display = '';
    }else{
	document.getElementById(myid).style.display = 'none';
    }
}