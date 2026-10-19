"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewSettings``."""

from typing_extensions import TypedDict


class CodeReviewSettings(TypedDict, closed=True):
    controls_scanning: "bool"
    """<p>Indicates whether controls scanning is enabled for code reviews.</p>"""
    general_purpose_scanning: "bool"
    """<p>Indicates whether general-purpose scanning is enabled for code reviews.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewSettings) -> dict:
    out: dict = {}
    out["controlsScanning"] = value["controls_scanning"]
    out["generalPurposeScanning"] = value["general_purpose_scanning"]
    return out


def deserialize_json(data: dict) -> CodeReviewSettings:
    out: CodeReviewSettings = {}  # type: ignore[typeddict-item]
    if data.get("controlsScanning") is not None:
        out["controls_scanning"] = data["controlsScanning"]
    else:
        out["controls_scanning"] = False
    if data.get("generalPurposeScanning") is not None:
        out["general_purpose_scanning"] = data["generalPurposeScanning"]
    else:
        out["general_purpose_scanning"] = False
    return out
