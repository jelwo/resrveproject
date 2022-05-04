window.onload = function(){
    let target = document.getElementsByTagName("input");
    let arr = []
    for(let i of target){
        if  (i.value == "予約"){
        } else {
            i.readOnly = true;
            i.classList.add("form-control");
            i.style.width = 500 + 'px';
            arr.push(i.value);
        };
    };

    arr.shift();
    let date1 = arr[0] + '-' + arr[1].replace(':','-');
    let date2 = arr[2] + '-' + arr[3].replace(':','-');
    date1 = date1.split('-');
    date2 = date2.split('-');
    let new_date1 = new Date(Number(date1[0]),Number(date1[1]),Number(date1[2]),Number(date1[3]),Number(date1[4]));
    let new_date2 = new Date(Number(date2[0]),Number(date2[1]),Number(date2[2]),Number(date2[3]),Number(date2[4]));

    if(new_date1.getTime() >= new_date2.getTime()){
        alert('日付逝ってね？');
        history.back();
    };
};