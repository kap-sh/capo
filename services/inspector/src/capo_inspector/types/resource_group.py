"""Generated from Smithy shape ``com.amazonaws.inspector#ResourceGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.resource_group_tags
    import capo_inspector.types.timestamp


class ResourceGroup(TypedDict, closed=True):
    arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the resource group.</p>"""
    tags: "capo_inspector.types.resource_group_tags.ResourceGroupTags"
    """<p>The tags (key and value pairs) of the resource group. This data type property is used in the <a>CreateResourceGroup</a> action.</p>"""
    created_at: "capo_inspector.types.timestamp.Timestamp"
    """<p>The time at which resource group is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceGroup) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_inspector.types.resource_group_tags

    out["tags"] = capo_inspector.types.resource_group_tags.serialize_aws_json_1_1(
        value["tags"]
    )
    import capo_inspector.types.timestamp

    out["createdAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
        value["created_at"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceGroup:
    out: ResourceGroup = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("tags") is not None:
        import capo_inspector.types.resource_group_tags

        out["tags"] = capo_inspector.types.resource_group_tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        out["tags"] = []
    if data.get("createdAt") is not None:
        import capo_inspector.types.timestamp

        out["created_at"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
