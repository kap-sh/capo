"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectClientAlias``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.port_number
    import capo_ecs.types.service_connect_test_traffic_rules
    import capo_ecs.types.string


class ServiceConnectClientAlias(TypedDict, closed=True):
    port: "capo_ecs.types.port_number.PortNumber"
    """<p>The listening port number for the Service Connect proxy. This port is available inside of all of the tasks within the same namespace.</p> <p>To avoid changing your applications in client Amazon ECS services, set this to the same port that the client application uses by default. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    dns_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>dnsName</code> is the name that you use in the applications of client tasks to connect to this service. The name must be a valid DNS name but doesn't need to be fully-qualified. The name can include up to 127 characters. The name can include lowercase letters, numbers, underscores (_), hyphens (-), and periods (.). The name can't start with a hyphen.</p> <p>If this parameter isn't specified, the default value of <code>discoveryName.namespace</code> is used. If the <code>discoveryName</code> isn't specified, the port mapping name from the task definition is used in <code>portName.namespace</code>.</p> <p>To avoid changing your applications in client Amazon ECS services, set this to the same name that the client application uses by default. For example, a few common names are <code>database</code>, <code>db</code>, or the lowercase name of a database, such as <code>mysql</code> or <code>redis</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    test_traffic_rules: NotRequired[
        "capo_ecs.types.service_connect_test_traffic_rules.ServiceConnectTestTrafficRules"
    ]
    """<p>The configuration for test traffic routing rules used during blue/green deployments with Amazon ECS Service Connect. This allows you to route a portion of traffic to the new service revision of your service for testing before shifting all production traffic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectClientAlias) -> dict:
    out: dict = {}
    out["port"] = value["port"]
    if "dns_name" in value:
        out["dnsName"] = value["dns_name"]
    if "test_traffic_rules" in value:
        import capo_ecs.types.service_connect_test_traffic_rules

        out["testTrafficRules"] = (
            capo_ecs.types.service_connect_test_traffic_rules.serialize_aws_json_1_1(
                value["test_traffic_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceConnectClientAlias:
    out: ServiceConnectClientAlias = {}  # type: ignore[typeddict-item]
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        raise DeserializationError("ServiceConnectClientAlias.port required")
    if data.get("dnsName") is not None:
        out["dns_name"] = data["dnsName"]
    if data.get("testTrafficRules") is not None:
        import capo_ecs.types.service_connect_test_traffic_rules

        out["test_traffic_rules"] = (
            capo_ecs.types.service_connect_test_traffic_rules.deserialize_aws_json_1_1(
                data["testTrafficRules"]
            )
        )
    return out
