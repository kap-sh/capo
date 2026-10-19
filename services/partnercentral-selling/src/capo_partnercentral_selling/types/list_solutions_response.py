"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListSolutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.solution_list


class ListSolutionsResponse(TypedDict, closed=True):
    solution_summaries: "capo_partnercentral_selling.types.solution_list.SolutionList"
    """<p>An array with minimal details for solutions matching the request criteria.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSolutionsResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.solution_list

    out["SolutionSummaries"] = (
        capo_partnercentral_selling.types.solution_list.serialize_aws_json_1_0(
            value["solution_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSolutionsResponse:
    out: ListSolutionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("SolutionSummaries") is not None:
        import capo_partnercentral_selling.types.solution_list

        out["solution_summaries"] = (
            capo_partnercentral_selling.types.solution_list.deserialize_aws_json_1_0(
                data["SolutionSummaries"]
            )
        )
    else:
        out["solution_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
