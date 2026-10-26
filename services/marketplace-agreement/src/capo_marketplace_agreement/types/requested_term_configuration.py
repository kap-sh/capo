"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RequestedTermConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_agreement.errors import DeserializationError, SerializationError
from capo_marketplace_agreement.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.configurable_upfront_pricing_term_configuration
    import capo_marketplace_agreement.types.renewal_term_configuration
    import capo_marketplace_agreement.types.variable_payment_term_configuration


class _RequestedTermConfiguration_configurableUpfrontPricingTermConfiguration(
    TypedDict, closed=True
):
    configurableUpfrontPricingTermConfiguration: "capo_marketplace_agreement.types.configurable_upfront_pricing_term_configuration.ConfigurableUpfrontPricingTermConfiguration"


class _RequestedTermConfiguration_renewalTermConfiguration(TypedDict, closed=True):
    renewalTermConfiguration: "capo_marketplace_agreement.types.renewal_term_configuration.RenewalTermConfiguration"


class _RequestedTermConfiguration_variablePaymentTermConfiguration(
    TypedDict, closed=True
):
    variablePaymentTermConfiguration: "capo_marketplace_agreement.types.variable_payment_term_configuration.VariablePaymentTermConfiguration"


RequestedTermConfiguration: TypeAlias = (
    _RequestedTermConfiguration_configurableUpfrontPricingTermConfiguration
    | _RequestedTermConfiguration_renewalTermConfiguration
    | _RequestedTermConfiguration_variablePaymentTermConfiguration
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestedTermConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RequestedTermConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "configurableUpfrontPricingTermConfiguration" in value:
        import capo_marketplace_agreement.types.configurable_upfront_pricing_term_configuration

        return {
            "configurableUpfrontPricingTermConfiguration": capo_marketplace_agreement.types.configurable_upfront_pricing_term_configuration.serialize_aws_json_1_0(
                value["configurableUpfrontPricingTermConfiguration"]
            )
        }
    elif "renewalTermConfiguration" in value:
        import capo_marketplace_agreement.types.renewal_term_configuration

        return {
            "renewalTermConfiguration": capo_marketplace_agreement.types.renewal_term_configuration.serialize_aws_json_1_0(
                value["renewalTermConfiguration"]
            )
        }
    elif "variablePaymentTermConfiguration" in value:
        import capo_marketplace_agreement.types.variable_payment_term_configuration

        return {
            "variablePaymentTermConfiguration": capo_marketplace_agreement.types.variable_payment_term_configuration.serialize_aws_json_1_0(
                value["variablePaymentTermConfiguration"]
            )
        }
    else:
        raise SerializationError("RequestedTermConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RequestedTermConfiguration:
    if data.get("configurableUpfrontPricingTermConfiguration") is not None:
        import capo_marketplace_agreement.types.configurable_upfront_pricing_term_configuration

        return {
            "configurableUpfrontPricingTermConfiguration": capo_marketplace_agreement.types.configurable_upfront_pricing_term_configuration.deserialize_aws_json_1_0(
                data["configurableUpfrontPricingTermConfiguration"]
            )
        }
    elif data.get("renewalTermConfiguration") is not None:
        import capo_marketplace_agreement.types.renewal_term_configuration

        return {
            "renewalTermConfiguration": capo_marketplace_agreement.types.renewal_term_configuration.deserialize_aws_json_1_0(
                data["renewalTermConfiguration"]
            )
        }
    elif data.get("variablePaymentTermConfiguration") is not None:
        import capo_marketplace_agreement.types.variable_payment_term_configuration

        return {
            "variablePaymentTermConfiguration": capo_marketplace_agreement.types.variable_payment_term_configuration.deserialize_aws_json_1_0(
                data["variablePaymentTermConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RequestedTermConfiguration: no recognized variant key"
        )
