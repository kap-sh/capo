"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioUsageModificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries
    import capo_bcm_pricing_calculator.types.resource_id


class BatchUpdateBillScenarioUsageModificationRequest(TypedDict, closed=True):
    bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Bill Scenario for which you want to modify the usage lines. </p>"""
    usage_modifications: "capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries.BatchUpdateBillScenarioUsageModificationEntries"
    """<p> List of usage lines that you want to update in a Bill Scenario identified by the usage ID. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchUpdateBillScenarioUsageModificationRequest,
) -> dict:
    out: dict = {}
    out["billScenarioId"] = value["bill_scenario_id"]
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries

    out["usageModifications"] = (
        capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries.serialize_aws_json_1_0(
            value["usage_modifications"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchUpdateBillScenarioUsageModificationRequest:
    out: BatchUpdateBillScenarioUsageModificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("billScenarioId") is not None:
        out["bill_scenario_id"] = data["billScenarioId"]
    else:
        out["bill_scenario_id"] = ""
    if data.get("usageModifications") is not None:
        import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries

        out["usage_modifications"] = (
            capo_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries.deserialize_aws_json_1_0(
                data["usageModifications"]
            )
        )
    else:
        out["usage_modifications"] = []
    return out
