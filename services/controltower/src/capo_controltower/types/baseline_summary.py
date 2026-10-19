"""Generated from Smithy shape ``com.amazonaws.controltower#BaselineSummary``."""

from typing_extensions import NotRequired, TypedDict


class BaselineSummary(TypedDict, closed=True):
    arn: "str"
    """<p>The full ARN of a Baseline.</p>"""
    name: "str"
    """<p>The human-readable name of a Baseline.</p>"""
    description: NotRequired["str"]
    """<p>A summary description of a Baseline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BaselineSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> BaselineSummary:
    out: BaselineSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
