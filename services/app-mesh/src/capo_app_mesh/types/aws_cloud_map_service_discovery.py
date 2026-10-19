"""Generated from Smithy shape ``com.amazonaws.appmesh#AwsCloudMapServiceDiscovery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.aws_cloud_map_instance_attributes
    import capo_app_mesh.types.aws_cloud_map_name
    import capo_app_mesh.types.ip_preference


class AwsCloudMapServiceDiscovery(TypedDict, closed=True):
    namespace_name: "capo_app_mesh.types.aws_cloud_map_name.AwsCloudMapName"
    """<p>The name of the Cloud Map namespace to use.</p>"""
    service_name: "capo_app_mesh.types.aws_cloud_map_name.AwsCloudMapName"
    """<p>The name of the Cloud Map service to use.</p>"""
    attributes: NotRequired[
        "capo_app_mesh.types.aws_cloud_map_instance_attributes.AwsCloudMapInstanceAttributes"
    ]
    """<p>A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.</p>"""
    ip_preference: NotRequired["capo_app_mesh.types.ip_preference.IpPreference"]
    """<p>The preferred IP version that this virtual node uses. Setting the IP preference on the virtual node only overrides the IP preference set for the mesh on this specific node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudMapServiceDiscovery) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    out["serviceName"] = value["service_name"]
    if "attributes" in value:
        import capo_app_mesh.types.aws_cloud_map_instance_attributes

        out["attributes"] = (
            capo_app_mesh.types.aws_cloud_map_instance_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "ip_preference" in value:
        out["ipPreference"] = value["ip_preference"]
    return out


def deserialize_json(data: dict) -> AwsCloudMapServiceDiscovery:
    out: AwsCloudMapServiceDiscovery = {}  # type: ignore[typeddict-item]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    else:
        out["namespace_name"] = ""
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("attributes") is not None:
        import capo_app_mesh.types.aws_cloud_map_instance_attributes

        out["attributes"] = (
            capo_app_mesh.types.aws_cloud_map_instance_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if data.get("ipPreference") is not None:
        out["ip_preference"] = data["ipPreference"]
    return out
