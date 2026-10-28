"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FieldPosition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_amplifyuibuilder.errors import DeserializationError, SerializationError
from capo_amplifyuibuilder.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.fixed_position


class FieldPositionFixedMember(TypedDict, closed=True):
    fixed: "capo_amplifyuibuilder.types.fixed_position.FixedPosition"


class FieldPositionRightOfMember(TypedDict, closed=True):
    rightOf: "str"


class FieldPositionBelowMember(TypedDict, closed=True):
    below: "str"


FieldPosition: TypeAlias = (
    FieldPositionFixedMember
    | FieldPositionRightOfMember
    | FieldPositionBelowMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FieldPosition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FieldPosition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "fixed" in value:
        import capo_amplifyuibuilder.types.fixed_position

        return {
            "fixed": capo_amplifyuibuilder.types.fixed_position.serialize_json(
                value["fixed"]
            )
        }
    elif "rightOf" in value:
        return {"rightOf": value["rightOf"]}
    elif "below" in value:
        return {"below": value["below"]}
    else:
        raise SerializationError("FieldPosition: no variant present")


def deserialize_json(data: dict) -> FieldPosition:
    if data.get("fixed") is not None:
        import capo_amplifyuibuilder.types.fixed_position

        return {
            "fixed": capo_amplifyuibuilder.types.fixed_position.deserialize_json(
                data["fixed"]
            )
        }
    elif data.get("rightOf") is not None:
        return {"rightOf": data["rightOf"]}
    elif data.get("below") is not None:
        return {"below": data["below"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FieldPosition: no recognized variant key")
