"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)
from capo_network_security_manager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_network_security_manager.types.alb_configuration
    import capo_network_security_manager.types.string_map


class _ResourceCriteria_tags(TypedDict, closed=True):
    tags: "capo_network_security_manager.types.string_map.StringMap"


class _ResourceCriteria_albConfig(TypedDict, closed=True):
    albConfig: "capo_network_security_manager.types.alb_configuration.AlbConfiguration"


ResourceCriteria: TypeAlias = (
    _ResourceCriteria_tags | _ResourceCriteria_albConfig | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ResourceCriteria) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ResourceCriteria: cannot serialize unknown variant {value.name!r}"
        )
    elif "tags" in value:
        import capo_network_security_manager.types.string_map

        return {
            "tags": capo_network_security_manager.types.string_map.serialize_json(
                value["tags"]
            )
        }
    elif "albConfig" in value:
        import capo_network_security_manager.types.alb_configuration

        return {
            "albConfig": capo_network_security_manager.types.alb_configuration.serialize_json(
                value["albConfig"]
            )
        }
    else:
        raise SerializationError("ResourceCriteria: no variant present")


def deserialize_json(data: dict) -> ResourceCriteria:
    if data.get("tags") is not None:
        import capo_network_security_manager.types.string_map

        return {
            "tags": capo_network_security_manager.types.string_map.deserialize_json(
                data["tags"]
            )
        }
    elif data.get("albConfig") is not None:
        import capo_network_security_manager.types.alb_configuration

        return {
            "albConfig": capo_network_security_manager.types.alb_configuration.deserialize_json(
                data["albConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ResourceCriteria: no recognized variant key")
