"""Generated from Smithy shape ``com.amazonaws.cloudhsm#AddTagsToResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.string
    import capo_cloudhsm.types.tag_list


class AddTagsToResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_cloudhsm.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the AWS CloudHSM resource to tag.</p>"""
    tag_list: "capo_cloudhsm.types.tag_list.TagList"
    """<p>One or more tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_cloudhsm.types.tag_list

    out["TagList"] = capo_cloudhsm.types.tag_list.serialize_aws_json_1_1(
        value["tag_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToResourceRequest:
    out: AddTagsToResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagList") is not None:
        import capo_cloudhsm.types.tag_list

        out["tag_list"] = capo_cloudhsm.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    else:
        out["tag_list"] = []
    return out
