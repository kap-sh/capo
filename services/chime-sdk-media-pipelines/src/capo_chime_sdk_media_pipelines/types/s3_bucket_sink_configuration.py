"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#S3BucketSinkConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn


class S3BucketSinkConfiguration(TypedDict, closed=True):
    destination: "capo_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The destination URL of the S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketSinkConfiguration) -> dict:
    out: dict = {}
    out["Destination"] = value["destination"]
    return out


def deserialize_json(data: dict) -> S3BucketSinkConfiguration:
    out: S3BucketSinkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Destination") is not None:
        out["destination"] = data["Destination"]
    else:
        out["destination"] = ""
    return out


def redact_sensitive(value: S3BucketSinkConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "destination" in value:
        out["destination"] = "*** Sensitive Data Redacted ***"
    return out
