"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.parameter_name
    import capo_cleanrooms.types.parameter_type
    import capo_cleanrooms.types.parameter_value


class AnalysisParameter(TypedDict, closed=True):
    name: "capo_cleanrooms.types.parameter_name.ParameterName"
    """<p>The name of the parameter. The name must use only alphanumeric or underscore (_) characters.</p>"""
    type: "capo_cleanrooms.types.parameter_type.ParameterType"
    """<p>The type of parameter.</p>"""
    default_value: NotRequired["capo_cleanrooms.types.parameter_value.ParameterValue"]
    """<p>Optional. The default value that is applied in the analysis template. The member who can query can override this value in the query editor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisParameter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_cleanrooms.types.parameter_type

    out["type"] = capo_cleanrooms.types.parameter_type.serialize_json(value["type"])
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> AnalysisParameter:
    out: AnalysisParameter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_cleanrooms.types.parameter_type

        out["type"] = capo_cleanrooms.types.parameter_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cleanrooms.types.parameter_type.ParameterType", ""
        )
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    return out
