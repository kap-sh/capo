"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteAccountPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.dry_run
    import capo_cloudwatch_logs.types.policy_name
    import capo_cloudwatch_logs.types.policy_type


class DeleteAccountPolicyRequest(TypedDict, closed=True):
    policy_name: "capo_cloudwatch_logs.types.policy_name.PolicyName"
    """<p>The name of the policy to delete.</p>"""
    policy_type: "capo_cloudwatch_logs.types.policy_type.PolicyType"
    """<p>The type of policy to delete.</p>"""
    dry_run: NotRequired["capo_cloudwatch_logs.types.dry_run.DryRun"]
    """<p>Specifies whether to preview the impact of deleting the policy without deleting it. If you specify <code>true</code>, CloudWatch Logs does not delete the policy and returns the estimated impact in <code>dryRunResult</code>. The default is <code>false</code>.</p> <p>Specifying <code>dryRun</code> is valid only when you specify <code>RETENTION_POLICY</code> for <code>policyType</code>. Only one dry run can be in progress for an account at a time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAccountPolicyRequest) -> dict:
    out: dict = {}
    out["policyName"] = value["policy_name"]
    import capo_cloudwatch_logs.types.policy_type

    out["policyType"] = capo_cloudwatch_logs.types.policy_type.serialize_aws_json_1_1(
        value["policy_type"]
    )
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAccountPolicyRequest:
    out: DeleteAccountPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyName") is not None:
        out["policy_name"] = data["policyName"]
    else:
        out["policy_name"] = ""
    if data.get("policyType") is not None:
        import capo_cloudwatch_logs.types.policy_type

        out["policy_type"] = (
            capo_cloudwatch_logs.types.policy_type.deserialize_aws_json_1_1(
                data["policyType"]
            )
        )
    else:
        import typing

        out["policy_type"] = typing.cast(
            "capo_cloudwatch_logs.types.policy_type.PolicyType", ""
        )
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
