"""Generated from Smithy shape ``com.amazonaws.connectcases#LayoutContent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.basic_layout


class _LayoutContent_basic(TypedDict, closed=True):
    basic: "capo_connectcases.types.basic_layout.BasicLayout"


LayoutContent: TypeAlias = _LayoutContent_basic | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: LayoutContent) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"LayoutContent: cannot serialize unknown variant {value.name!r}"
        )
    elif "basic" in value:
        import capo_connectcases.types.basic_layout

        return {
            "basic": capo_connectcases.types.basic_layout.serialize_json(value["basic"])
        }
    else:
        raise SerializationError("LayoutContent: no variant present")


def deserialize_json(data: dict) -> LayoutContent:
    if data.get("basic") is not None:
        import capo_connectcases.types.basic_layout

        return {
            "basic": capo_connectcases.types.basic_layout.deserialize_json(
                data["basic"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("LayoutContent: no recognized variant key")
