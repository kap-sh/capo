"""Generated from Smithy shape ``com.amazonaws.healthlake#TransformationInputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_s3_uri
    import capo_healthlake.types.source_format


class TransformationInputDataConfig(TypedDict, closed=True):
    s3_uri: "capo_healthlake.types.data_transformation_s3_uri.DataTransformationS3Uri"
    """<p>The Amazon S3 URI of the input data to transform.</p>"""
    source_format: NotRequired["capo_healthlake.types.source_format.SourceFormat"]
    """<p>The format of the source data files (C-CDA or CSV).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformationInputDataConfig) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "source_format" in value:
        import capo_healthlake.types.source_format

        out["SourceFormat"] = (
            capo_healthlake.types.source_format.serialize_aws_json_1_0(
                value["source_format"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TransformationInputDataConfig:
    out: TransformationInputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("SourceFormat") is not None:
        import capo_healthlake.types.source_format

        out["source_format"] = (
            capo_healthlake.types.source_format.deserialize_aws_json_1_0(
                data["SourceFormat"]
            )
        )
    return out
