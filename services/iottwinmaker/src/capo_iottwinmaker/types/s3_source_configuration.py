"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#S3SourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.s3_source_location


class S3SourceConfiguration(TypedDict, closed=True):
    location: "capo_iottwinmaker.types.s3_source_location.S3SourceLocation"
    """<p>The S3 destination source configuration location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3SourceConfiguration) -> dict:
    out: dict = {}
    out["location"] = value["location"]
    return out


def deserialize_json(data: dict) -> S3SourceConfiguration:
    out: S3SourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        out["location"] = ""
    return out
