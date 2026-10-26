"""Generated from Smithy shape ``com.amazonaws.omics#ReferenceItem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError, SerializationError
from capo_omics.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_omics.types.reference_arn


class _ReferenceItem_referenceArn(TypedDict, closed=True):
    referenceArn: "capo_omics.types.reference_arn.ReferenceArn"


ReferenceItem: TypeAlias = _ReferenceItem_referenceArn | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceItem) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ReferenceItem: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "referenceArn" in value:
        return {"referenceArn": value["referenceArn"]}
    else:
        raise SerializationError("ReferenceItem: no variant present")


def deserialize_json(data: dict) -> ReferenceItem:
    if data.get("referenceArn") is not None:
        return {"referenceArn": data["referenceArn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ReferenceItem: no recognized variant key")
