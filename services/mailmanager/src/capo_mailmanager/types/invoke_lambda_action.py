"""Generated from Smithy shape ``com.amazonaws.mailmanager#InvokeLambdaAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.action_failure_policy
    import capo_mailmanager.types.iam_role_arn
    import capo_mailmanager.types.lambda_function_arn
    import capo_mailmanager.types.lambda_invocation_type
    import capo_mailmanager.types.lambda_retry_time_minutes


class InvokeLambdaAction(TypedDict, closed=True):
    action_failure_policy: NotRequired[
        "capo_mailmanager.types.action_failure_policy.ActionFailurePolicy"
    ]
    """<p>A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the Amazon Web Services Lambda function no longer exists.</p>"""
    function_arn: "capo_mailmanager.types.lambda_function_arn.LambdaFunctionArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda function to invoke.</p>"""
    invocation_type: (
        "capo_mailmanager.types.lambda_invocation_type.LambdaInvocationType"
    )
    """<p>The invocation type of the Lambda function. Use EVENT for asynchronous invocation or REQUEST_RESPONSE for synchronous invocation.</p>"""
    role_arn: "capo_mailmanager.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to use to invoke the Lambda function.</p>"""
    retry_time_minutes: NotRequired[
        "capo_mailmanager.types.lambda_retry_time_minutes.LambdaRetryTimeMinutes"
    ]
    """<p>The maximum time in minutes that the email processing can be retried if the Lambda invocation fails. The maximum value is 2160 minutes (36 hours).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvokeLambdaAction) -> dict:
    out: dict = {}
    if "action_failure_policy" in value:
        import capo_mailmanager.types.action_failure_policy

        out["ActionFailurePolicy"] = (
            capo_mailmanager.types.action_failure_policy.serialize_aws_json_1_0(
                value["action_failure_policy"]
            )
        )
    out["FunctionArn"] = value["function_arn"]
    import capo_mailmanager.types.lambda_invocation_type

    out["InvocationType"] = (
        capo_mailmanager.types.lambda_invocation_type.serialize_aws_json_1_0(
            value["invocation_type"]
        )
    )
    out["RoleArn"] = value["role_arn"]
    if "retry_time_minutes" in value:
        out["RetryTimeMinutes"] = value["retry_time_minutes"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvokeLambdaAction:
    out: InvokeLambdaAction = {}  # type: ignore[typeddict-item]
    if data.get("ActionFailurePolicy") is not None:
        import capo_mailmanager.types.action_failure_policy

        out["action_failure_policy"] = (
            capo_mailmanager.types.action_failure_policy.deserialize_aws_json_1_0(
                data["ActionFailurePolicy"]
            )
        )
    if data.get("FunctionArn") is not None:
        out["function_arn"] = data["FunctionArn"]
    else:
        out["function_arn"] = ""
    if data.get("InvocationType") is not None:
        import capo_mailmanager.types.lambda_invocation_type

        out["invocation_type"] = (
            capo_mailmanager.types.lambda_invocation_type.deserialize_aws_json_1_0(
                data["InvocationType"]
            )
        )
    else:
        import typing

        out["invocation_type"] = typing.cast(
            "capo_mailmanager.types.lambda_invocation_type.LambdaInvocationType", ""
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("RetryTimeMinutes") is not None:
        out["retry_time_minutes"] = data["RetryTimeMinutes"]
    return out
