"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutAccountPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.account_policy


class PutAccountPolicyResponse(TypedDict, closed=True):
    account_policy: NotRequired[
        "capo_cloudwatch_logs.types.account_policy.AccountPolicy"
    ]
    """<p>The account policy that you created.</p>"""


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
    return out
