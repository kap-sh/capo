"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.log_configuration
    import capo_ecs.types.service_connect_access_log_configuration
    import capo_ecs.types.service_connect_service_list
    import capo_ecs.types.string


class ServiceConnectConfiguration(TypedDict, closed=True):
    enabled: "capo_ecs.types.boolean.Boolean"
    """<p>Specifies whether to use Service Connect with this service.</p>"""
    namespace: NotRequired["capo_ecs.types.string.String"]
    """<p>The namespace name or full Amazon Resource Name (ARN) of the Cloud Map namespace for use with Service Connect. The namespace must be in the same Amazon Web Services Region as the Amazon ECS service and cluster. The type of namespace doesn't affect Service Connect. For more information about Cloud Map, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html">Working with Services</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    services: NotRequired[
        "capo_ecs.types.service_connect_service_list.ServiceConnectServiceList"
    ]
    """<p>The list of Service Connect service objects. These are names and aliases (also known as endpoints) that are used by other Amazon ECS services to connect to this service. </p> <p>This field is not required for a "client" Amazon ECS service that's a member of a namespace only to connect to other services within the namespace. An example of this would be a frontend application that accepts incoming requests from either a load balancer that's attached to the service or by other means.</p> <p>An object selects a port from the task definition, assigns a name for the Cloud Map service, and a list of aliases (endpoints) and ports for client applications to refer to this service.</p>"""
    log_configuration: NotRequired["capo_ecs.types.log_configuration.LogConfiguration"]
    access_log_configuration: NotRequired[
        "capo_ecs.types.service_connect_access_log_configuration.ServiceConnectAccessLogConfiguration"
    ]
    """<p>The configuration for Service Connect access logging. Access logs capture detailed information about requests made to your service, including request patterns, response codes, and timing data. They can be useful for debugging connectivity issues, monitoring service performance, and auditing service-to-service communication for security and compliance purposes.</p> <note> <p>To enable access logs, you must also specify a <code>logConfiguration</code> in the <code>serviceConnectConfiguration</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "services" in value:
        import capo_ecs.types.service_connect_service_list

        out["services"] = (
            capo_ecs.types.service_connect_service_list.serialize_aws_json_1_1(
                value["services"]
            )
        )
    if "log_configuration" in value:
        import capo_ecs.types.log_configuration

        out["logConfiguration"] = (
            capo_ecs.types.log_configuration.serialize_aws_json_1_1(
                value["log_configuration"]
            )
        )
    if "access_log_configuration" in value:
        import capo_ecs.types.service_connect_access_log_configuration

        out["accessLogConfiguration"] = (
            capo_ecs.types.service_connect_access_log_configuration.serialize_aws_json_1_1(
                value["access_log_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceConnectConfiguration:
    out: ServiceConnectConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("services") is not None:
        import capo_ecs.types.service_connect_service_list

        out["services"] = (
            capo_ecs.types.service_connect_service_list.deserialize_aws_json_1_1(
                data["services"]
            )
        )
    if data.get("logConfiguration") is not None:
        import capo_ecs.types.log_configuration

        out["log_configuration"] = (
            capo_ecs.types.log_configuration.deserialize_aws_json_1_1(
                data["logConfiguration"]
            )
        )
    if data.get("accessLogConfiguration") is not None:
        import capo_ecs.types.service_connect_access_log_configuration

        out["access_log_configuration"] = (
            capo_ecs.types.service_connect_access_log_configuration.deserialize_aws_json_1_1(
                data["accessLogConfiguration"]
            )
        )
    return out
