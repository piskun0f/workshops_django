from django.shortcuts import render
from io import BytesIO
import matplotlib.pyplot as plt

from .models import *
import datetime
import base64
import requests

def index(request):
    return render(request, 'index.html', {'posts': get_graphs()})

def get_str_models(models):
    return list(map(lambda model: str(model), models))

def get_graph_from_plt(plt):
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_clients_sums():
    clients = Client.objects.all()
    client_orders_sum = []
    for c in clients:
        client_orders = Order.objects.filter(client=c)
        client_sum = 0
        for order in client_orders:
            client_sum += order.final_sum
        client_orders_sum.append(client_sum)

    x = get_str_models(clients)
    y = client_orders_sum

    plt.figure(dpi=100)
    plt.scatter(x, y, marker='o')
    plt.xlabel('Клиенты')
    plt.ylabel('Сумма всех заказов')
    plt.title("Клиенты с суммами всех заказов")

    return get_graph_from_plt(plt)

def get_employees_orders_services():
    employees = Employee.objects.all()
    employee_orders_counts = []
    for e in employees:
        employee_orders_count = Services_order.objects.filter(employee=e).count()
        employee_orders_counts.append(employee_orders_count)

    x = get_str_models(employees)
    y = employee_orders_counts

    plt.figure(dpi=100)
    plt.scatter(x, y, marker='o')
    plt.xlabel('Сотрудники')
    plt.ylabel('Колличество предоставленных услуг')
    plt.title("Сотрудники и предоставленные ими услуги")

    return get_graph_from_plt(plt)

def get_workshop_client_count():
    workshops = Workshop.objects.all()
    workshops_client_count = []
    for w in workshops:
        workshop_orders = Order.objects.filter(workshop=w)
        workshop_clients = []
        for o in workshop_orders:
            if o.client not in workshop_clients:
                workshop_clients.append(o.client)
        workshops_client_count.append(len(workshop_clients))

    x = get_str_models(workshops)
    y = workshops_client_count

    plt.figure(dpi=100)
    plt.scatter(x, y, marker='o')
    plt.xlabel('Мастерские')
    plt.ylabel('Колличество клиентов')
    plt.title("Клиенты в мастерских")

    return get_graph_from_plt(plt)


def get_graphs():
    return [
        get_clients_sums(),
        get_employees_orders_services(),
        get_workshop_client_count()
    ]



