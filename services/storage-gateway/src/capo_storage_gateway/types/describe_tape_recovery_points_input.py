"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeTapeRecoveryPointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.marker
    import capo_storage_gateway.types.positive_int_object


class DescribeTapeRecoveryPointsInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    marker: NotRequired["capo_storage_gateway.types.marker.Marker"]
    """<p>An opaque string that indicates the position at which to begin describing the virtual tape recovery points.</p>"""
    limit: NotRequired[
        "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
    ]
    """<p>Specifies that the number of virtual tape recovery points that are described be limited to the specified number.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTapeRecoveryPointsInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTapeRecoveryPointsInput:
    out: DescribeTapeRecoveryPointsInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
