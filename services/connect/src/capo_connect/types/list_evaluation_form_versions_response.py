"""Generated from Smithy shape ``com.amazonaws.connect#ListEvaluationFormVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_version_summary_list
    import capo_connect.types.next_token


class ListEvaluationFormVersionsResponse(TypedDict, closed=True):
    evaluation_form_version_summary_list: "capo_connect.types.evaluation_form_version_summary_list.EvaluationFormVersionSummaryList"
    """<p>Provides details about a list of evaluation forms belonging to an instance.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEvaluationFormVersionsResponse) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_version_summary_list

    out["EvaluationFormVersionSummaryList"] = (
        capo_connect.types.evaluation_form_version_summary_list.serialize_json(
            value["evaluation_form_version_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEvaluationFormVersionsResponse:
    out: ListEvaluationFormVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationFormVersionSummaryList") is not None:
        import capo_connect.types.evaluation_form_version_summary_list

        out["evaluation_form_version_summary_list"] = (
            capo_connect.types.evaluation_form_version_summary_list.deserialize_json(
                data["EvaluationFormVersionSummaryList"]
            )
        )
    else:
        out["evaluation_form_version_summary_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
