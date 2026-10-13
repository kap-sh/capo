"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyNextScenarioResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_scenario


class GetAutomatedReasoningPolicyNextScenarioResponse(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy.</p>"""
    scenario: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_scenario.AutomatedReasoningPolicyScenario"
    ]
    """<p>The next test scenario to validate, including the test expression and expected results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyNextScenarioResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    if "scenario" in value:
        import capo_bedrock.types.automated_reasoning_policy_scenario

        out["scenario"] = (
            capo_bedrock.types.automated_reasoning_policy_scenario.serialize_json(
                value["scenario"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyNextScenarioResponse:
    out: GetAutomatedReasoningPolicyNextScenarioResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyNextScenarioResponse.policy_arn required"
        )
    if data.get("scenario") is not None:
        import capo_bedrock.types.automated_reasoning_policy_scenario

        out["scenario"] = (
            capo_bedrock.types.automated_reasoning_policy_scenario.deserialize_json(
                data["scenario"]
            )
        )
    return out


def redact_sensitive(
    value: GetAutomatedReasoningPolicyNextScenarioResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "scenario" in value:
        import capo_bedrock.types.automated_reasoning_policy_scenario

        out["scenario"] = (
            capo_bedrock.types.automated_reasoning_policy_scenario.redact_sensitive(
                value["scenario"]
            )
        )
    return out
