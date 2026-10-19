"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetDeviceDiscoveryResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.connector_association_id
    import capo_iot_managed_integrations.types.device_discovery_arn
    import capo_iot_managed_integrations.types.device_discovery_id
    import capo_iot_managed_integrations.types.device_discovery_status
    import capo_iot_managed_integrations.types.discovery_finished_at
    import capo_iot_managed_integrations.types.discovery_started_at
    import capo_iot_managed_integrations.types.discovery_type
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.tags_map


class GetDeviceDiscoveryResponse(TypedDict, closed=True):
    id: "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId"
    """<p>The id of the device discovery job request.</p>"""
    arn: "capo_iot_managed_integrations.types.device_discovery_arn.DeviceDiscoveryArn"
    """<p>The Amazon Resource Name (ARN) of the device discovery job request.</p>"""
    discovery_type: "capo_iot_managed_integrations.types.discovery_type.DiscoveryType"
    """<p>The discovery type supporting the type of device to be discovered in the device discovery job request.</p>"""
    status: "capo_iot_managed_integrations.types.device_discovery_status.DeviceDiscoveryStatus"
    """<p>The status of the device discovery job request.</p>"""
    started_at: (
        "capo_iot_managed_integrations.types.discovery_started_at.DiscoveryStartedAt"
    )
    """<p>The timestamp value for the start time of the device discovery.</p>"""
    controller_id: NotRequired[
        "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The id of the end-user's IoT hub.</p>"""
    connector_association_id: NotRequired[
        "capo_iot_managed_integrations.types.connector_association_id.ConnectorAssociationId"
    ]
    """<p>The ID tracking the current discovery process for one connector association.</p>"""
    account_association_id: NotRequired[
        "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    ]
    """<p>The identifier of the account association used for the device discovery.</p>"""
    finished_at: NotRequired[
        "capo_iot_managed_integrations.types.discovery_finished_at.DiscoveryFinishedAt"
    ]
    """<p>The timestamp value for the completion time of the device discovery.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the device discovery request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceDiscoveryResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    import capo_iot_managed_integrations.types.discovery_type

    out["DiscoveryType"] = (
        capo_iot_managed_integrations.types.discovery_type.serialize_json(
            value["discovery_type"]
        )
    )
    import capo_iot_managed_integrations.types.device_discovery_status

    out["Status"] = (
        capo_iot_managed_integrations.types.device_discovery_status.serialize_json(
            value["status"]
        )
    )
    import capo_iot_managed_integrations.types.discovery_started_at

    out["StartedAt"] = (
        capo_iot_managed_integrations.types.discovery_started_at.serialize_json(
            value["started_at"]
        )
    )
    if "controller_id" in value:
        out["ControllerId"] = value["controller_id"]
    if "connector_association_id" in value:
        out["ConnectorAssociationId"] = value["connector_association_id"]
    if "account_association_id" in value:
        out["AccountAssociationId"] = value["account_association_id"]
    if "finished_at" in value:
        import capo_iot_managed_integrations.types.discovery_finished_at

        out["FinishedAt"] = (
            capo_iot_managed_integrations.types.discovery_finished_at.serialize_json(
                value["finished_at"]
            )
        )
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetDeviceDiscoveryResponse:
    out: GetDeviceDiscoveryResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("DiscoveryType") is not None:
        import capo_iot_managed_integrations.types.discovery_type

        out["discovery_type"] = (
            capo_iot_managed_integrations.types.discovery_type.deserialize_json(
                data["DiscoveryType"]
            )
        )
    else:
        import typing

        out["discovery_type"] = typing.cast(
            "capo_iot_managed_integrations.types.discovery_type.DiscoveryType", ""
        )
    if data.get("Status") is not None:
        import capo_iot_managed_integrations.types.device_discovery_status

        out["status"] = (
            capo_iot_managed_integrations.types.device_discovery_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iot_managed_integrations.types.device_discovery_status.DeviceDiscoveryStatus",
            "",
        )
    if data.get("StartedAt") is not None:
        import capo_iot_managed_integrations.types.discovery_started_at

        out["started_at"] = (
            capo_iot_managed_integrations.types.discovery_started_at.deserialize_json(
                data["StartedAt"]
            )
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("ControllerId") is not None:
        out["controller_id"] = data["ControllerId"]
    if data.get("ConnectorAssociationId") is not None:
        out["connector_association_id"] = data["ConnectorAssociationId"]
    if data.get("AccountAssociationId") is not None:
        out["account_association_id"] = data["AccountAssociationId"]
    if data.get("FinishedAt") is not None:
        import capo_iot_managed_integrations.types.discovery_finished_at

        out["finished_at"] = (
            capo_iot_managed_integrations.types.discovery_finished_at.deserialize_json(
                data["FinishedAt"]
            )
        )
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: GetDeviceDiscoveryResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
