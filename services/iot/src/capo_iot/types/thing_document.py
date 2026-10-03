"""Generated from Smithy shape ``com.amazonaws.iot#ThingDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.attributes
    import capo_iot.types.json_document
    import capo_iot.types.thing_connectivity
    import capo_iot.types.thing_group_name_list
    import capo_iot.types.thing_id
    import capo_iot.types.thing_name
    import capo_iot.types.thing_type_name


class ThingDocument(TypedDict, closed=True):
    thing_name: NotRequired["capo_iot.types.thing_name.ThingName"]
    """<p>The thing name.</p>"""
    thing_id: NotRequired["capo_iot.types.thing_id.ThingId"]
    """<p>The thing ID.</p>"""
    thing_type_name: NotRequired["capo_iot.types.thing_type_name.ThingTypeName"]
    """<p>The thing type name.</p>"""
    thing_group_names: NotRequired[
        "capo_iot.types.thing_group_name_list.ThingGroupNameList"
    ]
    """<p>Thing group and billing group names.</p>"""
    attributes: NotRequired["capo_iot.types.attributes.Attributes"]
    """<p>The attributes.</p>"""
    shadow: NotRequired["capo_iot.types.json_document.JsonDocument"]
    """<p>The unnamed shadow and named shadow.</p> <p>For more information about shadows, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html">IoT Device Shadow service.</a> </p>"""
    device_defender: NotRequired["capo_iot.types.json_document.JsonDocument"]
    """<p>Contains Device Defender data.</p> <p>For more information about Device Defender, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html">Device Defender</a>. </p>"""
    connectivity: NotRequired["capo_iot.types.thing_connectivity.ThingConnectivity"]
    """<p>Indicates whether the thing is connected to the Amazon Web Services IoT Core service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThingDocument) -> dict:
    out: dict = {}
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "thing_id" in value:
        out["thingId"] = value["thing_id"]
    if "thing_type_name" in value:
        out["thingTypeName"] = value["thing_type_name"]
    if "thing_group_names" in value:
        import capo_iot.types.thing_group_name_list

        out["thingGroupNames"] = capo_iot.types.thing_group_name_list.serialize_json(
            value["thing_group_names"]
        )
    if "attributes" in value:
        import capo_iot.types.attributes

        out["attributes"] = capo_iot.types.attributes.serialize_json(
            value["attributes"]
        )
    if "shadow" in value:
        out["shadow"] = value["shadow"]
    if "device_defender" in value:
        out["deviceDefender"] = value["device_defender"]
    if "connectivity" in value:
        import capo_iot.types.thing_connectivity

        out["connectivity"] = capo_iot.types.thing_connectivity.serialize_json(
            value["connectivity"]
        )
    return out


def deserialize_json(data: dict) -> ThingDocument:
    out: ThingDocument = {}  # type: ignore[typeddict-item]
    if data.get("thingName") is not None:
        out["thing_name"] = data["thingName"]
    if data.get("thingId") is not None:
        out["thing_id"] = data["thingId"]
    if data.get("thingTypeName") is not None:
        out["thing_type_name"] = data["thingTypeName"]
    if data.get("thingGroupNames") is not None:
        import capo_iot.types.thing_group_name_list

        out["thing_group_names"] = (
            capo_iot.types.thing_group_name_list.deserialize_json(
                data["thingGroupNames"]
            )
        )
    if data.get("attributes") is not None:
        import capo_iot.types.attributes

        out["attributes"] = capo_iot.types.attributes.deserialize_json(
            data["attributes"]
        )
    if data.get("shadow") is not None:
        out["shadow"] = data["shadow"]
    if data.get("deviceDefender") is not None:
        out["device_defender"] = data["deviceDefender"]
    if data.get("connectivity") is not None:
        import capo_iot.types.thing_connectivity

        out["connectivity"] = capo_iot.types.thing_connectivity.deserialize_json(
            data["connectivity"]
        )
    return out
