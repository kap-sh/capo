"""Generated from Smithy shape ``com.amazonaws.drs#StagingSourceServer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.bounded_string
    import capo_drs.types.source_server_arn
    import capo_drs.types.tags_map


class StagingSourceServer(TypedDict, closed=True):
    hostname: NotRequired["capo_drs.types.bounded_string.BoundedString"]
    """<p>Hostname of staging source server.</p>"""
    arn: NotRequired["capo_drs.types.source_server_arn.SourceServerARN"]
    """<p>The ARN of the source server.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>A list of tags associated with the staging source server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StagingSourceServer) -> dict:
    out: dict = {}
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StagingSourceServer:
    out: StagingSourceServer = {}  # type: ignore[typeddict-item]
    if data.get("hostname") is not None:
        out["hostname"] = data["hostname"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: StagingSourceServer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
