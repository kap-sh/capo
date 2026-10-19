"""Generated from Smithy shape ``com.amazonaws.budgets#ScpActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.policy_id
    import capo_budgets.types.target_ids


class ScpActionDefinition(TypedDict, closed=True):
    policy_id: "capo_budgets.types.policy_id.PolicyId"
    """<p>The policy ID attached. </p>"""
    target_ids: "capo_budgets.types.target_ids.TargetIds"
    """<p>A list of target IDs. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScpActionDefinition) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    import capo_budgets.types.target_ids

    out["TargetIds"] = capo_budgets.types.target_ids.serialize_aws_json_1_1(
        value["target_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScpActionDefinition:
    out: ScpActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        out["policy_id"] = ""
    if data.get("TargetIds") is not None:
        import capo_budgets.types.target_ids

        out["target_ids"] = capo_budgets.types.target_ids.deserialize_aws_json_1_1(
            data["TargetIds"]
        )
    else:
        out["target_ids"] = []
    return out
