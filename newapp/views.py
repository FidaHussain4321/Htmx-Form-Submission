from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegistrationForm
import plotly.express as px
import pandas as pd


class FileUploadView(View):
    def get(self, request):
        return render(request, 'fileupload.html')
    def post(self, request):
        file = request.FILES['file']
        df = pd.read_csv(file)
        return render(request, 'partial.html', {'df': df})



def pandas_view(request):
    df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    df=df.head(10)
    print(df)
    
    return render(request, 'pandas.html', {'df': df})   

def plotly_view(request):
    df = px.data.iris()
    df["point_size"]=3
    print(df)
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",size="point_size",width=800, height=600, hover_data=["petal_width"],title="flower dataset" )
    fig.update_layout(
        title_font_size=20,
        title_font_color="black",
        title_x=0.5,
        title_y=0.9,
        title_xanchor="center",
        xaxis_title="sepal_width",
        yaxis_title="sepal_length",
        xaxis_title_font_color="blue",
        yaxis_title_font_color="blue",
        
    )
    fig.add_shape(
     x0=df["sepal_width"].min(),
     x1=df["sepal_width"].max(),
     y0=df["sepal_length"].mean(),
     y1=df["sepal_length"].mean(),
     type="line",
     line=dict(color="yellow",width=2),
     name="average sepal length",
     showlegend=True    
    )
    fig.add_shape(
        y0=df["sepal_length"].min(),
        y1=df["sepal_length"].max(),
        x0=df["sepal_width"].mean(),
        x1=df["sepal_width"].mean(),
        type="line",
        line=dict(color="yellow",width=2),
        name="average sepal width",
        showlegend=True
    )
    fig.add_shape(
        x0=df["sepal_width"][df["sepal_length"].idxmax()] - 0.2,
        y0=df["sepal_length"][df["sepal_length"].idxmax()] - 0.2,
        x1=df["sepal_width"][df["sepal_length"].idxmax()] + 0.2,
        y1=df["sepal_length"][df["sepal_length"].idxmax()] + 0.2,
        type="circle",
        line=dict(color="pink",width=2),
        name="largest sepal length",
        fillcolor="rgba(255,192,203,0.3)",  # light pink fill with transparency

        showlegend=True
    )
    
    plot_fig = fig.to_html(
        full_html=False, include_plotlyjs="cdn", config={"responsive": True}
    )
    fig2=px.bar(df,x="species",y="petal_length",color="species",width=800,height=600)
    plot_fig2=fig2.to_html(
        full_html=False, include_plotlyjs="cdn", config={"responsive": True}
    )
    return render(request, 'plotly.html', {'fig': plot_fig,'fig2':plot_fig2})

def success(request):
    return render(request, 'success.html')

# Create your views here.
def getresults(request):
    props = {"goal": "2025"}
    return render(request, 'first.html', context=props)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # Or redirect to a success URL
        else:
            # Return form with validation errors
            return render(request, "registration/form_with_errors.html", {"form": form})    
    else:
        form = RegistrationForm()  # ✅ This line was over-indented before
        return render(request, 'registrationpage.html', {'form': form})

def dashboard_view(request):
    return render(request, 'dashboard.html')
