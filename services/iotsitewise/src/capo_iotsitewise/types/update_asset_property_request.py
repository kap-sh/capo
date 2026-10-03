"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateAssetPropertyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.property_alias
    import capo_iotsitewise.types.property_notification_state
    import capo_iotsitewise.types.property_unit


class UpdateAssetPropertyRequest(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset to be updated. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    property_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset property to be updated. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    property_alias: NotRequired["capo_iotsitewise.types.property_alias.PropertyAlias"]
    """<p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>If you omit this parameter, the alias is removed from the property.</p>"""
    property_notification_state: NotRequired[
        "capo_iotsitewise.types.property_notification_state.PropertyNotificationState"
    ]
    """<p>The MQTT notification state (enabled or disabled) for this asset property. When the notification state is enabled, IoT SiteWise publishes property value updates to a unique MQTT topic. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interact-with-other-services.html">Interacting with other services</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>If you omit this parameter, the notification state is set to <code>DISABLED</code>.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    property_unit: NotRequired["capo_iotsitewise.types.property_unit.PropertyUnit"]
    """<p>The unit of measure (such as Newtons or RPM) of the asset property. If you don't specify a value for this parameter, the service uses the value of the <code>assetModelProperty</code> in the asset model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetPropertyRequest) -> dict:
    out: dict = {}
    if "property_alias" in value:
        out["propertyAlias"] = value["property_alias"]
    if "property_notification_state" in value:
        import capo_iotsitewise.types.property_notification_state

        out["propertyNotificationState"] = (
            capo_iotsitewise.types.property_notification_state.serialize_json(
                value["property_notification_state"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "property_unit" in value:
        out["propertyUnit"] = value["property_unit"]
    return out


def deserialize_json(data: dict) -> UpdateAssetPropertyRequest:
    out: UpdateAssetPropertyRequest = {}  # type: ignore[typeddict-item]
    if data.get("propertyAlias") is not None:
        out["property_alias"] = data["propertyAlias"]
    if data.get("propertyNotificationState") is not None:
        import capo_iotsitewise.types.property_notification_state

        out["property_notification_state"] = (
            capo_iotsitewise.types.property_notification_state.deserialize_json(
                data["propertyNotificationState"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("propertyUnit") is not None:
        out["property_unit"] = data["propertyUnit"]
    return out
