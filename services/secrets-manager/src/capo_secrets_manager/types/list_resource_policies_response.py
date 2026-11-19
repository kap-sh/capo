"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ListResourcePoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.next_token_type
    import capo_secrets_manager.types.resource_policy_summary_list_type


class ListResourcePoliciesResponse(TypedDict, closed=True):
    resource_policies: "capo_secrets_manager.types.resource_policy_summary_list_type.ResourcePolicySummaryListType"
    """<p>A list of the resource policies attached to the secret.</p>"""
    next_token: NotRequired["capo_secrets_manager.types.next_token_type.NextTokenType"]
    """<p>Secrets Manager includes this value if there's more output available than what is included in the current response. To get the next results, call <code>ListResourcePolicies</code> again with this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcePoliciesResponse) -> dict:
    out: dict = {}
    import capo_secrets_manager.types.resource_policy_summary_list_type

    out["ResourcePolicies"] = (
        capo_secrets_manager.types.resource_policy_summary_list_type.serialize_aws_json_1_1(
            value["resource_policies"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcePoliciesResponse:
    out: ListResourcePoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourcePolicies") is not None:
        import capo_secrets_manager.types.resource_policy_summary_list_type

        out["resource_policies"] = (
            capo_secrets_manager.types.resource_policy_summary_list_type.deserialize_aws_json_1_1(
                data["ResourcePolicies"]
            )
        )
    else:
        out["resource_policies"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
