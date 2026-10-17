"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchCreateMemoryRecordsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.memory_records_create_input_list


class BatchCreateMemoryRecordsInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The unique ID of the memory resource where records will be created.</p>"""
    records: "capo_bedrock_agentcore.types.memory_records_create_input_list.MemoryRecordsCreateInputList"
    """<p>A list of memory record creation inputs to be processed in the batch operation.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure idempotent processing of the batch request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateMemoryRecordsInput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.memory_records_create_input_list

    out["records"] = (
        capo_bedrock_agentcore.types.memory_records_create_input_list.serialize_json(
            value["records"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> BatchCreateMemoryRecordsInput:
    out: BatchCreateMemoryRecordsInput = {}  # type: ignore[typeddict-item]
    if data.get("records") is not None:
        import capo_bedrock_agentcore.types.memory_records_create_input_list

        out["records"] = (
            capo_bedrock_agentcore.types.memory_records_create_input_list.deserialize_json(
                data["records"]
            )
        )
    else:
        raise DeserializationError("BatchCreateMemoryRecordsInput.records required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: BatchCreateMemoryRecordsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "records" in value:
        import capo_bedrock_agentcore.types.memory_records_create_input_list

        out["records"] = (
            capo_bedrock_agentcore.types.memory_records_create_input_list.redact_sensitive(
                value["records"]
            )
        )
    return out
