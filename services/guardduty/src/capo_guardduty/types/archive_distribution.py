"""Generated from Smithy shape ``com.amazonaws.guardduty#ArchiveDistribution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.percentage


class ArchiveDistribution(TypedDict, closed=True):
    archived_count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of archived findings.</p>"""
    unarchived_count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of unarchived findings.</p>"""
    archived_percentage: NotRequired["capo_guardduty.types.percentage.Percentage"]
    """<p>The percentage of findings that are archived, from 0 to 100.</p>"""
    unarchived_percentage: NotRequired["capo_guardduty.types.percentage.Percentage"]
    """<p>The percentage of findings that are unarchived, from 0 to 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveDistribution) -> dict:
    out: dict = {}
    if "archived_count" in value:
        out["archivedCount"] = value["archived_count"]
    if "unarchived_count" in value:
        out["unarchivedCount"] = value["unarchived_count"]
    if "archived_percentage" in value:
        out["archivedPercentage"] = (
            "NaN"
            if value["archived_percentage"] != value["archived_percentage"]
            else "Infinity"
            if value["archived_percentage"] == float("inf")
            else "-Infinity"
            if value["archived_percentage"] == float("-inf")
            else value["archived_percentage"]
        )
    if "unarchived_percentage" in value:
        out["unarchivedPercentage"] = (
            "NaN"
            if value["unarchived_percentage"] != value["unarchived_percentage"]
            else "Infinity"
            if value["unarchived_percentage"] == float("inf")
            else "-Infinity"
            if value["unarchived_percentage"] == float("-inf")
            else value["unarchived_percentage"]
        )
    return out


def deserialize_json(data: dict) -> ArchiveDistribution:
    out: ArchiveDistribution = {}  # type: ignore[typeddict-item]
    if data.get("archivedCount") is not None:
        out["archived_count"] = data["archivedCount"]
    if data.get("unarchivedCount") is not None:
        out["unarchived_count"] = data["unarchivedCount"]
    if data.get("archivedPercentage") is not None:
        out["archived_percentage"] = float(data["archivedPercentage"])
    if data.get("unarchivedPercentage") is not None:
        out["unarchived_percentage"] = float(data["unarchivedPercentage"])
    return out
