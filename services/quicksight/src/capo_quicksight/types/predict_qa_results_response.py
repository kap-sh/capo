"""Generated from Smithy shape ``com.amazonaws.quicksight#PredictQAResultsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.qa_result
    import capo_quicksight.types.qa_results
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class PredictQAResultsResponse(TypedDict, closed=True):
    primary_result: NotRequired["capo_quicksight.types.qa_result.QAResult"]
    """<p>The primary visual response.</p>"""
    additional_results: NotRequired["capo_quicksight.types.qa_results.QAResults"]
    """<p>Additional visual responses.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictQAResultsResponse) -> dict:
    out: dict = {}
    if "primary_result" in value:
        import capo_quicksight.types.qa_result

        out["PrimaryResult"] = capo_quicksight.types.qa_result.serialize_json(
            value["primary_result"]
        )
    if "additional_results" in value:
        import capo_quicksight.types.qa_results

        out["AdditionalResults"] = capo_quicksight.types.qa_results.serialize_json(
            value["additional_results"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> PredictQAResultsResponse:
    out: PredictQAResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryResult") is not None:
        import capo_quicksight.types.qa_result

        out["primary_result"] = capo_quicksight.types.qa_result.deserialize_json(
            data["PrimaryResult"]
        )
    if data.get("AdditionalResults") is not None:
        import capo_quicksight.types.qa_results

        out["additional_results"] = capo_quicksight.types.qa_results.deserialize_json(
            data["AdditionalResults"]
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: PredictQAResultsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_result" in value:
        import capo_quicksight.types.qa_result

        out["primary_result"] = capo_quicksight.types.qa_result.redact_sensitive(
            value["primary_result"]
        )
    if "additional_results" in value:
        import capo_quicksight.types.qa_results

        out["additional_results"] = capo_quicksight.types.qa_results.redact_sensitive(
            value["additional_results"]
        )
    return out
