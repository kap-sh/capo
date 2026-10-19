"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ListConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.connection_summary_list
    import capo_partnercentral_account.types.next_token


class ListConnectionsResponse(TypedDict, closed=True):
    connection_summaries: "capo_partnercentral_account.types.connection_summary_list.ConnectionSummaryList"
    """<p>A list of connection summaries matching the specified criteria.</p>"""
    next_token: NotRequired["capo_partnercentral_account.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results if more results are available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionsResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_account.types.connection_summary_list

    out["ConnectionSummaries"] = (
        capo_partnercentral_account.types.connection_summary_list.serialize_aws_json_1_0(
            value["connection_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionsResponse:
    out: ListConnectionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionSummaries") is not None:
        import capo_partnercentral_account.types.connection_summary_list

        out["connection_summaries"] = (
            capo_partnercentral_account.types.connection_summary_list.deserialize_aws_json_1_0(
                data["ConnectionSummaries"]
            )
        )
    else:
        out["connection_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
