from dash_extensions.enrich import html, dcc
import dash_svg
from src import config


def YearSelector(id_slider, id_input):
    div_slider = (config.seasons[1] - config.seasons[0] + 1) // 5
    marks_slider = {n: str(n) for n in range(config.seasons[0], config.seasons[1] + 1, div_slider)}
    marks_slider[config.seasons[1]] = str(config.seasons[1])
    return html.Div(
        className="flex flex-row items-top space-x-2 mx-2",
        children=[
            html.Div(
                className="w-full relative mb-6",
                children=[
                    dcc.Input(
                        id=id_slider,
                        type="range",
                        value=config.default_year,
                        min=config.seasons[0],
                        max=config.seasons[1],
                        step=1,
                        className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer",
                    ),
                    html.Span(
                        className="text-sm text-gray-500 absolute start-0 -bottom-6",
                        children=f"{config.seasons[0]}",
                    ),
                    html.Span(
                        className="text-sm text-gray-500 absolute end-0 -bottom-6",
                        children=f"{config.seasons[1]}",
                    ),
                ],
            ),
            dcc.Input(
                id=id_input,
                className="w-20 border border-gray rounded-lg px-2",
                type="number",
                min=config.seasons[0],
                max=config.seasons[1],
                value=config.default_year,
                style={"width": "20%", "display": "inline-block"},
            ),
        ],
    )
