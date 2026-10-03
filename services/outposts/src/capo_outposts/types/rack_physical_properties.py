"""Generated from Smithy shape ``com.amazonaws.outposts#RackPhysicalProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.fiber_optic_cable_type
    import capo_outposts.types.maximum_supported_weight_lbs
    import capo_outposts.types.optical_standard
    import capo_outposts.types.power_connector
    import capo_outposts.types.power_draw_kva
    import capo_outposts.types.power_feed_drop
    import capo_outposts.types.power_phase
    import capo_outposts.types.uplink_count
    import capo_outposts.types.uplink_gbps


class RackPhysicalProperties(TypedDict, closed=True):
    power_draw_kva: NotRequired["capo_outposts.types.power_draw_kva.PowerDrawKva"]
    """<p>The power draw available at the hardware placement position for the rack. </p>"""
    power_phase: NotRequired["capo_outposts.types.power_phase.PowerPhase"]
    """<p>The power option that you can provide for hardware.</p>"""
    power_connector: NotRequired["capo_outposts.types.power_connector.PowerConnector"]
    """<p>The power connector for the hardware. </p>"""
    power_feed_drop: NotRequired["capo_outposts.types.power_feed_drop.PowerFeedDrop"]
    """<p>The position of the power feed.</p>"""
    uplink_gbps: NotRequired["capo_outposts.types.uplink_gbps.UplinkGbps"]
    """<p>The uplink speed the rack supports for the connection to the Region. </p>"""
    uplink_count: NotRequired["capo_outposts.types.uplink_count.UplinkCount"]
    """<p>The number of uplinks each Outpost network device.</p>"""
    fiber_optic_cable_type: NotRequired[
        "capo_outposts.types.fiber_optic_cable_type.FiberOpticCableType"
    ]
    """<p>The type of fiber used to attach the Outpost to the network. </p>"""
    optical_standard: NotRequired[
        "capo_outposts.types.optical_standard.OpticalStandard"
    ]
    """<p>The type of optical standard used to attach the Outpost to the network. This field is dependent on uplink speed, fiber type, and distance to the upstream device. For more information about networking requirements for racks, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#facility-networking">Network</a> in the Amazon Web Services Outposts User Guide. </p>"""
    maximum_supported_weight_lbs: NotRequired[
        "capo_outposts.types.maximum_supported_weight_lbs.MaximumSupportedWeightLbs"
    ]
    """<p>The maximum rack weight that this site can support. <code>NO_LIMIT</code> is over 2000 lbs (907 kg). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RackPhysicalProperties) -> dict:
    out: dict = {}
    if "power_draw_kva" in value:
        import capo_outposts.types.power_draw_kva

        out["PowerDrawKva"] = capo_outposts.types.power_draw_kva.serialize_json(
            value["power_draw_kva"]
        )
    if "power_phase" in value:
        import capo_outposts.types.power_phase

        out["PowerPhase"] = capo_outposts.types.power_phase.serialize_json(
            value["power_phase"]
        )
    if "power_connector" in value:
        import capo_outposts.types.power_connector

        out["PowerConnector"] = capo_outposts.types.power_connector.serialize_json(
            value["power_connector"]
        )
    if "power_feed_drop" in value:
        import capo_outposts.types.power_feed_drop

        out["PowerFeedDrop"] = capo_outposts.types.power_feed_drop.serialize_json(
            value["power_feed_drop"]
        )
    if "uplink_gbps" in value:
        import capo_outposts.types.uplink_gbps

        out["UplinkGbps"] = capo_outposts.types.uplink_gbps.serialize_json(
            value["uplink_gbps"]
        )
    if "uplink_count" in value:
        import capo_outposts.types.uplink_count

        out["UplinkCount"] = capo_outposts.types.uplink_count.serialize_json(
            value["uplink_count"]
        )
    if "fiber_optic_cable_type" in value:
        import capo_outposts.types.fiber_optic_cable_type

        out["FiberOpticCableType"] = (
            capo_outposts.types.fiber_optic_cable_type.serialize_json(
                value["fiber_optic_cable_type"]
            )
        )
    if "optical_standard" in value:
        import capo_outposts.types.optical_standard

        out["OpticalStandard"] = capo_outposts.types.optical_standard.serialize_json(
            value["optical_standard"]
        )
    if "maximum_supported_weight_lbs" in value:
        import capo_outposts.types.maximum_supported_weight_lbs

        out["MaximumSupportedWeightLbs"] = (
            capo_outposts.types.maximum_supported_weight_lbs.serialize_json(
                value["maximum_supported_weight_lbs"]
            )
        )
    return out


def deserialize_json(data: dict) -> RackPhysicalProperties:
    out: RackPhysicalProperties = {}  # type: ignore[typeddict-item]
    if data.get("PowerDrawKva") is not None:
        import capo_outposts.types.power_draw_kva

        out["power_draw_kva"] = capo_outposts.types.power_draw_kva.deserialize_json(
            data["PowerDrawKva"]
        )
    if data.get("PowerPhase") is not None:
        import capo_outposts.types.power_phase

        out["power_phase"] = capo_outposts.types.power_phase.deserialize_json(
            data["PowerPhase"]
        )
    if data.get("PowerConnector") is not None:
        import capo_outposts.types.power_connector

        out["power_connector"] = capo_outposts.types.power_connector.deserialize_json(
            data["PowerConnector"]
        )
    if data.get("PowerFeedDrop") is not None:
        import capo_outposts.types.power_feed_drop

        out["power_feed_drop"] = capo_outposts.types.power_feed_drop.deserialize_json(
            data["PowerFeedDrop"]
        )
    if data.get("UplinkGbps") is not None:
        import capo_outposts.types.uplink_gbps

        out["uplink_gbps"] = capo_outposts.types.uplink_gbps.deserialize_json(
            data["UplinkGbps"]
        )
    if data.get("UplinkCount") is not None:
        import capo_outposts.types.uplink_count

        out["uplink_count"] = capo_outposts.types.uplink_count.deserialize_json(
            data["UplinkCount"]
        )
    if data.get("FiberOpticCableType") is not None:
        import capo_outposts.types.fiber_optic_cable_type

        out["fiber_optic_cable_type"] = (
            capo_outposts.types.fiber_optic_cable_type.deserialize_json(
                data["FiberOpticCableType"]
            )
        )
    if data.get("OpticalStandard") is not None:
        import capo_outposts.types.optical_standard

        out["optical_standard"] = capo_outposts.types.optical_standard.deserialize_json(
            data["OpticalStandard"]
        )
    if data.get("MaximumSupportedWeightLbs") is not None:
        import capo_outposts.types.maximum_supported_weight_lbs

        out["maximum_supported_weight_lbs"] = (
            capo_outposts.types.maximum_supported_weight_lbs.deserialize_json(
                data["MaximumSupportedWeightLbs"]
            )
        )
    return out
