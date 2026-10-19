"""Generated from Smithy shape ``com.amazonaws.glue#CreateBlueprintRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic512_char_string
    import capo_glue.types.orchestration_name_string
    import capo_glue.types.orchestration_s3_location
    import capo_glue.types.tags_map


class CreateBlueprintRequest(TypedDict, closed=True):
    name: "capo_glue.types.orchestration_name_string.OrchestrationNameString"
    """<p>The name of the blueprint.</p>"""
    description: NotRequired[
        "capo_glue.types.generic512_char_string.Generic512CharString"
    ]
    """<p>A description of the blueprint.</p>"""
    blueprint_location: (
        "capo_glue.types.orchestration_s3_location.OrchestrationS3Location"
    )
    """<p>Specifies a path in Amazon S3 where the blueprint is published.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>The tags to be applied to this blueprint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBlueprintRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["BlueprintLocation"] = value["blueprint_location"]
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBlueprintRequest:
    out: CreateBlueprintRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("BlueprintLocation") is not None:
        out["blueprint_location"] = data["BlueprintLocation"]
    else:
        out["blueprint_location"] = ""
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
