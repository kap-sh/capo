"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisLogExportS3OutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.key_prefix


class AnalysisLogExportS3OutputConfiguration(TypedDict, closed=True):
    bucket: "str"
    """<p>The S3 bucket that the exported analysis logs are written to. The bucket must be in the same Amazon Web Services Region as the collaboration.</p>"""
    key_prefix: NotRequired["capo_cleanrooms.types.key_prefix.KeyPrefix"]
    """<p>The S3 key prefix under which the exported analysis logs are written.</p> <p>Only one export can be in progress at a time for a given query and destination. To export the same query twice at once, use a different key prefix for the second export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisLogExportS3OutputConfiguration) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    return out


def deserialize_json(data: dict) -> AnalysisLogExportS3OutputConfiguration:
    out: AnalysisLogExportS3OutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("keyPrefix") is not None:
        out["key_prefix"] = data["keyPrefix"]
    return out
