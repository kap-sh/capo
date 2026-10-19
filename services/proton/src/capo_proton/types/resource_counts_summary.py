"""Generated from Smithy shape ``com.amazonaws.proton#ResourceCountsSummary``."""

from typing_extensions import NotRequired, TypedDict


class ResourceCountsSummary(TypedDict, closed=True):
    total: "int"
    """<p>The total number of resources of this type in the Amazon Web Services account.</p>"""
    failed: NotRequired["int"]
    """<p>The number of resources of this type in the Amazon Web Services account that failed to deploy.</p>"""
    up_to_date: NotRequired["int"]
    """<p>The number of resources of this type in the Amazon Web Services account that are up-to-date with their template.</p>"""
    behind_major: NotRequired["int"]
    """<p>The number of resources of this type in the Amazon Web Services account that need a major template version update.</p>"""
    behind_minor: NotRequired["int"]
    """<p>The number of resources of this type in the Amazon Web Services account that need a minor template version update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceCountsSummary) -> dict:
    out: dict = {}
    out["total"] = value["total"]
    if "failed" in value:
        out["failed"] = value["failed"]
    if "up_to_date" in value:
        out["upToDate"] = value["up_to_date"]
    if "behind_major" in value:
        out["behindMajor"] = value["behind_major"]
    if "behind_minor" in value:
        out["behindMinor"] = value["behind_minor"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceCountsSummary:
    out: ResourceCountsSummary = {}  # type: ignore[typeddict-item]
    if data.get("total") is not None:
        out["total"] = data["total"]
    else:
        out["total"] = 0
    if data.get("failed") is not None:
        out["failed"] = data["failed"]
    if data.get("upToDate") is not None:
        out["up_to_date"] = data["upToDate"]
    if data.get("behindMajor") is not None:
        out["behind_major"] = data["behindMajor"]
    if data.get("behindMinor") is not None:
        out["behind_minor"] = data["behindMinor"]
    return out
