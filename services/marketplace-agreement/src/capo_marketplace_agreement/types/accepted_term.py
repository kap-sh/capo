"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptedTerm``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_agreement.errors import DeserializationError, SerializationError
from capo_marketplace_agreement.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.byol_pricing_term
    import capo_marketplace_agreement.types.configurable_upfront_pricing_term
    import capo_marketplace_agreement.types.fixed_upfront_pricing_term
    import capo_marketplace_agreement.types.free_trial_pricing_term
    import capo_marketplace_agreement.types.legal_term
    import capo_marketplace_agreement.types.net_payment_term
    import capo_marketplace_agreement.types.payment_schedule_term
    import capo_marketplace_agreement.types.recurring_payment_term
    import capo_marketplace_agreement.types.renewal_term
    import capo_marketplace_agreement.types.support_term
    import capo_marketplace_agreement.types.usage_based_pricing_term
    import capo_marketplace_agreement.types.validity_term
    import capo_marketplace_agreement.types.variable_payment_term


class _AcceptedTerm_legalTerm(TypedDict, closed=True):
    legalTerm: "capo_marketplace_agreement.types.legal_term.LegalTerm"


class _AcceptedTerm_supportTerm(TypedDict, closed=True):
    supportTerm: "capo_marketplace_agreement.types.support_term.SupportTerm"


class _AcceptedTerm_renewalTerm(TypedDict, closed=True):
    renewalTerm: "capo_marketplace_agreement.types.renewal_term.RenewalTerm"


class _AcceptedTerm_usageBasedPricingTerm(TypedDict, closed=True):
    usageBasedPricingTerm: "capo_marketplace_agreement.types.usage_based_pricing_term.UsageBasedPricingTerm"


class _AcceptedTerm_configurableUpfrontPricingTerm(TypedDict, closed=True):
    configurableUpfrontPricingTerm: "capo_marketplace_agreement.types.configurable_upfront_pricing_term.ConfigurableUpfrontPricingTerm"


class _AcceptedTerm_byolPricingTerm(TypedDict, closed=True):
    byolPricingTerm: (
        "capo_marketplace_agreement.types.byol_pricing_term.ByolPricingTerm"
    )


class _AcceptedTerm_recurringPaymentTerm(TypedDict, closed=True):
    recurringPaymentTerm: (
        "capo_marketplace_agreement.types.recurring_payment_term.RecurringPaymentTerm"
    )


class _AcceptedTerm_validityTerm(TypedDict, closed=True):
    validityTerm: "capo_marketplace_agreement.types.validity_term.ValidityTerm"


class _AcceptedTerm_paymentScheduleTerm(TypedDict, closed=True):
    paymentScheduleTerm: (
        "capo_marketplace_agreement.types.payment_schedule_term.PaymentScheduleTerm"
    )


class _AcceptedTerm_freeTrialPricingTerm(TypedDict, closed=True):
    freeTrialPricingTerm: (
        "capo_marketplace_agreement.types.free_trial_pricing_term.FreeTrialPricingTerm"
    )


class _AcceptedTerm_fixedUpfrontPricingTerm(TypedDict, closed=True):
    fixedUpfrontPricingTerm: "capo_marketplace_agreement.types.fixed_upfront_pricing_term.FixedUpfrontPricingTerm"


class _AcceptedTerm_variablePaymentTerm(TypedDict, closed=True):
    variablePaymentTerm: (
        "capo_marketplace_agreement.types.variable_payment_term.VariablePaymentTerm"
    )


class _AcceptedTerm_netPaymentTerm(TypedDict, closed=True):
    netPaymentTerm: "capo_marketplace_agreement.types.net_payment_term.NetPaymentTerm"


