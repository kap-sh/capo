"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#EstimatedCharges``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.currency_code


class EstimatedCharges(TypedDict, closed=True):
    currency_code: NotRequired[
        "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>Defines the currency code for the charge.</p>"""
    agreement_value: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The total known amount customer has to pay across the lifecycle of the agreement.</p> <note> <p>This is the total contract value if accepted terms contain <code>ConfigurableUpfrontPricingTerm</code> or <code>FixedUpfrontPricingTerm</code>. In the case of pure contract pricing, this will be the total value of the contract. In the case of contracts with consumption pricing, this will only include the committed value and not include any overages that occur.</p> <p>If the accepted terms contain <code>PaymentScheduleTerm</code>, it will be the total payment schedule amount. This occurs when flexible payment schedule is used, and is the sum of all invoice charges in the payment schedule.</p> <p>In case a customer has amended an agreement, by purchasing more units of any dimension, this will include both the original cost as well as the added cost incurred due to addition of new units. </p> <p>This is <code>0</code> if the accepted terms contain <code>UsageBasedPricingTerm</code> without <code>ConfigurableUpfrontPricingTerm</code> or <code>RecurringPaymentTerm</code>. This occurs for usage-based pricing (such as SaaS metered or AMI/container hourly or monthly), because the exact usage is not known upfront.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EstimatedCharges) -> dict:
    out: dict = {}
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "agreement_value" in value:
        out["agreementValue"] = value["agreement_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EstimatedCharges:
    out: EstimatedCharges = {}  # type: ignore[typeddict-item]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("agreementValue") is not None:
        out["agreement_value"] = data["agreementValue"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EstimatedCharges) -> dict:
    out: dict = {}
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "agreement_value" in value:
        out["agreementValue"] = value["agreement_value"]
    return out


def deserialize_cbor(data: dict) -> EstimatedCharges:
    out: EstimatedCharges = {}  # type: ignore[typeddict-item]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("agreementValue") is not None:
        out["agreement_value"] = data["agreementValue"]
    return out
