"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.resource_id
    import capo_cloudhsm_v2.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_id: "capo_cloudhsm_v2.types.resource_id.ResourceId"
    """<p>The cluster identifier (ID) for the cluster that you are tagging. To find the cluster ID, use <a>DescribeClusters</a>.</p>"""
    tag_list: "capo_cloudhsm_v2.types.tag_list.TagList"
    """<p>A list of one or more tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_cloudhsm_v2.types.tag_list

    out["TagList"] = capo_cloudhsm_v2.types.tag_list.serialize_aws_json_1_1(
        value["tag_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("TagList") is not None:
        import capo_cloudhsm_v2.types.tag_list

        out["tag_list"] = capo_cloudhsm_v2.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    else:
        out["tag_list"] = []
    return out
