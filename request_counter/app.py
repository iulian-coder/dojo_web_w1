from flask import Flask, render_template, request

app = Flask(__name__)

counter_get = 0
counter_post = 0
counter_put = 0
counter_delete = 0


@app.route('/')
def index_home():
    return render_template(/)
@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index_home():
    global counter_get, counter_post, counter_put, counter_delete
    if request.method == 'GET':
        counter_get += 1
    elif request.method == 'POST':
        counter_post += 1
    elif request.method == 'PUT':
        counter_put += 1
    elif request.method == 'DELETE':
        counter_delete += 1
    return render_template('request-counter.html')


@app.route('/statistics')
def index_statics():
    return render_template('statistics.html',
                           counter_get=counter_get,
                           counter_post=counter_post,
                           counter_put=counter_put,
                           counter_delete=counter_delete)


@app.route('/export')
def index_export():
    data = 'GET:' + str(counter_get) + '\n' + 'POST:' + str(counter_put) + '\n' + 'DELETE' + str(counter_delete) + '\n' + 'PUT:' + str(counter_put)
    with open('request_counts.txt', 'w') as file:
        file.write(data)
    return "The data had been exported"


if __name__ == '__main__':
    app.run(debug=True)
