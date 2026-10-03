"""Generated from Smithy shape ``com.amazonaws.dataexchange#AutoExportRevisionDestinationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.__string


class AutoExportRevisionDestinationEntry(TypedDict, closed=True):
    bucket: "capo_dataexchange.types.__string.__string"
    """<p>The Amazon S3 bucket that is the destination for the event action.</p>"""
    key_pattern: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>A string representing the pattern for generated names of the individual assets in the revision. For more information about key patterns, see <a href="https://docs.aws.amazon.com/data-exchange/latest/userguide/jobs.html#revision-export-keypatterns">Key patterns when exporting revisions</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoExportRevisionDestinationEntry) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    if "key_pattern" in value:
        out["KeyPattern"] = value["key_pattern"]
    return out


def deserialize_json(data: dict) -> AutoExportRevisionDestinationEntry:
    out: AutoExportRevisionDestinationEntry = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        raise DeserializationError("AutoExportRevisionDestinationEntry.bucket required")
    if data.get("KeyPattern") is not None:
        out["key_pattern"] = data["KeyPattern"]
    return out
