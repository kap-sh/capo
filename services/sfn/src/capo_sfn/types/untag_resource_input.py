"""Generated from Smithy shape ``com.amazonaws.sfn#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the Step Functions state machine or activity.</p>"""
    tag_keys: "capo_sfn.types.tag_key_list.TagKeyList"
    """<p>The list of tags to remove from the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_sfn.types.tag_key_list

    out["tagKeys"] = capo_sfn.types.tag_key_list.serialize_aws_json_1_0(
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
        import capo_sfn.types.tag_key_list

        out["tag_keys"] = capo_sfn.types.tag_key_list.deserialize_aws_json_1_0(
            data["tagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
