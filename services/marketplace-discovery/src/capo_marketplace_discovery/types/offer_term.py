"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#OfferTerm``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError, SerializationError
from capo_marketplace_discovery.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.byol_pricing_term
    import capo_marketplace_discovery.types.configurable_upfront_pricing_term
    import capo_marketplace_discovery.types.fixed_upfront_pricing_term
    import capo_marketplace_discovery.types.free_trial_pricing_term
    import capo_marketplace_discovery.types.legal_term
    import capo_marketplace_discovery.types.net_payment_term
    import capo_marketplace_discovery.types.payment_schedule_term
    import capo_marketplace_discovery.types.recurring_payment_term
    import capo_marketplace_discovery.types.renewal_term
    import capo_marketplace_discovery.types.support_term
    import capo_marketplace_discovery.types.usage_based_pricing_term
    import capo_marketplace_discovery.types.validity_term
    import capo_marketplace_discovery.types.variable_payment_term


class _OfferTerm_byolPricingTerm(TypedDict, closed=True):
    byolPricingTerm: (
        "capo_marketplace_discovery.types.byol_pricing_term.ByolPricingTerm"
    )


class _OfferTerm_configurableUpfrontPricingTerm(TypedDict, closed=True):
    configurableUpfrontPricingTerm: "capo_marketplace_discovery.types.configurable_upfront_pricing_term.ConfigurableUpfrontPricingTerm"


class _OfferTerm_fixedUpfrontPricingTerm(TypedDict, closed=True):
    fixedUpfrontPricingTerm: "capo_marketplace_discovery.types.fixed_upfront_pricing_term.FixedUpfrontPricingTerm"


class _OfferTerm_freeTrialPricingTerm(TypedDict, closed=True):
    freeTrialPricingTerm: (
        "capo_marketplace_discovery.types.free_trial_pricing_term.FreeTrialPricingTerm"
    )


class _OfferTerm_legalTerm(TypedDict, closed=True):
    legalTerm: "capo_marketplace_discovery.types.legal_term.LegalTerm"


class _OfferTerm_paymentScheduleTerm(TypedDict, closed=True):
    paymentScheduleTerm: (
        "capo_marketplace_discovery.types.payment_schedule_term.PaymentScheduleTerm"
    )


class _OfferTerm_recurringPaymentTerm(TypedDict, closed=True):
    recurringPaymentTerm: (
        "capo_marketplace_discovery.types.recurring_payment_term.RecurringPaymentTerm"
    )


class _OfferTerm_renewalTerm(TypedDict, closed=True):
    renewalTerm: "capo_marketplace_discovery.types.renewal_term.RenewalTerm"


class _OfferTerm_supportTerm(TypedDict, closed=True):
    supportTerm: "capo_marketplace_discovery.types.support_term.SupportTerm"


class _OfferTerm_usageBasedPricingTerm(TypedDict, closed=True):
    usageBasedPricingTerm: "capo_marketplace_discovery.types.usage_based_pricing_term.UsageBasedPricingTerm"


class _OfferTerm_validityTerm(TypedDict, closed=True):
    validityTerm: "capo_marketplace_discovery.types.validity_term.ValidityTerm"


class _OfferTerm_variablePaymentTerm(TypedDict, closed=True):
    variablePaymentTerm: (
        "capo_marketplace_discovery.types.variable_payment_term.VariablePaymentTerm"
    )


class _OfferTerm_netPaymentTerm(TypedDict, closed=True):
    netPaymentTerm: "capo_marketplace_discovery.types.net_payment_term.NetPaymentTerm"


