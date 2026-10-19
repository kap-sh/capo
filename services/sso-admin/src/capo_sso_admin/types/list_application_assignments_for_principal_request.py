"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationAssignmentsForPrincipalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.list_application_assignments_filter
    import capo_sso_admin.types.max_results
    import capo_sso_admin.types.principal_id
    import capo_sso_admin.types.principal_type
    import capo_sso_admin.types.token


class ListApplicationAssignmentsForPrincipalRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>Specifies the instance of IAM Identity Center that contains principal and applications.</p>"""
    principal_id: "capo_sso_admin.types.principal_id.PrincipalId"
    """<p>Specifies the unique identifier of the principal for which you want to retrieve its assignments.</p>"""
    principal_type: "capo_sso_admin.types.principal_type.PrincipalType"
    """<p>Specifies the type of the principal for which you want to retrieve its assignments.</p>"""
    filter: NotRequired[
        "capo_sso_admin.types.list_application_assignments_filter.ListApplicationAssignmentsFilter"
    ]
    """<p>Filters the output to include only assignments associated with the application that has the specified ARN.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["capo_sso_admin.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListApplicationAssignmentsForPrincipalRequest,
) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["PrincipalId"] = value["principal_id"]
    import capo_sso_admin.types.principal_type

    out["PrincipalType"] = capo_sso_admin.types.principal_type.serialize_aws_json_1_1(
        value["principal_type"]
    )
    if "filter" in value:
        import capo_sso_admin.types.list_application_assignments_filter

        out["Filter"] = (
            capo_sso_admin.types.list_application_assignments_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListApplicationAssignmentsForPrincipalRequest:
    out: ListApplicationAssignmentsForPrincipalRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        out["instance_arn"] = ""
    if data.get("PrincipalId") is not None:
        out["principal_id"] = data["PrincipalId"]
    else:
        out["principal_id"] = ""
    if data.get("PrincipalType") is not None:
        import capo_sso_admin.types.principal_type

        out["principal_type"] = (
            capo_sso_admin.types.principal_type.deserialize_aws_json_1_1(
                data["PrincipalType"]
            )
        )
    else:
        import typing

        out["principal_type"] = typing.cast(
            "capo_sso_admin.types.principal_type.PrincipalType", ""
        )
    if data.get("Filter") is not None:
        import capo_sso_admin.types.list_application_assignments_filter

        out["filter"] = (
            capo_sso_admin.types.list_application_assignments_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
