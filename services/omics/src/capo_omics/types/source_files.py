"""Generated from Smithy shape ``com.amazonaws.omics#SourceFiles``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.s3_uri


class SourceFiles(TypedDict, closed=True):
    source1: "capo_omics.types.s3_uri.S3Uri"
    """<p>The location of the first file in Amazon S3.</p>"""
    source2: NotRequired["capo_omics.types.s3_uri.S3Uri"]
    """<p>The location of the second file in Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceFiles) -> dict:
    out: dict = {}
    out["source1"] = value["source1"]
    if "source2" in value:
        out["source2"] = value["source2"]
    return out


def deserialize_json(data: dict) -> SourceFiles:
    out: SourceFiles = {}  # type: ignore[typeddict-item]
    if data.get("source1") is not None:
        out["source1"] = data["source1"]
    else:
        out["source1"] = ""
    if data.get("source2") is not None:
        out["source2"] = data["source2"]
    return out
