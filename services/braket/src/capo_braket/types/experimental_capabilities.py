"""Generated from Smithy shape ``com.amazonaws.braket#ExperimentalCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_braket.errors import DeserializationError, SerializationError
from capo_braket.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_braket.types.experimental_capabilities_enablement_type


class _ExperimentalCapabilities_enabled(TypedDict, closed=True):
    enabled: "capo_braket.types.experimental_capabilities_enablement_type.ExperimentalCapabilitiesEnablementType"


ExperimentalCapabilities: TypeAlias = (
    _ExperimentalCapabilities_enabled | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentalCapabilities) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ExperimentalCapabilities: cannot serialize unknown variant {value.name!r}"
        )
    elif "enabled" in value:
        return {"enabled": value["enabled"]}
    else:
        raise SerializationError("ExperimentalCapabilities: no variant present")


def deserialize_json(data: dict) -> ExperimentalCapabilities:
    if data.get("enabled") is not None:
        return {"enabled": data["enabled"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "ExperimentalCapabilities: no recognized variant key"
        )
