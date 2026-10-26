"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Location``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError
from capo_application_signals.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_application_signals.types.code_location


class _Location_CodeLocation(TypedDict, closed=True):
    CodeLocation: "capo_application_signals.types.code_location.CodeLocation"


Location: TypeAlias = _Location_CodeLocation | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Location) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Location: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "CodeLocation" in value:
        import capo_application_signals.types.code_location

        return {
            "CodeLocation": capo_application_signals.types.code_location.serialize_json(
                value["CodeLocation"]
            )
        }
    else:
        raise SerializationError("Location: no variant present")


def deserialize_json(data: dict) -> Location:
    if data.get("CodeLocation") is not None:
        import capo_application_signals.types.code_location

        return {
            "CodeLocation": capo_application_signals.types.code_location.deserialize_json(
                data["CodeLocation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Location: no recognized variant key")
