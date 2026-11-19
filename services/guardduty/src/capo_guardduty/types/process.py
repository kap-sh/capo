"""Generated from Smithy shape ``com.amazonaws.guardduty#Process``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.finding_references
    import capo_guardduty.types.string


class Process(TypedDict, closed=True):
    uuid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique identifier of the process.</p>"""
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the process.</p>"""
    path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The path of the process executable.</p>"""
    parent_uuid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique identifier of the parent process. Not set for the root process.</p>"""
    findings: NotRequired["capo_guardduty.types.finding_references.FindingReferences"]
    """<p>The findings associated with this process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Process) -> dict:
    out: dict = {}
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    if "name" in value:
        out["name"] = value["name"]
    if "path" in value:
        out["path"] = value["path"]
    if "parent_uuid" in value:
        out["parentUuid"] = value["parent_uuid"]
    if "findings" in value:
        import capo_guardduty.types.finding_references

        out["findings"] = capo_guardduty.types.finding_references.serialize_json(
            value["findings"]
        )
    return out


def deserialize_json(data: dict) -> Process:
    out: Process = {}  # type: ignore[typeddict-item]
    if data.get("uuid") is not None:
        out["uuid"] = data["uuid"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("path") is not None:
        out["path"] = data["path"]
    if data.get("parentUuid") is not None:
        out["parent_uuid"] = data["parentUuid"]
    if data.get("findings") is not None:
        import capo_guardduty.types.finding_references

        out["findings"] = capo_guardduty.types.finding_references.deserialize_json(
            data["findings"]
        )
    return out
