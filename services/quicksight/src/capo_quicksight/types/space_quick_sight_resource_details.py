"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceQuickSightResourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError
from capo_quicksight.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_quicksight.types.arn


class _SpaceQuickSightResourceDetails_resourceArn(TypedDict, closed=True):
    resourceArn: "capo_quicksight.types.arn.Arn"


SpaceQuickSightResourceDetails: TypeAlias = (
    _SpaceQuickSightResourceDetails_resourceArn | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SpaceQuickSightResourceDetails) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SpaceQuickSightResourceDetails: cannot serialize unknown variant {value.name!r}"
        )
    elif "resourceArn" in value:
        return {"resourceArn": value["resourceArn"]}
    else:
        raise SerializationError("SpaceQuickSightResourceDetails: no variant present")


def deserialize_json(data: dict) -> SpaceQuickSightResourceDetails:
    if data.get("resourceArn") is not None:
        return {"resourceArn": data["resourceArn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "SpaceQuickSightResourceDetails: no recognized variant key"
        )
