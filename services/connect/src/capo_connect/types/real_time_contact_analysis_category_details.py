"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisCategoryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_points_of_interest


class RealTimeContactAnalysisCategoryDetails(TypedDict, closed=True):
    points_of_interest: "capo_connect.types.real_time_contact_analysis_points_of_interest.RealTimeContactAnalysisPointsOfInterest"
    """<p>List of PointOfInterest - objects describing a single match of a rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisCategoryDetails) -> dict:
    out: dict = {}
    import capo_connect.types.real_time_contact_analysis_points_of_interest

    out["PointsOfInterest"] = (
        capo_connect.types.real_time_contact_analysis_points_of_interest.serialize_json(
            value["points_of_interest"]
        )
    )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisCategoryDetails:
    out: RealTimeContactAnalysisCategoryDetails = {}  # type: ignore[typeddict-item]
    if data.get("PointsOfInterest") is not None:
        import capo_connect.types.real_time_contact_analysis_points_of_interest

        out["points_of_interest"] = (
            capo_connect.types.real_time_contact_analysis_points_of_interest.deserialize_json(
                data["PointsOfInterest"]
            )
        )
    else:
        out["points_of_interest"] = []
    return out
