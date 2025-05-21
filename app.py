from flask import request, Flask, render_template, redirect
from netmiko_switch import get_switch_info, deploy_vlan
# from scrapli_switch import get_switch_info, deploy_vlan

app = Flask(__name__)

@app.route("/")
def root():
    switch = request.args.get("switch")
    data = get_switch_info(switch)
    return render_template("index.html", **data)

@app.route("/deploy-vlan", methods=["POST"])
def deploy():
    data = dict(request.form)
    switch = data.pop("switch")
    interfaces = eval(data.pop("interfaces"))
    deploy_vlan(switch, interfaces, data)
    return redirect(f"/?switch={switch}")

if __name__ == "__main__":
    app.run(debug=True)