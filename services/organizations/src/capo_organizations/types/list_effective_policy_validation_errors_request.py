"""Generated from Smithy shape ``com.amazonaws.organizations#ListEffectivePolicyValidationErrorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.account_id
    import capo_organizations.types.effective_policy_type
    import capo_organizations.types.max_results
    import capo_organizations.types.next_token


class ListEffectivePolicyValidationErrorsRequest(TypedDict, closed=True):
    account_id: "capo_organizations.types.account_id.AccountId"
    """<p>The ID of the account that you want details about. Specifying an organization root or organizational unit (OU) as the target is not supported.</p>"""
    policy_type: "capo_organizations.types.effective_policy_type.EffectivePolicyType"
    """<p>The type of policy that you want information about. You can specify one of the following values:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html">DECLARATIVE_POLICY_EC2</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html">BACKUP_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html">TAG_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_chatbot.html">CHATBOT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html">AISERVICES_OPT_OUT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub.html">SECURITYHUB_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_upgrade_rollout.html">UPGRADE_ROLLOUT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inspector.html">INSPECTOR_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock.html">BEDROCK_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3.html">S3_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_network_security_director.html">NETWORK_SECURITY_DIRECTOR_POLICY</a> </p> </li> </ul>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""
    max_results: NotRequired["capo_organizations.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEffectivePolicyValidationErrorsRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    import capo_organizations.types.effective_policy_type

    out["PolicyType"] = (
        capo_organizations.types.effective_policy_type.serialize_aws_json_1_1(
            value["policy_type"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEffectivePolicyValidationErrorsRequest:
    out: ListEffectivePolicyValidationErrorsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "ListEffectivePolicyValidationErrorsRequest.account_id required"
        )
    if data.get("PolicyType") is not None:
        import capo_organizations.types.effective_policy_type

        out["policy_type"] = (
            capo_organizations.types.effective_policy_type.deserialize_aws_json_1_1(
                data["PolicyType"]
            )
        )
    else:
        raise DeserializationError(
            "ListEffectivePolicyValidationErrorsRequest.policy_type required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
