"""Generated from Smithy shape ``com.amazonaws.kinesis#ListStreamsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.boolean_object
    import capo_kinesis.types.next_token
    import capo_kinesis.types.stream_name_list
    import capo_kinesis.types.stream_summary_list


class ListStreamsOutput(TypedDict, closed=True):
    stream_names: "capo_kinesis.types.stream_name_list.StreamNameList"
    """<p>The names of the streams that are associated with the Amazon Web Services account making the <code>ListStreams</code> request.</p>"""
    has_more_streams: "capo_kinesis.types.boolean_object.BooleanObject"
    """<p>If set to <code>true</code>, there are more streams available to list.</p>"""
    next_token: NotRequired["capo_kinesis.types.next_token.NextToken"]
    """<p></p>"""
    stream_summaries: NotRequired[
        "capo_kinesis.types.stream_summary_list.StreamSummaryList"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStreamsOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.stream_name_list

    out["StreamNames"] = capo_kinesis.types.stream_name_list.serialize_aws_json_1_1(
        value["stream_names"]
    )
    out["HasMoreStreams"] = value["has_more_streams"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "stream_summaries" in value:
        import capo_kinesis.types.stream_summary_list

        out["StreamSummaries"] = (
            capo_kinesis.types.stream_summary_list.serialize_aws_json_1_1(
                value["stream_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStreamsOutput:
    out: ListStreamsOutput = {}  # type: ignore[typeddict-item]
    if data.get("StreamNames") is not None:
        import capo_kinesis.types.stream_name_list

        out["stream_names"] = (
            capo_kinesis.types.stream_name_list.deserialize_aws_json_1_1(
                data["StreamNames"]
            )
        )
    else:
        out["stream_names"] = []
    if data.get("HasMoreStreams") is not None:
        out["has_more_streams"] = data["HasMoreStreams"]
    else:
        out["has_more_streams"] = False
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("StreamSummaries") is not None:
        import capo_kinesis.types.stream_summary_list

        out["stream_summaries"] = (
            capo_kinesis.types.stream_summary_list.deserialize_aws_json_1_1(
                data["StreamSummaries"]
            )
        )
    return out
