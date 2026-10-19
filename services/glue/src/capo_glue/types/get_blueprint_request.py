"""Generated from Smithy shape ``com.amazonaws.glue#GetBlueprintRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.nullable_boolean


class GetBlueprintRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the blueprint.</p>"""
    include_blueprint: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether or not to include the blueprint in the response.</p>"""
    include_parameter_spec: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether or not to include the parameter specification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlueprintRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "include_blueprint" in value:
        out["IncludeBlueprint"] = value["include_blueprint"]
    if "include_parameter_spec" in value:
        out["IncludeParameterSpec"] = value["include_parameter_spec"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlueprintRequest:
    out: GetBlueprintRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("IncludeBlueprint") is not None:
        out["include_blueprint"] = data["IncludeBlueprint"]
    if data.get("IncludeParameterSpec") is not None:
        out["include_parameter_spec"] = data["IncludeParameterSpec"]
    return out
