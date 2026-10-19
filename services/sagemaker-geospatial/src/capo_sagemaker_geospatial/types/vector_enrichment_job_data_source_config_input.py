"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#VectorEnrichmentJobDataSourceConfigInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError, SerializationError
from capo_sagemaker_geospatial.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.vector_enrichment_job_s3_data


class _VectorEnrichmentJobDataSourceConfigInput_S3Data(TypedDict, closed=True):
    S3Data: "capo_sagemaker_geospatial.types.vector_enrichment_job_s3_data.VectorEnrichmentJobS3Data"


VectorEnrichmentJobDataSourceConfigInput: TypeAlias = (
    _VectorEnrichmentJobDataSourceConfigInput_S3Data | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: VectorEnrichmentJobDataSourceConfigInput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"VectorEnrichmentJobDataSourceConfigInput: cannot serialize unknown variant {value.name!r}"
        )
    elif "S3Data" in value:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_s3_data

        return {
            "S3Data": capo_sagemaker_geospatial.types.vector_enrichment_job_s3_data.serialize_json(
                value["S3Data"]
            )
        }
    else:
        raise SerializationError(
            "VectorEnrichmentJobDataSourceConfigInput: no variant present"
        )


def deserialize_json(data: dict) -> VectorEnrichmentJobDataSourceConfigInput:
    if data.get("S3Data") is not None:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_s3_data

        return {
            "S3Data": capo_sagemaker_geospatial.types.vector_enrichment_job_s3_data.deserialize_json(
                data["S3Data"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "VectorEnrichmentJobDataSourceConfigInput: no recognized variant key"
        )
