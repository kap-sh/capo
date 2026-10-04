"""Generated from Smithy shape ``com.amazonaws.billing#BusinessSupportTierCharge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class BusinessSupportTierCharge(TypedDict, closed=True):
    tier_description: "str"
    """<p>A human-readable description of the pricing tier, including the spend range and percentage rate applied.</p>"""
    tier_rate: "str"
    """<p>The percentage rate applied to Support-eligible spend within this pricing tier.</p>"""
    usage_slice: "str"
    """<p>The amount of Support-eligible spend that falls within this pricing tier.</p>"""
    tier_charge: "str"
    """<p>The Business Support charge amount calculated for this pricing tier.</p>"""
    charge_period_start_date: NotRequired["datetime.datetime"]
    """<p>The start date of the charge period for this tier charge.</p>"""
    charge_period_end_date: NotRequired["datetime.datetime"]
    """<p>The end date of the charge period for this tier charge.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessSupportTierCharge) -> dict:
    out: dict = {}
    out["tierDescription"] = value["tier_description"]
    out["tierRate"] = value["tier_rate"]
    out["usageSlice"] = value["usage_slice"]
    out["tierCharge"] = value["tier_charge"]
    if "charge_period_start_date" in value:
        import capo_billing.types._prelude.timestamp

        out["chargePeriodStartDate"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["charge_period_start_date"]
            )
        )
    if "charge_period_end_date" in value:
        import capo_billing.types._prelude.timestamp

        out["chargePeriodEndDate"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["charge_period_end_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BusinessSupportTierCharge:
    out: BusinessSupportTierCharge = {}  # type: ignore[typeddict-item]
    if data.get("tierDescription") is not None:
        out["tier_description"] = data["tierDescription"]
    else:
        raise DeserializationError(
            "BusinessSupportTierCharge.tier_description required"
        )
    if data.get("tierRate") is not None:
        out["tier_rate"] = data["tierRate"]
    else:
        raise DeserializationError("BusinessSupportTierCharge.tier_rate required")
    if data.get("usageSlice") is not None:
        out["usage_slice"] = data["usageSlice"]
    else:
        raise DeserializationError("BusinessSupportTierCharge.usage_slice required")
    if data.get("tierCharge") is not None:
        out["tier_charge"] = data["tierCharge"]
    else:
        raise DeserializationError("BusinessSupportTierCharge.tier_charge required")
    if data.get("chargePeriodStartDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["charge_period_start_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["chargePeriodStartDate"]
            )
        )
    if data.get("chargePeriodEndDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["charge_period_end_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["chargePeriodEndDate"]
            )
        )
    return out
