"""Generated from Smithy shape ``com.amazonaws.amp#ListAnomalyDetectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.anomaly_detector_summary_list
    import capo_amp.types.pagination_token


class ListAnomalyDetectorsResponse(TypedDict, closed=True):
    anomaly_detectors: (
        "capo_amp.types.anomaly_detector_summary_list.AnomalyDetectorSummaryList"
    )
    """<p>The list of anomaly detectors in the workspace.</p>"""
    next_token: NotRequired["capo_amp.types.pagination_token.PaginationToken"]
    """<p>The pagination token to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnomalyDetectorsResponse) -> dict:
    out: dict = {}
    import capo_amp.types.anomaly_detector_summary_list

    out["anomalyDetectors"] = (
        capo_amp.types.anomaly_detector_summary_list.serialize_json(
            value["anomaly_detectors"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnomalyDetectorsResponse:
    out: ListAnomalyDetectorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("anomalyDetectors") is not None:
        import capo_amp.types.anomaly_detector_summary_list

        out["anomaly_detectors"] = (
            capo_amp.types.anomaly_detector_summary_list.deserialize_json(
                data["anomalyDetectors"]
            )
        )
    else:
        out["anomaly_detectors"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
