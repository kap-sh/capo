"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentProviderConfigurationInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_input
    import capo_bedrock_agentcore_control.types.stripe_privy_configuration_input


class _PaymentProviderConfigurationInput_coinbaseCdpConfiguration(
    TypedDict, closed=True
):
    coinbaseCdpConfiguration: "capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_input.CoinbaseCdpConfigurationInput"


class _PaymentProviderConfigurationInput_stripePrivyConfiguration(
    TypedDict, closed=True
):
    stripePrivyConfiguration: "capo_bedrock_agentcore_control.types.stripe_privy_configuration_input.StripePrivyConfigurationInput"


PaymentProviderConfigurationInput: TypeAlias = (
    _PaymentProviderConfigurationInput_coinbaseCdpConfiguration
    | _PaymentProviderConfigurationInput_stripePrivyConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PaymentProviderConfigurationInput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PaymentProviderConfigurationInput: cannot serialize unknown variant {value.name!r}"
        )
    elif "coinbaseCdpConfiguration" in value:
        import capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_input

        return {
            "coinbaseCdpConfiguration": capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_input.serialize_json(
                value["coinbaseCdpConfiguration"]
            )
        }
    elif "stripePrivyConfiguration" in value:
        import capo_bedrock_agentcore_control.types.stripe_privy_configuration_input

        return {
            "stripePrivyConfiguration": capo_bedrock_agentcore_control.types.stripe_privy_configuration_input.serialize_json(
                value["stripePrivyConfiguration"]
            )
        }
    else:
        raise SerializationError(
            "PaymentProviderConfigurationInput: no variant present"
        )


def deserialize_json(data: dict) -> PaymentProviderConfigurationInput:
    if data.get("coinbaseCdpConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_input

        return {
            "coinbaseCdpConfiguration": capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_input.deserialize_json(
                data["coinbaseCdpConfiguration"]
            )
        }
    elif data.get("stripePrivyConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.stripe_privy_configuration_input

        return {
            "stripePrivyConfiguration": capo_bedrock_agentcore_control.types.stripe_privy_configuration_input.deserialize_json(
                data["stripePrivyConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "PaymentProviderConfigurationInput: no recognized variant key"
        )


def redact_sensitive(
    value: PaymentProviderConfigurationInput,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "coinbaseCdpConfiguration" in value:
        import capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_input

        out["coinbaseCdpConfiguration"] = (
            capo_bedrock_agentcore_control.types.coinbase_cdp_configuration_input.redact_sensitive(
                value["coinbaseCdpConfiguration"]
            )
        )
    if "stripePrivyConfiguration" in value:
        import capo_bedrock_agentcore_control.types.stripe_privy_configuration_input

        out["stripePrivyConfiguration"] = (
            capo_bedrock_agentcore_control.types.stripe_privy_configuration_input.redact_sensitive(
                value["stripePrivyConfiguration"]
            )
        )
    return out
