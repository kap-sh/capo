"""Generated from Smithy shape ``com.amazonaws.omics#VariantImportItemSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.s3_uri


class VariantImportItemSource(TypedDict, closed=True):
    source: "capo_omics.types.s3_uri.S3Uri"
    """<p>The source file's location in Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VariantImportItemSource) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    return out


def deserialize_json(data: dict) -> VariantImportItemSource:
    out: VariantImportItemSource = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    return out
