"""Generated from Smithy shape ``com.amazonaws.securityhub#CspmProviderUpdateConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.azure_update_configuration


class CspmProviderUpdateConfigurationAzureMember(TypedDict, closed=True):
    Azure: "capo_securityhub.types.azure_update_configuration.AzureUpdateConfiguration"


CspmProviderUpdateConfiguration: TypeAlias = (
    CspmProviderUpdateConfigurationAzureMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CspmProviderUpdateConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CspmProviderUpdateConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Azure" in value:
        import capo_securityhub.types.azure_update_configuration

        return {
            "Azure": capo_securityhub.types.azure_update_configuration.serialize_json(
                value["Azure"]
            )
        }
    else:
        raise SerializationError("CspmProviderUpdateConfiguration: no variant present")


def deserialize_json(data: dict) -> CspmProviderUpdateConfiguration:
    if data.get("Azure") is not None:
        import capo_securityhub.types.azure_update_configuration

        return {
            "Azure": capo_securityhub.types.azure_update_configuration.deserialize_json(
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
            "CspmProviderUpdateConfiguration: no recognized variant key"
        )
