"""Generated from Smithy shape ``com.amazonaws.kinesis#ListChannelsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.channel_summary_list
    import capo_kinesis.types.next_token


class ListChannelsOutput(TypedDict, closed=True):
    channel_summaries: "capo_kinesis.types.channel_summary_list.ChannelSummaryList"
    """<p>A list of channel summaries.</p>"""
    next_token: NotRequired["capo_kinesis.types.next_token.NextToken"]
    """<p>The pagination token to use in a subsequent call to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListChannelsOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.channel_summary_list

    out["ChannelSummaries"] = (
        capo_kinesis.types.channel_summary_list.serialize_aws_json_1_1(
            value["channel_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListChannelsOutput:
    out: ListChannelsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ChannelSummaries") is not None:
        import capo_kinesis.types.channel_summary_list

        out["channel_summaries"] = (
            capo_kinesis.types.channel_summary_list.deserialize_aws_json_1_1(
                data["ChannelSummaries"]
            )
        )
    else:
        out["channel_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
