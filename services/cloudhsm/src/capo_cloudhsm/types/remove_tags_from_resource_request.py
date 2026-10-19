"""Generated from Smithy shape ``com.amazonaws.cloudhsm#RemoveTagsFromResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.string
    import capo_cloudhsm.types.tag_key_list


class RemoveTagsFromResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_cloudhsm.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the AWS CloudHSM resource.</p>"""
    tag_key_list: "capo_cloudhsm.types.tag_key_list.TagKeyList"
    """<p>The tag key or keys to remove.</p> <p>Specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use <a>AddTagsToResource</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_cloudhsm.types.tag_key_list

    out["TagKeyList"] = capo_cloudhsm.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_key_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromResourceRequest:
    out: RemoveTagsFromResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeyList") is not None:
        import capo_cloudhsm.types.tag_key_list

        out["tag_key_list"] = capo_cloudhsm.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeyList"]
        )
    else:
        out["tag_key_list"] = []
    return out
