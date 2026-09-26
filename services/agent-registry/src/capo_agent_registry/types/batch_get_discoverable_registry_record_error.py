"""Generated from Smithy shape ``com.amazonaws.agentregistry#BatchGetDiscoverableRegistryRecordError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry.types.batch_get_discoverable_registry_record_error_code
    import capo_agent_registry.types.record_identifier
    import capo_agent_registry.types.registry_identifier


class BatchGetDiscoverableRegistryRecordError(TypedDict, closed=True):
    registry_id: "capo_agent_registry.types.registry_identifier.RegistryIdentifier"
    """<p> The identifier of the registry the record was requested from, echoed from the request.</p>"""
    record_id: "capo_agent_registry.types.record_identifier.RecordIdentifier"
    """<p> The identifier of the record that could not be retrieved, echoed from the request in the same format that you supplied (ARN or record ID).</p>"""
    error_code: "capo_agent_registry.types.batch_get_discoverable_registry_record_error_code.BatchGetDiscoverableRegistryRecordErrorCode"
    """<p> The machine-readable reason that the record could not be retrieved.</p>"""
    message: NotRequired["str"]
    """<p> An optional human-readable detail about the error. Do not parse this value programmatically.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDiscoverableRegistryRecordError) -> dict:
    out: dict = {}
    out["registryId"] = value["registry_id"]
    out["recordId"] = value["record_id"]
    import capo_agent_registry.types.batch_get_discoverable_registry_record_error_code

    out["errorCode"] = (
        capo_agent_registry.types.batch_get_discoverable_registry_record_error_code.serialize_json(
            value["error_code"]
        )
    )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetDiscoverableRegistryRecordError:
    out: BatchGetDiscoverableRegistryRecordError = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    else:
        raise DeserializationError(
            "BatchGetDiscoverableRegistryRecordError.registry_id required"
        )
    if data.get("recordId") is not None:
        out["record_id"] = data["recordId"]
    else:
        raise DeserializationError(
            "BatchGetDiscoverableRegistryRecordError.record_id required"
        )
    if data.get("errorCode") is not None:
        import capo_agent_registry.types.batch_get_discoverable_registry_record_error_code

        out["error_code"] = (
            capo_agent_registry.types.batch_get_discoverable_registry_record_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetDiscoverableRegistryRecordError.error_code required"
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
