from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "gogandabaoshe"
machine = TocMachine(
    states=[
        'user',
        'name',
        'category',
	    'takahashishouko',
	    'sakuramomo',
	    'miurasakura',
	    'shinodayuu',
	    'hashimotoarina',
	    'sonodamion',
	    'itochinami',
	    'ayamishunka',
	    'kogawaiori',
	    'takahashishouko_rand',
	    'sakuramomo_rand',
	    'miurasakura_rand',
	    'shinodayuu_rand',
	    'hashimotoarina_rand',
	    'sonodamion_rand',
	    'itochinami_rand',
	    'ayamishunka_rand',
	    'kogawaiori_rand',
	    'bigtits',
	    'uncensored',
	    'amateur',
	    'wife',
	    'schoolgirl',
	    'special',
	    'congrats'    
	    
	    
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'name',
            'conditions': 'is_going_to_name'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'special',
            'conditions': 'is_going_to_special'
        },
        {
            'trigger': 'advance',
            'source': 'special',
            'dest': 'congrats',
            'conditions': 'is_going_to_congrats'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'category',
            'conditions': 'is_going_to_category'
        },
        {
            'trigger': 'advance',
            'source': 'category',
            'dest': 'bigtits',
            'conditions': 'is_going_to_bigtits'
        },
        {
            'trigger': 'advance',
            'source': 'category',
            'dest': 'uncensored',
            'conditions': 'is_going_to_uncensored'
        },
        {
            'trigger': 'advance',
            'source': 'category',
            'dest': 'amateur',
            'conditions': 'is_going_to_amateur'
        },
        {
            'trigger': 'advance',
            'source': 'category',
            'dest': 'wife',
            'conditions': 'is_going_to_wife'
        },
        {
            'trigger': 'advance',
            'source': 'category',
            'dest': 'schoolgirl',
            'conditions': 'is_going_to_schoolgirl'
        },
	    {
	    'trigger': 'advance',
	    'source': 'name',
	    'dest': 'takahashishouko',
	    'conditions': 'is_going_to_takahashishouko'
	    },
        {
            'trigger': 'advance',
            'source': 'takahashishouko',
            'dest': 'takahashishouko_rand',
            'conditions': 'is_going_to_takahashishouko_rand'
        },
	    {
	    'trigger': 'advance',
	    'source': 'name',
	    'dest': 'sakuramomo',
	    'conditions': 'is_going_to_sakuramomo'
	    },
	    {
	    'trigger': 'advance',
	    'source': 'sakuramomo',
	    'dest': 'sakuramomo_rand',
	    'conditions': 'is_going_to_sakuramomo_rand'
	    },
	    {
	    'trigger': 'advance',
	    'source': 'name',
	    'dest': 'miurasakura',
	    'conditions': 'is_going_to_miurasakura'
	    },
        {
            'trigger': 'advance',
            'source': 'miurasakura',
            'dest': 'miurasakura_rand',
            'conditions': 'is_going_to_miurasakura_rand'
        },
	    {
	    'trigger': 'advance',
	    'source': 'name',
	    'dest': 'shinodayuu',
	    'conditions': 'is_going_to_shinodayuu'
	    },
        {
            'trigger': 'advance',
            'source': 'shinodayuu',
            'dest': 'shinodayuu_rand',
            'conditions': 'is_going_to_shinodayuu_rand'
        },
	    {
	    'trigger': 'advance',
	    'source': 'name',
	    'dest': 'hashimotoarina',
	    'conditions': 'is_going_to_hashimotoarina'
	    },
	    {
	    'trigger': 'advance',
	    'source': 'hashimotoarina',
	    'dest': 'hashimotoarina_rand',
	    'conditions': 'is_going_to_hashimotoarina_rand'
	    },
	    {
	    'trigger': 'advance',
	    'source': 'name',
	    'dest': 'sonodamion',
	    'conditions': 'is_going_to_sonodamion'
	    },
        {
            'trigger': 'advance',
            'source': 'sonodamion',
            'dest': 'sonodamion_rand',
            'conditions': 'is_going_to_sonodamion_rand'
        },
	    {
	    'trigger': 'advance',
	    'source': 'name',
	    'dest': 'itochinami',
	    'conditions': 'is_going_to_itochinami'
	    },
	    {
	    'trigger': 'advance',
	    'source': 'itochinami',
	    'dest': 'itochinami_rand',
	    'conditions': 'is_going_to_itochinami_rand'
	    },
	    {
	    'trigger': 'advance',
	    'source': 'name',
	    'dest': 'ayamishunka',
	    'conditions': 'is_going_to_ayamishunka'
	    },
	    {
	    'trigger': 'advance',
	    'source': 'ayamishunka',
	    'dest': 'ayamishunka_rand',
	    'conditions': 'is_going_to_ayamishunka_rand'
	    },
	    {
	    'trigger': 'advance',
	    'source': 'name',
	    'dest': 'kogawaiori',
	    'conditions': 'is_going_to_kogawaiori'
	    },
	    {
	    'trigger': 'advance',
	    'source': 'kogawaiori',
	    'dest': 'kogawaiori_rand',
	    'conditions': 'is_going_to_kogawaiori_rand'
	    },
        {
            'trigger': 'go_back',
            'source': [
                'name',
                'category',
		        'takahashishouko',
		        'sakuramomo',
		        'miurasakura',
		        'shinodayuu',
		        'hashimotoarina',
		        'sonodamion',
		        'itochinami',
		        'ayamishunka',
		        'kogawaiori',
		        'takahashishouko_rand',
		        'sakuramomo_rand',
		        'miurasakura_rand',
		        'shinodayuu_rand',
		        'hashimotoarina_rand',
		        'sonodamion_rand',
		        'itochinami_rand',
		        'ayamishunka_rand',
		        'kogawaiori_rand',
		        'bigtits',
		        'uncensored',
		        'amateur',
		        'wife',
		        'schoolgirl',
		        'special',
		        'congrats'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)
    show_fsm()

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
    
