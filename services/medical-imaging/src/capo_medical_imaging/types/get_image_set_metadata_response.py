"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetImageSetMetadataResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.image_set_metadata_blob


class GetImageSetMetadataResponse(TypedDict, closed=True):
    image_set_metadata_blob: (
        "capo_medical_imaging.types.image_set_metadata_blob.ImageSetMetadataBlob"
    )
    """<p>The blob containing the aggregated metadata information for the image set.</p>"""
    content_type: NotRequired["str"]
    """<p>The format in which the study metadata is returned to the customer. Default is <code>text/plain</code>.</p>"""
    content_encoding: NotRequired["str"]
    """<p>The compression format in which image set metadata attributes are returned.</p>"""


def redact_sensitive(value: GetImageSetMetadataResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "image_set_metadata_blob" in value:
        out["image_set_metadata_blob"] = "*** Streaming Data Redacted ***"
    return out
