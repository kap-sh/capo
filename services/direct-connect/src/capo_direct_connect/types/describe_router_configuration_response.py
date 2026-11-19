"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeRouterConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.router_config
    import capo_direct_connect.types.router_type
    import capo_direct_connect.types.virtual_interface_id
    import capo_direct_connect.types.virtual_interface_name


class DescribeRouterConfigurationResponse(TypedDict, closed=True):
    customer_router_config: NotRequired[
        "capo_direct_connect.types.router_config.RouterConfig"
    ]
    """<p>The customer router configuration.</p>"""
    router: NotRequired["capo_direct_connect.types.router_type.RouterType"]
    """<p>The details about the router.</p>"""
    virtual_interface_id: NotRequired[
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID assigned to the virtual interface.</p>"""
    virtual_interface_name: NotRequired[
        "capo_direct_connect.types.virtual_interface_name.VirtualInterfaceName"
    ]
    """<p>Provides the details about a virtual interface's router.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRouterConfigurationResponse) -> dict:
    out: dict = {}
    if "customer_router_config" in value:
        out["customerRouterConfig"] = value["customer_router_config"]
    if "router" in value:
        import capo_direct_connect.types.router_type

        out["router"] = capo_direct_connect.types.router_type.serialize_aws_json_1_1(
            value["router"]
        )
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "virtual_interface_name" in value:
        out["virtualInterfaceName"] = value["virtual_interface_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRouterConfigurationResponse:
    out: DescribeRouterConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("customerRouterConfig") is not None:
        out["customer_router_config"] = data["customerRouterConfig"]
    if data.get("router") is not None:
        import capo_direct_connect.types.router_type

        out["router"] = capo_direct_connect.types.router_type.deserialize_aws_json_1_1(
            data["router"]
        )
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("virtualInterfaceName") is not None:
        out["virtual_interface_name"] = data["virtualInterfaceName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeRouterConfigurationResponse) -> dict:
    out: dict = {}
    if "customer_router_config" in value:
        out["customerRouterConfig"] = value["customer_router_config"]
    if "router" in value:
        import capo_direct_connect.types.router_type

        out["router"] = capo_direct_connect.types.router_type.serialize_cbor(
            value["router"]
        )
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "virtual_interface_name" in value:
        out["virtualInterfaceName"] = value["virtual_interface_name"]
    return out


def deserialize_cbor(data: dict) -> DescribeRouterConfigurationResponse:
    out: DescribeRouterConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("customerRouterConfig") is not None:
        out["customer_router_config"] = data["customerRouterConfig"]
    if data.get("router") is not None:
        import capo_direct_connect.types.router_type

        out["router"] = capo_direct_connect.types.router_type.deserialize_cbor(
            data["router"]
        )
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("virtualInterfaceName") is not None:
        out["virtual_interface_name"] = data["virtualInterfaceName"]
    return out
