"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HttpInstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.attributes
    import capo_servicediscovery.types.health_status
    import capo_servicediscovery.types.namespace_name_http
    import capo_servicediscovery.types.resource_id
    import capo_servicediscovery.types.service_name


class HttpInstanceSummary(TypedDict, closed=True):
    instance_id: NotRequired["capo_servicediscovery.types.resource_id.ResourceId"]
    """<p>The ID of an instance that matches the values that you specified in the request.</p>"""
    namespace_name: NotRequired[
        "capo_servicediscovery.types.namespace_name_http.NamespaceNameHttp"
    ]
    """<p>The <code>HttpName</code> name of the namespace. It's found in the <code>HttpProperties</code> member of the <code>Properties</code> member of the namespace.</p>"""
    service_name: NotRequired["capo_servicediscovery.types.service_name.ServiceName"]
    """<p>The name of the service that you specified when you registered the instance.</p>"""
    health_status: NotRequired["capo_servicediscovery.types.health_status.HealthStatus"]
    """<p>If you configured health checking in the service, the current health status of the service instance.</p>"""
    attributes: NotRequired["capo_servicediscovery.types.attributes.Attributes"]
    """<p>If you included any attributes when you registered the instance, the values of those attributes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpInstanceSummary) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "namespace_name" in value:
        out["NamespaceName"] = value["namespace_name"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "health_status" in value:
        import capo_servicediscovery.types.health_status

        out["HealthStatus"] = (
            capo_servicediscovery.types.health_status.serialize_aws_json_1_1(
                value["health_status"]
            )
        )
    if "attributes" in value:
        import capo_servicediscovery.types.attributes

        out["Attributes"] = (
            capo_servicediscovery.types.attributes.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpInstanceSummary:
    out: HttpInstanceSummary = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("NamespaceName") is not None:
        out["namespace_name"] = data["NamespaceName"]
    if data.get("ServiceName") is not None:
        out["service_name"] = data["ServiceName"]
    if data.get("HealthStatus") is not None:
        import capo_servicediscovery.types.health_status

        out["health_status"] = (
            capo_servicediscovery.types.health_status.deserialize_aws_json_1_1(
                data["HealthStatus"]
            )
        )
    if data.get("Attributes") is not None:
        import capo_servicediscovery.types.attributes

        out["attributes"] = (
            capo_servicediscovery.types.attributes.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HttpInstanceSummary) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "namespace_name" in value:
        out["NamespaceName"] = value["namespace_name"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "health_status" in value:
        import capo_servicediscovery.types.health_status

        out["HealthStatus"] = capo_servicediscovery.types.health_status.serialize_cbor(
            value["health_status"]
        )
    if "attributes" in value:
        import capo_servicediscovery.types.attributes

        out["Attributes"] = capo_servicediscovery.types.attributes.serialize_cbor(
            value["attributes"]
        )
    return out


def deserialize_cbor(data: dict) -> HttpInstanceSummary:
    out: HttpInstanceSummary = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("NamespaceName") is not None:
        out["namespace_name"] = data["NamespaceName"]
    if data.get("ServiceName") is not None:
        out["service_name"] = data["ServiceName"]
    if data.get("HealthStatus") is not None:
        import capo_servicediscovery.types.health_status

        out["health_status"] = (
            capo_servicediscovery.types.health_status.deserialize_cbor(
                data["HealthStatus"]
            )
        )
    if data.get("Attributes") is not None:
        import capo_servicediscovery.types.attributes

        out["attributes"] = capo_servicediscovery.types.attributes.deserialize_cbor(
            data["Attributes"]
        )
    return out
