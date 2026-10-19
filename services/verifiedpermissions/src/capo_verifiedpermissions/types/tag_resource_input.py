"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.amazon_resource_name
    import capo_verifiedpermissions.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: (
        "capo_verifiedpermissions.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN of the resource that you're adding tags to.</p>"""
    tags: "capo_verifiedpermissions.types.tag_map.TagMap"
    """<p>The list of key-value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_verifiedpermissions.types.tag_map

    out["tags"] = capo_verifiedpermissions.types.tag_map.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_verifiedpermissions.types.tag_map

        out["tags"] = capo_verifiedpermissions.types.tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
