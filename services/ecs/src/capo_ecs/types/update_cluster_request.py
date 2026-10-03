"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.cluster_configuration
    import capo_ecs.types.cluster_service_connect_defaults_request
    import capo_ecs.types.cluster_settings
    import capo_ecs.types.string


class UpdateClusterRequest(TypedDict, closed=True):
    cluster: "capo_ecs.types.string.String"
    """<p>The name of the cluster to modify the settings for.</p>"""
    settings: NotRequired["capo_ecs.types.cluster_settings.ClusterSettings"]
    """<p>The cluster settings for your cluster.</p>"""
    configuration: NotRequired[
        "capo_ecs.types.cluster_configuration.ClusterConfiguration"
    ]
    """<p>The execute command configuration for the cluster.</p>"""
    service_connect_defaults: NotRequired[
        "capo_ecs.types.cluster_service_connect_defaults_request.ClusterServiceConnectDefaultsRequest"
    ]
    """<p>Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the <code>enabled</code> parameter to <code>true</code> in the <code>ServiceConnectConfiguration</code>. You can set the namespace of each service individually in the <code>ServiceConnectConfiguration</code> to override this default parameter.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    if "settings" in value:
        import capo_ecs.types.cluster_settings

        out["settings"] = capo_ecs.types.cluster_settings.serialize_aws_json_1_1(
            value["settings"]
        )
    if "configuration" in value:
        import capo_ecs.types.cluster_configuration

        out["configuration"] = (
            capo_ecs.types.cluster_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "service_connect_defaults" in value:
        import capo_ecs.types.cluster_service_connect_defaults_request

        out["serviceConnectDefaults"] = (
            capo_ecs.types.cluster_service_connect_defaults_request.serialize_aws_json_1_1(
                value["service_connect_defaults"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterRequest:
    out: UpdateClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    else:
        raise DeserializationError("UpdateClusterRequest.cluster required")
    if data.get("settings") is not None:
        import capo_ecs.types.cluster_settings

        out["settings"] = capo_ecs.types.cluster_settings.deserialize_aws_json_1_1(
            data["settings"]
        )
    if data.get("configuration") is not None:
        import capo_ecs.types.cluster_configuration

        out["configuration"] = (
            capo_ecs.types.cluster_configuration.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if data.get("serviceConnectDefaults") is not None:
        import capo_ecs.types.cluster_service_connect_defaults_request

        out["service_connect_defaults"] = (
            capo_ecs.types.cluster_service_connect_defaults_request.deserialize_aws_json_1_1(
                data["serviceConnectDefaults"]
            )
        )
    return out
