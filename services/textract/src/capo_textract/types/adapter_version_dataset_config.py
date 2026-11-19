"""Generated from Smithy shape ``com.amazonaws.textract#AdapterVersionDatasetConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.s3_object


class AdapterVersionDatasetConfig(TypedDict, closed=True):
    manifest_s3_object: NotRequired["capo_textract.types.s3_object.S3Object"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdapterVersionDatasetConfig) -> dict:
    out: dict = {}
    if "manifest_s3_object" in value:
        import capo_textract.types.s3_object

        out["ManifestS3Object"] = capo_textract.types.s3_object.serialize_aws_json_1_1(
            value["manifest_s3_object"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdapterVersionDatasetConfig:
    out: AdapterVersionDatasetConfig = {}  # type: ignore[typeddict-item]
    if data.get("ManifestS3Object") is not None:
        import capo_textract.types.s3_object

        out["manifest_s3_object"] = (
            capo_textract.types.s3_object.deserialize_aws_json_1_1(
                data["ManifestS3Object"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AdapterVersionDatasetConfig) -> dict:
    out: dict = {}
    if "manifest_s3_object" in value:
        import capo_textract.types.s3_object

        out["ManifestS3Object"] = capo_textract.types.s3_object.serialize_cbor(
            value["manifest_s3_object"]
        )
    return out


def deserialize_cbor(data: dict) -> AdapterVersionDatasetConfig:
    out: AdapterVersionDatasetConfig = {}  # type: ignore[typeddict-item]
    if data.get("ManifestS3Object") is not None:
        import capo_textract.types.s3_object

        out["manifest_s3_object"] = capo_textract.types.s3_object.deserialize_cbor(
            data["ManifestS3Object"]
        )
    return out
