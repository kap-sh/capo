"""Generated from Smithy shape ``com.amazonaws.inspector2#CvssScoreAdjustment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string


class CvssScoreAdjustment(TypedDict, closed=True):
    metric: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The metric used to adjust the CVSS score.</p>"""
    reason: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The reason the CVSS score has been adjustment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CvssScoreAdjustment) -> dict:
    out: dict = {}
    out["metric"] = value["metric"]
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> CvssScoreAdjustment:
    out: CvssScoreAdjustment = {}  # type: ignore[typeddict-item]
    if data.get("metric") is not None:
        out["metric"] = data["metric"]
    else:
        out["metric"] = ""
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        out["reason"] = ""
    return out
