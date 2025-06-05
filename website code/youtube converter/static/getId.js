function myFuntion() {

    const urlvalue = document.getElementById("searchbox").value;

    const dict_values = {urlvalue}
    const s = JSON.stringify(dict_values);

    console.log(s);
    window.alert(s)
    $.ajax({
        url:"/test",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
}