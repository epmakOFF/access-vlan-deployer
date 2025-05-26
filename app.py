import json

from flask import Flask, redirect, render_template, request

# from netmiko_switch import deploy_vlan, get_switch_info

from scrapli_switch import get_switch_info, deploy_vlan

app = Flask(__name__)


@app.route("/<switch>")
def root(switch):
    """
    Обрабатываем запрос на http://localhost:5000/?switch=cisco-sw
    """
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
    # если не преобразовывать в json, то вернется строка
    # и ее придется прогонять через eval, что не рекомендуется
    interfaces = json.loads(form_data.pop("interfaces"))
    vlans = form_data
    deploy_vlan(switch, interfaces, vlans)
    return redirect(f"/{switch}")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
