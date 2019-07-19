from pdf import html_to_pdf

def data_to_html(test_data):
    f = open('test.html', 'w')

    tmp = ''
    for test in test_data:
        for title, data in test.items():
            tmp += '<h3>' + title + '</h3>' \
                                    '<table><tr>'
            newData = data['data']
            for col in newData.keys():
                tmp += '<th scope="col">' + col + '</th>'
            tmp += '</tr>' \
                '<tr>'
            for row in newData.values():
                if isinstance(row, list):
                    tmp += '<td scope="row">'
                    for test in range(len(row)):
                        tmp += "<br>" + row[test] + "</br>"
                    tmp += '</td>'
                else:
                    tmp += '<th scope="row">' + row + '</th>'
            tmp += '</tr></table>'
    message = \
        """<!doctype html>
            <html lang="en">

            <head>
            <!-- style CSS -->
                <link rel="stylesheet" href="style.css">
                <title>SDC HACK - ORIOS</title>
            </head>
            <body>
            <div>
                <h1>Voici le rapport des vunérabilités présente sur votre site</h1>
            </div> 
            %s
            </body>
        </html>"""
    f.write(message % (tmp))
    f.close()
    html_to_pdf()




