"""Generated from Smithy shape ``com.amazonaws.connect#ListEvaluationFormsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_summary_list
    import capo_connect.types.next_token


class ListEvaluationFormsResponse(TypedDict, closed=True):
    evaluation_form_summary_list: (
        "capo_connect.types.evaluation_form_summary_list.EvaluationFormSummaryList"
    )
    """<p>Provides details about a list of evaluation forms belonging to an instance.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEvaluationFormsResponse) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_summary_list

    out["EvaluationFormSummaryList"] = (
        capo_connect.types.evaluation_form_summary_list.serialize_json(
            value["evaluation_form_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEvaluationFormsResponse:
    out: ListEvaluationFormsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationFormSummaryList") is not None:
        import capo_connect.types.evaluation_form_summary_list

        out["evaluation_form_summary_list"] = (
            capo_connect.types.evaluation_form_summary_list.deserialize_json(
                data["EvaluationFormSummaryList"]
            )
        )
    else:
        out["evaluation_form_summary_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
