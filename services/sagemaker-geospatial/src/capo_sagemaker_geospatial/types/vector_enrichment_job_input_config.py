"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#VectorEnrichmentJobInputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.vector_enrichment_job_data_source_config_input
    import capo_sagemaker_geospatial.types.vector_enrichment_job_document_type


class VectorEnrichmentJobInputConfig(TypedDict, closed=True):
    document_type: "capo_sagemaker_geospatial.types.vector_enrichment_job_document_type.VectorEnrichmentJobDocumentType"
    """<p>The input structure that defines the data source file type.</p>"""
    data_source_config: "capo_sagemaker_geospatial.types.vector_enrichment_job_data_source_config_input.VectorEnrichmentJobDataSourceConfigInput"
    """<p>The input structure for the data source that represents the storage type of the input data objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorEnrichmentJobInputConfig) -> dict:
    out: dict = {}
    out["DocumentType"] = value["document_type"]
    import capo_sagemaker_geospatial.types.vector_enrichment_job_data_source_config_input

    out["DataSourceConfig"] = (
        capo_sagemaker_geospatial.types.vector_enrichment_job_data_source_config_input.serialize_json(
            value["data_source_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> VectorEnrichmentJobInputConfig:
    out: VectorEnrichmentJobInputConfig = {}  # type: ignore[typeddict-item]
    if data.get("DocumentType") is not None:
        out["document_type"] = data["DocumentType"]
    else:
        out["document_type"] = ""
    if data.get("DataSourceConfig") is not None:
        import capo_sagemaker_geospatial.types.vector_enrichment_job_data_source_config_input

        out["data_source_config"] = (
            capo_sagemaker_geospatial.types.vector_enrichment_job_data_source_config_input.deserialize_json(
                data["DataSourceConfig"]
            )
        )
    else:
        out["data_source_config"] = {"$unknown": {"name": ""}}
    return out
