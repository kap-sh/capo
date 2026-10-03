"""Generated from Smithy shape ``com.amazonaws.dataexchange#RevisionDestinationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.id


class RevisionDestinationEntry(TypedDict, closed=True):
    bucket: "capo_dataexchange.types.__string.__string"
    """<p>The Amazon S3 bucket that is the destination for the assets in the revision.</p>"""
    key_pattern: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>A string representing the pattern for generated names of the individual assets in the revision. For more information about key patterns, see <a href="https://docs.aws.amazon.com/data-exchange/latest/userguide/jobs.html#revision-export-keypatterns">Key patterns when exporting revisions</a>.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevisionDestinationEntry) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    if "key_pattern" in value:
        out["KeyPattern"] = value["key_pattern"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> RevisionDestinationEntry:
    out: RevisionDestinationEntry = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        raise DeserializationError("RevisionDestinationEntry.bucket required")
    if data.get("KeyPattern") is not None:
        out["key_pattern"] = data["KeyPattern"]
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError("RevisionDestinationEntry.revision_id required")
    return out
