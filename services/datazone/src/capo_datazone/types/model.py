"""Generated from Smithy shape ``com.amazonaws.datazone#Model``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.smithy


class _Model_smithy(TypedDict, closed=True):
    smithy: "capo_datazone.types.smithy.Smithy"


Model: TypeAlias = _Model_smithy | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Model) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Model: cannot serialize unknown variant {value.name!r}"
        )
    elif "smithy" in value:
        return {"smithy": value["smithy"]}
    else:
        raise SerializationError("Model: no variant present")


def deserialize_json(data: dict) -> Model:
    if data.get("smithy") is not None:
        return {"smithy": data["smithy"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Model: no recognized variant key")
