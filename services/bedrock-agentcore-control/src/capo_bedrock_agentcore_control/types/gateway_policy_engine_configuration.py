"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayPolicyEngineConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_policy_engine_arn
    import capo_bedrock_agentcore_control.types.gateway_policy_engine_mode


class GatewayPolicyEngineConfiguration(TypedDict, closed=True):
    arn: "capo_bedrock_agentcore_control.types.gateway_policy_engine_arn.GatewayPolicyEngineArn"
    """<p>The ARN of the policy engine. The policy engine contains Cedar or Dogwood policies that define fine-grained authorization rules specifying who can perform what actions on which resources as agents interact through the gateway.</p>"""
    mode: "capo_bedrock_agentcore_control.types.gateway_policy_engine_mode.GatewayPolicyEngineMode"
    """<p>The enforcement mode for the policy engine. Valid values include:</p> <ul> <li> <p> <code>LOG_ONLY</code> - The policy engine evaluates each action against your policies and adds traces on whether tool calls would be allowed or denied, but does not enforce the decision. Use this mode to test and validate policies before enabling enforcement.</p> </li> <li> <p> <code>ENFORCE</code> - The policy engine evaluates actions against your policies and enforces decisions by allowing or denying agent operations. Test and validate policies in <code>LOG_ONLY</code> mode before enabling enforcement to avoid unintended denials or adversely affecting production traffic.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayPolicyEngineConfiguration) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_bedrock_agentcore_control.types.gateway_policy_engine_mode

    out["mode"] = (
        capo_bedrock_agentcore_control.types.gateway_policy_engine_mode.serialize_json(
            value["mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> GatewayPolicyEngineConfiguration:
    out: GatewayPolicyEngineConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("mode") is not None:
        import capo_bedrock_agentcore_control.types.gateway_policy_engine_mode

        out["mode"] = (
            capo_bedrock_agentcore_control.types.gateway_policy_engine_mode.deserialize_json(
                data["mode"]
            )
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_bedrock_agentcore_control.types.gateway_policy_engine_mode.GatewayPolicyEngineMode",
            "",
        )
    return out