OfferTerm: TypeAlias = (
    _OfferTerm_byolPricingTerm
    | _OfferTerm_configurableUpfrontPricingTerm
    | _OfferTerm_fixedUpfrontPricingTerm
    | _OfferTerm_freeTrialPricingTerm
    | _OfferTerm_legalTerm
    | _OfferTerm_paymentScheduleTerm
    | _OfferTerm_recurringPaymentTerm
    | _OfferTerm_renewalTerm
    | _OfferTerm_supportTerm
    | _OfferTerm_usageBasedPricingTerm
    | _OfferTerm_validityTerm
    | _OfferTerm_variablePaymentTerm
    | _OfferTerm_netPaymentTerm
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: OfferTerm) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OfferTerm: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "byolPricingTerm" in value:
        import capo_marketplace_discovery.types.byol_pricing_term

        return {
            "byolPricingTerm": capo_marketplace_discovery.types.byol_pricing_term.serialize_json(
                value["byolPricingTerm"]
            )
        }
    elif "configurableUpfrontPricingTerm" in value:
        import capo_marketplace_discovery.types.configurable_upfront_pricing_term

        return {
            "configurableUpfrontPricingTerm": capo_marketplace_discovery.types.configurable_upfront_pricing_term.serialize_json(
                value["configurableUpfrontPricingTerm"]
            )
        }
    elif "fixedUpfrontPricingTerm" in value:
        import capo_marketplace_discovery.types.fixed_upfront_pricing_term

        return {
            "fixedUpfrontPricingTerm": capo_marketplace_discovery.types.fixed_upfront_pricing_term.serialize_json(
                value["fixedUpfrontPricingTerm"]
            )
        }
    elif "freeTrialPricingTerm" in value:
        import capo_marketplace_discovery.types.free_trial_pricing_term

        return {
            "freeTrialPricingTerm": capo_marketplace_discovery.types.free_trial_pricing_term.serialize_json(
                value["freeTrialPricingTerm"]
            )
        }
    elif "legalTerm" in value:
        import capo_marketplace_discovery.types.legal_term

        return {
            "legalTerm": capo_marketplace_discovery.types.legal_term.serialize_json(
                value["legalTerm"]
            )
        }
    elif "paymentScheduleTerm" in value:
        import capo_marketplace_discovery.types.payment_schedule_term

        return {
            "paymentScheduleTerm": capo_marketplace_discovery.types.payment_schedule_term.serialize_json(
                value["paymentScheduleTerm"]
            )
        }
    elif "recurringPaymentTerm" in value:
        import capo_marketplace_discovery.types.recurring_payment_term

        return {
            "recurringPaymentTerm": capo_marketplace_discovery.types.recurring_payment_term.serialize_json(
                value["recurringPaymentTerm"]
            )
        }
    elif "renewalTerm" in value:
        import capo_marketplace_discovery.types.renewal_term

        return {
            "renewalTerm": capo_marketplace_discovery.types.renewal_term.serialize_json(
                value["renewalTerm"]
            )
        }
    elif "supportTerm" in value:
        import capo_marketplace_discovery.types.support_term

        return {
            "supportTerm": capo_marketplace_discovery.types.support_term.serialize_json(
                value["supportTerm"]
            )
        }
    elif "usageBasedPricingTerm" in value:
        import capo_marketplace_discovery.types.usage_based_pricing_term

        return {
            "usageBasedPricingTerm": capo_marketplace_discovery.types.usage_based_pricing_term.serialize_json(
                value["usageBasedPricingTerm"]
            )
        }
    elif "validityTerm" in value:
        import capo_marketplace_discovery.types.validity_term

        return {
            "validityTerm": capo_marketplace_discovery.types.validity_term.serialize_json(
                value["validityTerm"]
            )
        }
    elif "variablePaymentTerm" in value:
        import capo_marketplace_discovery.types.variable_payment_term

        return {
            "variablePaymentTerm": capo_marketplace_discovery.types.variable_payment_term.serialize_json(
                value["variablePaymentTerm"]
            )
        }
    elif "netPaymentTerm" in value:
        import capo_marketplace_discovery.types.net_payment_term

        return {
            "netPaymentTerm": capo_marketplace_discovery.types.net_payment_term.serialize_json(
                value["netPaymentTerm"]
            )
        }
    else:
        raise SerializationError("OfferTerm: no variant present")


