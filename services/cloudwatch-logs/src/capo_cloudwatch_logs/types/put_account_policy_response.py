"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutAccountPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.account_policy
    import capo_cloudwatch_logs.types.dry_run_result


class PutAccountPolicyResponse(TypedDict, closed=True):
    account_policy: NotRequired[
        "capo_cloudwatch_logs.types.account_policy.AccountPolicy"
    ]
    """<p>The account policy that you created.</p>"""
    dry_run_result: NotRequired[
        "capo_cloudwatch_logs.types.dry_run_result.DryRunResult"
    ]
    """<p>The estimated impact of the policy on log groups in the account. This field is returned only when the request specifies <code>dryRun</code> as <code>true</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAccountPolicyResponse) -> dict:
    out: dict = {}
    if "account_policy" in value:
        import capo_cloudwatch_logs.types.account_policy

        out["accountPolicy"] = (
            capo_cloudwatch_logs.types.account_policy.serialize_aws_json_1_1(
                value["account_policy"]
            )
        )
    if "dry_run_result" in value:
        import capo_cloudwatch_logs.types.dry_run_result

        out["dryRunResult"] = (
            capo_cloudwatch_logs.types.dry_run_result.serialize_aws_json_1_1(
                value["dry_run_result"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAccountPolicyResponse:
    out: PutAccountPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("accountPolicy") is not None:
        import capo_cloudwatch_logs.types.account_policy

        out["account_policy"] = (
            capo_cloudwatch_logs.types.account_policy.deserialize_aws_json_1_1(
                data["accountPolicy"]
            )
        )
    if data.get("dryRunResult") is not None:
        import capo_cloudwatch_logs.types.dry_run_result

        out["dry_run_result"] = (
            capo_cloudwatch_logs.types.dry_run_result.deserialize_aws_json_1_1(
                data["dryRunResult"]
            )
        )
    return out
