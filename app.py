from flask import Flask,render_template,request

app = Flask(__name__)
@app.route("/")

def visitors_count():
	f = open("count.txt","r")
	count = int(f.read())
	f.close()

	count += 1

	f = open("count.txt","w")
	f.write(str(count))
	f.close()

	return render_template("index.html",counter=count)

@app.route("/",methods=["POST"])
def update():
	f = open("count.txt","r")
	count = int(f.read())
	f.close()

	country_name = request.form["text"]
	url = "https://covidstats-sdbd.onrender.com/?country="
	final_url = url+country_name

	print(final_url)
	return render_template("index.html",counter=count,image=final_url)

if __name__ == "__main__":
	app.run()