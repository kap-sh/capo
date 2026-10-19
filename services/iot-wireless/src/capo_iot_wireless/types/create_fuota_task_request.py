"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateFuotaTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.client_request_token
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.file_descriptor
    import capo_iot_wireless.types.firmware_update_image
    import capo_iot_wireless.types.firmware_update_role
    import capo_iot_wireless.types.fragment_interval_ms
    import capo_iot_wireless.types.fragment_size_bytes
    import capo_iot_wireless.types.fuota_task_name
    import capo_iot_wireless.types.lo_ra_wan_fuota_task
    import capo_iot_wireless.types.redundancy_percent
    import capo_iot_wireless.types.tag_list


class CreateFuotaTaskRequest(TypedDict, closed=True):
    name: NotRequired["capo_iot_wireless.types.fuota_task_name.FuotaTaskName"]
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    client_request_token: NotRequired[
        "capo_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_fuota_task.LoRaWANFuotaTask"
    ]
    firmware_update_image: (
        "capo_iot_wireless.types.firmware_update_image.FirmwareUpdateImage"
    )
    firmware_update_role: (
        "capo_iot_wireless.types.firmware_update_role.FirmwareUpdateRole"
    )
    tags: NotRequired["capo_iot_wireless.types.tag_list.TagList"]
    redundancy_percent: NotRequired[
        "capo_iot_wireless.types.redundancy_percent.RedundancyPercent"
    ]
    fragment_size_bytes: NotRequired[
        "capo_iot_wireless.types.fragment_size_bytes.FragmentSizeBytes"
    ]
    fragment_interval_ms: NotRequired[
        "capo_iot_wireless.types.fragment_interval_ms.FragmentIntervalMS"
    ]
    descriptor: NotRequired["capo_iot_wireless.types.file_descriptor.FileDescriptor"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateFuotaTaskRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_fuota_task

        out["LoRaWAN"] = capo_iot_wireless.types.lo_ra_wan_fuota_task.serialize_json(
            value["lo_ra_wan"]
        )
    out["FirmwareUpdateImage"] = value["firmware_update_image"]
    out["FirmwareUpdateRole"] = value["firmware_update_role"]
    if "tags" in value:
        import capo_iot_wireless.types.tag_list

        out["Tags"] = capo_iot_wireless.types.tag_list.serialize_json(value["tags"])
    if "redundancy_percent" in value:
        out["RedundancyPercent"] = value["redundancy_percent"]
    if "fragment_size_bytes" in value:
        out["FragmentSizeBytes"] = value["fragment_size_bytes"]
    if "fragment_interval_ms" in value:
        out["FragmentIntervalMS"] = value["fragment_interval_ms"]
    if "descriptor" in value:
        out["Descriptor"] = value["descriptor"]
    return out


def deserialize_json(data: dict) -> CreateFuotaTaskRequest:
    out: CreateFuotaTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("LoRaWAN") is not None:
        import capo_iot_wireless.types.lo_ra_wan_fuota_task

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_fuota_task.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if data.get("FirmwareUpdateImage") is not None:
        out["firmware_update_image"] = data["FirmwareUpdateImage"]
    else:
        out["firmware_update_image"] = ""
    if data.get("FirmwareUpdateRole") is not None:
        out["firmware_update_role"] = data["FirmwareUpdateRole"]
    else:
        out["firmware_update_role"] = ""
    if data.get("Tags") is not None:
        import capo_iot_wireless.types.tag_list

        out["tags"] = capo_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    if data.get("RedundancyPercent") is not None:
        out["redundancy_percent"] = data["RedundancyPercent"]
    if data.get("FragmentSizeBytes") is not None:
        out["fragment_size_bytes"] = data["FragmentSizeBytes"]
    if data.get("FragmentIntervalMS") is not None:
        out["fragment_interval_ms"] = data["FragmentIntervalMS"]
    if data.get("Descriptor") is not None:
        out["descriptor"] = data["Descriptor"]
    return out
