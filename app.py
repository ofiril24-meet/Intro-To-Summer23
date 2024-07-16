from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
	return '''<html>
	<h1>football clubs</h1>
	<p>welcome to my photo gallery containing football clubs from 3 different countries</p>



<a href = "/sclub1">go to Spanish clubs</a>
<a href = "/eclub1">go to English clubs</a>
<a href = "/iclub1">go to Israeli clubs</a>

	</html '''

@app.route('/sclub1')
def sclub1():
	return '''<html>
<img src="https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_%28crest%29.svg/1200px-FC_Barcelona_%28crest%29.svg.png" style="width:400px;">
	
<a href = "/sclub2">go to Real Madrid</a>   
<a href = "/sclub3">go to Atletico Madrid</a>   
<a href = "/home"> go to the home page</a>

	</html> '''

@app.route('/sclub2')
def sclub2():
	return '''<html>
<img src="https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg" style="width:400px;">
	
<a href = "/sclub3">go to Atletico</a>   
<a href = "/home"> go to the home page</a>
<a href = "/sclub1">go to Barcelona</a>   

</html> '''

@app.route('/sclub3')
def sclub3():
	return '''<html>
<img src="https://1000logos.net/wp-content/uploads/2018/05/Atletico-Madrid-Logo.png" style="width:400px;">
	

<a href = "/home"> go to the home page</a>
<a href = "/sclub2">go to Real Madrid</a>   
<a href = "/sclub1">go to Barcelona</a> 

</html> '''




@app.route('/eclub1')
def eclub1():
	return '''<html>
<img src="https://play-lh.googleusercontent.com/i2OSOyplwv4yPnAzEuuv686uL1o6-C3wNKsX22tp29M9H3OJxPc7HjwpMa4yH7hIq9Vo" style="width:400px;">
	
<a href = "/eclub2">go to Arsenal</a>   
<a href = "/eclub3">go to Liverpool</a>   
<a href = "/home"> go to the home page</a>

	</html> '''

@app.route('/eclub2')
def eclub2():
	return '''<html>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKgXu7ZBK1tE1lATNl8554pU5V96k0oyqZgw&s" style="width:400px;">
	
<a href = "/eclub3">go to Liverpool</a>   
<a href = "/home"> go to the home page</a>
<a href = "/eclub1">go to Man city</a>   

</html> '''

@app.route('/eclub3')
def eclub3():
	return '''<html>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBDklYlhngkJv1VMrnpDAJcekiERzZg93ing&s" style="width:400px;">
	

<a href = "/home"> go to the home page</a>
<a href = "/eclub2">go to Arsenal</a>   
<a href = "/eclub1">go to Man city</a> 

</html> '''




@app.route('/iclub1')
def iclub1():
	return '''<html>
<img src="https://media.licdn.com/dms/image/C560BAQE6g2L4IFyG2w/company-logo_200_200/0/1637064706855/maccabi_tel_aviv_fc_logo?e=2147483647&v=beta&t=Y07kThtB3GWYctoRGm-vN9QHch6nzBr0nELe4NK2-Iw" style="width:400px;">
	
<a href = "/iclub2">go to Maccabi Haifa</a>   
<a href = "/iclub3">go to Hapoel Beer Sheva</a>   
<a href = "/home"> go to the home page</a>

	</html> '''

@app.route('/iclub2')
def iclub2():
	return '''<html>
<img src="https://thumbs.dreamstime.com/b/collection-vector-logos-most-famous-football-teams-world-maccabi-haifa-logo-154875230.jpg" style="width:400px;">
	
<a href = "/iclub3">go to Hapoel Beer Sheva</a>   
<a href = "/home"> go to the home page</a>
<a href = "/iclub1">go to Maccabi Tel Aviv</a>   

</html> '''

@app.route('/iclub3')
def iclub3():
	return '''<html>
<img src="https://upload.wikimedia.org/wikipedia/en/thumb/8/85/Logo-hapoel-positive.svg/225px-Logo-hapoel-positive.svg.png" style="width:400px;">
	

<a href = "/home"> go to the home page</a>
<a href = "/iclub2">go to Maccabi Haifa</a>   
<a href = "/iclub1">go to Maccabi Tel Aviv</a> 

</html> '''

    
if __name__ == '__main__':
    app.run(debug=True)