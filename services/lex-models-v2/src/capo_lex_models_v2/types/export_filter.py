"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.export_filter_name
    import capo_lex_models_v2.types.export_filter_operator
    import capo_lex_models_v2.types.filter_values


class ExportFilter(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.export_filter_name.ExportFilterName"
    """<p>The name of the field to use for filtering.</p>"""
    values: "capo_lex_models_v2.types.filter_values.FilterValues"
    """<p>The values to use to filter the response. The values must be <code>Bot</code>, <code>BotLocale</code>, or <code>CustomVocabulary</code>.</p>"""
    operator: "capo_lex_models_v2.types.export_filter_operator.ExportFilterOperator"
    """<p>The operator to use for the filter. Specify EQ when the <code>ListExports</code> operation should return only resource types that equal the specified value. Specify CO when the <code>ListExports</code> operation should return resource types that contain the specified value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportFilter) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.export_filter_name

    out["name"] = capo_lex_models_v2.types.export_filter_name.serialize_json(
        value["name"]
    )
    import capo_lex_models_v2.types.filter_values

    out["values"] = capo_lex_models_v2.types.filter_values.serialize_json(
        value["values"]
    )
    import capo_lex_models_v2.types.export_filter_operator

    out["operator"] = capo_lex_models_v2.types.export_filter_operator.serialize_json(
        value["operator"]
    )
    return out


def deserialize_json(data: dict) -> ExportFilter:
    out: ExportFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_lex_models_v2.types.export_filter_name

        out["name"] = capo_lex_models_v2.types.export_filter_name.deserialize_json(
            data["name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_lex_models_v2.types.export_filter_name.ExportFilterName", ""
        )
    if data.get("values") is not None:
        import capo_lex_models_v2.types.filter_values

        out["values"] = capo_lex_models_v2.types.filter_values.deserialize_json(
            data["values"]
        )
    else:
        out["values"] = []
    if data.get("operator") is not None:
        import capo_lex_models_v2.types.export_filter_operator

        out["operator"] = (
            capo_lex_models_v2.types.export_filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_lex_models_v2.types.export_filter_operator.ExportFilterOperator", ""
        )
    return out
