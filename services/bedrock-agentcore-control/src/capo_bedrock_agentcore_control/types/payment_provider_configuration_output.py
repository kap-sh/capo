"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentProviderConfigurationOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_output
    import capo_bedrock_agentcore_control.types.stripe_privy_configuration_output


class _PaymentProviderConfigurationOutput_coinbaseCdpConfiguration(
    TypedDict, closed=True
):
    coinbaseCdpConfiguration: "capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_output.CoinbaseCdpConfigurationOutput"


class _PaymentProviderConfigurationOutput_stripePrivyConfiguration(
    TypedDict, closed=True
):
    stripePrivyConfiguration: "capo_bedrock_agentcore_control.types.stripe_privy_configuration_output.StripePrivyConfigurationOutput"


PaymentProviderConfigurationOutput: TypeAlias = (
    _PaymentProviderConfigurationOutput_coinbaseCdpConfiguration
    | _PaymentProviderConfigurationOutput_stripePrivyConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PaymentProviderConfigurationOutput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PaymentProviderConfigurationOutput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "coinbaseCdpConfiguration" in value:
        import capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_output

        return {
            "coinbaseCdpConfiguration": capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_output.serialize_json(
                value["coinbaseCdpConfiguration"]
            )
        }
    elif "stripePrivyConfiguration" in value:
        import capo_bedrock_agentcore_control.types.stripe_privy_configuration_output

        return {
            "stripePrivyConfiguration": capo_bedrock_agentcore_control.types.stripe_privy_configuration_output.serialize_json(
                value["stripePrivyConfiguration"]
            )
        }
    else:
        raise SerializationError(
            "PaymentProviderConfigurationOutput: no variant present"
        )


def deserialize_json(data: dict) -> PaymentProviderConfigurationOutput:
    if data.get("coinbaseCdpConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_output

        return {
            "coinbaseCdpConfiguration": capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_output.deserialize_json(
                data["coinbaseCdpConfiguration"]
            )
        }
    elif data.get("stripePrivyConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.stripe_privy_configuration_output

        return {
            "stripePrivyConfiguration": capo_bedrock_agentcore_control.types.stripe_privy_configuration_output.deserialize_json(
                data["stripePrivyConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "PaymentProviderConfigurationOutput: no recognized variant key"
        )
