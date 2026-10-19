"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.page_size
    import capo_cost_explorer.types.tag_list


class GetTagsResponse(TypedDict, closed=True):
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token for the next set of retrievable results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""
    tags: "capo_cost_explorer.types.tag_list.TagList"
    """<p>The tags that match your request.</p>"""
    return_size: "capo_cost_explorer.types.page_size.PageSize"
    """<p>The number of query results that Amazon Web Services returns at a time.</p>"""
    total_size: "capo_cost_explorer.types.page_size.PageSize"
    """<p>The total number of query results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTagsResponse) -> dict:
    out: dict = {}
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    import capo_cost_explorer.types.tag_list

    out["Tags"] = capo_cost_explorer.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    out["ReturnSize"] = value["return_size"]
    out["TotalSize"] = value["total_size"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTagsResponse:
    out: GetTagsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    if data.get("Tags") is not None:
        import capo_cost_explorer.types.tag_list

        out["tags"] = capo_cost_explorer.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        out["tags"] = []
    if data.get("ReturnSize") is not None:
        out["return_size"] = data["ReturnSize"]
    else:
        out["return_size"] = 0
    if data.get("TotalSize") is not None:
        out["total_size"] = data["TotalSize"]
    else:
        out["total_size"] = 0
    return out
