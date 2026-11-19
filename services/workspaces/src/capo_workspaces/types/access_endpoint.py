"""Generated from Smithy shape ``com.amazonaws.workspaces#AccessEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.access_endpoint_type
    import capo_workspaces.types.alphanumeric_dash_underscore_non_empty_string


class AccessEndpoint(TypedDict, closed=True):
    access_endpoint_type: NotRequired[
        "capo_workspaces.types.access_endpoint_type.AccessEndpointType"
    ]
    """<p>Indicates the type of access endpoint.</p>"""
    vpc_endpoint_id: NotRequired[
        "capo_workspaces.types.alphanumeric_dash_underscore_non_empty_string.AlphanumericDashUnderscoreNonEmptyString"
    ]
    """<p>Indicates the VPC endpoint to use for access.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessEndpoint) -> dict:
    out: dict = {}
    if "access_endpoint_type" in value:
        import capo_workspaces.types.access_endpoint_type

        out["AccessEndpointType"] = (
            capo_workspaces.types.access_endpoint_type.serialize_aws_json_1_1(
                value["access_endpoint_type"]
            )
        )
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessEndpoint:
    out: AccessEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("AccessEndpointType") is not None:
        import capo_workspaces.types.access_endpoint_type

        out["access_endpoint_type"] = (
            capo_workspaces.types.access_endpoint_type.deserialize_aws_json_1_1(
                data["AccessEndpointType"]
            )
        )
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessEndpoint) -> dict:
    out: dict = {}
    if "access_endpoint_type" in value:
        import capo_workspaces.types.access_endpoint_type

        out["AccessEndpointType"] = (
            capo_workspaces.types.access_endpoint_type.serialize_cbor(
                value["access_endpoint_type"]
            )
        )
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_cbor(data: dict) -> AccessEndpoint:
    out: AccessEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("AccessEndpointType") is not None:
        import capo_workspaces.types.access_endpoint_type

        out["access_endpoint_type"] = (
            capo_workspaces.types.access_endpoint_type.deserialize_cbor(
                data["AccessEndpointType"]
            )
        )
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    return out
