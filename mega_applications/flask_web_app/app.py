from flask import Flask, render_template

app=Flask(__name__)

@app.route('/') #decorator specify the url
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN


    ##Data from Yahoo Finance
    start = datetime.datetime(2017,9,1)
    end = datetime.datetime(2017,10,20)
    # end = datetime.datetime.now() #today
    df = data.DataReader(name="AMZN", data_source="yahoo",start=start,end=end)
    # type(df) #pandas.core.frame.DataFrame
    def inc_dec(c, o):
        if c > o:
            value="Rise"
        elif c < o:
            value = "Fall"
        else:
            value = "Same"
        return value

    df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close, df.Open)]
    df["Middle"] = (df.Close + df.Open) / 2
    df["Height"] = abs(df.Open-df.Close)
    df.head()

    # Use Bokeh for plotting

    p=figure(x_axis_type='datetime', width=1000, height=300, responsive=True)
    p.title.text="Candlestick Chart"
    hours_12 = 12*60*60*1000
    p.grid.grid_line_alpha = 0.2

    p.segment(df.index, df.High, df.index, df.Low, color="black")

    p.rect(df.index[df.Status== "Rise"],df.Middle[df.Status== "Rise"],
           hours_12, df.Height[df.Status== "Rise"], fill_color="#03AD3E",
           line_color="black" )
    p.rect(df.index[df.Status== "Fall"],df.Middle[df.Status== "Fall"],
           hours_12, df.Height[df.Status== "Fall"], fill_color="#E30400",
           line_color="black" )
    # for deploying to webserver
    script1, div1 = components(p)

    # generate dynamic js & css script files
    cdn_js=CDN.js_files[0]
    cdn_css=CDN.css_files[0]
    return render_template("plot.html",
    script1=script1,
    div1=div1,
    cdn_css=cdn_css,
    cdn_js=cdn_js)
    # output_file("candle_stick_chart.html")
    # show(p)

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
