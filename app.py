import json

from flask import Flask, redirect, render_template, request

from scrapli_switch import deploy_vlan, get_switch_info

# from netmiko_switch import deploy_vlan, get_switch_info


app = Flask(__name__)


@app.route("/<switch>")
def root(switch):
    """
    Обрабатываем запрос на http://localhost:5000/cisco-sw
    """
    data = get_switch_info(switch)
    if data:
        return render_template("pretty-index.html", **data)
    else:
        return "Can't get data from switch", 404


@app.route("/deploy-vlan", methods=["POST"])
def deploy():
    """
    Обрабатываем нажатие кнопки 
    (POST запрос в http://localhost:5000/deploy-vlan)
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

