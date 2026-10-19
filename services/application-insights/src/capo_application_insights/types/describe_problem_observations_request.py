"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeProblemObservationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.problem_id


class DescribeProblemObservationsRequest(TypedDict, closed=True):
    problem_id: "capo_application_insights.types.problem_id.ProblemId"
    """<p>The ID of the problem.</p>"""
    account_id: NotRequired["capo_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProblemObservationsRequest) -> dict:
    out: dict = {}
    out["ProblemId"] = value["problem_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProblemObservationsRequest:
    out: DescribeProblemObservationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProblemId") is not None:
        out["problem_id"] = data["ProblemId"]
    else:
        out["problem_id"] = ""
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out
