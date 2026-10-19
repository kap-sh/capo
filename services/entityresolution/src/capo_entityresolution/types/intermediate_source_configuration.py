"""Generated from Smithy shape ``com.amazonaws.entityresolution#IntermediateSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.s3_path


class IntermediateSourceConfiguration(TypedDict, closed=True):
    intermediate_s3_path: "capo_entityresolution.types.s3_path.S3Path"
    """<p>The Amazon S3 location (bucket and prefix). For example: <code>s3://provider_bucket/DOC-EXAMPLE-BUCKET</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateSourceConfiguration) -> dict:
    out: dict = {}
    out["intermediateS3Path"] = value["intermediate_s3_path"]
    return out


def deserialize_json(data: dict) -> IntermediateSourceConfiguration:
    out: IntermediateSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("intermediateS3Path") is not None:
        out["intermediate_s3_path"] = data["intermediateS3Path"]
    else:
        out["intermediate_s3_path"] = ""
    return out
