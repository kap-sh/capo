"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteAccountPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.policy_name
    import capo_cloudwatch_logs.types.policy_type


class DeleteAccountPolicyRequest(TypedDict, closed=True):
    policy_name: "capo_cloudwatch_logs.types.policy_name.PolicyName"
    """<p>The name of the policy to delete.</p>"""
    policy_type: "capo_cloudwatch_logs.types.policy_type.PolicyType"
    """<p>The type of policy to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAccountPolicyRequest) -> dict:
    out: dict = {}
    out["policyName"] = value["policy_name"]
    import capo_cloudwatch_logs.types.policy_type

    out["policyType"] = capo_cloudwatch_logs.types.policy_type.serialize_aws_json_1_1(
        value["policy_type"]
    )
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
    return out
