"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListDiscoveredDevicesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.discovered_device_list_definition
    import capo_iot_managed_integrations.types.next_token


class ListDiscoveredDevicesResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_iot_managed_integrations.types.discovered_device_list_definition.DiscoveredDeviceListDefinition"
    ]
    """<p>The list of discovered devices that match the specified criteria.</p>"""
    next_token: NotRequired["capo_iot_managed_integrations.types.next_token.NextToken"]
    """<p>A token used for pagination of results when there are more discovered devices than can be returned in a single response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDiscoveredDevicesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_iot_managed_integrations.types.discovered_device_list_definition

        out["Items"] = (
            capo_iot_managed_integrations.types.discovered_device_list_definition.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDiscoveredDevicesResponse:
    out: ListDiscoveredDevicesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_iot_managed_integrations.types.discovered_device_list_definition

        out["items"] = (
            capo_iot_managed_integrations.types.discovered_device_list_definition.deserialize_json(
                data["Items"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListDiscoveredDevicesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_iot_managed_integrations.types.discovered_device_list_definition

        out["items"] = (
            capo_iot_managed_integrations.types.discovered_device_list_definition.redact_sensitive(
                value["items"]
            )
        )
    return out
