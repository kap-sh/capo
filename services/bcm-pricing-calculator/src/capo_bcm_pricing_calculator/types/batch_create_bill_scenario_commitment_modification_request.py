"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioCommitmentModificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries
    import capo_bcm_pricing_calculator.types.client_token
    import capo_bcm_pricing_calculator.types.resource_id


class BatchCreateBillScenarioCommitmentModificationRequest(TypedDict, closed=True):
    bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Bill Scenario for which you want to create the modeled commitment. </p>"""
    commitment_modifications: "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries.BatchCreateBillScenarioCommitmentModificationEntries"
    """<p> List of commitments that you want to model in the Bill Scenario. </p>"""
    client_token: NotRequired[
        "capo_bcm_pricing_calculator.types.client_token.ClientToken"
    ]
    """<p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioCommitmentModificationRequest,
) -> dict:
    out: dict = {}
    out["billScenarioId"] = value["bill_scenario_id"]
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries

    out["commitmentModifications"] = (
        capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries.serialize_aws_json_1_0(
            value["commitment_modifications"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchCreateBillScenarioCommitmentModificationRequest:
    out: BatchCreateBillScenarioCommitmentModificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("billScenarioId") is not None:
        out["bill_scenario_id"] = data["billScenarioId"]
    else:
        out["bill_scenario_id"] = ""
    if data.get("commitmentModifications") is not None:
        import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries

        out["commitment_modifications"] = (
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_commitment_modification_entries.deserialize_aws_json_1_0(
                data["commitmentModifications"]
            )
        )
    else:
        out["commitment_modifications"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
