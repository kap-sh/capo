"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestTemplateParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.parameter_type


class TestTemplateParameter(TypedDict, closed=True):
    name: "str"
    """<p>The name of the parameter.</p>"""
    description: NotRequired["str"]
    """<p>A description of the parameter.</p>"""
    type: "capo_resiliencehubv2.types.parameter_type.ParameterType"
    """<p>The data type of the parameter.</p>"""
    required: "bool"
    """<p>Indicates whether the parameter is required.</p>"""
    default_value: NotRequired["str"]
    """<p>The default value of the parameter.</p>"""
    max_values: NotRequired["int"]
    """<p>The maximum number of values the parameter accepts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestTemplateParameter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_resiliencehubv2.types.parameter_type

    out["type"] = capo_resiliencehubv2.types.parameter_type.serialize_json(
        value["type"]
    )
    out["required"] = value["required"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "max_values" in value:
        out["maxValues"] = value["max_values"]
    return out


def deserialize_json(data: dict) -> TestTemplateParameter:
    out: TestTemplateParameter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_resiliencehubv2.types.parameter_type

        out["type"] = capo_resiliencehubv2.types.parameter_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_resiliencehubv2.types.parameter_type.ParameterType", ""
        )
    if data.get("required") is not None:
        out["required"] = data["required"]
    else:
        out["required"] = False
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    if data.get("maxValues") is not None:
        out["max_values"] = data["maxValues"]
    return out
