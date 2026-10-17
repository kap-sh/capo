"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchUpdateMemoryRecordsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.memory_records_update_input_list
    import capo_bedrock_agentcore.types.record_expiry_specification


class BatchUpdateMemoryRecordsInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The unique ID of the memory resource where records will be updated.</p>"""
    records: "capo_bedrock_agentcore.types.memory_records_update_input_list.MemoryRecordsUpdateInputList"
    """<p>A list of memory record update inputs to be processed in the batch operation.</p>"""
    record_expiry_specification: NotRequired[
        "capo_bedrock_agentcore.types.record_expiry_specification.RecordExpirySpecification"
    ]
    """<p>The record expiry (long-term memory time-to-live) applied to every record updated by this request. Set <code>recordExpiryDurationDays</code> to configure or overwrite the number of days after which the records expire, or set <code>action</code> to <code>REMOVE</code> to clear a previously configured expiry so that the records no longer expire.</p> <p>When you do not provide this value, the service determines each record's expiry from its current state:</p> <ul> <li> <p>If the record already has an expiry configured, the service resets and reapplies the expiry based on the last applied <code>recordExpiryDurationDays</code>.</p> </li> <li> <p>If the record does not have an expiry configured, no expiry is applied and the record remains non-expiring. This is the outcome regardless of whether the record's strategy configures an expiry.</p> </li> </ul> <p>Providing an explicit <code>recordExpiryDurationDays</code> always takes precedence: it overwrites an existing expiry, or sets one on a record that previously had none.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateMemoryRecordsInput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.memory_records_update_input_list

    out["records"] = (
        capo_bedrock_agentcore.types.memory_records_update_input_list.serialize_json(
            value["records"]
        )
    )
    if "record_expiry_specification" in value:
        import capo_bedrock_agentcore.types.record_expiry_specification

        out["recordExpirySpecification"] = (
            capo_bedrock_agentcore.types.record_expiry_specification.serialize_json(
                value["record_expiry_specification"]
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
    if data.get("recordExpirySpecification") is not None:
        import capo_bedrock_agentcore.types.record_expiry_specification

        out["record_expiry_specification"] = (
            capo_bedrock_agentcore.types.record_expiry_specification.deserialize_json(
                data["recordExpirySpecification"]
            )
        )
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
