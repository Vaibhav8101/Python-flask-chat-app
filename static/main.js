//console.log(3+3) for printing
//var x=5
//if (x>2)
//{
	//console.log('greater')
//}
//else
//{
	//console.log('smaller')
//}
//function area(l,b)
//{
	//a=l*b
	//return a
//}
//a1=area(l,b)
//for (var i=1;i<=5;i++)
//{

//}
console.log('Hello')
var socket = io.connect(location.protocol+'//'+document.domain+':'+location.port);
function send(){
	var msgBox=document.getElementById('msgBox')
	socket.emit('msg',msgBox.value)
	msgBox.value=""
}


socket.on('push',function(data){
	var msgList=document.getElementById('msgList')
	msgList.innerHTML+="<p>"+data+"</p>"
})


function fetchUsers	()
{
	fetch('/users').then(function(res){
		res.json().then(function(data){
			console.log(data)
		})
	})
}
// var socket = io.connect(location.protocal+'//'+document.domain+':'+location.port);
// // socket.on('connect', function() {
//     socket.emit('my event', {data: 'I\'m connected!'});
// });
// function send(){
// 	socket.emit('msg','Hello')//client send message


