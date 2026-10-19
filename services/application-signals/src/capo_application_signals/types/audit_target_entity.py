"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AuditTargetEntity``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError
from capo_application_signals.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_application_signals.types.canary_entity
    import capo_application_signals.types.service_entity
    import capo_application_signals.types.service_level_objective_entity
    import capo_application_signals.types.service_operation_entity


class _AuditTargetEntity_Service(TypedDict, closed=True):
    Service: "capo_application_signals.types.service_entity.ServiceEntity"


class _AuditTargetEntity_Slo(TypedDict, closed=True):
    Slo: "capo_application_signals.types.service_level_objective_entity.ServiceLevelObjectiveEntity"


class _AuditTargetEntity_ServiceOperation(TypedDict, closed=True):
    ServiceOperation: (
        "capo_application_signals.types.service_operation_entity.ServiceOperationEntity"
    )


class _AuditTargetEntity_Canary(TypedDict, closed=True):
    Canary: "capo_application_signals.types.canary_entity.CanaryEntity"


AuditTargetEntity: TypeAlias = (
    _AuditTargetEntity_Service
    | _AuditTargetEntity_Slo
    | _AuditTargetEntity_ServiceOperation
    | _AuditTargetEntity_Canary
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AuditTargetEntity) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AuditTargetEntity: cannot serialize unknown variant {value.name!r}"
        )
    elif "Service" in value:
        import capo_application_signals.types.service_entity

        return {
            "Service": capo_application_signals.types.service_entity.serialize_json(
                value["Service"]
            )
        }
    elif "Slo" in value:
        import capo_application_signals.types.service_level_objective_entity

        return {
            "Slo": capo_application_signals.types.service_level_objective_entity.serialize_json(
                value["Slo"]
            )
        }
    elif "ServiceOperation" in value:
        import capo_application_signals.types.service_operation_entity

        return {
            "ServiceOperation": capo_application_signals.types.service_operation_entity.serialize_json(
                value["ServiceOperation"]
            )
        }
    elif "Canary" in value:
        import capo_application_signals.types.canary_entity

        return {
            "Canary": capo_application_signals.types.canary_entity.serialize_json(
                value["Canary"]
            )
        }
    else:
        raise SerializationError("AuditTargetEntity: no variant present")


def deserialize_json(data: dict) -> AuditTargetEntity:
    if data.get("Service") is not None:
        import capo_application_signals.types.service_entity

        return {
            "Service": capo_application_signals.types.service_entity.deserialize_json(
                data["Service"]
            )
        }
    elif data.get("Slo") is not None:
        import capo_application_signals.types.service_level_objective_entity

        return {
            "Slo": capo_application_signals.types.service_level_objective_entity.deserialize_json(
                data["Slo"]
            )
        }
    elif data.get("ServiceOperation") is not None:
        import capo_application_signals.types.service_operation_entity

        return {
            "ServiceOperation": capo_application_signals.types.service_operation_entity.deserialize_json(
                data["ServiceOperation"]
            )
        }
    elif data.get("Canary") is not None:
        import capo_application_signals.types.canary_entity

        return {
            "Canary": capo_application_signals.types.canary_entity.deserialize_json(
                data["Canary"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AuditTargetEntity: no recognized variant key")
