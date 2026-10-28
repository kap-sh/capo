"""Generated from Smithy shape ``com.amazonaws.applicationsignals#LocationIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError
from capo_application_signals.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_application_signals.types.code_location


class LocationIdentifierCodeLocationMember(TypedDict, closed=True):
    CodeLocation: "capo_application_signals.types.code_location.CodeLocation"


class LocationIdentifierLocationHashMember(TypedDict, closed=True):
    LocationHash: "str"


LocationIdentifier: TypeAlias = (
    LocationIdentifierCodeLocationMember
    | LocationIdentifierLocationHashMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: LocationIdentifier) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"LocationIdentifier: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
            return {"$unknown": {"name": name}}
        raise DeserializationError("LocationIdentifier: no recognized variant key")
