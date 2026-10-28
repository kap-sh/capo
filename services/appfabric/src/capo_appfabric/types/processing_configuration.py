"""Generated from Smithy shape ``com.amazonaws.appfabric#ProcessingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_appfabric.errors import DeserializationError, SerializationError
from capo_appfabric.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_appfabric.types.audit_log_processing_configuration


class ProcessingConfigurationAuditLogMember(TypedDict, closed=True):
    auditLog: "capo_appfabric.types.audit_log_processing_configuration.AuditLogProcessingConfiguration"


ProcessingConfiguration: TypeAlias = (
    ProcessingConfigurationAuditLogMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProcessingConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProcessingConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "auditLog" in value:
        import capo_appfabric.types.audit_log_processing_configuration

        return {
            "auditLog": capo_appfabric.types.audit_log_processing_configuration.serialize_json(
                value["auditLog"]
            )
        }
    else:
        raise SerializationError("ProcessingConfiguration: no variant present")


def deserialize_json(data: dict) -> ProcessingConfiguration:
    if data.get("auditLog") is not None:
        import capo_appfabric.types.audit_log_processing_configuration

        return {
            "auditLog": capo_appfabric.types.audit_log_processing_configuration.deserialize_json(
                data["auditLog"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ProcessingConfiguration: no recognized variant key")
