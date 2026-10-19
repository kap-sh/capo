"""Generated from Smithy shape ``com.amazonaws.glue#CreateRegistryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.description_string
    import capo_glue.types.schema_registry_name_string
    import capo_glue.types.tags_map


class CreateRegistryInput(TypedDict, closed=True):
    registry_name: (
        "capo_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    )
    """<p>Name of the registry to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of the registry. If description is not provided, there will not be any default value for this.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>Amazon Web Services tags that contain a key value pair and may be searched by console, command line, or API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRegistryInput) -> dict:
    out: dict = {}
    out["RegistryName"] = value["registry_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRegistryInput:
    out: CreateRegistryInput = {}  # type: ignore[typeddict-item]
    if data.get("RegistryName") is not None:
        out["registry_name"] = data["RegistryName"]
    else:
        out["registry_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
