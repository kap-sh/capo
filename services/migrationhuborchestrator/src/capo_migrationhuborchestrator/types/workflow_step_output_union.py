"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#WorkflowStepOutputUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_migrationhuborchestrator.errors import (
    DeserializationError,
    SerializationError,
)
from capo_migrationhuborchestrator.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.max_string_list
    import capo_migrationhuborchestrator.types.max_string_value


class WorkflowStepOutputUnionIntegerValueMember(TypedDict, closed=True):
    integerValue: "int"


class WorkflowStepOutputUnionStringValueMember(TypedDict, closed=True):
    stringValue: "capo_migrationhuborchestrator.types.max_string_value.MaxStringValue"


class WorkflowStepOutputUnionListOfStringValueMember(TypedDict, closed=True):
    listOfStringValue: (
        "capo_migrationhuborchestrator.types.max_string_list.MaxStringList"
    )


WorkflowStepOutputUnion: TypeAlias = (
    WorkflowStepOutputUnionIntegerValueMember
    | WorkflowStepOutputUnionStringValueMember
    | WorkflowStepOutputUnionListOfStringValueMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepOutputUnion) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"WorkflowStepOutputUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "integerValue" in value:
        return {"integerValue": value["integerValue"]}
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "listOfStringValue" in value:
        import capo_migrationhuborchestrator.types.max_string_list

        return {
            "listOfStringValue": capo_migrationhuborchestrator.types.max_string_list.serialize_json(
                value["listOfStringValue"]
            )
        }
    else:
        raise SerializationError("WorkflowStepOutputUnion: no variant present")


def deserialize_json(data: dict) -> WorkflowStepOutputUnion:
    if data.get("integerValue") is not None:
        return {"integerValue": data["integerValue"]}
    elif data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    elif data.get("listOfStringValue") is not None:
        import capo_migrationhuborchestrator.types.max_string_list

        return {
            "listOfStringValue": capo_migrationhuborchestrator.types.max_string_list.deserialize_json(
                data["listOfStringValue"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("WorkflowStepOutputUnion: no recognized variant key")
