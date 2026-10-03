"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListAccountAssignmentDeletionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.max_results
    import capo_sso_admin.types.operation_status_filter
    import capo_sso_admin.types.token


class ListAccountAssignmentDeletionStatusRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    max_results: NotRequired["capo_sso_admin.types.max_results.MaxResults"]
    """<p>The maximum number of results to display for the assignment.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""
    filter: NotRequired[
        "capo_sso_admin.types.operation_status_filter.OperationStatusFilter"
    ]
    """<p>Filters results based on the passed attribute value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountAssignmentDeletionStatusRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filter" in value:
        import capo_sso_admin.types.operation_status_filter

        out["Filter"] = (
            capo_sso_admin.types.operation_status_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountAssignmentDeletionStatusRequest:
    out: ListAccountAssignmentDeletionStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "ListAccountAssignmentDeletionStatusRequest.instance_arn required"
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filter") is not None:
        import capo_sso_admin.types.operation_status_filter

        out["filter"] = (
            capo_sso_admin.types.operation_status_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    return out
