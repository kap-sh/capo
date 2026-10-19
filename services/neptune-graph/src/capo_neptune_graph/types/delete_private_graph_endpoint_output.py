"""Generated from Smithy shape ``com.amazonaws.neptunegraph#DeletePrivateGraphEndpointOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.private_graph_endpoint_status
    import capo_neptune_graph.types.subnet_ids
    import capo_neptune_graph.types.vpc_endpoint_id
    import capo_neptune_graph.types.vpc_id


class DeletePrivateGraphEndpointOutput(TypedDict, closed=True):
    vpc_id: "capo_neptune_graph.types.vpc_id.VpcId"
    """<p>The ID of the VPC where the private endpoint was deleted.</p>"""
    subnet_ids: "capo_neptune_graph.types.subnet_ids.SubnetIds"
    """<p>The subnet IDs involved.</p>"""
    status: "capo_neptune_graph.types.private_graph_endpoint_status.PrivateGraphEndpointStatus"
    """<p>The status of the delete operation.</p>"""
    vpc_endpoint_id: NotRequired[
        "capo_neptune_graph.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>The ID of the VPC endpoint that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePrivateGraphEndpointOutput) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import capo_neptune_graph.types.subnet_ids

    out["subnetIds"] = capo_neptune_graph.types.subnet_ids.serialize_json(
        value["subnet_ids"]
    )
    import capo_neptune_graph.types.private_graph_endpoint_status

    out["status"] = (
        capo_neptune_graph.types.private_graph_endpoint_status.serialize_json(
            value["status"]
        )
    )
    if "vpc_endpoint_id" in value:
        out["vpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_json(data: dict) -> DeletePrivateGraphEndpointOutput:
    out: DeletePrivateGraphEndpointOutput = {}  # type: ignore[typeddict-item]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("subnetIds") is not None:
        import capo_neptune_graph.types.subnet_ids

        out["subnet_ids"] = capo_neptune_graph.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    else:
        out["subnet_ids"] = []
    if data.get("status") is not None:
        import capo_neptune_graph.types.private_graph_endpoint_status

        out["status"] = (
            capo_neptune_graph.types.private_graph_endpoint_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_neptune_graph.types.private_graph_endpoint_status.PrivateGraphEndpointStatus",
            "",
        )
    if data.get("vpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["vpcEndpointId"]
    return out
