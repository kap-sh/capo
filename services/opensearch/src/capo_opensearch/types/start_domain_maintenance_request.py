"""Generated from Smithy shape ``com.amazonaws.opensearch#StartDomainMaintenanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.maintenance_type
    import capo_opensearch.types.node_id


class StartDomainMaintenanceRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    action: "capo_opensearch.types.maintenance_type.MaintenanceType"
    """<p>The name of the action.</p>"""
    node_id: NotRequired["capo_opensearch.types.node_id.NodeId"]
    """<p>The ID of the data node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDomainMaintenanceRequest) -> dict:
    out: dict = {}
    import capo_opensearch.types.maintenance_type

    out["Action"] = capo_opensearch.types.maintenance_type.serialize_json(
        value["action"]
    )
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    return out


def deserialize_json(data: dict) -> StartDomainMaintenanceRequest:
    out: StartDomainMaintenanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_opensearch.types.maintenance_type

        out["action"] = capo_opensearch.types.maintenance_type.deserialize_json(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_opensearch.types.maintenance_type.MaintenanceType", ""
        )
    if data.get("NodeId") is not None:
        out["node_id"] = data["NodeId"]
    return out
