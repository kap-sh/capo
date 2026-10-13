"""Generated from Smithy shape ``com.amazonaws.datazone#S3Destination``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.notebook_s3_uri


class S3Destination(TypedDict, closed=True):
    uri: NotRequired["capo_datazone.types.notebook_s3_uri.NotebookS3Uri"]
    """<p>The Amazon Simple Storage Service URI of the exported notebook.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Destination) -> dict:
    out: dict = {}
    if "uri" in value:
        out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    return out


def redact_sensitive(value: S3Destination) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "uri" in value:
        out["uri"] = "*** Sensitive Data Redacted ***"
    return out
