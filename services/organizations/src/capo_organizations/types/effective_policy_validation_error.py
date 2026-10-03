"""Generated from Smithy shape ``com.amazonaws.organizations#EffectivePolicyValidationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.error_code
    import capo_organizations.types.error_message
    import capo_organizations.types.path_to_error
    import capo_organizations.types.policy_ids


class EffectivePolicyValidationError(TypedDict, closed=True):
    error_code: NotRequired["capo_organizations.types.error_code.ErrorCode"]
    """<p>The error code for the validation error. For example, <code>ELEMENTS_TOO_MANY</code>.</p>"""
    error_message: NotRequired["capo_organizations.types.error_message.ErrorMessage"]
    """<p>The error message for the validation error.</p>"""
    path_to_error: NotRequired["capo_organizations.types.path_to_error.PathToError"]
    """<p>The path within the effective policy where the validation error occurred.</p>"""
    contributing_policies: NotRequired["capo_organizations.types.policy_ids.PolicyIds"]
    """<p>The individual policies <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.html">inherited</a> and <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_attach.html">attached</a> to the account which contributed to the validation error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EffectivePolicyValidationError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "path_to_error" in value:
        out["PathToError"] = value["path_to_error"]
    if "contributing_policies" in value:
        import capo_organizations.types.policy_ids

        out["ContributingPolicies"] = (
            capo_organizations.types.policy_ids.serialize_aws_json_1_1(
                value["contributing_policies"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EffectivePolicyValidationError:
    out: EffectivePolicyValidationError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("PathToError") is not None:
        out["path_to_error"] = data["PathToError"]
    if data.get("ContributingPolicies") is not None:
        import capo_organizations.types.policy_ids

        out["contributing_policies"] = (
            capo_organizations.types.policy_ids.deserialize_aws_json_1_1(
                data["ContributingPolicies"]
            )
        )
    return out
