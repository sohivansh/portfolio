let on = true
var nam = document.getElementById('name');
nam.addEventListener("click",function(){
    if (on == true){        
        nam.innerHTML = 'a learner and ';
        on = false;
    }
    else{
        nam.innerHTML = 'Vansh Sohi,';
        on = true;
    }
});



        