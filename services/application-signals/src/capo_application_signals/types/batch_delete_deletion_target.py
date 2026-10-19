"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchDeleteDeletionTarget``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError
from capo_application_signals.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_application_signals.types.batch_delete_by_resource_arns
    import capo_application_signals.types.batch_delete_scope


class _BatchDeleteDeletionTarget_Scope(TypedDict, closed=True):
    Scope: "capo_application_signals.types.batch_delete_scope.BatchDeleteScope"


class _BatchDeleteDeletionTarget_ResourceArns(TypedDict, closed=True):
    ResourceArns: "capo_application_signals.types.batch_delete_by_resource_arns.BatchDeleteByResourceArns"


BatchDeleteDeletionTarget: TypeAlias = (
    _BatchDeleteDeletionTarget_Scope
    | _BatchDeleteDeletionTarget_ResourceArns
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDeletionTarget) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"BatchDeleteDeletionTarget: cannot serialize unknown variant {value.name!r}"
        )
    elif "Scope" in value:
        import capo_application_signals.types.batch_delete_scope

        return {
            "Scope": capo_application_signals.types.batch_delete_scope.serialize_json(
                value["Scope"]
            )
        }
    elif "ResourceArns" in value:
        import capo_application_signals.types.batch_delete_by_resource_arns

        return {
            "ResourceArns": capo_application_signals.types.batch_delete_by_resource_arns.serialize_json(
                value["ResourceArns"]
            )
        }
    else:
        raise SerializationError("BatchDeleteDeletionTarget: no variant present")


def deserialize_json(data: dict) -> BatchDeleteDeletionTarget:
    if data.get("Scope") is not None:
        import capo_application_signals.types.batch_delete_scope

        return {
            "Scope": capo_application_signals.types.batch_delete_scope.deserialize_json(
                data["Scope"]
            )
        }
    elif data.get("ResourceArns") is not None:
        import capo_application_signals.types.batch_delete_by_resource_arns

        return {
            "ResourceArns": capo_application_signals.types.batch_delete_by_resource_arns.deserialize_json(
                data["ResourceArns"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "BatchDeleteDeletionTarget: no recognized variant key"
        )
