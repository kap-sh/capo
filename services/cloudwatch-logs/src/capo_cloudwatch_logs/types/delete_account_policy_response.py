"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteAccountPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.dry_run_result


class DeleteAccountPolicyResponse(TypedDict, closed=True):
    dry_run_result: NotRequired[
        "capo_cloudwatch_logs.types.dry_run_result.DryRunResult"
    ]
    """<p>The estimated impact of deleting the policy. This field is returned only when the request specifies <code>dryRun</code> as <code>true</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAccountPolicyResponse) -> dict:
    out: dict = {}
    if "dry_run_result" in value:
        import capo_cloudwatch_logs.types.dry_run_result

        out["dryRunResult"] = (
            capo_cloudwatch_logs.types.dry_run_result.serialize_aws_json_1_1(
                value["dry_run_result"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAccountPolicyResponse:
    out: DeleteAccountPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("dryRunResult") is not None:
        import capo_cloudwatch_logs.types.dry_run_result

        out["dry_run_result"] = (
            capo_cloudwatch_logs.types.dry_run_result.deserialize_aws_json_1_1(
                data["dryRunResult"]
            )
        )
    return out
