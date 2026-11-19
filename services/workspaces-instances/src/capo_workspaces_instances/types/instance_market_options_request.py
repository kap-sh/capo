"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceMarketOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.market_type_enum
    import capo_workspaces_instances.types.spot_market_options


class InstanceMarketOptionsRequest(TypedDict, closed=True):
    market_type: NotRequired[
        "capo_workspaces_instances.types.market_type_enum.MarketTypeEnum"
    ]
    """<p>Specifies the type of marketplace for instance deployment.</p>"""
    spot_options: NotRequired[
        "capo_workspaces_instances.types.spot_market_options.SpotMarketOptions"
    ]
    """<p>Configuration options for spot instance deployment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceMarketOptionsRequest) -> dict:
    out: dict = {}
    if "market_type" in value:
        import capo_workspaces_instances.types.market_type_enum

        out["MarketType"] = (
            capo_workspaces_instances.types.market_type_enum.serialize_aws_json_1_0(
                value["market_type"]
            )
        )
    if "spot_options" in value:
        import capo_workspaces_instances.types.spot_market_options

        out["SpotOptions"] = (
            capo_workspaces_instances.types.spot_market_options.serialize_aws_json_1_0(
                value["spot_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceMarketOptionsRequest:
    out: InstanceMarketOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MarketType") is not None:
        import capo_workspaces_instances.types.market_type_enum

        out["market_type"] = (
            capo_workspaces_instances.types.market_type_enum.deserialize_aws_json_1_0(
                data["MarketType"]
            )
        )
    if data.get("SpotOptions") is not None:
        import capo_workspaces_instances.types.spot_market_options

        out["spot_options"] = (
            capo_workspaces_instances.types.spot_market_options.deserialize_aws_json_1_0(
                data["SpotOptions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceMarketOptionsRequest) -> dict:
    out: dict = {}
    if "market_type" in value:
        import capo_workspaces_instances.types.market_type_enum

        out["MarketType"] = (
            capo_workspaces_instances.types.market_type_enum.serialize_cbor(
                value["market_type"]
            )
        )
    if "spot_options" in value:
        import capo_workspaces_instances.types.spot_market_options

        out["SpotOptions"] = (
            capo_workspaces_instances.types.spot_market_options.serialize_cbor(
                value["spot_options"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> InstanceMarketOptionsRequest:
    out: InstanceMarketOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MarketType") is not None:
        import capo_workspaces_instances.types.market_type_enum

        out["market_type"] = (
            capo_workspaces_instances.types.market_type_enum.deserialize_cbor(
                data["MarketType"]
            )
        )
    if data.get("SpotOptions") is not None:
        import capo_workspaces_instances.types.spot_market_options

        out["spot_options"] = (
            capo_workspaces_instances.types.spot_market_options.deserialize_cbor(
                data["SpotOptions"]
            )
        )
    return out
