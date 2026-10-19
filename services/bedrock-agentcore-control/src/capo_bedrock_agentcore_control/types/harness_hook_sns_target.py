"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessHookSnsTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_sns_topic_arn


class HarnessHookSnsTarget(TypedDict, closed=True):
    arn: "capo_bedrock_agentcore_control.types.harness_sns_topic_arn.HarnessSnsTopicArn"
    """<p>The ARN of the Amazon SNS topic to publish hook events to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessHookSnsTarget) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> HarnessHookSnsTarget:
    out: HarnessHookSnsTarget = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
