"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_filter_name
    import capo_lex_models_v2.types.bot_filter_operator
    import capo_lex_models_v2.types.filter_values


class BotFilter(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.bot_filter_name.BotFilterName"
    """<p>The name of the field to filter the list of bots.</p>"""
    values: "capo_lex_models_v2.types.filter_values.FilterValues"
    """<p>The value to use for filtering the list of bots.</p>"""
    operator: "capo_lex_models_v2.types.bot_filter_operator.BotFilterOperator"
    """<p>The operator to use for the filter. Specify <code>EQ</code> when the <code>ListBots</code> operation should return only aliases that equal the specified value. Specify <code>CO</code> when the <code>ListBots</code> operation should return aliases that contain the specified value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotFilter) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.bot_filter_name

    out["name"] = capo_lex_models_v2.types.bot_filter_name.serialize_json(value["name"])
    import capo_lex_models_v2.types.filter_values

    out["values"] = capo_lex_models_v2.types.filter_values.serialize_json(
        value["values"]
    )
    import capo_lex_models_v2.types.bot_filter_operator

    out["operator"] = capo_lex_models_v2.types.bot_filter_operator.serialize_json(
        value["operator"]
    )
    return out


def deserialize_json(data: dict) -> BotFilter:
    out: BotFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_lex_models_v2.types.bot_filter_name

        out["name"] = capo_lex_models_v2.types.bot_filter_name.deserialize_json(
            data["name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_lex_models_v2.types.bot_filter_name.BotFilterName", ""
        )
    if data.get("values") is not None:
        import capo_lex_models_v2.types.filter_values

        out["values"] = capo_lex_models_v2.types.filter_values.deserialize_json(
            data["values"]
        )
    else:
        out["values"] = []
    if data.get("operator") is not None:
        import capo_lex_models_v2.types.bot_filter_operator

        out["operator"] = capo_lex_models_v2.types.bot_filter_operator.deserialize_json(
            data["operator"]
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_lex_models_v2.types.bot_filter_operator.BotFilterOperator", ""
        )
    return out
