"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsSoftwareRevenue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.monetary_value


class AwsSoftwareRevenue(TypedDict, closed=True):
    value: NotRequired["capo_partnercentral_selling.types.monetary_value.MonetaryValue"]
    discount: NotRequired["str"]
    """<p>Discount percentage offered on the software revenue. Percent convention: 15.00 means 15%.</p>"""
    effective_date: NotRequired["str"]
    """<p>Contract effective (start) date in YYYY-MM-DD format.</p>"""
    expiration_date: NotRequired["str"]
    """<p>Contract expiration (end) date in YYYY-MM-DD format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsSoftwareRevenue) -> dict:
    out: dict = {}
    if "value" in value:
        import capo_partnercentral_selling.types.monetary_value

        out["Value"] = (
            capo_partnercentral_selling.types.monetary_value.serialize_aws_json_1_0(
                value["value"]
            )
        )
    if "discount" in value:
        out["Discount"] = value["discount"]
    if "effective_date" in value:
        out["EffectiveDate"] = value["effective_date"]
    if "expiration_date" in value:
        out["ExpirationDate"] = value["expiration_date"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsSoftwareRevenue:
    out: AwsSoftwareRevenue = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        import capo_partnercentral_selling.types.monetary_value

        out["value"] = (
            capo_partnercentral_selling.types.monetary_value.deserialize_aws_json_1_0(
                data["Value"]
            )
        )
    if data.get("Discount") is not None:
        out["discount"] = data["Discount"]
    if data.get("EffectiveDate") is not None:
        out["effective_date"] = data["EffectiveDate"]
    if data.get("ExpirationDate") is not None:
        out["expiration_date"] = data["ExpirationDate"]
    return out


def redact_sensitive(value: AwsSoftwareRevenue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        import capo_partnercentral_selling.types.monetary_value

        out["value"] = (
            capo_partnercentral_selling.types.monetary_value.redact_sensitive(
                value["value"]
            )
        )
    return out
