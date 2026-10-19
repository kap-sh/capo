"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.next_tags_for_resource_results_token
    import capo_timestream_query.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: "capo_timestream_query.types.tag_list.TagList"
    """<p>The tags currently associated with the Timestream resource. </p>"""
    next_token: NotRequired[
        "capo_timestream_query.types.next_tags_for_resource_results_token.NextTagsForResourceResultsToken"
    ]
    """<p>A pagination token to resume pagination with a subsequent call to <code>ListTagsForResourceResponse</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import capo_timestream_query.types.tag_list

    out["Tags"] = capo_timestream_query.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_timestream_query.types.tag_list

        out["tags"] = capo_timestream_query.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        out["tags"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
