from h2o_wave import Q, ui, data

def add_chart(box, title, plot_type='interval'):
    return ui.plot_card(
        box=box,
        title=title,
        data=data('xvalue yvalue'),
        plot=ui.plot([ui.mark(type=plot_type, x='=xvalue', y='=yvalue', color='=yvalue')])
    )

def add_gauge_card(box, key, value):
    return ui.tall_gauge_stat_card(
                box=box,
                title=key,
                value='={{intl value minimum_fraction_digits=2 maximum_fraction_digits=2}}',
                aux_value='',
                plot_color='$red',
                progress=value,
                data=dict(value=value),
            )

def add_stat_card(box, key, value):
    return ui.large_stat_card(
            box=box,
            title=key,
            value='={{intl value}}',
            aux_value='',
            data = dict(value=value),
            caption=key + " of the selected customer"
        )


def add_header_card(box):
    return ui.header_card(box=box, 
                icon='UserFollowed', 
                icon_color='Yellow', 
                title="Credit Scoring Wave Application", 
                subtitle="Generate Credit Score Predictions using Driverless AI" )

def add_sidebar_card(box, customer_ids):
    id_choices = [ui.choice(_, "Customer:" + str(_)) for _ in customer_ids]
    return ui.form_card(box=box,
                        items = [
                                 ui.text_xl(content='Select Customer Record'),
                                 ui.dropdown(name='customer_id', label='CustomerID', choices=id_choices),
                                 ui.button(name='predict', label='Generate', primary=True)
                                 ])

def add_text_card(box, text):
    return ui.form_card(box=box, items = [ui.text_l(text)])
