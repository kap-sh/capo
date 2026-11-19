"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeTagsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.tag_list


class DescribeTagsResult(TypedDict, closed=True):
    tag_list: NotRequired["capo_workspaces.types.tag_list.TagList"]
    """<p>The tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagsResult) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import capo_workspaces.types.tag_list

        out["TagList"] = capo_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagsResult:
    out: DescribeTagsResult = {}  # type: ignore[typeddict-item]
    if data.get("TagList") is not None:
        import capo_workspaces.types.tag_list

        out["tag_list"] = capo_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeTagsResult) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import capo_workspaces.types.tag_list

        out["TagList"] = capo_workspaces.types.tag_list.serialize_cbor(
            value["tag_list"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeTagsResult:
    out: DescribeTagsResult = {}  # type: ignore[typeddict-item]
    if data.get("TagList") is not None:
        import capo_workspaces.types.tag_list

        out["tag_list"] = capo_workspaces.types.tag_list.deserialize_cbor(
            data["TagList"]
        )
    return out
