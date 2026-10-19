"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#S3DestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.s3_destination_location


class S3DestinationConfiguration(TypedDict, closed=True):
    location: "capo_iottwinmaker.types.s3_destination_location.S3DestinationLocation"
    """<p>The S3 destination configuration location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DestinationConfiguration) -> dict:
    out: dict = {}
    out["location"] = value["location"]
    return out


def deserialize_json(data: dict) -> S3DestinationConfiguration:
    out: S3DestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        out["location"] = ""
    return out
