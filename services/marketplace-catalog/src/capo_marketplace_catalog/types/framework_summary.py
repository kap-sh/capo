"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#FrameworkSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_catalog.errors import DeserializationError, SerializationError
from capo_marketplace_catalog.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.ami_security_summary
    import capo_marketplace_catalog.types.container_security_summary


class FrameworkSummaryAMISecuritySummaryMember(TypedDict, closed=True):
    AMISecuritySummary: (
        "capo_marketplace_catalog.types.ami_security_summary.AMISecuritySummary"
    )


class FrameworkSummaryContainerSecuritySummaryMember(TypedDict, closed=True):
    ContainerSecuritySummary: "capo_marketplace_catalog.types.container_security_summary.ContainerSecuritySummary"


FrameworkSummary: TypeAlias = (
    FrameworkSummaryAMISecuritySummaryMember
    | FrameworkSummaryContainerSecuritySummaryMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkSummary) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FrameworkSummary: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "AMISecuritySummary" in value:
        import capo_marketplace_catalog.types.ami_security_summary

        return {
            "AMISecuritySummary": capo_marketplace_catalog.types.ami_security_summary.serialize_json(
                value["AMISecuritySummary"]
            )
        }
    elif "ContainerSecuritySummary" in value:
        import capo_marketplace_catalog.types.container_security_summary

        return {
            "ContainerSecuritySummary": capo_marketplace_catalog.types.container_security_summary.serialize_json(
                value["ContainerSecuritySummary"]
            )
        }
    else:
        raise SerializationError("FrameworkSummary: no variant present")


def deserialize_json(data: dict) -> FrameworkSummary:
    if data.get("AMISecuritySummary") is not None:
        import capo_marketplace_catalog.types.ami_security_summary

        return {
            "AMISecuritySummary": capo_marketplace_catalog.types.ami_security_summary.deserialize_json(
                data["AMISecuritySummary"]
            )
        }
    elif data.get("ContainerSecuritySummary") is not None:
        import capo_marketplace_catalog.types.container_security_summary

        return {
            "ContainerSecuritySummary": capo_marketplace_catalog.types.container_security_summary.deserialize_json(
                data["ContainerSecuritySummary"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FrameworkSummary: no recognized variant key")
