"""Generated from Smithy shape ``com.amazonaws.inspector2#CvssScore``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string


class CvssScore(TypedDict, closed=True):
    base_score: "float"
    """<p>The base CVSS score used for the finding.</p>"""
    scoring_vector: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The vector string of the CVSS score.</p>"""
    version: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The version of CVSS used for the score.</p>"""
    source: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The source of the CVSS score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CvssScore) -> dict:
    out: dict = {}
    out["baseScore"] = (
        "NaN"
        if value["base_score"] != value["base_score"]
        else "Infinity"
        if value["base_score"] == float("inf")
        else "-Infinity"
        if value["base_score"] == float("-inf")
        else value["base_score"]
    )
    out["scoringVector"] = value["scoring_vector"]
    out["version"] = value["version"]
    out["source"] = value["source"]
    return out


def deserialize_json(data: dict) -> CvssScore:
    out: CvssScore = {}  # type: ignore[typeddict-item]
    if data.get("baseScore") is not None:
        out["base_score"] = float(data["baseScore"])
    else:
        out["base_score"] = 0.0
    if data.get("scoringVector") is not None:
        out["scoring_vector"] = data["scoringVector"]
    else:
        out["scoring_vector"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    return out
