"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_dataset_target_configuration
    import capo_supplychain.types.data_integration_flow_s3_target_configuration
    import capo_supplychain.types.data_integration_flow_target_type


class DataIntegrationFlowTarget(TypedDict, closed=True):
    target_type: "capo_supplychain.types.data_integration_flow_target_type.DataIntegrationFlowTargetType"
    """<p>The DataIntegrationFlow target type.</p>"""
    s3_target: NotRequired[
        "capo_supplychain.types.data_integration_flow_s3_target_configuration.DataIntegrationFlowS3TargetConfiguration"
    ]
    """<p>The S3 DataIntegrationFlow target.</p>"""
    dataset_target: NotRequired[
        "capo_supplychain.types.data_integration_flow_dataset_target_configuration.DataIntegrationFlowDatasetTargetConfiguration"
    ]
    """<p>The dataset DataIntegrationFlow target. Note that for AWS Supply Chain dataset under <b>asc</b> namespace, it has a connection_id internal field that is not allowed to be provided by client directly, they will be auto populated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowTarget) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_flow_target_type

    out["targetType"] = (
        capo_supplychain.types.data_integration_flow_target_type.serialize_json(
            value["target_type"]
        )
    )
    if "s3_target" in value:
        import capo_supplychain.types.data_integration_flow_s3_target_configuration

        out["s3Target"] = (
            capo_supplychain.types.data_integration_flow_s3_target_configuration.serialize_json(
                value["s3_target"]
            )
        )
    if "dataset_target" in value:
        import capo_supplychain.types.data_integration_flow_dataset_target_configuration

        out["datasetTarget"] = (
            capo_supplychain.types.data_integration_flow_dataset_target_configuration.serialize_json(
                value["dataset_target"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowTarget:
    out: DataIntegrationFlowTarget = {}  # type: ignore[typeddict-item]
    if data.get("targetType") is not None:
        import capo_supplychain.types.data_integration_flow_target_type

        out["target_type"] = (
            capo_supplychain.types.data_integration_flow_target_type.deserialize_json(
                data["targetType"]
            )
        )
    else:
        import typing

        out["target_type"] = typing.cast(
            "capo_supplychain.types.data_integration_flow_target_type.DataIntegrationFlowTargetType",
            "",
        )
    if data.get("s3Target") is not None:
        import capo_supplychain.types.data_integration_flow_s3_target_configuration

        out["s3_target"] = (
            capo_supplychain.types.data_integration_flow_s3_target_configuration.deserialize_json(
                data["s3Target"]
            )
        )
    if data.get("datasetTarget") is not None:
        import capo_supplychain.types.data_integration_flow_dataset_target_configuration

        out["dataset_target"] = (
            capo_supplychain.types.data_integration_flow_dataset_target_configuration.deserialize_json(
                data["datasetTarget"]
            )
        )
    return out
