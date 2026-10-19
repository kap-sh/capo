"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#RegisterAccountAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.device_discovery_id
    import capo_iot_managed_integrations.types.managed_thing_id


class RegisterAccountAssociationRequest(TypedDict, closed=True):
    managed_thing_id: (
        "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    )
    """<p>The identifier of the managed thing to register with the account association.</p>"""
    account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    """<p>The identifier of the account association to register with the managed thing.</p>"""
    device_discovery_id: (
        "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId"
    )
    """<p>The identifier of the device discovery job associated with this registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterAccountAssociationRequest) -> dict:
    out: dict = {}
    out["ManagedThingId"] = value["managed_thing_id"]
    out["AccountAssociationId"] = value["account_association_id"]
    out["DeviceDiscoveryId"] = value["device_discovery_id"]
    return out


def deserialize_json(data: dict) -> RegisterAccountAssociationRequest:
    out: RegisterAccountAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ManagedThingId") is not None:
        out["managed_thing_id"] = data["ManagedThingId"]
    else:
        out["managed_thing_id"] = ""
    if data.get("AccountAssociationId") is not None:
        out["account_association_id"] = data["AccountAssociationId"]
    else:
        out["account_association_id"] = ""
    if data.get("DeviceDiscoveryId") is not None:
        out["device_discovery_id"] = data["DeviceDiscoveryId"]
    else:
        out["device_discovery_id"] = ""
    return out
