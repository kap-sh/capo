"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialsProviderConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.payment_credential_provider_configuration


class _CredentialsProviderConfiguration_coinbaseCDP(TypedDict, closed=True):
    coinbaseCDP: "capo_bedrock_agentcore_control.types.payment_credential_provider_configuration.PaymentCredentialProviderConfiguration"


class _CredentialsProviderConfiguration_stripePrivy(TypedDict, closed=True):
    stripePrivy: "capo_bedrock_agentcore_control.types.payment_credential_provider_configuration.PaymentCredentialProviderConfiguration"


CredentialsProviderConfiguration: TypeAlias = (
    _CredentialsProviderConfiguration_coinbaseCDP
    | _CredentialsProviderConfiguration_stripePrivy
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CredentialsProviderConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CredentialsProviderConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "coinbaseCDP" in value:
        import capo_bedrock_agentcore_control.types.payment_credential_provider_configuration

        return {
            "coinbaseCDP": capo_bedrock_agentcore_control.types.payment_credential_provider_configuration.serialize_json(
                value["coinbaseCDP"]
            )
        }
    elif "stripePrivy" in value:
        import capo_bedrock_agentcore_control.types.payment_credential_provider_configuration

        return {
            "stripePrivy": capo_bedrock_agentcore_control.types.payment_credential_provider_configuration.serialize_json(
                value["stripePrivy"]
            )
        }
    else:
        raise SerializationError("CredentialsProviderConfiguration: no variant present")


def deserialize_json(data: dict) -> CredentialsProviderConfiguration:
    if data.get("coinbaseCDP") is not None:
        import capo_bedrock_agentcore_control.types.payment_credential_provider_configuration

        return {
            "coinbaseCDP": capo_bedrock_agentcore_control.types.payment_credential_provider_configuration.deserialize_json(
                data["coinbaseCDP"]
            )
        }
    elif data.get("stripePrivy") is not None:
        import capo_bedrock_agentcore_control.types.payment_credential_provider_configuration

        return {
            "stripePrivy": capo_bedrock_agentcore_control.types.payment_credential_provider_configuration.deserialize_json(
                data["stripePrivy"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "CredentialsProviderConfiguration: no recognized variant key"
        )
