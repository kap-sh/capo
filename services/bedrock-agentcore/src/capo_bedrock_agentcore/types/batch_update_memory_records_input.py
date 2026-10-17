"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchUpdateMemoryRecordsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.memory_records_update_input_list


class BatchUpdateMemoryRecordsInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The unique ID of the memory resource where records will be updated.</p>"""
    records: "capo_bedrock_agentcore.types.memory_records_update_input_list.MemoryRecordsUpdateInputList"
    """<p>A list of memory record update inputs to be processed in the batch operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateMemoryRecordsInput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.memory_records_update_input_list

    out["records"] = (
        capo_bedrock_agentcore.types.memory_records_update_input_list.serialize_json(
            value["records"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateMemoryRecordsInput:
    out: BatchUpdateMemoryRecordsInput = {}  # type: ignore[typeddict-item]
    if data.get("records") is not None:
        import capo_bedrock_agentcore.types.memory_records_update_input_list

        out["records"] = (
            capo_bedrock_agentcore.types.memory_records_update_input_list.deserialize_json(
                data["records"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateMemoryRecordsInput.records required")
    return out


def redact_sensitive(value: BatchUpdateMemoryRecordsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "records" in value:
        import capo_bedrock_agentcore.types.memory_records_update_input_list

        out["records"] = (
            capo_bedrock_agentcore.types.memory_records_update_input_list.redact_sensitive(
                value["records"]
            )
        )
    return out
