"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_supplychain.types.data_integration_event_dataset_target_details
    import capo_supplychain.types.data_integration_event_group_id
    import capo_supplychain.types.data_integration_event_type
    import capo_supplychain.types.uuid


class DataIntegrationEvent(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    event_id: "capo_supplychain.types.uuid.UUID"
    """<p>The unique event identifier.</p>"""
    event_type: (
        "capo_supplychain.types.data_integration_event_type.DataIntegrationEventType"
    )
    """<p>The data event type.</p>"""
    event_group_id: "capo_supplychain.types.data_integration_event_group_id.DataIntegrationEventGroupId"
    """<p>Event identifier (for example, orderId for InboundOrder) used for data sharding or partitioning.</p>"""
    event_timestamp: "datetime.datetime"
    """<p>The event timestamp (in epoch seconds).</p>"""
    dataset_target_details: NotRequired[
        "capo_supplychain.types.data_integration_event_dataset_target_details.DataIntegrationEventDatasetTargetDetails"
    ]
    """<p>The target dataset details for a DATASET event type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationEvent) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["eventId"] = value["event_id"]
    import capo_supplychain.types.data_integration_event_type

    out["eventType"] = (
        capo_supplychain.types.data_integration_event_type.serialize_json(
            value["event_type"]
        )
    )
    out["eventGroupId"] = value["event_group_id"]
    import capo_supplychain.types._prelude.timestamp

    out["eventTimestamp"] = capo_supplychain.types._prelude.timestamp.serialize_json(
        value["event_timestamp"]
    )
    if "dataset_target_details" in value:
        import capo_supplychain.types.data_integration_event_dataset_target_details

        out["datasetTargetDetails"] = (
            capo_supplychain.types.data_integration_event_dataset_target_details.serialize_json(
                value["dataset_target_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationEvent:
    out: DataIntegrationEvent = {}  # type: ignore[typeddict-item]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    else:
        out["instance_id"] = ""
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = ""
    if data.get("eventType") is not None:
        import capo_supplychain.types.data_integration_event_type

        out["event_type"] = (
            capo_supplychain.types.data_integration_event_type.deserialize_json(
                data["eventType"]
            )
        )
    else:
        import typing

        out["event_type"] = typing.cast(
            "capo_supplychain.types.data_integration_event_type.DataIntegrationEventType",
            "",
        )
    if data.get("eventGroupId") is not None:
        out["event_group_id"] = data["eventGroupId"]
    else:
        out["event_group_id"] = ""
    if data.get("eventTimestamp") is not None:
        import capo_supplychain.types._prelude.timestamp

        out["event_timestamp"] = (
            capo_supplychain.types._prelude.timestamp.deserialize_json(
                data["eventTimestamp"]
            )
        )
    else:
        import datetime

        out["event_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("datasetTargetDetails") is not None:
        import capo_supplychain.types.data_integration_event_dataset_target_details

        out["dataset_target_details"] = (
            capo_supplychain.types.data_integration_event_dataset_target_details.deserialize_json(
                data["datasetTargetDetails"]
            )
        )
    return out
