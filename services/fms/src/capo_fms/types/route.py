"""Generated from Smithy shape ``com.amazonaws.fms#Route``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.destination_type
    import capo_fms.types.length_bounded_string
    import capo_fms.types.target_type


class Route(TypedDict, closed=True):
    destination_type: NotRequired["capo_fms.types.destination_type.DestinationType"]
    """<p>The type of destination for the route.</p>"""
    target_type: NotRequired["capo_fms.types.target_type.TargetType"]
    """<p>The type of target for the route.</p>"""
    destination: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>The destination of the route.</p>"""
    target: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>The route's target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Route) -> dict:
    out: dict = {}
    if "destination_type" in value:
        import capo_fms.types.destination_type

        out["DestinationType"] = capo_fms.types.destination_type.serialize_aws_json_1_1(
            value["destination_type"]
        )
    if "target_type" in value:
        import capo_fms.types.target_type

        out["TargetType"] = capo_fms.types.target_type.serialize_aws_json_1_1(
            value["target_type"]
        )
    if "destination" in value:
        out["Destination"] = value["destination"]
    if "target" in value:
        out["Target"] = value["target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Route:
    out: Route = {}  # type: ignore[typeddict-item]
    if data.get("DestinationType") is not None:
        import capo_fms.types.destination_type

        out["destination_type"] = (
            capo_fms.types.destination_type.deserialize_aws_json_1_1(
                data["DestinationType"]
            )
        )
    if data.get("TargetType") is not None:
        import capo_fms.types.target_type

        out["target_type"] = capo_fms.types.target_type.deserialize_aws_json_1_1(
            data["TargetType"]
        )
    if data.get("Destination") is not None:
        out["destination"] = data["Destination"]
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Route) -> dict:
    out: dict = {}
    if "destination_type" in value:
        import capo_fms.types.destination_type

        out["DestinationType"] = capo_fms.types.destination_type.serialize_cbor(
            value["destination_type"]
        )
    if "target_type" in value:
        import capo_fms.types.target_type

        out["TargetType"] = capo_fms.types.target_type.serialize_cbor(
            value["target_type"]
        )
    if "destination" in value:
        out["Destination"] = value["destination"]
    if "target" in value:
        out["Target"] = value["target"]
    return out


def deserialize_cbor(data: dict) -> Route:
    out: Route = {}  # type: ignore[typeddict-item]
    if data.get("DestinationType") is not None:
        import capo_fms.types.destination_type

        out["destination_type"] = capo_fms.types.destination_type.deserialize_cbor(
            data["DestinationType"]
        )
    if data.get("TargetType") is not None:
        import capo_fms.types.target_type

        out["target_type"] = capo_fms.types.target_type.deserialize_cbor(
            data["TargetType"]
        )
    if data.get("Destination") is not None:
        out["destination"] = data["Destination"]
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    return out
