"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListProblemsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.pagination_token
    import capo_application_insights.types.problem_list
    import capo_application_insights.types.resource_group_name


class ListProblemsResponse(TypedDict, closed=True):
    problem_list: NotRequired[
        "capo_application_insights.types.problem_list.ProblemList"
    ]
    """<p>The list of problems. </p>"""
    next_token: NotRequired[
        "capo_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The token used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""
    resource_group_name: NotRequired[
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p> The name of the resource group. </p>"""
    account_id: NotRequired["capo_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProblemsResponse) -> dict:
    out: dict = {}
    if "problem_list" in value:
        import capo_application_insights.types.problem_list

        out["ProblemList"] = (
            capo_application_insights.types.problem_list.serialize_aws_json_1_1(
                value["problem_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProblemsResponse:
    out: ListProblemsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProblemList") is not None:
        import capo_application_insights.types.problem_list

        out["problem_list"] = (
            capo_application_insights.types.problem_list.deserialize_aws_json_1_1(
                data["ProblemList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListProblemsResponse) -> dict:
    out: dict = {}
    if "problem_list" in value:
        import capo_application_insights.types.problem_list

        out["ProblemList"] = (
            capo_application_insights.types.problem_list.serialize_cbor(
                value["problem_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_cbor(data: dict) -> ListProblemsResponse:
    out: ListProblemsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProblemList") is not None:
        import capo_application_insights.types.problem_list

        out["problem_list"] = (
            capo_application_insights.types.problem_list.deserialize_cbor(
                data["ProblemList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out
