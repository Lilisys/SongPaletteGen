//Set up a blank canvas
var canvas = document.createElement('canvas'),
    ctx = canvas.getContext('2d');
canvas.setAttribute('width', 2000);
canvas.setAttribute('height', 3000);

//Set up the canvas on screen
var preview = document.getElementById('preview'),
	ctx = canvas.getContext('2d');
ctx.fillStyle = '#ffffff';
//Globals
var hex0 = "";
var hex1 = "";
var hex2 = "";
//For fillRects
var smallBound = 10;
var smallOffset0 = 260;
var smallOffset1 = 270;
var smallOffset2 = 280;
var bigBound = smallBound * 10;
var bigOffset0 = smallOffset0 * 10;
var bigOffset1 = smallOffset1 * 10;
var bigOffset2 = smallOffset2 * 10;
//Show preview
//inputs with quotes and parens in the form "(r,g,b)" 
function doPreview(rgb0, rgb1, rgb2) {
	//Assign hex vals from given rgb
	hex0 = 	rgb2hex("rgb" + rgb0);
	hex1 = 	rgb2hex("rgb" + rgb1);
	hex2 = 	rgb2hex("rgb" + rgb2);
	
	//For the preview
	var c = document.getElementById("preview");
	var ctx = c.getContext("2d");
	console.log(hex0, hex1, hex2)
	ctx.fillStyle = hex0;
	ctx.fillRect(smallBound, smallOffset0, smallBound, smallBound);
	ctx.fillStyle = hex1;
	ctx.fillRect(smallBound, smallOffset1, smallBound, smallBound);
	ctx.fillStyle = hex2;
	ctx.fillRect(smallBound, smallOffset2, smallBound, smallBound);  

}

function doPreviewHex(in_hex0, in_hex1, in_hex2) {
	//Assign hex vals from given rgb
	hex0 = 	in_hex0;
	hex1 = 	in_hex1;
	hex2 = 	in_hex2;
	
	//For the preview
	var c = document.getElementById("preview");
	var ctx = c.getContext("2d");
	console.log(hex0, hex1, hex2)
	ctx.fillStyle = hex0;
	ctx.fillRect(smallBound, smallOffset0, smallBound, smallBound);
	ctx.fillStyle = hex1;
	ctx.fillRect(smallBound, smallOffset1, smallBound, smallBound);
	ctx.fillStyle = hex2;
	ctx.fillRect(smallBound, smallOffset2, smallBound, smallBound);  

}



//Init generals 
// ctx.fillStyle = '#ffffff';
ctx.fillRect(0, 0, canvas.width, canvas.height);

// call it like
// rgb2hex("rgb(123,0,33)")
function rgb2hex(rgb) {
    rgb = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    console.log(rgb);
    function hex(x) {
        return ("0" + parseInt(x).toString(16)).slice(-2);
    }
    return "#" + hex(rgb[1]) + hex(rgb[2]) + hex(rgb[3]);
}



function download() {
	//For the actual canvas
	var c = canvas
	var ctx = c.getContext("2d");
	ctx.fillStyle = hex0;
	ctx.fillRect(bigBound, bigOffset0, bigBound, bigBound);
	ctx.fillStyle = hex1;
	ctx.fillRect(bigBound, bigOffset1, bigBound, bigBound);
	ctx.fillStyle = hex2;
	ctx.fillRect(bigBound, bigOffset2, bigBound, bigBound); 

    var dt = canvas.toDataURL();
    this.href = dt; //this may not work in the future..
}
document.getElementById('download').addEventListener('click', download, false);



/**
 * START
 */
// doPreview(	"(123, 222, 11)", 
// 			"(97, 55, 234)", 
// 			"(222, 13, 121)");
