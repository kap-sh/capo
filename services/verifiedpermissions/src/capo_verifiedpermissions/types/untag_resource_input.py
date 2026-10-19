"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.amazon_resource_name
    import capo_verifiedpermissions.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: (
        "capo_verifiedpermissions.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN of the resource from which you are removing tags.</p>"""
    tag_keys: "capo_verifiedpermissions.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_verifiedpermissions.types.tag_key_list

    out["tagKeys"] = capo_verifiedpermissions.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_verifiedpermissions.types.tag_key_list

        out["tag_keys"] = (
            capo_verifiedpermissions.types.tag_key_list.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
