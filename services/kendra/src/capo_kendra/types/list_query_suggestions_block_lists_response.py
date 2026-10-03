"""Generated from Smithy shape ``com.amazonaws.kendra#ListQuerySuggestionsBlockListsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.next_token
    import capo_kendra.types.query_suggestions_block_list_summary_items


class ListQuerySuggestionsBlockListsResponse(TypedDict, closed=True):
    block_list_summary_items: NotRequired[
        "capo_kendra.types.query_suggestions_block_list_summary_items.QuerySuggestionsBlockListSummaryItems"
    ]
    """<p>Summary items for a block list.</p> <p>This includes summary items on the block list ID, block list name, when the block list was created, when the block list was last updated, and the count of block words/phrases in the block list.</p> <p>For information on the current quota limits for block lists, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas for Amazon Kendra</a>.</p>"""
    next_token: NotRequired["capo_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of block lists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListQuerySuggestionsBlockListsResponse) -> dict:
    out: dict = {}
    if "block_list_summary_items" in value:
        import capo_kendra.types.query_suggestions_block_list_summary_items

        out["BlockListSummaryItems"] = (
            capo_kendra.types.query_suggestions_block_list_summary_items.serialize_aws_json_1_1(
                value["block_list_summary_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListQuerySuggestionsBlockListsResponse:
    out: ListQuerySuggestionsBlockListsResponse = {}  # type: ignore[typeddict-item]
    if data.get("BlockListSummaryItems") is not None:
        import capo_kendra.types.query_suggestions_block_list_summary_items

        out["block_list_summary_items"] = (
            capo_kendra.types.query_suggestions_block_list_summary_items.deserialize_aws_json_1_1(
                data["BlockListSummaryItems"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
