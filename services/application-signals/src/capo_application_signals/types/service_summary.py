"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.attribute_maps
    import capo_application_signals.types.attributes
    import capo_application_signals.types.metric_references
    import capo_application_signals.types.service_groups


class ServiceSummary(TypedDict, closed=True):
    key_attributes: "capo_application_signals.types.attributes.Attributes"
    """<p>This is a string-to-string map that help identify the objects discovered by Application Signals. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>"""
    attribute_maps: NotRequired[
        "capo_application_signals.types.attribute_maps.AttributeMaps"
    ]
    """<p>This structure contains one or more string-to-string maps that help identify this service. It can include <i>platform attributes</i>, <i>application attributes</i>, and <i>telemetry attributes</i>.</p> <p>Platform attributes contain information the service's platform.</p> <ul> <li> <p> <code>PlatformType</code> defines the hosted-in platform.</p> </li> <li> <p> <code>EKS.Cluster</code> is the name of the Amazon EKS cluster.</p> </li> <li> <p> <code>K8s.Cluster</code> is the name of the self-hosted Kubernetes cluster.</p> </li> <li> <p> <code>K8s.Namespace</code> is the name of the Kubernetes namespace in either Amazon EKS or Kubernetes clusters.</p> </li> <li> <p> <code>K8s.Workload</code> is the name of the Kubernetes workload in either Amazon EKS or Kubernetes clusters.</p> </li> <li> <p> <code>K8s.Node</code> is the name of the Kubernetes node in either Amazon EKS or Kubernetes clusters.</p> </li> <li> <p> <code>K8s.Pod</code> is the name of the Kubernetes pod in either Amazon EKS or Kubernetes clusters.</p> </li> <li> <p> <code>EC2.AutoScalingGroup</code> is the name of the Amazon EC2 Auto Scaling group.</p> </li> <li> <p> <code>EC2.InstanceId</code> is the ID of the Amazon EC2 instance.</p> </li> <li> <p> <code>Host</code> is the name of the host, for all platform types.</p> </li> </ul> <p>Application attributes contain information about the application.</p> <ul> <li> <p> <code>AWS.Application</code> is the application's name in Amazon Web Services Service Catalog AppRegistry.</p> </li> <li> <p> <code>AWS.Application.ARN</code> is the application's ARN in Amazon Web Services Service Catalog AppRegistry.</p> </li> </ul> <p>Telemetry attributes contain telemetry information.</p> <ul> <li> <p> <code>Telemetry.SDK</code> is the fingerprint of the OpenTelemetry SDK version for instrumented services.</p> </li> <li> <p> <code>Telemetry.Agent</code> is the fingerprint of the agent used to collect and send telemetry data.</p> </li> <li> <p> <code>Telemetry.Source</code> Specifies the point of application where the telemetry was collected or specifies what was used for the source of telemetry data.</p> </li> </ul>"""
    metric_references: (
        "capo_application_signals.types.metric_references.MetricReferences"
    )
    """<p>An array of structures that each contain information about one metric associated with this service.</p>"""
    service_groups: NotRequired[
        "capo_application_signals.types.service_groups.ServiceGroups"
    ]
    """<p>An array of service groups that this service belongs to, based on the configured grouping attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceSummary) -> dict:
    out: dict = {}
    import capo_application_signals.types.attributes

    out["KeyAttributes"] = capo_application_signals.types.attributes.serialize_json(
        value["key_attributes"]
    )
    if "attribute_maps" in value:
        import capo_application_signals.types.attribute_maps

        out["AttributeMaps"] = (
            capo_application_signals.types.attribute_maps.serialize_json(
                value["attribute_maps"]
            )
        )
    import capo_application_signals.types.metric_references

    out["MetricReferences"] = (
        capo_application_signals.types.metric_references.serialize_json(
            value["metric_references"]
        )
    )
    if "service_groups" in value:
        import capo_application_signals.types.service_groups

        out["ServiceGroups"] = (
            capo_application_signals.types.service_groups.serialize_json(
                value["service_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceSummary:
    out: ServiceSummary = {}  # type: ignore[typeddict-item]
    if data.get("KeyAttributes") is not None:
        import capo_application_signals.types.attributes

        out["key_attributes"] = (
            capo_application_signals.types.attributes.deserialize_json(
                data["KeyAttributes"]
            )
        )
    else:
        out["key_attributes"] = {}
    if data.get("AttributeMaps") is not None:
        import capo_application_signals.types.attribute_maps

        out["attribute_maps"] = (
            capo_application_signals.types.attribute_maps.deserialize_json(
                data["AttributeMaps"]
            )
        )
    if data.get("MetricReferences") is not None:
        import capo_application_signals.types.metric_references

        out["metric_references"] = (
            capo_application_signals.types.metric_references.deserialize_json(
                data["MetricReferences"]
            )
        )
    else:
        out["metric_references"] = []
    if data.get("ServiceGroups") is not None:
        import capo_application_signals.types.service_groups

        out["service_groups"] = (
            capo_application_signals.types.service_groups.deserialize_json(
                data["ServiceGroups"]
            )
        )
    return out
