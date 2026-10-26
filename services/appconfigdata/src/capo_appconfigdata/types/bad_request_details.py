"""Generated from Smithy shape ``com.amazonaws.appconfigdata#BadRequestDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_appconfigdata.errors import DeserializationError, SerializationError
from capo_appconfigdata.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_appconfigdata.types.invalid_parameter_map


class _BadRequestDetails_InvalidParameters(TypedDict, closed=True):
    InvalidParameters: (
        "capo_appconfigdata.types.invalid_parameter_map.InvalidParameterMap"
    )


BadRequestDetails: TypeAlias = _BadRequestDetails_InvalidParameters | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"BadRequestDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "InvalidParameters" in value:
        import capo_appconfigdata.types.invalid_parameter_map

        return {
            "InvalidParameters": capo_appconfigdata.types.invalid_parameter_map.serialize_json(
                value["InvalidParameters"]
            )
        }
    else:
        raise SerializationError("BadRequestDetails: no variant present")


def deserialize_json(data: dict) -> BadRequestDetails:
    if data.get("InvalidParameters") is not None:
        import capo_appconfigdata.types.invalid_parameter_map

        return {
            "InvalidParameters": capo_appconfigdata.types.invalid_parameter_map.deserialize_json(
                data["InvalidParameters"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("BadRequestDetails: no recognized variant key")
