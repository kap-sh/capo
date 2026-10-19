"""Generated from Smithy shape ``com.amazonaws.rtbfabric#RejectLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rtbfabric.types.connectivity_type
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.link_attributes
    import capo_rtbfabric.types.link_direction
    import capo_rtbfabric.types.link_id
    import capo_rtbfabric.types.link_log_settings
    import capo_rtbfabric.types.link_status
    import capo_rtbfabric.types.module_configuration_list


class RejectLinkResponse(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    peer_gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the peer gateway.</p>"""
    status: "capo_rtbfabric.types.link_status.LinkStatus"
    """<p>The status of the link.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the link was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the link was updated.</p>"""
    direction: NotRequired["capo_rtbfabric.types.link_direction.LinkDirection"]
    """<p>The direction of the link.</p>"""
    flow_modules: NotRequired[
        "capo_rtbfabric.types.module_configuration_list.ModuleConfigurationList"
    ]
    """<p>The configuration of flow modules.</p>"""
    pending_flow_modules: NotRequired[
        "capo_rtbfabric.types.module_configuration_list.ModuleConfigurationList"
    ]
    """<p>The configuration of pending flow modules.</p>"""
    attributes: NotRequired["capo_rtbfabric.types.link_attributes.LinkAttributes"]
    """<p>Attributes of the link.</p>"""
    log_settings: NotRequired["capo_rtbfabric.types.link_log_settings.LinkLogSettings"]
    connectivity_type: NotRequired[
        "capo_rtbfabric.types.connectivity_type.ConnectivityType"
    ]
    """<p>The connectivity type of the link.</p>"""
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectLinkResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["peerGatewayId"] = value["peer_gateway_id"]
    import capo_rtbfabric.types.link_status

    out["status"] = capo_rtbfabric.types.link_status.serialize_json(value["status"])
    import capo_rtbfabric.types._prelude.timestamp

    out["createdAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_rtbfabric.types._prelude.timestamp

    out["updatedAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "direction" in value:
        import capo_rtbfabric.types.link_direction

        out["direction"] = capo_rtbfabric.types.link_direction.serialize_json(
            value["direction"]
        )
    if "flow_modules" in value:
        import capo_rtbfabric.types.module_configuration_list

        out["flowModules"] = (
            capo_rtbfabric.types.module_configuration_list.serialize_json(
                value["flow_modules"]
            )
        )
    if "pending_flow_modules" in value:
        import capo_rtbfabric.types.module_configuration_list

        out["pendingFlowModules"] = (
            capo_rtbfabric.types.module_configuration_list.serialize_json(
                value["pending_flow_modules"]
            )
        )
    if "attributes" in value:
        import capo_rtbfabric.types.link_attributes

        out["attributes"] = capo_rtbfabric.types.link_attributes.serialize_json(
            value["attributes"]
        )
    if "log_settings" in value:
        import capo_rtbfabric.types.link_log_settings

        out["logSettings"] = capo_rtbfabric.types.link_log_settings.serialize_json(
            value["log_settings"]
        )
    if "connectivity_type" in value:
        import capo_rtbfabric.types.connectivity_type

        out["connectivityType"] = capo_rtbfabric.types.connectivity_type.serialize_json(
            value["connectivity_type"]
        )
    out["linkId"] = value["link_id"]
    return out


def deserialize_json(data: dict) -> RejectLinkResponse:
    out: RejectLinkResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    else:
        out["gateway_id"] = ""
    if data.get("peerGatewayId") is not None:
        out["peer_gateway_id"] = data["peerGatewayId"]
    else:
        out["peer_gateway_id"] = ""
    if data.get("status") is not None:
        import capo_rtbfabric.types.link_status

        out["status"] = capo_rtbfabric.types.link_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_rtbfabric.types.link_status.LinkStatus", "")
    if data.get("createdAt") is not None:
        import capo_rtbfabric.types._prelude.timestamp

        out["created_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_rtbfabric.types._prelude.timestamp

        out["updated_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("direction") is not None:
        import capo_rtbfabric.types.link_direction

        out["direction"] = capo_rtbfabric.types.link_direction.deserialize_json(
            data["direction"]
        )
    if data.get("flowModules") is not None:
        import capo_rtbfabric.types.module_configuration_list

        out["flow_modules"] = (
            capo_rtbfabric.types.module_configuration_list.deserialize_json(
                data["flowModules"]
            )
        )
    if data.get("pendingFlowModules") is not None:
        import capo_rtbfabric.types.module_configuration_list

        out["pending_flow_modules"] = (
            capo_rtbfabric.types.module_configuration_list.deserialize_json(
                data["pendingFlowModules"]
            )
        )
    if data.get("attributes") is not None:
        import capo_rtbfabric.types.link_attributes

        out["attributes"] = capo_rtbfabric.types.link_attributes.deserialize_json(
            data["attributes"]
        )
    if data.get("logSettings") is not None:
        import capo_rtbfabric.types.link_log_settings

        out["log_settings"] = capo_rtbfabric.types.link_log_settings.deserialize_json(
            data["logSettings"]
        )
    if data.get("connectivityType") is not None:
        import capo_rtbfabric.types.connectivity_type

        out["connectivity_type"] = (
            capo_rtbfabric.types.connectivity_type.deserialize_json(
                data["connectivityType"]
            )
        )
    if data.get("linkId") is not None:
        out["link_id"] = data["linkId"]
    else:
        out["link_id"] = ""
    return out
