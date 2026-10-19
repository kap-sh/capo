"""Generated from Smithy shape ``com.amazonaws.qbusiness#IdentityProviderConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.open_id_connect_provider_configuration
    import capo_qbusiness.types.saml_provider_configuration


class _IdentityProviderConfiguration_samlConfiguration(TypedDict, closed=True):
    samlConfiguration: (
        "capo_qbusiness.types.saml_provider_configuration.SamlProviderConfiguration"
    )


class _IdentityProviderConfiguration_openIDConnectConfiguration(TypedDict, closed=True):
    openIDConnectConfiguration: "capo_qbusiness.types.open_id_connect_provider_configuration.OpenIDConnectProviderConfiguration"


IdentityProviderConfiguration: TypeAlias = (
    _IdentityProviderConfiguration_samlConfiguration
    | _IdentityProviderConfiguration_openIDConnectConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"IdentityProviderConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "samlConfiguration" in value:
        import capo_qbusiness.types.saml_provider_configuration

        return {
            "samlConfiguration": capo_qbusiness.types.saml_provider_configuration.serialize_json(
                value["samlConfiguration"]
            )
        }
    elif "openIDConnectConfiguration" in value:
        import capo_qbusiness.types.open_id_connect_provider_configuration

        return {
            "openIDConnectConfiguration": capo_qbusiness.types.open_id_connect_provider_configuration.serialize_json(
                value["openIDConnectConfiguration"]
            )
        }
    else:
        raise SerializationError("IdentityProviderConfiguration: no variant present")


def deserialize_json(data: dict) -> IdentityProviderConfiguration:
    if data.get("samlConfiguration") is not None:
        import capo_qbusiness.types.saml_provider_configuration

        return {
            "samlConfiguration": capo_qbusiness.types.saml_provider_configuration.deserialize_json(
                data["samlConfiguration"]
            )
        }
    elif data.get("openIDConnectConfiguration") is not None:
        import capo_qbusiness.types.open_id_connect_provider_configuration

        return {
            "openIDConnectConfiguration": capo_qbusiness.types.open_id_connect_provider_configuration.deserialize_json(
                data["openIDConnectConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "IdentityProviderConfiguration: no recognized variant key"
        )