AcceptedTerm: TypeAlias = (
    _AcceptedTerm_legalTerm
    | _AcceptedTerm_supportTerm
    | _AcceptedTerm_renewalTerm
    | _AcceptedTerm_usageBasedPricingTerm
    | _AcceptedTerm_configurableUpfrontPricingTerm
    | _AcceptedTerm_byolPricingTerm
    | _AcceptedTerm_recurringPaymentTerm
    | _AcceptedTerm_validityTerm
    | _AcceptedTerm_paymentScheduleTerm
    | _AcceptedTerm_freeTrialPricingTerm
    | _AcceptedTerm_fixedUpfrontPricingTerm
    | _AcceptedTerm_variablePaymentTerm
    | _AcceptedTerm_netPaymentTerm
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptedTerm) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AcceptedTerm: cannot serialize unknown variant {value.name!r}"
        )
    elif "legalTerm" in value:
        import capo_marketplace_agreement.types.legal_term

        return {
            "legalTerm": capo_marketplace_agreement.types.legal_term.serialize_aws_json_1_0(
                value["legalTerm"]
            )
        }
    elif "supportTerm" in value:
        import capo_marketplace_agreement.types.support_term

        return {
            "supportTerm": capo_marketplace_agreement.types.support_term.serialize_aws_json_1_0(
                value["supportTerm"]
            )
        }
    elif "renewalTerm" in value:
        import capo_marketplace_agreement.types.renewal_term

        return {
            "renewalTerm": capo_marketplace_agreement.types.renewal_term.serialize_aws_json_1_0(
                value["renewalTerm"]
            )
        }
    elif "usageBasedPricingTerm" in value:
        import capo_marketplace_agreement.types.usage_based_pricing_term

        return {
            "usageBasedPricingTerm": capo_marketplace_agreement.types.usage_based_pricing_term.serialize_aws_json_1_0(
                value["usageBasedPricingTerm"]
            )
        }
    elif "configurableUpfrontPricingTerm" in value:
        import capo_marketplace_agreement.types.configurable_upfront_pricing_term

        return {
            "configurableUpfrontPricingTerm": capo_marketplace_agreement.types.configurable_upfront_pricing_term.serialize_aws_json_1_0(
                value["configurableUpfrontPricingTerm"]
            )
        }
    elif "byolPricingTerm" in value:
        import capo_marketplace_agreement.types.byol_pricing_term

        return {
            "byolPricingTerm": capo_marketplace_agreement.types.byol_pricing_term.serialize_aws_json_1_0(
                value["byolPricingTerm"]
            )
        }
    elif "recurringPaymentTerm" in value:
        import capo_marketplace_agreement.types.recurring_payment_term

        return {
            "recurringPaymentTerm": capo_marketplace_agreement.types.recurring_payment_term.serialize_aws_json_1_0(
                value["recurringPaymentTerm"]
            )
        }
    elif "validityTerm" in value:
        import capo_marketplace_agreement.types.validity_term

        return {
            "validityTerm": capo_marketplace_agreement.types.validity_term.serialize_aws_json_1_0(
                value["validityTerm"]
            )
        }
    elif "paymentScheduleTerm" in value:
        import capo_marketplace_agreement.types.payment_schedule_term

        return {
            "paymentScheduleTerm": capo_marketplace_agreement.types.payment_schedule_term.serialize_aws_json_1_0(
                value["paymentScheduleTerm"]
            )
        }
    elif "freeTrialPricingTerm" in value:
        import capo_marketplace_agreement.types.free_trial_pricing_term

        return {
            "freeTrialPricingTerm": capo_marketplace_agreement.types.free_trial_pricing_term.serialize_aws_json_1_0(
                value["freeTrialPricingTerm"]
            )
        }
    elif "fixedUpfrontPricingTerm" in value:
        import capo_marketplace_agreement.types.fixed_upfront_pricing_term

        return {
            "fixedUpfrontPricingTerm": capo_marketplace_agreement.types.fixed_upfront_pricing_term.serialize_aws_json_1_0(
                value["fixedUpfrontPricingTerm"]
            )
        }
    elif "variablePaymentTerm" in value:
        import capo_marketplace_agreement.types.variable_payment_term

        return {
            "variablePaymentTerm": capo_marketplace_agreement.types.variable_payment_term.serialize_aws_json_1_0(
                value["variablePaymentTerm"]
            )
        }
    elif "netPaymentTerm" in value:
        import capo_marketplace_agreement.types.net_payment_term

        return {
            "netPaymentTerm": capo_marketplace_agreement.types.net_payment_term.serialize_aws_json_1_0(
                value["netPaymentTerm"]
            )
        }
    else:
        raise SerializationError("AcceptedTerm: no variant present")


