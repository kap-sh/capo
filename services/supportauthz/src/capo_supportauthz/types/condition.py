"""Generated from Smithy shape ``com.amazonaws.supportauthz#Condition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_supportauthz.errors import DeserializationError, SerializationError
from capo_supportauthz.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import datetime


class _Condition_allowAfter(TypedDict, closed=True):
    allowAfter: "datetime.datetime"


class _Condition_allowBefore(TypedDict, closed=True):
    allowBefore: "datetime.datetime"


Condition: TypeAlias = (
    _Condition_allowAfter | _Condition_allowBefore | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Condition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "allowAfter" in value:
        import capo_supportauthz.types._prelude.timestamp

        return {
            "allowAfter": capo_supportauthz.types._prelude.timestamp.serialize_json(
                value["allowAfter"]
            )
        }
    elif "allowBefore" in value:
        import capo_supportauthz.types._prelude.timestamp

        return {
            "allowBefore": capo_supportauthz.types._prelude.timestamp.serialize_json(
                value["allowBefore"]
            )
        }
    else:
        raise SerializationError("Condition: no variant present")


def deserialize_json(data: dict) -> Condition:
    if data.get("allowAfter") is not None:
        import capo_supportauthz.types._prelude.timestamp

        return {
            "allowAfter": capo_supportauthz.types._prelude.timestamp.deserialize_json(
                data["allowAfter"]
            )
        }
    elif data.get("allowBefore") is not None:
        import capo_supportauthz.types._prelude.timestamp

        return {
            "allowBefore": capo_supportauthz.types._prelude.timestamp.deserialize_json(
                data["allowBefore"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Condition: no recognized variant key")
