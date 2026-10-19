"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#FrameworkFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_catalog.errors import DeserializationError, SerializationError
from capo_marketplace_catalog.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.ami_security_filters
    import capo_marketplace_catalog.types.container_security_filters


class _FrameworkFilters_AMISecurityFilters(TypedDict, closed=True):
    AMISecurityFilters: (
        "capo_marketplace_catalog.types.ami_security_filters.AMISecurityFilters"
    )


class _FrameworkFilters_ContainerSecurityFilters(TypedDict, closed=True):
    ContainerSecurityFilters: "capo_marketplace_catalog.types.container_security_filters.ContainerSecurityFilters"


FrameworkFilters: TypeAlias = (
    _FrameworkFilters_AMISecurityFilters
    | _FrameworkFilters_ContainerSecurityFilters
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkFilters) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"FrameworkFilters: cannot serialize unknown variant {value.name!r}"
        )
    elif "AMISecurityFilters" in value:
        import capo_marketplace_catalog.types.ami_security_filters

        return {
            "AMISecurityFilters": capo_marketplace_catalog.types.ami_security_filters.serialize_json(
                value["AMISecurityFilters"]
            )
        }
    elif "ContainerSecurityFilters" in value:
        import capo_marketplace_catalog.types.container_security_filters

        return {
            "ContainerSecurityFilters": capo_marketplace_catalog.types.container_security_filters.serialize_json(
                value["ContainerSecurityFilters"]
            )
        }
    else:
        raise SerializationError("FrameworkFilters: no variant present")


def deserialize_json(data: dict) -> FrameworkFilters:
    if data.get("AMISecurityFilters") is not None:
        import capo_marketplace_catalog.types.ami_security_filters

        return {
            "AMISecurityFilters": capo_marketplace_catalog.types.ami_security_filters.deserialize_json(
                data["AMISecurityFilters"]
            )
        }
    elif data.get("ContainerSecurityFilters") is not None:
        import capo_marketplace_catalog.types.container_security_filters

        return {
            "ContainerSecurityFilters": capo_marketplace_catalog.types.container_security_filters.deserialize_json(
                data["ContainerSecurityFilters"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("FrameworkFilters: no recognized variant key")
