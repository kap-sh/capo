"""Generated from Smithy shape ``com.amazonaws.appmesh#AwsCloudMapInstanceAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.aws_cloud_map_instance_attribute_key
    import capo_app_mesh.types.aws_cloud_map_instance_attribute_value


class AwsCloudMapInstanceAttribute(TypedDict, closed=True):
    key: "capo_app_mesh.types.aws_cloud_map_instance_attribute_key.AwsCloudMapInstanceAttributeKey"
    """<p>The name of an Cloud Map service instance attribute key. Any Cloud Map service instance that contains the specified key and value is returned.</p>"""
    value: "capo_app_mesh.types.aws_cloud_map_instance_attribute_value.AwsCloudMapInstanceAttributeValue"
    """<p>The value of an Cloud Map service instance attribute key. Any Cloud Map service instance that contains the specified key and value is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudMapInstanceAttribute) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AwsCloudMapInstanceAttribute:
    out: AwsCloudMapInstanceAttribute = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
