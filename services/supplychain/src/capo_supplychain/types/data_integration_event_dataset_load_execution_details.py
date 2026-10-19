"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEventDatasetLoadExecutionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_event_dataset_load_status


class DataIntegrationEventDatasetLoadExecutionDetails(TypedDict, closed=True):
    status: "capo_supplychain.types.data_integration_event_dataset_load_status.DataIntegrationEventDatasetLoadStatus"
    """<p>The event load execution status to target dataset.</p>"""
    message: NotRequired["str"]
    """<p>The failure message (if any) of failed event load execution to dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationEventDatasetLoadExecutionDetails) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_event_dataset_load_status

    out["status"] = (
        capo_supplychain.types.data_integration_event_dataset_load_status.serialize_json(
            value["status"]
        )
    )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DataIntegrationEventDatasetLoadExecutionDetails:
    out: DataIntegrationEventDatasetLoadExecutionDetails = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_supplychain.types.data_integration_event_dataset_load_status

        out["status"] = (
            capo_supplychain.types.data_integration_event_dataset_load_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_supplychain.types.data_integration_event_dataset_load_status.DataIntegrationEventDatasetLoadStatus",
            "",
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
