"""Generated from Smithy shape ``com.amazonaws.appfabric#DestinationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_appfabric.errors import DeserializationError, SerializationError
from capo_appfabric.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_appfabric.types.audit_log_destination_configuration


class DestinationConfigurationAuditLogMember(TypedDict, closed=True):
    auditLog: "capo_appfabric.types.audit_log_destination_configuration.AuditLogDestinationConfiguration"


DestinationConfiguration: TypeAlias = (
    DestinationConfigurationAuditLogMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DestinationConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "auditLog" in value:
        import capo_appfabric.types.audit_log_destination_configuration

        return {
            "auditLog": capo_appfabric.types.audit_log_destination_configuration.serialize_json(
                value["auditLog"]
            )
        }
    else:
        raise SerializationError("DestinationConfiguration: no variant present")


def deserialize_json(data: dict) -> DestinationConfiguration:
    if data.get("auditLog") is not None:
        import capo_appfabric.types.audit_log_destination_configuration

        return {
            "auditLog": capo_appfabric.types.audit_log_destination_configuration.deserialize_json(
                data["auditLog"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "DestinationConfiguration: no recognized variant key"
        )
