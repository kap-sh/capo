"""Generated from Smithy shape ``com.amazonaws.inspector2#CvssScoreDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cvss_score_adjustment_list
    import capo_inspector2.types.non_empty_string


class CvssScoreDetails(TypedDict, closed=True):
    score_source: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The source for the CVSS score.</p>"""
    cvss_source: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The source of the CVSS data.</p>"""
    version: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The CVSS version used in scoring.</p>"""
    score: "float"
    """<p>The CVSS score.</p>"""
    scoring_vector: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The vector for the CVSS score.</p>"""
    adjustments: NotRequired[
        "capo_inspector2.types.cvss_score_adjustment_list.CvssScoreAdjustmentList"
    ]
    """<p>An object that contains details about adjustment Amazon Inspector made to the CVSS score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CvssScoreDetails) -> dict:
    out: dict = {}
    out["scoreSource"] = value["score_source"]
    if "cvss_source" in value:
        out["cvssSource"] = value["cvss_source"]
    out["version"] = value["version"]
    out["score"] = (
        "NaN"
        if value["score"] != value["score"]
        else "Infinity"
        if value["score"] == float("inf")
        else "-Infinity"
        if value["score"] == float("-inf")
        else value["score"]
    )
    out["scoringVector"] = value["scoring_vector"]
    if "adjustments" in value:
        import capo_inspector2.types.cvss_score_adjustment_list

        out["adjustments"] = (
            capo_inspector2.types.cvss_score_adjustment_list.serialize_json(
                value["adjustments"]
            )
        )
    return out


def deserialize_json(data: dict) -> CvssScoreDetails:
    out: CvssScoreDetails = {}  # type: ignore[typeddict-item]
    if data.get("scoreSource") is not None:
        out["score_source"] = data["scoreSource"]
    else:
        out["score_source"] = ""
    if data.get("cvssSource") is not None:
        out["cvss_source"] = data["cvssSource"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    else:
        out["score"] = 0.0
    if data.get("scoringVector") is not None:
        out["scoring_vector"] = data["scoringVector"]
    else:
        out["scoring_vector"] = ""
    if data.get("adjustments") is not None:
        import capo_inspector2.types.cvss_score_adjustment_list

        out["adjustments"] = (
            capo_inspector2.types.cvss_score_adjustment_list.deserialize_json(
                data["adjustments"]
            )
        )
    return out
