"""Generated from Smithy shape ``com.amazonaws.sfn#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the Step Functions state machine or activity.</p>"""
    tags: "capo_sfn.types.tag_list.TagList"
    """<p>The list of tags to add to a resource.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: <code>_ . : / = + - @</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_sfn.types.tag_list

    out["tags"] = capo_sfn.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_sfn.types.tag_list

        out["tags"] = capo_sfn.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    else:
        out["tags"] = []
    return out
