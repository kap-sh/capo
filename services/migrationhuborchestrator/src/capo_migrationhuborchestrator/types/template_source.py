"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#TemplateSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_migrationhuborchestrator.errors import (
    DeserializationError,
    SerializationError,
)
from capo_migrationhuborchestrator.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.migration_workflow_id


class _TemplateSource_workflowId(TypedDict, closed=True):
    workflowId: (
        "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    )


TemplateSource: TypeAlias = _TemplateSource_workflowId | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"TemplateSource: cannot serialize unknown variant {value.name!r}"
        )
    elif "workflowId" in value:
        return {"workflowId": value["workflowId"]}
    else:
        raise SerializationError("TemplateSource: no variant present")


def deserialize_json(data: dict) -> TemplateSource:
    if data.get("workflowId") is not None:
        return {"workflowId": data["workflowId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("TemplateSource: no recognized variant key")
