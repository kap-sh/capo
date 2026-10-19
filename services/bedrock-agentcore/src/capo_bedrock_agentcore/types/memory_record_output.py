"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_record_id
    import capo_bedrock_agentcore.types.memory_record_status
    import capo_bedrock_agentcore.types.request_identifier


class MemoryRecordOutput(TypedDict, closed=True):
    memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId"
    """<p>The unique ID associated to the memory record.</p>"""
    status: "capo_bedrock_agentcore.types.memory_record_status.MemoryRecordStatus"
    """<p>The status of the memory record operation (e.g., SUCCEEDED, FAILED).</p>"""
    request_identifier: NotRequired[
        "capo_bedrock_agentcore.types.request_identifier.RequestIdentifier"
    ]
    """<p>The client-provided identifier that was used to track this record operation.</p>"""
    error_code: NotRequired["int"]
    """<p>The error code returned when the memory record operation fails.</p>"""
    error_message: NotRequired["str"]
    """<p>A human-readable error message describing why the memory record operation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordOutput) -> dict:
    out: dict = {}
    out["memoryRecordId"] = value["memory_record_id"]
    import capo_bedrock_agentcore.types.memory_record_status

    out["status"] = capo_bedrock_agentcore.types.memory_record_status.serialize_json(
        value["status"]
    )
    if "request_identifier" in value:
        out["requestIdentifier"] = value["request_identifier"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> MemoryRecordOutput:
    out: MemoryRecordOutput = {}  # type: ignore[typeddict-item]
    if data.get("memoryRecordId") is not None:
        out["memory_record_id"] = data["memoryRecordId"]
    else:
        out["memory_record_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.memory_record_status

        out["status"] = (
            capo_bedrock_agentcore.types.memory_record_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.memory_record_status.MemoryRecordStatus", ""
        )
    if data.get("requestIdentifier") is not None:
        out["request_identifier"] = data["requestIdentifier"]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
