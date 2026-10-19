"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetBlueprintsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.batch_get_blueprint_names
    import capo_glue.types.nullable_boolean


class BatchGetBlueprintsRequest(TypedDict, closed=True):
    names: "capo_glue.types.batch_get_blueprint_names.BatchGetBlueprintNames"
    """<p>A list of blueprint names.</p>"""
    include_blueprint: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether or not to include the blueprint in the response.</p>"""
    include_parameter_spec: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether or not to include the parameters, as a JSON string, for the blueprint in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetBlueprintsRequest) -> dict:
    out: dict = {}
    import capo_glue.types.batch_get_blueprint_names

    out["Names"] = capo_glue.types.batch_get_blueprint_names.serialize_aws_json_1_1(
        value["names"]
    )
    if "include_blueprint" in value:
        out["IncludeBlueprint"] = value["include_blueprint"]
    if "include_parameter_spec" in value:
        out["IncludeParameterSpec"] = value["include_parameter_spec"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetBlueprintsRequest:
    out: BatchGetBlueprintsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_glue.types.batch_get_blueprint_names

        out["names"] = (
            capo_glue.types.batch_get_blueprint_names.deserialize_aws_json_1_1(
                data["Names"]
            )
        )
    else:
        out["names"] = []
    if data.get("IncludeBlueprint") is not None:
        out["include_blueprint"] = data["IncludeBlueprint"]
    if data.get("IncludeParameterSpec") is not None:
        out["include_parameter_spec"] = data["IncludeParameterSpec"]
    return out
