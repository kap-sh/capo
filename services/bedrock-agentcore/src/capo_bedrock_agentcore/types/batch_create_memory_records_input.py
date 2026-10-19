"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchCreateMemoryRecordsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.memory_records_create_input_list
    import capo_bedrock_agentcore.types.record_expiry_specification


class BatchCreateMemoryRecordsInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The unique ID of the memory resource where records will be created.</p>"""
    records: "capo_bedrock_agentcore.types.memory_records_create_input_list.MemoryRecordsCreateInputList"
    """<p>A list of memory record creation inputs to be processed in the batch operation.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure idempotent processing of the batch request.</p>"""
    record_expiry_specification: NotRequired[
        "capo_bedrock_agentcore.types.record_expiry_specification.RecordExpirySpecification"
    ]
    """<p>The record expiry (long-term memory time-to-live) applied to every record created by this request. Set <code>recordExpiryDurationDays</code> to the number of days after which the records expire. Only the expiry provided here is applied; the records' strategy association has no effect on their expiry. If you do not provide this value, the records do not expire. The <code>REMOVE</code> action does not apply when creating records.</p>"""


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
    if "record_expiry_specification" in value:
        import capo_bedrock_agentcore.types.record_expiry_specification

        out["recordExpirySpecification"] = (
            capo_bedrock_agentcore.types.record_expiry_specification.serialize_json(
                value["record_expiry_specification"]
            )
        )
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
        out["records"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("recordExpirySpecification") is not None:
        import capo_bedrock_agentcore.types.record_expiry_specification

        out["record_expiry_specification"] = (
            capo_bedrock_agentcore.types.record_expiry_specification.deserialize_json(
                data["recordExpirySpecification"]
            )
        )
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
