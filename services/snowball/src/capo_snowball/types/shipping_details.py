"""Generated from Smithy shape ``com.amazonaws.snowball#ShippingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.shipment
    import capo_snowball.types.shipping_option


class ShippingDetails(TypedDict, closed=True):
    shipping_option: NotRequired["capo_snowball.types.shipping_option.ShippingOption"]
    """<p>The shipping speed for a particular job. This speed doesn't dictate how soon you'll get the Snow device from the job's creation date. This speed represents how quickly it moves to its destination while in transit. Regional shipping speeds are as follows:</p> <ul> <li> <p>In Australia, you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day.</p> </li> <li> <p>In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.</p> </li> <li> <p>In India, Snow devices are delivered in one to seven days.</p> </li> <li> <p>In the United States of America (US), you have access to one-day shipping and two-day shipping.</p> </li> </ul>"""
    inbound_shipment: NotRequired["capo_snowball.types.shipment.Shipment"]
    """<p>The <code>Status</code> and <code>TrackingNumber</code> values for a Snow device being returned to Amazon Web Services for a particular job.</p>"""
    outbound_shipment: NotRequired["capo_snowball.types.shipment.Shipment"]
    """<p>The <code>Status</code> and <code>TrackingNumber</code> values for a Snow device being delivered to the address that you specified for a particular job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShippingDetails) -> dict:
    out: dict = {}
    if "shipping_option" in value:
        import capo_snowball.types.shipping_option

        out["ShippingOption"] = (
            capo_snowball.types.shipping_option.serialize_aws_json_1_1(
                value["shipping_option"]
            )
        )
    if "inbound_shipment" in value:
        import capo_snowball.types.shipment

        out["InboundShipment"] = capo_snowball.types.shipment.serialize_aws_json_1_1(
            value["inbound_shipment"]
        )
    if "outbound_shipment" in value:
        import capo_snowball.types.shipment

        out["OutboundShipment"] = capo_snowball.types.shipment.serialize_aws_json_1_1(
            value["outbound_shipment"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ShippingDetails:
    out: ShippingDetails = {}  # type: ignore[typeddict-item]
    if data.get("ShippingOption") is not None:
        import capo_snowball.types.shipping_option

        out["shipping_option"] = (
            capo_snowball.types.shipping_option.deserialize_aws_json_1_1(
                data["ShippingOption"]
            )
        )
    if data.get("InboundShipment") is not None:
        import capo_snowball.types.shipment

        out["inbound_shipment"] = capo_snowball.types.shipment.deserialize_aws_json_1_1(
            data["InboundShipment"]
        )
    if data.get("OutboundShipment") is not None:
        import capo_snowball.types.shipment

        out["outbound_shipment"] = (
            capo_snowball.types.shipment.deserialize_aws_json_1_1(
                data["OutboundShipment"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ShippingDetails) -> dict:
    out: dict = {}
    if "shipping_option" in value:
        import capo_snowball.types.shipping_option

        out["ShippingOption"] = capo_snowball.types.shipping_option.serialize_cbor(
            value["shipping_option"]
        )
    if "inbound_shipment" in value:
        import capo_snowball.types.shipment

        out["InboundShipment"] = capo_snowball.types.shipment.serialize_cbor(
            value["inbound_shipment"]
        )
    if "outbound_shipment" in value:
        import capo_snowball.types.shipment

        out["OutboundShipment"] = capo_snowball.types.shipment.serialize_cbor(
            value["outbound_shipment"]
        )
    return out


def deserialize_cbor(data: dict) -> ShippingDetails:
    out: ShippingDetails = {}  # type: ignore[typeddict-item]
    if data.get("ShippingOption") is not None:
        import capo_snowball.types.shipping_option

        out["shipping_option"] = capo_snowball.types.shipping_option.deserialize_cbor(
            data["ShippingOption"]
        )
    if data.get("InboundShipment") is not None:
        import capo_snowball.types.shipment

        out["inbound_shipment"] = capo_snowball.types.shipment.deserialize_cbor(
            data["InboundShipment"]
        )
    if data.get("OutboundShipment") is not None:
        import capo_snowball.types.shipment

        out["outbound_shipment"] = capo_snowball.types.shipment.deserialize_cbor(
            data["OutboundShipment"]
        )
    return out
