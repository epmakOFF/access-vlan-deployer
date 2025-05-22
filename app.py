import json
from flask import request, Flask, render_template, redirect
from netmiko_switch import get_switch_info, deploy_vlan
# from scrapli_switch import get_switch_info, deploy_vlan

app = Flask(__name__)

@app.route("/")
def root():
    """
    Обрабатываем запрос на http://localhost:5000/?switch=cisco-sw
    """
    switch = request.args.get("switch")
    data = get_switch_info(switch)
    return render_template("pretty-index.html", **data)

@app.route("/deploy-vlan", methods=["POST"])
def deploy():
    """
    Обрабатываем нажатие кнопки (POST запрос в http://localhost:5000/deploy-vlan)
    """
    form_data = request.form.copy()
    switch = form_data.pop("switch")
    # данные берутся из формы {{ interfaces | tojson | safe }}
    # если не преобразовывать в json, то будет строка
    interfaces = json.loads(form_data.pop("interfaces"))
    vlans = form_data
    deploy_vlan(switch, interfaces, vlans)
    return redirect(f"/?switch={switch}")

if __name__ == "__main__":
    app.run(debug=True)