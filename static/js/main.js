// var images = document.getElementsByTagName('img');
// var srcList = [];
// var i = 0;

// setInterval(function(){
//     if(images.length > i){
//         srcList.push(images[i].src);
//         var link = document.createElement("a");
//         link.id=i;
//         link.download = images[i].src;
//         link.href = images[i].src;
//         link.click();
//         i++;
//     }
// },1500);


function download_all(){
    var images = document.getElementsByTagName('img');
    var srcList = [];
    var i = 0;
    for(let i in images){
        if(images.length > i){

        srcList.push(images[i].src);
        var link = document.createElement("a");
        link.id=i;
        link.download = images[i].src;
        link.href = images[i].src;
        link.click();
        i++;
        }
        i++;
            }
};

function myFunction() {
    alert("This process will take around minute please be patinet and don't try again before one(1) minute");
  }

// const throttleInput=document.getElementById("Btn") ;
// throttleInput.onclick = function() {
//     if (!throttleInput.hasAttribute('data-prevent-double-click')) {
//       throttleInput.setAttribute('data-prevent-double-click', true);
//       throttleInput.setAttribute('disabled', true);
    
//     }

//     setTimeout(function() {
//         throttleInput.removeAttribute('disabled');
//         throttleInput.removeAttribute('data-prevent-double-click');
//       }, 9000);
// }