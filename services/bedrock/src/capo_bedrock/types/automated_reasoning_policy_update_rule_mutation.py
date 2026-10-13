"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateRuleMutation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule


class AutomatedReasoningPolicyUpdateRuleMutation(TypedDict, closed=True):
    rule: "capo_bedrock.types.automated_reasoning_policy_definition_rule.AutomatedReasoningPolicyDefinitionRule"
    """<p>The updated rule definition containing the modified formal logical expression and any changed metadata for the existing rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyUpdateRuleMutation) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_definition_rule

    out["rule"] = (
        capo_bedrock.types.automated_reasoning_policy_definition_rule.serialize_json(
            value["rule"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyUpdateRuleMutation:
    out: AutomatedReasoningPolicyUpdateRuleMutation = {}  # type: ignore[typeddict-item]
    if data.get("rule") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule

        out["rule"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_rule.deserialize_json(
                data["rule"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateRuleMutation.rule required"
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyUpdateRuleMutation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rule" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule

        out["rule"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_rule.redact_sensitive(
                value["rule"]
            )
        )
    return out
