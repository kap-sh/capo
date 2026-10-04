"""Generated from Smithy shape ``com.amazonaws.organizations#ListEffectivePolicyValidationErrorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.account_id
    import capo_organizations.types.effective_policy_type
    import capo_organizations.types.effective_policy_validation_errors
    import capo_organizations.types.next_token
    import capo_organizations.types.path
    import capo_organizations.types.timestamp


class ListEffectivePolicyValidationErrorsResponse(TypedDict, closed=True):
    account_id: NotRequired["capo_organizations.types.account_id.AccountId"]
    """<p>The ID of the specified account.</p>"""
    policy_type: NotRequired[
        "capo_organizations.types.effective_policy_type.EffectivePolicyType"
    ]
    """<p>The specified policy type. One of the following values:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html">DECLARATIVE_POLICY_EC2</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html">BACKUP_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html">TAG_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_chatbot.html">CHATBOT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html">AISERVICES_OPT_OUT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub.html">SECURITYHUB_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_upgrade_rollout.html">UPGRADE_ROLLOUT_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inspector.html">INSPECTOR_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock.html">BEDROCK_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3.html">S3_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_network_security_director.html">NETWORK_SECURITY_DIRECTOR_POLICY</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_guardduty.html">GUARDDUTY_POLICY</a> </p> </li> </ul>"""
    path: NotRequired["capo_organizations.types.path.Path"]
    """<p>The path in the organization where the specified account exists.</p>"""
    evaluation_timestamp: NotRequired["capo_organizations.types.timestamp.Timestamp"]
    """<p>The time when the latest effective policy was generated for the specified account.</p>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""
    effective_policy_validation_errors: NotRequired[
        "capo_organizations.types.effective_policy_validation_errors.EffectivePolicyValidationErrors"
    ]
    """<p>The <code>EffectivePolicyValidationError</code> object contains details about the validation errors that occurred when generating or enforcing an effective policy, such as which policies contributed to the error and location of the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEffectivePolicyValidationErrorsResponse) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "policy_type" in value:
        import capo_organizations.types.effective_policy_type

        out["PolicyType"] = (
            capo_organizations.types.effective_policy_type.serialize_aws_json_1_1(
                value["policy_type"]
            )
        )
    if "path" in value:
        out["Path"] = value["path"]
    if "evaluation_timestamp" in value:
        import capo_organizations.types.timestamp

        out["EvaluationTimestamp"] = (
            capo_organizations.types.timestamp.serialize_aws_json_1_1(
                value["evaluation_timestamp"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "effective_policy_validation_errors" in value:
        import capo_organizations.types.effective_policy_validation_errors

        out["EffectivePolicyValidationErrors"] = (
            capo_organizations.types.effective_policy_validation_errors.serialize_aws_json_1_1(
                value["effective_policy_validation_errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEffectivePolicyValidationErrorsResponse:
    out: ListEffectivePolicyValidationErrorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("PolicyType") is not None:
        import capo_organizations.types.effective_policy_type

        out["policy_type"] = (
            capo_organizations.types.effective_policy_type.deserialize_aws_json_1_1(
                data["PolicyType"]
            )
        )
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("EvaluationTimestamp") is not None:
        import capo_organizations.types.timestamp

        out["evaluation_timestamp"] = (
            capo_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["EvaluationTimestamp"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("EffectivePolicyValidationErrors") is not None:
        import capo_organizations.types.effective_policy_validation_errors

        out["effective_policy_validation_errors"] = (
            capo_organizations.types.effective_policy_validation_errors.deserialize_aws_json_1_1(
                data["EffectivePolicyValidationErrors"]
            )
        )
    return out