def deserialize_aws_json_1_0(data: dict) -> AcceptedTerm:
    if data.get("legalTerm") is not None:
        import capo_marketplace_agreement.types.legal_term

        return {
            "legalTerm": capo_marketplace_agreement.types.legal_term.deserialize_aws_json_1_0(
                data["legalTerm"]
            )
        }
    elif data.get("supportTerm") is not None:
        import capo_marketplace_agreement.types.support_term

        return {
            "supportTerm": capo_marketplace_agreement.types.support_term.deserialize_aws_json_1_0(
                data["supportTerm"]
            )
        }
    elif data.get("renewalTerm") is not None:
        import capo_marketplace_agreement.types.renewal_term

        return {
            "renewalTerm": capo_marketplace_agreement.types.renewal_term.deserialize_aws_json_1_0(
                data["renewalTerm"]
            )
        }
    elif data.get("usageBasedPricingTerm") is not None:
        import capo_marketplace_agreement.types.usage_based_pricing_term

        return {
            "usageBasedPricingTerm": capo_marketplace_agreement.types.usage_based_pricing_term.deserialize_aws_json_1_0(
                data["usageBasedPricingTerm"]
            )
        }
    elif data.get("configurableUpfrontPricingTerm") is not None:
        import capo_marketplace_agreement.types.configurable_upfront_pricing_term

        return {
            "configurableUpfrontPricingTerm": capo_marketplace_agreement.types.configurable_upfront_pricing_term.deserialize_aws_json_1_0(
                data["configurableUpfrontPricingTerm"]
            )
        }
    elif data.get("byolPricingTerm") is not None:
        import capo_marketplace_agreement.types.byol_pricing_term

        return {
            "byolPricingTerm": capo_marketplace_agreement.types.byol_pricing_term.deserialize_aws_json_1_0(
                data["byolPricingTerm"]
            )
        }
    elif data.get("recurringPaymentTerm") is not None:
        import capo_marketplace_agreement.types.recurring_payment_term

        return {
            "recurringPaymentTerm": capo_marketplace_agreement.types.recurring_payment_term.deserialize_aws_json_1_0(
                data["recurringPaymentTerm"]
            )
        }
    elif data.get("validityTerm") is not None:
        import capo_marketplace_agreement.types.validity_term

        return {
            "validityTerm": capo_marketplace_agreement.types.validity_term.deserialize_aws_json_1_0(
                data["validityTerm"]
            )
        }
    elif data.get("paymentScheduleTerm") is not None:
        import capo_marketplace_agreement.types.payment_schedule_term

        return {
            "paymentScheduleTerm": capo_marketplace_agreement.types.payment_schedule_term.deserialize_aws_json_1_0(
                data["paymentScheduleTerm"]
            )
        }
    elif data.get("freeTrialPricingTerm") is not None:
        import capo_marketplace_agreement.types.free_trial_pricing_term

        return {
            "freeTrialPricingTerm": capo_marketplace_agreement.types.free_trial_pricing_term.deserialize_aws_json_1_0(
                data["freeTrialPricingTerm"]
            )
        }
    elif data.get("fixedUpfrontPricingTerm") is not None:
        import capo_marketplace_agreement.types.fixed_upfront_pricing_term

        return {
            "fixedUpfrontPricingTerm": capo_marketplace_agreement.types.fixed_upfront_pricing_term.deserialize_aws_json_1_0(
                data["fixedUpfrontPricingTerm"]
            )
        }
    elif data.get("variablePaymentTerm") is not None:
        import capo_marketplace_agreement.types.variable_payment_term

        return {
            "variablePaymentTerm": capo_marketplace_agreement.types.variable_payment_term.deserialize_aws_json_1_0(
                data["variablePaymentTerm"]
            )
        }
    elif data.get("netPaymentTerm") is not None:
        import capo_marketplace_agreement.types.net_payment_term

        return {
            "netPaymentTerm": capo_marketplace_agreement.types.net_payment_term.deserialize_aws_json_1_0(
                data["netPaymentTerm"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AcceptedTerm: no recognized variant key")
