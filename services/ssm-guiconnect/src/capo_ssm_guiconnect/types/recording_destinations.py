"""Generated from Smithy shape ``com.amazonaws.ssmguiconnect#RecordingDestinations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_guiconnect.types.s3_buckets


class RecordingDestinations(TypedDict, closed=True):
    s3_buckets: "capo_ssm_guiconnect.types.s3_buckets.S3Buckets"
    """<p>The S3 bucket where RDP connection recordings are stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecordingDestinations) -> dict:
    out: dict = {}
    import capo_ssm_guiconnect.types.s3_buckets

    out["S3Buckets"] = capo_ssm_guiconnect.types.s3_buckets.serialize_json(
        value["s3_buckets"]
    )
    return out


def deserialize_json(data: dict) -> RecordingDestinations:
    out: RecordingDestinations = {}  # type: ignore[typeddict-item]
    if data.get("S3Buckets") is not None:
        import capo_ssm_guiconnect.types.s3_buckets

        out["s3_buckets"] = capo_ssm_guiconnect.types.s3_buckets.deserialize_json(
            data["S3Buckets"]
        )
    else:
        out["s3_buckets"] = []
    return out
