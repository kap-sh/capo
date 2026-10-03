"""Generated from Smithy shape ``com.amazonaws.sts#AssumeRootRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element
from capo_sts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sts.types.minimum_session_token_size_type
    import capo_sts.types.policy_descriptor_type
    import capo_sts.types.root_duration_seconds_type
    import capo_sts.types.target_principal_type


class AssumeRootRequest(TypedDict, closed=True):
    target_principal: "capo_sts.types.target_principal_type.TargetPrincipalType"
    """<p>The member account principal ARN or account ID.</p>"""
    task_policy_arn: "capo_sts.types.policy_descriptor_type.PolicyDescriptorType"
    """<p>The identity based policy that scopes the session to the privileged tasks that can be performed. You must use one of following Amazon Web Services managed policies to scope root session actions:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMAuditRootUserCredentials">IAMAuditRootUserCredentials</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMCreateRootUserPassword">IAMCreateRootUserPassword</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMDeleteRootUserCredentials">IAMDeleteRootUserCredentials</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-S3UnlockBucketPolicy">S3UnlockBucketPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-SQSUnlockQueuePolicy">SQSUnlockQueuePolicy</a> </p> </li> </ul>"""
    duration_seconds: NotRequired[
        "capo_sts.types.root_duration_seconds_type.RootDurationSecondsType"
    ]
    """<p>The duration, in seconds, of the privileged session. The value can range from 0 seconds up to the maximum session duration of 900 seconds (15 minutes). If you specify a value higher than this setting, the operation fails.</p> <p>By default, the value is set to <code>900</code> seconds.</p>"""
    minimum_session_token_size: NotRequired[
        "capo_sts.types.minimum_session_token_size_type.minimumSessionTokenSizeType"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AssumeRootRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TargetPrincipal", str(value["target_principal"])))
    import capo_sts.types.policy_descriptor_type

    capo_sts.types.policy_descriptor_type.serialize_query(
        value["task_policy_arn"], pairs, f"{key_prefix}TaskPolicyArn"
    )
    if "duration_seconds" in value:
        pairs.append((f"{key_prefix}DurationSeconds", str(value["duration_seconds"])))
    if "minimum_session_token_size" in value:
        pairs.append(
            (
                f"{key_prefix}MinimumSessionTokenSize",
                str(value["minimum_session_token_size"]),
            )
        )


def deserialize_query(el: Element) -> AssumeRootRequest:
    out: AssumeRootRequest = {}  # type: ignore[typeddict-item]
    child_target_principal = el.find("TargetPrincipal")
    if child_target_principal is not None:
        out["target_principal"] = str(child_target_principal.text or "")
    else:
        raise DeserializationError("AssumeRootRequest.target_principal required")
    child_task_policy_arn = el.find("TaskPolicyArn")
    if child_task_policy_arn is not None:
        import capo_sts.types.policy_descriptor_type

        out["task_policy_arn"] = (
            capo_sts.types.policy_descriptor_type.deserialize_query(
                child_task_policy_arn
            )
        )
    else:
        raise DeserializationError("AssumeRootRequest.task_policy_arn required")
    child_duration_seconds = el.find("DurationSeconds")
    if child_duration_seconds is not None:
        out["duration_seconds"] = int(child_duration_seconds.text or "")
    child_minimum_session_token_size = el.find("MinimumSessionTokenSize")
    if child_minimum_session_token_size is not None:
        out["minimum_session_token_size"] = int(
            child_minimum_session_token_size.text or ""
        )
    return out
