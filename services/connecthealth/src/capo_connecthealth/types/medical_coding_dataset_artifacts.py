"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalCodingDatasetArtifacts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.s3_uri


class MedicalCodingDatasetArtifacts(TypedDict, closed=True):
    evaluation_s3_uri: NotRequired["capo_connecthealth.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 location, under the s3OutputPath of the dataset, of the evaluation scores for the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalCodingDatasetArtifacts) -> dict:
    out: dict = {}
    if "evaluation_s3_uri" in value:
        out["evaluationS3Uri"] = value["evaluation_s3_uri"]
    return out


def deserialize_json(data: dict) -> MedicalCodingDatasetArtifacts:
    out: MedicalCodingDatasetArtifacts = {}  # type: ignore[typeddict-item]
    if data.get("evaluationS3Uri") is not None:
        out["evaluation_s3_uri"] = data["evaluationS3Uri"]
    return out
