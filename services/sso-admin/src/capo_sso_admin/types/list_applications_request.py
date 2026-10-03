"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.list_applications_filter
    import capo_sso_admin.types.max_results
    import capo_sso_admin.types.token


class ListApplicationsRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center application under which the operation will run. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    max_results: NotRequired["capo_sso_admin.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    filter: NotRequired[
        "capo_sso_admin.types.list_applications_filter.ListApplicationsFilter"
    ]
    """<p>Filters response results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filter" in value:
        import capo_sso_admin.types.list_applications_filter

        out["Filter"] = (
            capo_sso_admin.types.list_applications_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("ListApplicationsRequest.instance_arn required")
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filter") is not None:
        import capo_sso_admin.types.list_applications_filter

        out["filter"] = (
            capo_sso_admin.types.list_applications_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    return out
