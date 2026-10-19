"""Generated from Smithy shape ``com.amazonaws.codecommit#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.resource_arn
    import capo_codecommit.types.tag_keys_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_codecommit.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to which you want to remove tags.</p>"""
    tag_keys: "capo_codecommit.types.tag_keys_list.TagKeysList"
    """<p>The tag key for each tag that you want to remove from the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_codecommit.types.tag_keys_list

    out["tagKeys"] = capo_codecommit.types.tag_keys_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_codecommit.types.tag_keys_list

        out["tag_keys"] = capo_codecommit.types.tag_keys_list.deserialize_aws_json_1_1(
            data["tagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
