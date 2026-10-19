"""Generated from Smithy shape ``com.amazonaws.connect#ListContactEvaluationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_summary_list
    import capo_connect.types.next_token


class ListContactEvaluationsResponse(TypedDict, closed=True):
    evaluation_summary_list: (
        "capo_connect.types.evaluation_summary_list.EvaluationSummaryList"
    )
    """<p>Provides details about a list of contact evaluations belonging to an instance.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p> <important> <p>This is always returned as null in the response.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactEvaluationsResponse) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_summary_list

    out["EvaluationSummaryList"] = (
        capo_connect.types.evaluation_summary_list.serialize_json(
            value["evaluation_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContactEvaluationsResponse:
    out: ListContactEvaluationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationSummaryList") is not None:
        import capo_connect.types.evaluation_summary_list

        out["evaluation_summary_list"] = (
            capo_connect.types.evaluation_summary_list.deserialize_json(
                data["EvaluationSummaryList"]
            )
        )
    else:
        out["evaluation_summary_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
