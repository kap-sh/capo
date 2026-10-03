"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ZonalStatisticsConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.kms_key
    import capo_sagemaker_geospatial.types.s3_uri
    import capo_sagemaker_geospatial.types.string_list_input
    import capo_sagemaker_geospatial.types.zonal_statistics_list_input


class ZonalStatisticsConfigInput(TypedDict, closed=True):
    zone_s3_path: "capo_sagemaker_geospatial.types.s3_uri.S3Uri"
    """<p>The Amazon S3 path pointing to the GeoJSON containing the polygonal zones.</p>"""
    statistics: "capo_sagemaker_geospatial.types.zonal_statistics_list_input.ZonalStatisticsListInput"
    """<p>List of zonal statistics to compute.</p>"""
    target_bands: NotRequired[
        "capo_sagemaker_geospatial.types.string_list_input.StringListInput"
    ]
    """<p>Bands used in the operation. If no target bands are specified, it uses all bands available input.</p>"""
    zone_s3_path_kms_key_id: NotRequired[
        "capo_sagemaker_geospatial.types.kms_key.KmsKey"
    ]
    """<p>The Amazon Resource Name (ARN) or an ID of a Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to decrypt your output artifacts with Amazon S3 server-side encryption. The SageMaker execution role must have <code>kms:GenerateDataKey</code> permission.</p> <p>The <code>KmsKeyId</code> can be any of the following formats:</p> <ul> <li> <p>// KMS Key ID</p> <p> <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>// Amazon Resource Name (ARN) of a KMS Key</p> <p> <code>"arn:aws:kms:&lt;region&gt;:&lt;account&gt;:key/&lt;key-id-12ab-34cd-56ef-1234567890ab&gt;"</code> </p> </li> </ul> <p>For more information about key identifiers, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id">Key identifiers (KeyID)</a> in the Amazon Web Services Key Management Service (Amazon Web Services KMS) documentation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ZonalStatisticsConfigInput) -> dict:
    out: dict = {}
    out["ZoneS3Path"] = value["zone_s3_path"]
    import capo_sagemaker_geospatial.types.zonal_statistics_list_input

    out["Statistics"] = (
        capo_sagemaker_geospatial.types.zonal_statistics_list_input.serialize_json(
            value["statistics"]
        )
    )
    if "target_bands" in value:
        import capo_sagemaker_geospatial.types.string_list_input

        out["TargetBands"] = (
            capo_sagemaker_geospatial.types.string_list_input.serialize_json(
                value["target_bands"]
            )
        )
    if "zone_s3_path_kms_key_id" in value:
        out["ZoneS3PathKmsKeyId"] = value["zone_s3_path_kms_key_id"]
    return out


def deserialize_json(data: dict) -> ZonalStatisticsConfigInput:
    out: ZonalStatisticsConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("ZoneS3Path") is not None:
        out["zone_s3_path"] = data["ZoneS3Path"]
    else:
        raise DeserializationError("ZonalStatisticsConfigInput.zone_s3_path required")
    if data.get("Statistics") is not None:
        import capo_sagemaker_geospatial.types.zonal_statistics_list_input

        out["statistics"] = (
            capo_sagemaker_geospatial.types.zonal_statistics_list_input.deserialize_json(
                data["Statistics"]
            )
        )
    else:
        raise DeserializationError("ZonalStatisticsConfigInput.statistics required")
    if data.get("TargetBands") is not None:
        import capo_sagemaker_geospatial.types.string_list_input

        out["target_bands"] = (
            capo_sagemaker_geospatial.types.string_list_input.deserialize_json(
                data["TargetBands"]
            )
        )
    if data.get("ZoneS3PathKmsKeyId") is not None:
        out["zone_s3_path_kms_key_id"] = data["ZoneS3PathKmsKeyId"]
    return out
