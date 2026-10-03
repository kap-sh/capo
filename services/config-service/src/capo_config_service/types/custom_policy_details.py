"""Generated from Smithy shape ``com.amazonaws.configservice#CustomPolicyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.boolean
    import capo_config_service.types.policy_runtime
    import capo_config_service.types.policy_text


class CustomPolicyDetails(TypedDict, closed=True):
    policy_runtime: "capo_config_service.types.policy_runtime.PolicyRuntime"
    """<p>The runtime system for your Config Custom Policy rule. Guard is a policy-as-code language that allows you to write policies that are enforced by Config Custom Policy rules. For more information about Guard, see the <a href="https://github.com/aws-cloudformation/cloudformation-guard">Guard GitHub Repository</a>.</p>"""
    policy_text: "capo_config_service.types.policy_text.PolicyText"
    """<p>The policy definition containing the logic for your Config Custom Policy rule.</p>"""
    enable_debug_log_delivery: "capo_config_service.types.boolean.Boolean"
    """<p>The boolean expression for enabling debug logging for your Config Custom Policy rule. The default value is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomPolicyDetails) -> dict:
    out: dict = {}
    out["PolicyRuntime"] = value["policy_runtime"]
    out["PolicyText"] = value["policy_text"]
    out["EnableDebugLogDelivery"] = value.get("enable_debug_log_delivery", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomPolicyDetails:
    out: CustomPolicyDetails = {}  # type: ignore[typeddict-item]
    if data.get("PolicyRuntime") is not None:
        out["policy_runtime"] = data["PolicyRuntime"]
    else:
        raise DeserializationError("CustomPolicyDetails.policy_runtime required")
    if data.get("PolicyText") is not None:
        out["policy_text"] = data["PolicyText"]
    else:
        raise DeserializationError("CustomPolicyDetails.policy_text required")
    if data.get("EnableDebugLogDelivery") is not None:
        out["enable_debug_log_delivery"] = data["EnableDebugLogDelivery"]
    else:
        out["enable_debug_log_delivery"] = False
    return out
