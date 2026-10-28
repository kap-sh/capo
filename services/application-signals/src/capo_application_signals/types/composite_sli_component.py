"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CompositeSliComponent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError
from capo_application_signals.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_application_signals.types.operation_name


class CompositeSliComponentOperationNameMember(TypedDict, closed=True):
    OperationName: "capo_application_signals.types.operation_name.OperationName"


CompositeSliComponent: TypeAlias = (
    CompositeSliComponentOperationNameMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CompositeSliComponent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CompositeSliComponent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "OperationName" in value:
        return {"OperationName": value["OperationName"]}
    else:
        raise SerializationError("CompositeSliComponent: no variant present")


def deserialize_json(data: dict) -> CompositeSliComponent:
    if data.get("OperationName") is not None:
        return {"OperationName": data["OperationName"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CompositeSliComponent: no recognized variant key")
