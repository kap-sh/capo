"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateMulticastGroupWithFuotaTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.fuota_task_id
    import capo_iot_wireless.types.multicast_group_id


class AssociateMulticastGroupWithFuotaTaskRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId"
    multicast_group_id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId"


# --- restJson1 ser/de ---
def serialize_json(value: AssociateMulticastGroupWithFuotaTaskRequest) -> dict:
    out: dict = {}
    out["MulticastGroupId"] = value["multicast_group_id"]
    return out


def deserialize_json(data: dict) -> AssociateMulticastGroupWithFuotaTaskRequest:
    out: AssociateMulticastGroupWithFuotaTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("MulticastGroupId") is not None:
        out["multicast_group_id"] = data["MulticastGroupId"]
    else:
        out["multicast_group_id"] = ""
    return out
