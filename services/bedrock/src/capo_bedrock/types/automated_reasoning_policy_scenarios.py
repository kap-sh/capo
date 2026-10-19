"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyScenarios``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_scenario_list


class AutomatedReasoningPolicyScenarios(TypedDict, closed=True):
    policy_scenarios: "capo_bedrock.types.automated_reasoning_policy_scenario_list.AutomatedReasoningPolicyScenarioList"
    """<p>Represents a collection of generated policy scenarios.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyScenarios) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_scenario_list

    out["policyScenarios"] = (
        capo_bedrock.types.automated_reasoning_policy_scenario_list.serialize_json(
            value["policy_scenarios"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyScenarios:
    out: AutomatedReasoningPolicyScenarios = {}  # type: ignore[typeddict-item]
    if data.get("policyScenarios") is not None:
        import capo_bedrock.types.automated_reasoning_policy_scenario_list

        out["policy_scenarios"] = (
            capo_bedrock.types.automated_reasoning_policy_scenario_list.deserialize_json(
                data["policyScenarios"]
            )
        )
    else:
        out["policy_scenarios"] = []
    return out


def redact_sensitive(value: AutomatedReasoningPolicyScenarios) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy_scenarios" in value:
        import capo_bedrock.types.automated_reasoning_policy_scenario_list

        out["policy_scenarios"] = (
            capo_bedrock.types.automated_reasoning_policy_scenario_list.redact_sensitive(
                value["policy_scenarios"]
            )
        )
    return out
