"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteBillScenarioUsageModificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_entries
    import capo_bcm_pricing_calculator.types.resource_id


class BatchDeleteBillScenarioUsageModificationRequest(TypedDict, closed=True):
    bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Bill Scenario for which you want to delete the modeled usage. </p>"""
    ids: "capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_entries.BatchDeleteBillScenarioUsageModificationEntries"
    """<p> List of usage that you want to delete from the Bill Scenario. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchDeleteBillScenarioUsageModificationRequest,
) -> dict:
    out: dict = {}
    out["billScenarioId"] = value["bill_scenario_id"]
    import capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_entries

    out["ids"] = (
        capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_entries.serialize_aws_json_1_0(
            value["ids"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchDeleteBillScenarioUsageModificationRequest:
    out: BatchDeleteBillScenarioUsageModificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("billScenarioId") is not None:
        out["bill_scenario_id"] = data["billScenarioId"]
    else:
        out["bill_scenario_id"] = ""
    if data.get("ids") is not None:
        import capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_entries

        out["ids"] = (
            capo_bcm_pricing_calculator.types.batch_delete_bill_scenario_usage_modification_entries.deserialize_aws_json_1_0(
                data["ids"]
            )
        )
    else:
        out["ids"] = []
    return out
