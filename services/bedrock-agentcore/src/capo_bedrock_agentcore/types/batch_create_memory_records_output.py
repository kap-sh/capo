"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchCreateMemoryRecordsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_records_output_list


class BatchCreateMemoryRecordsOutput(TypedDict, closed=True):
    successful_records: "capo_bedrock_agentcore.types.memory_records_output_list.MemoryRecordsOutputList"
    """<p>A list of memory records that were successfully created during the batch operation.</p>"""
    failed_records: "capo_bedrock_agentcore.types.memory_records_output_list.MemoryRecordsOutputList"
    """<p>A list of memory records that failed to be created, including error details for each failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateMemoryRecordsOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.memory_records_output_list

    out["successfulRecords"] = (
        capo_bedrock_agentcore.types.memory_records_output_list.serialize_json(
            value["successful_records"]
        )
    )
    import capo_bedrock_agentcore.types.memory_records_output_list

    out["failedRecords"] = (
        capo_bedrock_agentcore.types.memory_records_output_list.serialize_json(
            value["failed_records"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateMemoryRecordsOutput:
    out: BatchCreateMemoryRecordsOutput = {}  # type: ignore[typeddict-item]
    if data.get("successfulRecords") is not None:
        import capo_bedrock_agentcore.types.memory_records_output_list

        out["successful_records"] = (
            capo_bedrock_agentcore.types.memory_records_output_list.deserialize_json(
                data["successfulRecords"]
            )
        )
    else:
        out["successful_records"] = []
    if data.get("failedRecords") is not None:
        import capo_bedrock_agentcore.types.memory_records_output_list

        out["failed_records"] = (
            capo_bedrock_agentcore.types.memory_records_output_list.deserialize_json(
                data["failedRecords"]
            )
        )
    else:
        out["failed_records"] = []
    return out
