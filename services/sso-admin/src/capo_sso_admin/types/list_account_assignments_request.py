"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListAccountAssignmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.max_results
    import capo_sso_admin.types.permission_set_arn
    import capo_sso_admin.types.target_id
    import capo_sso_admin.types.token


class ListAccountAssignmentsRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    account_id: "capo_sso_admin.types.target_id.TargetId"
    """<p>The identifier of the Amazon Web Services account from which to list the assignments.</p>"""
    permission_set_arn: "capo_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the permission set from which to list assignments.</p>"""
    max_results: NotRequired["capo_sso_admin.types.max_results.MaxResults"]
    """<p>The maximum number of results to display for the assignment.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountAssignmentsRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["AccountId"] = value["account_id"]
    out["PermissionSetArn"] = value["permission_set_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountAssignmentsRequest:
    out: ListAccountAssignmentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "ListAccountAssignmentsRequest.instance_arn required"
        )
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("ListAccountAssignmentsRequest.account_id required")
    if data.get("PermissionSetArn") is not None:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        raise DeserializationError(
            "ListAccountAssignmentsRequest.permission_set_arn required"
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
