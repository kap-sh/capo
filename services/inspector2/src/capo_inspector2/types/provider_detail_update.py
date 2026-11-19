"""Generated from Smithy shape ``com.amazonaws.inspector2#ProviderDetailUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError, SerializationError
from capo_inspector2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_inspector2.types.azure_provider_detail_update
    import capo_inspector2.types.gcp_provider_detail_update


class ProviderDetailUpdateAzureMember(TypedDict, closed=True):
    azure: (
        "capo_inspector2.types.azure_provider_detail_update.AzureProviderDetailUpdate"
    )


class ProviderDetailUpdateGcpMember(TypedDict, closed=True):
    gcp: "capo_inspector2.types.gcp_provider_detail_update.GcpProviderDetailUpdate"


ProviderDetailUpdate: TypeAlias = (
    ProviderDetailUpdateAzureMember | ProviderDetailUpdateGcpMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderDetailUpdate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProviderDetailUpdate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "azure" in value:
        import capo_inspector2.types.azure_provider_detail_update

        return {
            "azure": capo_inspector2.types.azure_provider_detail_update.serialize_json(
                value["azure"]
            )
        }
    elif "gcp" in value:
        import capo_inspector2.types.gcp_provider_detail_update

        return {
            "gcp": capo_inspector2.types.gcp_provider_detail_update.serialize_json(
                value["gcp"]
            )
        }
    else:
        raise SerializationError("ProviderDetailUpdate: no variant present")


def deserialize_json(data: dict) -> ProviderDetailUpdate:
    if data.get("azure") is not None:
        import capo_inspector2.types.azure_provider_detail_update

        return {
            "azure": capo_inspector2.types.azure_provider_detail_update.deserialize_json(
                data["azure"]
            )
        }
    elif data.get("gcp") is not None:
        import capo_inspector2.types.gcp_provider_detail_update

        return {
            "gcp": capo_inspector2.types.gcp_provider_detail_update.deserialize_json(
                data["gcp"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ProviderDetailUpdate: no recognized variant key")
