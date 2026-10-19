"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioCommitmentModificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entries
    import capo_bcm_pricing_calculator.types.resource_id


class BatchUpdateBillScenarioCommitmentModificationRequest(TypedDict, closed=True):
    bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Bill Scenario for which you want to modify the commitment group of a modeled commitment. </p>"""
    commitment_modifications: "capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entries.BatchUpdateBillScenarioCommitmentModificationEntries"
    """<p> List of commitments that you want to update in a Bill Scenario. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchUpdateBillScenarioCommitmentModificationRequest,
) -> dict:
    out: dict = {}
    out["billScenarioId"] = value["bill_scenario_id"]
    import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entries

    out["commitmentModifications"] = (
        capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entries.serialize_aws_json_1_0(
            value["commitment_modifications"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchUpdateBillScenarioCommitmentModificationRequest:
    out: BatchUpdateBillScenarioCommitmentModificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("billScenarioId") is not None:
        out["bill_scenario_id"] = data["billScenarioId"]
    else:
        out["bill_scenario_id"] = ""
    if data.get("commitmentModifications") is not None:
        import capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entries

        out["commitment_modifications"] = (
            capo_bcm_pricing_calculator.types.batch_update_bill_scenario_commitment_modification_entries.deserialize_aws_json_1_0(
                data["commitmentModifications"]
            )
        )
    else:
        out["commitment_modifications"] = []
    return out
