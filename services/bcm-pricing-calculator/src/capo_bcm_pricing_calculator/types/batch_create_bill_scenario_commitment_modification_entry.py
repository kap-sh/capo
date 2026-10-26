"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioCommitmentModificationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.account_id
    import capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action
    import capo_bcm_pricing_calculator.types.key
    import capo_bcm_pricing_calculator.types.usage_group


class BatchCreateBillScenarioCommitmentModificationEntry(TypedDict, closed=True):
    key: "capo_bcm_pricing_calculator.types.key.Key"
    """<p> A unique identifier for this entry in the batch operation. This can be any valid string. This key is useful to identify errors associated with any commitment entry as any error is returned with this key. </p>"""
    group: NotRequired["capo_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> An optional group identifier for the commitment modification. </p>"""
    usage_account_id: "capo_bcm_pricing_calculator.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID to which this commitment will be applied to. </p>"""
    commitment_action: "capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action.BillScenarioCommitmentModificationAction"
    """<p> The specific commitment action to be taken (e.g., adding a Reserved Instance or Savings Plan). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioCommitmentModificationEntry,
) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "group" in value:
        out["group"] = value["group"]
    out["usageAccountId"] = value["usage_account_id"]
    import capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action

    out["commitmentAction"] = (
        capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action.serialize_aws_json_1_0(
            value["commitment_action"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchCreateBillScenarioCommitmentModificationEntry:
    out: BatchCreateBillScenarioCommitmentModificationEntry = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("group") is not None:
        out["group"] = data["group"]
    if data.get("usageAccountId") is not None:
        out["usage_account_id"] = data["usageAccountId"]
    else:
        out["usage_account_id"] = ""
    if data.get("commitmentAction") is not None:
        import capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action

        out["commitment_action"] = (
            capo_bcm_pricing_calculator.types.bill_scenario_commitment_modification_action.deserialize_aws_json_1_0(
                data["commitmentAction"]
            )
        )
    else:
        out["commitment_action"] = {"$unknown": {"name": ""}}
    return out
