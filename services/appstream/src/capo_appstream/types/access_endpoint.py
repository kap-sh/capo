"""Generated from Smithy shape ``com.amazonaws.appstream#AccessEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.access_endpoint_type
    import capo_appstream.types.string


class AccessEndpoint(TypedDict, closed=True):
    endpoint_type: NotRequired[
        "capo_appstream.types.access_endpoint_type.AccessEndpointType"
    ]
    """<p>The type of interface endpoint.</p>"""
    vpce_id: NotRequired["capo_appstream.types.string.String"]
    """<p>The identifier (ID) of the VPC in which the interface endpoint is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessEndpoint) -> dict:
    out: dict = {}
    if "endpoint_type" in value:
        import capo_appstream.types.access_endpoint_type

        out["EndpointType"] = (
            capo_appstream.types.access_endpoint_type.serialize_aws_json_1_1(
                value["endpoint_type"]
            )
        )
    if "vpce_id" in value:
        out["VpceId"] = value["vpce_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessEndpoint:
    out: AccessEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("EndpointType") is not None:
        import capo_appstream.types.access_endpoint_type

        out["endpoint_type"] = (
            capo_appstream.types.access_endpoint_type.deserialize_aws_json_1_1(
                data["EndpointType"]
            )
        )
    if data.get("VpceId") is not None:
        out["vpce_id"] = data["VpceId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessEndpoint) -> dict:
    out: dict = {}
    if "endpoint_type" in value:
        import capo_appstream.types.access_endpoint_type

        out["EndpointType"] = capo_appstream.types.access_endpoint_type.serialize_cbor(
            value["endpoint_type"]
        )
    if "vpce_id" in value:
        out["VpceId"] = value["vpce_id"]
    return out


def deserialize_cbor(data: dict) -> AccessEndpoint:
    out: AccessEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("EndpointType") is not None:
        import capo_appstream.types.access_endpoint_type

        out["endpoint_type"] = (
            capo_appstream.types.access_endpoint_type.deserialize_cbor(
                data["EndpointType"]
            )
        )
    if data.get("VpceId") is not None:
        out["vpce_id"] = data["VpceId"]
    return out
