"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioUsageModificationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.usage_amounts
    import capo_bcm_pricing_calculator.types.usage_group


class BatchUpdateBillScenarioUsageModificationEntry(TypedDict, closed=True):
    id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the usage modification to update. </p>"""
    group: NotRequired["capo_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> The updated group identifier for the usage modification. </p>"""
    amounts: NotRequired["capo_bcm_pricing_calculator.types.usage_amounts.UsageAmounts"]
    """<p> The updated usage amounts for the modification. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchUpdateBillScenarioUsageModificationEntry,
) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "group" in value:
        out["group"] = value["group"]
    if "amounts" in value:
        import capo_bcm_pricing_calculator.types.usage_amounts

        out["amounts"] = (
            capo_bcm_pricing_calculator.types.usage_amounts.serialize_aws_json_1_0(
                value["amounts"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchUpdateBillScenarioUsageModificationEntry:
    out: BatchUpdateBillScenarioUsageModificationEntry = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("group") is not None:
        out["group"] = data["group"]
    if data.get("amounts") is not None:
        import capo_bcm_pricing_calculator.types.usage_amounts

        out["amounts"] = (
            capo_bcm_pricing_calculator.types.usage_amounts.deserialize_aws_json_1_0(
                data["amounts"]
            )
        )
    return out
