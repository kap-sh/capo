"""Generated from Smithy shape ``com.amazonaws.iot#ThingIndexingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.device_defender_indexing_mode
    import capo_iot.types.fields
    import capo_iot.types.indexing_filter
    import capo_iot.types.named_shadow_indexing_mode
    import capo_iot.types.thing_connectivity_indexing_mode
    import capo_iot.types.thing_indexing_mode


class ThingIndexingConfiguration(TypedDict, closed=True):
    thing_indexing_mode: "capo_iot.types.thing_indexing_mode.ThingIndexingMode"
    """<p>Thing indexing mode. Valid values are:</p> <ul> <li> <p>REGISTRY – Your thing index contains registry data only.</p> </li> <li> <p>REGISTRY_AND_SHADOW - Your thing index contains registry and shadow data.</p> </li> <li> <p>OFF - Thing indexing is disabled.</p> </li> </ul>"""
    thing_connectivity_indexing_mode: NotRequired[
        "capo_iot.types.thing_connectivity_indexing_mode.ThingConnectivityIndexingMode"
    ]
    """<p>Thing connectivity indexing mode. Valid values are: </p> <ul> <li> <p>STATUS – Your thing index contains connectivity status. To enable thing connectivity indexing, <i>thingIndexMode</i> must not be set to OFF.</p> </li> <li> <p>OFF - Thing connectivity status indexing is disabled.</p> </li> </ul>"""
    device_defender_indexing_mode: NotRequired[
        "capo_iot.types.device_defender_indexing_mode.DeviceDefenderIndexingMode"
    ]
    """<p>Device Defender indexing mode. Valid values are:</p> <ul> <li> <p>VIOLATIONS – Your thing index contains Device Defender violations. To enable Device Defender indexing, <i>deviceDefenderIndexingMode</i> must not be set to OFF.</p> </li> <li> <p>OFF - Device Defender indexing is disabled.</p> </li> </ul> <p>For more information about Device Defender violations, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html">Device Defender Detect.</a> </p>"""
    named_shadow_indexing_mode: NotRequired[
        "capo_iot.types.named_shadow_indexing_mode.NamedShadowIndexingMode"
    ]
    """<p>Named shadow indexing mode. Valid values are:</p> <ul> <li> <p>ON – Your thing index contains named shadow. To enable thing named shadow indexing, <i>namedShadowIndexingMode</i> must not be set to OFF.</p> </li> <li> <p>OFF - Named shadow indexing is disabled.</p> </li> </ul> <p>For more information about Shadows, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html">IoT Device Shadow service.</a> </p>"""
    managed_fields: NotRequired["capo_iot.types.fields.Fields"]
    """<p>Contains fields that are indexed and whose types are already known by the Fleet Indexing service. This is an optional field. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-index.html#managed-field">Managed fields</a> in the <i>Amazon Web Services IoT Core Developer Guide</i>.</p> <note> <p>You can't modify managed fields by updating fleet indexing configuration.</p> </note>"""
    custom_fields: NotRequired["capo_iot.types.fields.Fields"]
    """<p>Contains custom field names and their data type.</p>"""
    filter: NotRequired["capo_iot.types.indexing_filter.IndexingFilter"]
    """<p>Provides additional selections for named shadows and geolocation data. </p> <p>To add named shadows to your fleet indexing configuration, set <code>namedShadowIndexingMode</code> to be ON and specify your shadow names in <code>namedShadowNames</code> filter.</p> <p>To add geolocation data to your fleet indexing configuration: </p> <ul> <li> <p>If you store geolocation data in a class/unnamed shadow, set <code>thingIndexingMode</code> to be <code>REGISTRY_AND_SHADOW</code> and specify your geolocation data in <code>geoLocations</code> filter. </p> </li> <li> <p>If you store geolocation data in a named shadow, set <code>namedShadowIndexingMode</code> to be <code>ON</code>, add the shadow name in <code>namedShadowNames</code> filter, and specify your geolocation data in <code>geoLocations</code> filter. For more information, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-index.html">Managing fleet indexing</a>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThingIndexingConfiguration) -> dict:
    out: dict = {}
    import capo_iot.types.thing_indexing_mode

    out["thingIndexingMode"] = capo_iot.types.thing_indexing_mode.serialize_json(
        value["thing_indexing_mode"]
    )
    if "thing_connectivity_indexing_mode" in value:
        import capo_iot.types.thing_connectivity_indexing_mode

        out["thingConnectivityIndexingMode"] = (
            capo_iot.types.thing_connectivity_indexing_mode.serialize_json(
                value["thing_connectivity_indexing_mode"]
            )
        )
    if "device_defender_indexing_mode" in value:
        import capo_iot.types.device_defender_indexing_mode

        out["deviceDefenderIndexingMode"] = (
            capo_iot.types.device_defender_indexing_mode.serialize_json(
                value["device_defender_indexing_mode"]
            )
        )
    if "named_shadow_indexing_mode" in value:
        import capo_iot.types.named_shadow_indexing_mode

        out["namedShadowIndexingMode"] = (
            capo_iot.types.named_shadow_indexing_mode.serialize_json(
                value["named_shadow_indexing_mode"]
            )
        )
    if "managed_fields" in value:
        import capo_iot.types.fields

        out["managedFields"] = capo_iot.types.fields.serialize_json(
            value["managed_fields"]
        )
    if "custom_fields" in value:
        import capo_iot.types.fields

        out["customFields"] = capo_iot.types.fields.serialize_json(
            value["custom_fields"]
        )
    if "filter" in value:
        import capo_iot.types.indexing_filter

        out["filter"] = capo_iot.types.indexing_filter.serialize_json(value["filter"])
    return out


def deserialize_json(data: dict) -> ThingIndexingConfiguration:
    out: ThingIndexingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("thingIndexingMode") is not None:
        import capo_iot.types.thing_indexing_mode

        out["thing_indexing_mode"] = (
            capo_iot.types.thing_indexing_mode.deserialize_json(
                data["thingIndexingMode"]
            )
        )
    else:
        raise DeserializationError(
            "ThingIndexingConfiguration.thing_indexing_mode required"
        )
    if data.get("thingConnectivityIndexingMode") is not None:
        import capo_iot.types.thing_connectivity_indexing_mode

        out["thing_connectivity_indexing_mode"] = (
            capo_iot.types.thing_connectivity_indexing_mode.deserialize_json(
                data["thingConnectivityIndexingMode"]
            )
        )
    if data.get("deviceDefenderIndexingMode") is not None:
        import capo_iot.types.device_defender_indexing_mode

        out["device_defender_indexing_mode"] = (
            capo_iot.types.device_defender_indexing_mode.deserialize_json(
                data["deviceDefenderIndexingMode"]
            )
        )
    if data.get("namedShadowIndexingMode") is not None:
        import capo_iot.types.named_shadow_indexing_mode

        out["named_shadow_indexing_mode"] = (
            capo_iot.types.named_shadow_indexing_mode.deserialize_json(
                data["namedShadowIndexingMode"]
            )
        )
    if data.get("managedFields") is not None:
        import capo_iot.types.fields

        out["managed_fields"] = capo_iot.types.fields.deserialize_json(
            data["managedFields"]
        )
    if data.get("customFields") is not None:
        import capo_iot.types.fields

        out["custom_fields"] = capo_iot.types.fields.deserialize_json(
            data["customFields"]
        )
    if data.get("filter") is not None:
        import capo_iot.types.indexing_filter

        out["filter"] = capo_iot.types.indexing_filter.deserialize_json(data["filter"])
    return out
