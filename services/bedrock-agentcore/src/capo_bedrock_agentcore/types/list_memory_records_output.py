"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListMemoryRecordsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_record_summary_list
    import capo_bedrock_agentcore.types.pagination_token


class ListMemoryRecordsOutput(TypedDict, closed=True):
    memory_record_summaries: "capo_bedrock_agentcore.types.memory_record_summary_list.MemoryRecordSummaryList"
    """<p>The list of memory record summaries that match the specified criteria.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMemoryRecordsOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.memory_record_summary_list

    out["memoryRecordSummaries"] = (
        capo_bedrock_agentcore.types.memory_record_summary_list.serialize_json(
            value["memory_record_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMemoryRecordsOutput:
    out: ListMemoryRecordsOutput = {}  # type: ignore[typeddict-item]
    if data.get("memoryRecordSummaries") is not None:
        import capo_bedrock_agentcore.types.memory_record_summary_list

        out["memory_record_summaries"] = (
            capo_bedrock_agentcore.types.memory_record_summary_list.deserialize_json(
                data["memoryRecordSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListMemoryRecordsOutput.memory_record_summaries required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListMemoryRecordsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "memory_record_summaries" in value:
        import capo_bedrock_agentcore.types.memory_record_summary_list

        out["memory_record_summaries"] = (
            capo_bedrock_agentcore.types.memory_record_summary_list.redact_sensitive(
                value["memory_record_summaries"]
            )
        )
    return out
