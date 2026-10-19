"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateModelManifestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.manifest_status
    import capo_iotfleetwise.types.node_paths
    import capo_iotfleetwise.types.resource_name


class UpdateModelManifestRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the vehicle model to update. </p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p> A brief description of the vehicle model. </p>"""
    nodes_to_add: NotRequired["capo_iotfleetwise.types.node_paths.NodePaths"]
    """<p> A list of <code>fullyQualifiedName</code> of nodes, which are a general abstraction of signals, to add to the vehicle model. </p>"""
    nodes_to_remove: NotRequired["capo_iotfleetwise.types.node_paths.NodePaths"]
    """<p> A list of <code>fullyQualifiedName</code> of nodes, which are a general abstraction of signals, to remove from the vehicle model. </p>"""
    status: NotRequired["capo_iotfleetwise.types.manifest_status.ManifestStatus"]
    """<p> The state of the vehicle model. If the status is <code>ACTIVE</code>, the vehicle model can't be edited. If the status is <code>DRAFT</code>, you can edit the vehicle model. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateModelManifestRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "nodes_to_add" in value:
        import capo_iotfleetwise.types.node_paths

        out["nodesToAdd"] = capo_iotfleetwise.types.node_paths.serialize_aws_json_1_0(
            value["nodes_to_add"]
        )
    if "nodes_to_remove" in value:
        import capo_iotfleetwise.types.node_paths

        out["nodesToRemove"] = (
            capo_iotfleetwise.types.node_paths.serialize_aws_json_1_0(
                value["nodes_to_remove"]
            )
        )
    if "status" in value:
        import capo_iotfleetwise.types.manifest_status

        out["status"] = capo_iotfleetwise.types.manifest_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateModelManifestRequest:
    out: UpdateModelManifestRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("nodesToAdd") is not None:
        import capo_iotfleetwise.types.node_paths

        out["nodes_to_add"] = (
            capo_iotfleetwise.types.node_paths.deserialize_aws_json_1_0(
                data["nodesToAdd"]
            )
        )
    if data.get("nodesToRemove") is not None:
        import capo_iotfleetwise.types.node_paths

        out["nodes_to_remove"] = (
            capo_iotfleetwise.types.node_paths.deserialize_aws_json_1_0(
                data["nodesToRemove"]
            )
        )
    if data.get("status") is not None:
        import capo_iotfleetwise.types.manifest_status

        out["status"] = (
            capo_iotfleetwise.types.manifest_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    return out
