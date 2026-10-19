"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateSignalCatalogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.node_paths
    import capo_iotfleetwise.types.nodes
    import capo_iotfleetwise.types.resource_name


class UpdateSignalCatalogRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the signal catalog to update. </p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p> A brief description of the signal catalog to update.</p>"""
    nodes_to_add: NotRequired["capo_iotfleetwise.types.nodes.Nodes"]
    """<p> A list of information about nodes to add to the signal catalog. </p>"""
    nodes_to_update: NotRequired["capo_iotfleetwise.types.nodes.Nodes"]
    """<p> A list of information about nodes to update in the signal catalog. </p>"""
    nodes_to_remove: NotRequired["capo_iotfleetwise.types.node_paths.NodePaths"]
    """<p> A list of <code>fullyQualifiedName</code> of nodes to remove from the signal catalog. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSignalCatalogRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "nodes_to_add" in value:
        import capo_iotfleetwise.types.nodes

        out["nodesToAdd"] = capo_iotfleetwise.types.nodes.serialize_aws_json_1_0(
            value["nodes_to_add"]
        )
    if "nodes_to_update" in value:
        import capo_iotfleetwise.types.nodes

        out["nodesToUpdate"] = capo_iotfleetwise.types.nodes.serialize_aws_json_1_0(
            value["nodes_to_update"]
        )
    if "nodes_to_remove" in value:
        import capo_iotfleetwise.types.node_paths

        out["nodesToRemove"] = (
            capo_iotfleetwise.types.node_paths.serialize_aws_json_1_0(
                value["nodes_to_remove"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSignalCatalogRequest:
    out: UpdateSignalCatalogRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("nodesToAdd") is not None:
        import capo_iotfleetwise.types.nodes

        out["nodes_to_add"] = capo_iotfleetwise.types.nodes.deserialize_aws_json_1_0(
            data["nodesToAdd"]
        )
    if data.get("nodesToUpdate") is not None:
        import capo_iotfleetwise.types.nodes

        out["nodes_to_update"] = capo_iotfleetwise.types.nodes.deserialize_aws_json_1_0(
            data["nodesToUpdate"]
        )
    if data.get("nodesToRemove") is not None:
        import capo_iotfleetwise.types.node_paths

        out["nodes_to_remove"] = (
            capo_iotfleetwise.types.node_paths.deserialize_aws_json_1_0(
                data["nodesToRemove"]
            )
        )
    return out
