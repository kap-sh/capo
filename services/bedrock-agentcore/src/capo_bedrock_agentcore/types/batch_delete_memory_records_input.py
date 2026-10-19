"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchDeleteMemoryRecordsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.memory_records_delete_input_list


class BatchDeleteMemoryRecordsInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The unique ID of the memory resource where records will be deleted.</p>"""
    records: "capo_bedrock_agentcore.types.memory_records_delete_input_list.MemoryRecordsDeleteInputList"
    """<p>A list of memory record deletion inputs to be processed in the batch operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteMemoryRecordsInput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.memory_records_delete_input_list

    out["records"] = (
        capo_bedrock_agentcore.types.memory_records_delete_input_list.serialize_json(
            value["records"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteMemoryRecordsInput:
    out: BatchDeleteMemoryRecordsInput = {}  # type: ignore[typeddict-item]
    if data.get("records") is not None:
        import capo_bedrock_agentcore.types.memory_records_delete_input_list

        out["records"] = (
            capo_bedrock_agentcore.types.memory_records_delete_input_list.deserialize_json(
                data["records"]
            )
        )
    else:
        out["records"] = []
    return out
