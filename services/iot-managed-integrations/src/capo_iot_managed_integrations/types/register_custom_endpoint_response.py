"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#RegisterCustomEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.endpoint_address


class RegisterCustomEndpointResponse(TypedDict, closed=True):
    endpoint_address: (
        "capo_iot_managed_integrations.types.endpoint_address.EndpointAddress"
    )
    """<p>The IoT managed integrations dedicated, custom endpoint for the device to route traffic through.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterCustomEndpointResponse) -> dict:
    out: dict = {}
    out["EndpointAddress"] = value["endpoint_address"]
    return out


def deserialize_json(data: dict) -> RegisterCustomEndpointResponse:
    out: RegisterCustomEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("EndpointAddress") is not None:
        out["endpoint_address"] = data["EndpointAddress"]
    else:
        out["endpoint_address"] = ""
    return out
