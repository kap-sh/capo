"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentCategories``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_matched_details


class RealTimeContactAnalysisSegmentCategories(TypedDict, closed=True):
    matched_details: "capo_connect.types.real_time_contact_analysis_matched_details.RealTimeContactAnalysisMatchedDetails"
    """<p>Map between the name of the matched rule and RealTimeContactAnalysisCategoryDetails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentCategories) -> dict:
    out: dict = {}
    import capo_connect.types.real_time_contact_analysis_matched_details

    out["MatchedDetails"] = (
        capo_connect.types.real_time_contact_analysis_matched_details.serialize_json(
            value["matched_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisSegmentCategories:
    out: RealTimeContactAnalysisSegmentCategories = {}  # type: ignore[typeddict-item]
    if data.get("MatchedDetails") is not None:
        import capo_connect.types.real_time_contact_analysis_matched_details

        out["matched_details"] = (
            capo_connect.types.real_time_contact_analysis_matched_details.deserialize_json(
                data["MatchedDetails"]
            )
        )
    else:
        out["matched_details"] = {}
    return out
