"""Generated from Smithy shape ``com.amazonaws.panorama#NodeInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.node_id
    import capo_panorama.types.node_instance_id
    import capo_panorama.types.node_instance_status
    import capo_panorama.types.node_name
    import capo_panorama.types.node_package_name
    import capo_panorama.types.node_package_patch_version
    import capo_panorama.types.node_package_version


class NodeInstance(TypedDict, closed=True):
    node_instance_id: "capo_panorama.types.node_instance_id.NodeInstanceId"
    """<p>The instance's ID.</p>"""
    node_id: NotRequired["capo_panorama.types.node_id.NodeId"]
    """<p>The node's ID.</p>"""
    package_name: NotRequired["capo_panorama.types.node_package_name.NodePackageName"]
    """<p>The instance's package name.</p>"""
    package_version: NotRequired[
        "capo_panorama.types.node_package_version.NodePackageVersion"
    ]
    """<p>The instance's package version.</p>"""
    package_patch_version: NotRequired[
        "capo_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    ]
    """<p>The instance's package patch version.</p>"""
    node_name: NotRequired["capo_panorama.types.node_name.NodeName"]
    """<p>The instance's name.</p>"""
    current_status: "capo_panorama.types.node_instance_status.NodeInstanceStatus"
    """<p>The instance's current status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeInstance) -> dict:
    out: dict = {}
    out["NodeInstanceId"] = value["node_instance_id"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "package_name" in value:
        out["PackageName"] = value["package_name"]
    if "package_version" in value:
        out["PackageVersion"] = value["package_version"]
    if "package_patch_version" in value:
        out["PackagePatchVersion"] = value["package_patch_version"]
    if "node_name" in value:
        out["NodeName"] = value["node_name"]
    out["CurrentStatus"] = value["current_status"]
    return out


def deserialize_json(data: dict) -> NodeInstance:
    out: NodeInstance = {}  # type: ignore[typeddict-item]
    if data.get("NodeInstanceId") is not None:
        out["node_instance_id"] = data["NodeInstanceId"]
    else:
        out["node_instance_id"] = ""
    if data.get("NodeId") is not None:
        out["node_id"] = data["NodeId"]
    if data.get("PackageName") is not None:
        out["package_name"] = data["PackageName"]
    if data.get("PackageVersion") is not None:
        out["package_version"] = data["PackageVersion"]
    if data.get("PackagePatchVersion") is not None:
        out["package_patch_version"] = data["PackagePatchVersion"]
    if data.get("NodeName") is not None:
        out["node_name"] = data["NodeName"]
    if data.get("CurrentStatus") is not None:
        out["current_status"] = data["CurrentStatus"]
    else:
        out["current_status"] = ""
    return out
