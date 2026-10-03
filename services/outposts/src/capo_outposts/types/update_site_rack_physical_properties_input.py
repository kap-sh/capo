"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateSiteRackPhysicalPropertiesInput``."""

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
    import capo_outposts.types.site_id
    import capo_outposts.types.uplink_count
    import capo_outposts.types.uplink_gbps


class UpdateSiteRackPhysicalPropertiesInput(TypedDict, closed=True):
    site_id: "capo_outposts.types.site_id.SiteId"
    """<p> The ID or the Amazon Resource Name (ARN) of the site. </p>"""
    power_draw_kva: NotRequired["capo_outposts.types.power_draw_kva.PowerDrawKva"]
    """<p>The power draw, in kVA, available at the hardware placement position for the rack.</p>"""
    power_phase: NotRequired["capo_outposts.types.power_phase.PowerPhase"]
    """<p>The power option that you can provide for hardware. </p> <ul> <li> <p>Single-phase AC feed: 200 V to 277 V, 50 Hz or 60 Hz</p> </li> <li> <p>Three-phase AC feed: 346 V to 480 V, 50 Hz or 60 Hz</p> </li> </ul>"""
    power_connector: NotRequired["capo_outposts.types.power_connector.PowerConnector"]
    """<p>The power connector that Amazon Web Services should plan to provide for connections to the hardware. Note the correlation between <code>PowerPhase</code> and <code>PowerConnector</code>. </p> <ul> <li> <p>Single-phase AC feed</p> <ul> <li> <p> <b>L6-30P</b> – (common in US); 30A; single phase</p> </li> <li> <p> <b>IEC309 (blue)</b> – P+N+E, 6hr; 32 A; single phase</p> </li> </ul> </li> <li> <p>Three-phase AC feed</p> <ul> <li> <p> <b>AH530P7W (red)</b> – 3P+N+E, 7hr; 30A; three phase</p> </li> <li> <p> <b>AH532P6W (red)</b> – 3P+N+E, 6hr; 32A; three phase</p> </li> <li> <p> <b>CS8365C</b> – (common in US); 3P+E, 50A; three phase</p> </li> </ul> </li> </ul>"""
    power_feed_drop: NotRequired["capo_outposts.types.power_feed_drop.PowerFeedDrop"]
    """<p>Indicates whether the power feed comes above or below the rack. </p>"""
    uplink_gbps: NotRequired["capo_outposts.types.uplink_gbps.UplinkGbps"]
    """<p>The uplink speed the rack should support for the connection to the Region. </p>"""
    uplink_count: NotRequired["capo_outposts.types.uplink_count.UplinkCount"]
    """<p>Racks come with two Outpost network devices. Depending on the supported uplink speed at the site, the Outpost network devices provide a variable number of uplinks. Specify the number of uplinks for each Outpost network device that you intend to use to connect the rack to your network. Note the correlation between <code>UplinkGbps</code> and <code>UplinkCount</code>. </p> <ul> <li> <p>1Gbps - Uplinks available: 1, 2, 4, 6, 8</p> </li> <li> <p>10Gbps - Uplinks available: 1, 2, 4, 8, 12, 16</p> </li> <li> <p>40 and 100 Gbps- Uplinks available: 1, 2, 4</p> </li> </ul>"""
    fiber_optic_cable_type: NotRequired[
        "capo_outposts.types.fiber_optic_cable_type.FiberOpticCableType"
    ]
    """<p>The type of fiber that you will use to attach the Outpost to your network. </p>"""
    optical_standard: NotRequired[
        "capo_outposts.types.optical_standard.OpticalStandard"
    ]
    """<p>The type of optical standard that you will use to attach the Outpost to your network. This field is dependent on uplink speed, fiber type, and distance to the upstream device. For more information about networking requirements for racks, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#facility-networking">Network</a> in the Amazon Web Services Outposts User Guide. </p> <ul> <li> <p> <code>OPTIC_10GBASE_SR</code>: 10GBASE-SR</p> </li> <li> <p> <code>OPTIC_10GBASE_IR</code>: 10GBASE-IR</p> </li> <li> <p> <code>OPTIC_10GBASE_LR</code>: 10GBASE-LR</p> </li> <li> <p> <code>OPTIC_40GBASE_SR</code>: 40GBASE-SR</p> </li> <li> <p> <code>OPTIC_40GBASE_ESR</code>: 40GBASE-ESR</p> </li> <li> <p> <code>OPTIC_40GBASE_IR4_LR4L</code>: 40GBASE-IR (LR4L)</p> </li> <li> <p> <code>OPTIC_40GBASE_LR4</code>: 40GBASE-LR4</p> </li> <li> <p> <code>OPTIC_100GBASE_SR4</code>: 100GBASE-SR4</p> </li> <li> <p> <code>OPTIC_100GBASE_CWDM4</code>: 100GBASE-CWDM4</p> </li> <li> <p> <code>OPTIC_100GBASE_LR4</code>: 100GBASE-LR4</p> </li> <li> <p> <code>OPTIC_100G_PSM4_MSA</code>: 100G PSM4 MSA</p> </li> <li> <p> <code>OPTIC_1000BASE_LX</code>: 1000Base-LX</p> </li> <li> <p> <code>OPTIC_1000BASE_SX</code> : 1000Base-SX</p> </li> </ul>"""
    maximum_supported_weight_lbs: NotRequired[
        "capo_outposts.types.maximum_supported_weight_lbs.MaximumSupportedWeightLbs"
    ]
    """<p>The maximum rack weight that this site can support. <code>NO_LIMIT</code> is over 2000lbs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSiteRackPhysicalPropertiesInput) -> dict:
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


def deserialize_json(data: dict) -> UpdateSiteRackPhysicalPropertiesInput:
    out: UpdateSiteRackPhysicalPropertiesInput = {}  # type: ignore[typeddict-item]
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
