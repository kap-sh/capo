"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SoftwareRevenue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date
    import capo_partnercentral_selling.types.monetary_value
    import capo_partnercentral_selling.types.revenue_model


class SoftwareRevenue(TypedDict, closed=True):
    delivery_model: NotRequired[
        "capo_partnercentral_selling.types.revenue_model.RevenueModel"
    ]
    """<p>Specifies the customer's intended payment type agreement or procurement method to acquire the solution or service outlined in the <code>Opportunity</code>.</p>"""
    value: NotRequired["capo_partnercentral_selling.types.monetary_value.MonetaryValue"]
    """<p>Specifies the payment value (amount and currency).</p>"""
    effective_date: NotRequired["capo_partnercentral_selling.types.date.Date"]
    """<p>Specifies the <code>Opportunity</code>'s customer engagement start date for the contract's effectiveness.</p>"""
    expiration_date: NotRequired["capo_partnercentral_selling.types.date.Date"]
    """<p>Specifies the expiration date for the contract between the customer and Amazon Web Services partner. It signifies the termination date of the agreed-upon engagement period between both parties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SoftwareRevenue) -> dict:
    out: dict = {}
    if "delivery_model" in value:
        import capo_partnercentral_selling.types.revenue_model

        out["DeliveryModel"] = (
            capo_partnercentral_selling.types.revenue_model.serialize_aws_json_1_0(
                value["delivery_model"]
            )
        )
    if "value" in value:
        import capo_partnercentral_selling.types.monetary_value

        out["Value"] = (
            capo_partnercentral_selling.types.monetary_value.serialize_aws_json_1_0(
                value["value"]
            )
        )
    if "effective_date" in value:
        out["EffectiveDate"] = value["effective_date"]
    if "expiration_date" in value:
        out["ExpirationDate"] = value["expiration_date"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SoftwareRevenue:
    out: SoftwareRevenue = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryModel") is not None:
        import capo_partnercentral_selling.types.revenue_model

        out["delivery_model"] = (
            capo_partnercentral_selling.types.revenue_model.deserialize_aws_json_1_0(
                data["DeliveryModel"]
            )
        )
    if data.get("Value") is not None:
        import capo_partnercentral_selling.types.monetary_value

        out["value"] = (
            capo_partnercentral_selling.types.monetary_value.deserialize_aws_json_1_0(
                data["Value"]
            )
        )
    if data.get("EffectiveDate") is not None:
        out["effective_date"] = data["EffectiveDate"]
    if data.get("ExpirationDate") is not None:
        out["expiration_date"] = data["ExpirationDate"]
    return out


def redact_sensitive(value: SoftwareRevenue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        import capo_partnercentral_selling.types.monetary_value

        out["value"] = (
            capo_partnercentral_selling.types.monetary_value.redact_sensitive(
                value["value"]
            )
        )
    return out
