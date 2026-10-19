"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_dataset_source_configuration
    import capo_supplychain.types.data_integration_flow_s3_source_configuration
    import capo_supplychain.types.data_integration_flow_source_name
    import capo_supplychain.types.data_integration_flow_source_type


class DataIntegrationFlowSource(TypedDict, closed=True):
    source_type: "capo_supplychain.types.data_integration_flow_source_type.DataIntegrationFlowSourceType"
    """<p>The DataIntegrationFlow source type.</p>"""
    source_name: "capo_supplychain.types.data_integration_flow_source_name.DataIntegrationFlowSourceName"
    """<p>The DataIntegrationFlow source name that can be used as table alias in SQL transformation query.</p>"""
    s3_source: NotRequired[
        "capo_supplychain.types.data_integration_flow_s3_source_configuration.DataIntegrationFlowS3SourceConfiguration"
    ]
    """<p>The S3 DataIntegrationFlow source.</p>"""
    dataset_source: NotRequired[
        "capo_supplychain.types.data_integration_flow_dataset_source_configuration.DataIntegrationFlowDatasetSourceConfiguration"
    ]
    """<p>The dataset DataIntegrationFlow source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowSource) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_flow_source_type

    out["sourceType"] = (
        capo_supplychain.types.data_integration_flow_source_type.serialize_json(
            value["source_type"]
        )
    )
    out["sourceName"] = value["source_name"]
    if "s3_source" in value:
        import capo_supplychain.types.data_integration_flow_s3_source_configuration

        out["s3Source"] = (
            capo_supplychain.types.data_integration_flow_s3_source_configuration.serialize_json(
                value["s3_source"]
            )
        )
    if "dataset_source" in value:
        import capo_supplychain.types.data_integration_flow_dataset_source_configuration

        out["datasetSource"] = (
            capo_supplychain.types.data_integration_flow_dataset_source_configuration.serialize_json(
                value["dataset_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowSource:
    out: DataIntegrationFlowSource = {}  # type: ignore[typeddict-item]
    if data.get("sourceType") is not None:
        import capo_supplychain.types.data_integration_flow_source_type

        out["source_type"] = (
            capo_supplychain.types.data_integration_flow_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_supplychain.types.data_integration_flow_source_type.DataIntegrationFlowSourceType",
            "",
        )
    if data.get("sourceName") is not None:
        out["source_name"] = data["sourceName"]
    else:
        out["source_name"] = ""
    if data.get("s3Source") is not None:
        import capo_supplychain.types.data_integration_flow_s3_source_configuration

        out["s3_source"] = (
            capo_supplychain.types.data_integration_flow_s3_source_configuration.deserialize_json(
                data["s3Source"]
            )
        )
    if data.get("datasetSource") is not None:
        import capo_supplychain.types.data_integration_flow_dataset_source_configuration

        out["dataset_source"] = (
            capo_supplychain.types.data_integration_flow_dataset_source_configuration.deserialize_json(
                data["datasetSource"]
            )
        )
    return out
