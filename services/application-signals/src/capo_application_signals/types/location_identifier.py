"""Generated from Smithy shape ``com.amazonaws.applicationsignals#LocationIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError
from capo_application_signals.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_application_signals.types.code_location


class _LocationIdentifier_CodeLocation(TypedDict, closed=True):
    CodeLocation: "capo_application_signals.types.code_location.CodeLocation"


class _LocationIdentifier_LocationHash(TypedDict, closed=True):
    LocationHash: "str"


LocationIdentifier: TypeAlias = (
    _LocationIdentifier_CodeLocation
    | _LocationIdentifier_LocationHash
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: LocationIdentifier) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"LocationIdentifier: cannot serialize unknown variant {value.name!r}"
        )
    elif "CodeLocation" in value:
        import capo_application_signals.types.code_location

        return {
            "CodeLocation": capo_application_signals.types.code_location.serialize_json(
                value["CodeLocation"]
            )
        }
    elif "LocationHash" in value:
        return {"LocationHash": value["LocationHash"]}
    else:
        raise SerializationError("LocationIdentifier: no variant present")


def deserialize_json(data: dict) -> LocationIdentifier:
    if data.get("CodeLocation") is not None:
        import capo_application_signals.types.code_location

        return {
            "CodeLocation": capo_application_signals.types.code_location.deserialize_json(
                data["CodeLocation"]
            )
        }
    elif data.get("LocationHash") is not None:
        return {"LocationHash": data["LocationHash"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("LocationIdentifier: no recognized variant key")
