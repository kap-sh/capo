"""Generated from Smithy shape ``com.amazonaws.drs#CreateExtendedSourceServerRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.source_server_arn
    import capo_drs.types.tags_map


class CreateExtendedSourceServerRequest(TypedDict, closed=True):
    source_server_arn: "capo_drs.types.source_server_arn.SourceServerARN"
    """<p>This defines the ARN of the source server in staging Account based on which you want to create an extended source server.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>A list of tags associated with the extended source server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExtendedSourceServerRequest) -> dict:
    out: dict = {}
    out["sourceServerArn"] = value["source_server_arn"]
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateExtendedSourceServerRequest:
    out: CreateExtendedSourceServerRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerArn") is not None:
        out["source_server_arn"] = data["sourceServerArn"]
    else:
        out["source_server_arn"] = ""
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateExtendedSourceServerRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
