"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAnalysisResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.analysis
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeAnalysisResponse(TypedDict, closed=True):
    analysis: NotRequired["capo_quicksight.types.analysis.Analysis"]
    """<p>A metadata structure that contains summary information for the analysis that you're describing.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAnalysisResponse) -> dict:
    out: dict = {}
    if "analysis" in value:
        import capo_quicksight.types.analysis

        out["Analysis"] = capo_quicksight.types.analysis.serialize_json(
            value["analysis"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAnalysisResponse:
    out: DescribeAnalysisResponse = {}  # type: ignore[typeddict-item]
    if data.get("Analysis") is not None:
        import capo_quicksight.types.analysis

        out["analysis"] = capo_quicksight.types.analysis.deserialize_json(
            data["Analysis"]
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: DescribeAnalysisResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "analysis" in value:
        import capo_quicksight.types.analysis

        out["analysis"] = capo_quicksight.types.analysis.redact_sensitive(
            value["analysis"]
        )
    return out
