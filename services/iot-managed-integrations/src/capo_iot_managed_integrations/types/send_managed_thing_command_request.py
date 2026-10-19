"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SendManagedThingCommandRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.command_endpoints
    import capo_iot_managed_integrations.types.connector_association_id
    import capo_iot_managed_integrations.types.managed_thing_id


class SendManagedThingCommandRequest(TypedDict, closed=True):
    managed_thing_id: (
        "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    )
    """<p>The id of the device.</p>"""
    endpoints: "capo_iot_managed_integrations.types.command_endpoints.CommandEndpoints"
    """<p>The device endpoint.</p>"""
    connector_association_id: NotRequired[
        "capo_iot_managed_integrations.types.connector_association_id.ConnectorAssociationId"
    ]
    """<p>The ID tracking the current discovery process for one connector association.</p>"""
    account_association_id: NotRequired[
        "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    ]
    """<p>The identifier of the account association to use when sending a command to a managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendManagedThingCommandRequest) -> dict:
    out: dict = {}
    import capo_iot_managed_integrations.types.command_endpoints

    out["Endpoints"] = (
        capo_iot_managed_integrations.types.command_endpoints.serialize_json(
            value["endpoints"]
        )
    )
    if "connector_association_id" in value:
        out["ConnectorAssociationId"] = value["connector_association_id"]
    if "account_association_id" in value:
        out["AccountAssociationId"] = value["account_association_id"]
    return out


def deserialize_json(data: dict) -> SendManagedThingCommandRequest:
    out: SendManagedThingCommandRequest = {}  # type: ignore[typeddict-item]
    if data.get("Endpoints") is not None:
        import capo_iot_managed_integrations.types.command_endpoints

        out["endpoints"] = (
            capo_iot_managed_integrations.types.command_endpoints.deserialize_json(
                data["Endpoints"]
            )
        )
    else:
        out["endpoints"] = []
    if data.get("ConnectorAssociationId") is not None:
        out["connector_association_id"] = data["ConnectorAssociationId"]
    if data.get("AccountAssociationId") is not None:
        out["account_association_id"] = data["AccountAssociationId"]
    return out


def redact_sensitive(value: SendManagedThingCommandRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoints" in value:
        import capo_iot_managed_integrations.types.command_endpoints

        out["endpoints"] = (
            capo_iot_managed_integrations.types.command_endpoints.redact_sensitive(
                value["endpoints"]
            )
        )
    return out
