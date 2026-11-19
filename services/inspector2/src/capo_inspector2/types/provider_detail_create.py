"""Generated from Smithy shape ``com.amazonaws.inspector2#ProviderDetailCreate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError, SerializationError
from capo_inspector2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_inspector2.types.azure_provider_detail_create
    import capo_inspector2.types.gcp_provider_detail_create


class ProviderDetailCreateAzureMember(TypedDict, closed=True):
    azure: (
        "capo_inspector2.types.azure_provider_detail_create.AzureProviderDetailCreate"
    )


class ProviderDetailCreateGcpMember(TypedDict, closed=True):
    gcp: "capo_inspector2.types.gcp_provider_detail_create.GcpProviderDetailCreate"


ProviderDetailCreate: TypeAlias = (
    ProviderDetailCreateAzureMember | ProviderDetailCreateGcpMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderDetailCreate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProviderDetailCreate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "azure" in value:
        import capo_inspector2.types.azure_provider_detail_create

        return {
            "azure": capo_inspector2.types.azure_provider_detail_create.serialize_json(
                value["azure"]
            )
        }
    elif "gcp" in value:
        import capo_inspector2.types.gcp_provider_detail_create

        return {
            "gcp": capo_inspector2.types.gcp_provider_detail_create.serialize_json(
                value["gcp"]
            )
        }
    else:
        raise SerializationError("ProviderDetailCreate: no variant present")


def deserialize_json(data: dict) -> ProviderDetailCreate:
    if data.get("azure") is not None:
        import capo_inspector2.types.azure_provider_detail_create

        return {
            "azure": capo_inspector2.types.azure_provider_detail_create.deserialize_json(
                data["azure"]
            )
        }
    elif data.get("gcp") is not None:
        import capo_inspector2.types.gcp_provider_detail_create

        return {
            "gcp": capo_inspector2.types.gcp_provider_detail_create.deserialize_json(
                data["gcp"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ProviderDetailCreate: no recognized variant key")
