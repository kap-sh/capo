"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderEndpointConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_entityresolution.errors import DeserializationError, SerializationError
from capo_entityresolution.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_entityresolution.types.provider_marketplace_configuration


class ProviderEndpointConfigurationMarketplaceConfigurationMember(
    TypedDict, closed=True
):
    marketplaceConfiguration: "capo_entityresolution.types.provider_marketplace_configuration.ProviderMarketplaceConfiguration"


ProviderEndpointConfiguration: TypeAlias = (
    ProviderEndpointConfigurationMarketplaceConfigurationMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderEndpointConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProviderEndpointConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "marketplaceConfiguration" in value:
        import capo_entityresolution.types.provider_marketplace_configuration

        return {
            "marketplaceConfiguration": capo_entityresolution.types.provider_marketplace_configuration.serialize_json(
                value["marketplaceConfiguration"]
            )
        }
    else:
        raise SerializationError("ProviderEndpointConfiguration: no variant present")


def deserialize_json(data: dict) -> ProviderEndpointConfiguration:
    if data.get("marketplaceConfiguration") is not None:
        import capo_entityresolution.types.provider_marketplace_configuration

        return {
            "marketplaceConfiguration": capo_entityresolution.types.provider_marketplace_configuration.deserialize_json(
                data["marketplaceConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ProviderEndpointConfiguration: no recognized variant key"
        )
