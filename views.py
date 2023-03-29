from .models import Sale, Claim
import csv
from django.http import HttpResponse
import seaborn as sns
from django.shortcuts import render
from matplotlib.backends.backend_agg import FigureCanvasAgg

def reports_dashboard(request):
    sales = Sale.objects.all()
    claims = Claim.objects.all()

    context = {'sales': sales, 'claims': claims}
    return render(request, 'reports_dashboard.html', context)

# export sales report as CSV file
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sales_report.csv"'
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(['Rank', 'Dealership', 'Daily Sales', 'Total Revenue'])

    # Query the sales data from the database
    sales = Sale.objects.all()

    # Write each sale as a row in the CSV file
    for i, sale in enumerate(sales, start=1):
        writer.writerow([i, sale.dealership, sale.daily_sales, sale.total_revenue])

    return response

# sales bar graph
def bar_graph(request):
    # Query the data for the bar graph from the database
    data = [sale.total_revenue for sale in Sale.objects.all()]

    # Create the bar graph using Seaborn
    sns.set(style="whitegrid")
    fig = sns.barplot(x=range(len(data)), y=data)
    canvas = FigureCanvasAgg(fig)
    html_graph = canvas.print_html()

    return render(request, 'bar_graph.html', {'html_graph': html_graph})





