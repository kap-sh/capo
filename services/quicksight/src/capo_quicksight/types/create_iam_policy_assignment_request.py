"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateIAMPolicyAssignmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.assignment_status
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.iam_policy_assignment_name
    import capo_quicksight.types.identity_map
    import capo_quicksight.types.namespace


class CreateIAMPolicyAssignmentRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account where you want to assign an IAM policy to Amazon Quick Sight users or groups.</p>"""
    assignment_name: (
        "capo_quicksight.types.iam_policy_assignment_name.IAMPolicyAssignmentName"
    )
    """<p>The name of the assignment, also called a rule. The name must be unique within the Amazon Web Services account.</p>"""
    assignment_status: "capo_quicksight.types.assignment_status.AssignmentStatus"
    """<p>The status of the assignment. Possible values are as follows:</p> <ul> <li> <p> <code>ENABLED</code> - Anything specified in this assignment is used when creating the data source.</p> </li> <li> <p> <code>DISABLED</code> - This assignment isn't used when creating the data source.</p> </li> <li> <p> <code>DRAFT</code> - This assignment is an unfinished draft and isn't used when creating the data source.</p> </li> </ul>"""
    policy_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN for the IAM policy to apply to the Amazon Quick Sight users and groups specified in this assignment.</p>"""
    identities: NotRequired["capo_quicksight.types.identity_map.IdentityMap"]
    """<p>The Amazon Quick Sight users, groups, or both that you want to assign the policy to.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace that contains the assignment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIAMPolicyAssignmentRequest) -> dict:
    out: dict = {}
    out["AssignmentName"] = value["assignment_name"]
    import capo_quicksight.types.assignment_status

    out["AssignmentStatus"] = capo_quicksight.types.assignment_status.serialize_json(
        value["assignment_status"]
    )
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    if "identities" in value:
        import capo_quicksight.types.identity_map

        out["Identities"] = capo_quicksight.types.identity_map.serialize_json(
            value["identities"]
        )
    return out


def deserialize_json(data: dict) -> CreateIAMPolicyAssignmentRequest:
    out: CreateIAMPolicyAssignmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssignmentName") is not None:
        out["assignment_name"] = data["AssignmentName"]
    else:
        out["assignment_name"] = ""
    if data.get("AssignmentStatus") is not None:
        import capo_quicksight.types.assignment_status

        out["assignment_status"] = (
            capo_quicksight.types.assignment_status.deserialize_json(
                data["AssignmentStatus"]
            )
        )
    else:
        import typing

        out["assignment_status"] = typing.cast(
            "capo_quicksight.types.assignment_status.AssignmentStatus", ""
        )
    if data.get("PolicyArn") is not None:
        out["policy_arn"] = data["PolicyArn"]
    if data.get("Identities") is not None:
        import capo_quicksight.types.identity_map

        out["identities"] = capo_quicksight.types.identity_map.deserialize_json(
            data["Identities"]
        )
    return out
