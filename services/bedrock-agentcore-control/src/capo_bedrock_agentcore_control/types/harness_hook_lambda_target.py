"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessHookLambdaTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_hook_failure_mode
    import capo_bedrock_agentcore_control.types.harness_lambda_function_arn


class HarnessHookLambdaTarget(TypedDict, closed=True):
    arn: "capo_bedrock_agentcore_control.types.harness_lambda_function_arn.HarnessLambdaFunctionArn"
    """<p>The ARN of the Lambda function to invoke.</p>"""
    timeout_seconds: "int"
    """<p>The maximum number of seconds to wait for the Lambda function response. The default is 60 seconds.</p>"""
    failure_mode: "capo_bedrock_agentcore_control.types.harness_hook_failure_mode.HarnessHookFailureMode"
    """<p>The behavior when the Lambda function times out, returns an error, or returns an invalid response. The default is <code>DENY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessHookLambdaTarget) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["timeoutSeconds"] = value.get("timeout_seconds", 60)
    import capo_bedrock_agentcore_control.types.harness_hook_failure_mode

    out["failureMode"] = (
        capo_bedrock_agentcore_control.types.harness_hook_failure_mode.serialize_json(
            value.get("failure_mode", "deny")
        )
    )
    return out


def deserialize_json(data: dict) -> HarnessHookLambdaTarget:
    out: HarnessHookLambdaTarget = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("timeoutSeconds") is not None:
        out["timeout_seconds"] = data["timeoutSeconds"]
    else:
        out["timeout_seconds"] = 60
    if data.get("failureMode") is not None:
        import capo_bedrock_agentcore_control.types.harness_hook_failure_mode

        out["failure_mode"] = (
            capo_bedrock_agentcore_control.types.harness_hook_failure_mode.deserialize_json(
                data["failureMode"]
            )
        )
    else:
        out["failure_mode"] = "deny"
    return out
