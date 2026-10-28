"""Generated from Smithy shape ``com.amazonaws.securityhub#CspmProviderConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.azure_provider_configuration


class CspmProviderConfigurationAzureMember(TypedDict, closed=True):
    Azure: (
        "capo_securityhub.types.azure_provider_configuration.AzureProviderConfiguration"
    )


CspmProviderConfiguration: TypeAlias = (
    CspmProviderConfigurationAzureMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CspmProviderConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CspmProviderConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Azure" in value:
        import capo_securityhub.types.azure_provider_configuration

        return {
            "Azure": capo_securityhub.types.azure_provider_configuration.serialize_json(
                value["Azure"]
            )
        }
    else:
        raise SerializationError("CspmProviderConfiguration: no variant present")


def deserialize_json(data: dict) -> CspmProviderConfiguration:
    if data.get("Azure") is not None:
        import capo_securityhub.types.azure_provider_configuration

        return {
            "Azure": capo_securityhub.types.azure_provider_configuration.deserialize_json(
                data["Azure"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "CspmProviderConfiguration: no recognized variant key"
        )
