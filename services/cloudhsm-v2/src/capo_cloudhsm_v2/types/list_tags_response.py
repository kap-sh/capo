"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ListTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.next_token
    import capo_cloudhsm_v2.types.tag_list


class ListTagsResponse(TypedDict, closed=True):
    tag_list: "capo_cloudhsm_v2.types.tag_list.TagList"
    """<p>A list of tags.</p>"""
    next_token: NotRequired["capo_cloudhsm_v2.types.next_token.NextToken"]
    """<p>An opaque string that indicates that the response contains only a subset of tags. Use this value in a subsequent <code>ListTags</code> request to get more tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsResponse) -> dict:
    out: dict = {}
    import capo_cloudhsm_v2.types.tag_list

    out["TagList"] = capo_cloudhsm_v2.types.tag_list.serialize_aws_json_1_1(
        value["tag_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsResponse:
    out: ListTagsResponse = {}  # type: ignore[typeddict-item]
    if data.get("TagList") is not None:
        import capo_cloudhsm_v2.types.tag_list

        out["tag_list"] = capo_cloudhsm_v2.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    else:
        out["tag_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
