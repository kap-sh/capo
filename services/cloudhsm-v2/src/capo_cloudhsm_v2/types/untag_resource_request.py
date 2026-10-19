"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.resource_id
    import capo_cloudhsm_v2.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_id: "capo_cloudhsm_v2.types.resource_id.ResourceId"
    """<p>The cluster identifier (ID) for the cluster whose tags you are removing. To find the cluster ID, use <a>DescribeClusters</a>.</p>"""
    tag_key_list: "capo_cloudhsm_v2.types.tag_key_list.TagKeyList"
    """<p>A list of one or more tag keys for the tags that you are removing. Specify only the tag keys, not the tag values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_cloudhsm_v2.types.tag_key_list

    out["TagKeyList"] = capo_cloudhsm_v2.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_key_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("TagKeyList") is not None:
        import capo_cloudhsm_v2.types.tag_key_list

        out["tag_key_list"] = (
            capo_cloudhsm_v2.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeyList"]
            )
        )
    else:
        out["tag_key_list"] = []
    return out