def deserialize_json(data: dict) -> OfferTerm:
    if data.get("byolPricingTerm") is not None:
        import capo_marketplace_discovery.types.byol_pricing_term

        return {
            "byolPricingTerm": capo_marketplace_discovery.types.byol_pricing_term.deserialize_json(
                data["byolPricingTerm"]
            )
        }
    elif data.get("configurableUpfrontPricingTerm") is not None:
        import capo_marketplace_discovery.types.configurable_upfront_pricing_term

        return {
            "configurableUpfrontPricingTerm": capo_marketplace_discovery.types.configurable_upfront_pricing_term.deserialize_json(
                data["configurableUpfrontPricingTerm"]
            )
        }
    elif data.get("fixedUpfrontPricingTerm") is not None:
        import capo_marketplace_discovery.types.fixed_upfront_pricing_term

        return {
            "fixedUpfrontPricingTerm": capo_marketplace_discovery.types.fixed_upfront_pricing_term.deserialize_json(
                data["fixedUpfrontPricingTerm"]
            )
        }
    elif data.get("freeTrialPricingTerm") is not None:
        import capo_marketplace_discovery.types.free_trial_pricing_term

        return {
            "freeTrialPricingTerm": capo_marketplace_discovery.types.free_trial_pricing_term.deserialize_json(
                data["freeTrialPricingTerm"]
            )
        }
    elif data.get("legalTerm") is not None:
        import capo_marketplace_discovery.types.legal_term

        return {
            "legalTerm": capo_marketplace_discovery.types.legal_term.deserialize_json(
                data["legalTerm"]
            )
        }
    elif data.get("paymentScheduleTerm") is not None:
        import capo_marketplace_discovery.types.payment_schedule_term

        return {
            "paymentScheduleTerm": capo_marketplace_discovery.types.payment_schedule_term.deserialize_json(
                data["paymentScheduleTerm"]
            )
        }
    elif data.get("recurringPaymentTerm") is not None:
        import capo_marketplace_discovery.types.recurring_payment_term

        return {
            "recurringPaymentTerm": capo_marketplace_discovery.types.recurring_payment_term.deserialize_json(
                data["recurringPaymentTerm"]
            )
        }
    elif data.get("renewalTerm") is not None:
        import capo_marketplace_discovery.types.renewal_term

        return {
            "renewalTerm": capo_marketplace_discovery.types.renewal_term.deserialize_json(
                data["renewalTerm"]
            )
        }
    elif data.get("supportTerm") is not None:
        import capo_marketplace_discovery.types.support_term

        return {
            "supportTerm": capo_marketplace_discovery.types.support_term.deserialize_json(
                data["supportTerm"]
            )
        }
    elif data.get("usageBasedPricingTerm") is not None:
        import capo_marketplace_discovery.types.usage_based_pricing_term

        return {
            "usageBasedPricingTerm": capo_marketplace_discovery.types.usage_based_pricing_term.deserialize_json(
                data["usageBasedPricingTerm"]
            )
        }
    elif data.get("validityTerm") is not None:
        import capo_marketplace_discovery.types.validity_term

        return {
            "validityTerm": capo_marketplace_discovery.types.validity_term.deserialize_json(
                data["validityTerm"]
            )
        }
    elif data.get("variablePaymentTerm") is not None:
        import capo_marketplace_discovery.types.variable_payment_term

        return {
            "variablePaymentTerm": capo_marketplace_discovery.types.variable_payment_term.deserialize_json(
                data["variablePaymentTerm"]
            )
        }
    elif data.get("netPaymentTerm") is not None:
        import capo_marketplace_discovery.types.net_payment_term

        return {
            "netPaymentTerm": capo_marketplace_discovery.types.net_payment_term.deserialize_json(
                data["netPaymentTerm"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OfferTerm: no recognized variant key")
