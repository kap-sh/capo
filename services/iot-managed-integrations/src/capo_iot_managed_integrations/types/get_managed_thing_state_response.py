"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingStateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.state_endpoints


class GetManagedThingStateResponse(TypedDict, closed=True):
    endpoints: "capo_iot_managed_integrations.types.state_endpoints.StateEndpoints"
    """<p>The device endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingStateResponse) -> dict:
    out: dict = {}
    import capo_iot_managed_integrations.types.state_endpoints

    out["Endpoints"] = (
        capo_iot_managed_integrations.types.state_endpoints.serialize_json(
            value["endpoints"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetManagedThingStateResponse:
    out: GetManagedThingStateResponse = {}  # type: ignore[typeddict-item]
    if data.get("Endpoints") is not None:
        import capo_iot_managed_integrations.types.state_endpoints

        out["endpoints"] = (
            capo_iot_managed_integrations.types.state_endpoints.deserialize_json(
                data["Endpoints"]
            )
        )
    else:
        out["endpoints"] = []
    return out


def redact_sensitive(value: GetManagedThingStateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoints" in value:
        import capo_iot_managed_integrations.types.state_endpoints

        out["endpoints"] = (
            capo_iot_managed_integrations.types.state_endpoints.redact_sensitive(
                value["endpoints"]
            )
        )
    return out
