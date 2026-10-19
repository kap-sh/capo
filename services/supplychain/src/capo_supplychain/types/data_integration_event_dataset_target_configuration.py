"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEventDatasetTargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_dataset_arn
    import capo_supplychain.types.data_integration_event_dataset_operation_type


class DataIntegrationEventDatasetTargetConfiguration(TypedDict, closed=True):
    dataset_identifier: (
        "capo_supplychain.types.data_integration_dataset_arn.DataIntegrationDatasetArn"
    )
    """<p>The datalake dataset ARN identifier.</p>"""
    operation_type: "capo_supplychain.types.data_integration_event_dataset_operation_type.DataIntegrationEventDatasetOperationType"
    """<p>The target dataset load operation type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationEventDatasetTargetConfiguration) -> dict:
    out: dict = {}
    out["datasetIdentifier"] = value["dataset_identifier"]
    import capo_supplychain.types.data_integration_event_dataset_operation_type

    out["operationType"] = (
        capo_supplychain.types.data_integration_event_dataset_operation_type.serialize_json(
            value["operation_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataIntegrationEventDatasetTargetConfiguration:
    out: DataIntegrationEventDatasetTargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("datasetIdentifier") is not None:
        out["dataset_identifier"] = data["datasetIdentifier"]
    else:
        out["dataset_identifier"] = ""
    if data.get("operationType") is not None:
        import capo_supplychain.types.data_integration_event_dataset_operation_type

        out["operation_type"] = (
            capo_supplychain.types.data_integration_event_dataset_operation_type.deserialize_json(
                data["operationType"]
            )
        )
    else:
        import typing

        out["operation_type"] = typing.cast(
            "capo_supplychain.types.data_integration_event_dataset_operation_type.DataIntegrationEventDatasetOperationType",
            "",
        )
    return out
