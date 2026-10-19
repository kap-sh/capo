"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DiscoverInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.attributes
    import capo_servicediscovery.types.aws_account_id
    import capo_servicediscovery.types.discover_max_results
    import capo_servicediscovery.types.health_status_filter
    import capo_servicediscovery.types.namespace_name
    import capo_servicediscovery.types.service_name


class DiscoverInstancesRequest(TypedDict, closed=True):
    namespace_name: "capo_servicediscovery.types.namespace_name.NamespaceName"
    """<p>The <code>HttpName</code> name of the namespace. The <code>HttpName</code> is found in the <code>HttpProperties</code> member of the <code>Properties</code> member of the namespace. In most cases, <code>Name</code> and <code>HttpName</code> match. However, if you reuse <code>Name</code> for namespace creation, a generated hash is added to <code>HttpName</code> to distinguish the two.</p>"""
    service_name: "capo_servicediscovery.types.service_name.ServiceName"
    """<p>The name of the service that you specified when you registered the instance.</p>"""
    max_results: NotRequired[
        "capo_servicediscovery.types.discover_max_results.DiscoverMaxResults"
    ]
    """<p>The maximum number of instances that you want Cloud Map to return in the response to a <code>DiscoverInstances</code> request. If you don't specify a value for <code>MaxResults</code>, Cloud Map returns up to 100 instances.</p>"""
    query_parameters: NotRequired["capo_servicediscovery.types.attributes.Attributes"]
    """<p>Filters to scope the results based on custom attributes for the instance (for example, <code>{version=v1, az=1a}</code>). Only instances that match all the specified key-value pairs are returned.</p>"""
    optional_parameters: NotRequired[
        "capo_servicediscovery.types.attributes.Attributes"
    ]
    """<p>Opportunistic filters to scope the results based on custom attributes. If there are instances that match both the filters specified in both the <code>QueryParameters</code> parameter and this parameter, all of these instances are returned. Otherwise, the filters are ignored, and only instances that match the filters that are specified in the <code>QueryParameters</code> parameter are returned.</p>"""
    health_status: NotRequired[
        "capo_servicediscovery.types.health_status_filter.HealthStatusFilter"
    ]
    """<p>The health status of the instances that you want to discover. This parameter is ignored for services that don't have a health check configured, and all instances are returned.</p> <dl> <dt>HEALTHY</dt> <dd> <p>Returns healthy instances.</p> </dd> <dt>UNHEALTHY</dt> <dd> <p>Returns unhealthy instances.</p> </dd> <dt>ALL</dt> <dd> <p>Returns all instances.</p> </dd> <dt>HEALTHY_OR_ELSE_ALL</dt> <dd> <p>Returns healthy instances, unless none are reporting a healthy state. In that case, return all instances. This is also called failing open.</p> </dd> </dl>"""
    owner_account: NotRequired[
        "capo_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that owns the namespace associated with the instance, as specified in the namespace <code>ResourceOwner</code> field. For instances associated with namespaces that are shared with your account, you must specify an <code>OwnerAccount</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoverInstancesRequest) -> dict:
    out: dict = {}
    out["NamespaceName"] = value["namespace_name"]
    out["ServiceName"] = value["service_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "query_parameters" in value:
        import capo_servicediscovery.types.attributes

        out["QueryParameters"] = (
            capo_servicediscovery.types.attributes.serialize_aws_json_1_1(
                value["query_parameters"]
            )
        )
    if "optional_parameters" in value:
        import capo_servicediscovery.types.attributes

        out["OptionalParameters"] = (
            capo_servicediscovery.types.attributes.serialize_aws_json_1_1(
                value["optional_parameters"]
            )
        )
    if "health_status" in value:
        import capo_servicediscovery.types.health_status_filter

        out["HealthStatus"] = (
            capo_servicediscovery.types.health_status_filter.serialize_aws_json_1_1(
                value["health_status"]
            )
        )
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoverInstancesRequest:
    out: DiscoverInstancesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NamespaceName") is not None:
        out["namespace_name"] = data["NamespaceName"]
    else:
        out["namespace_name"] = ""
    if data.get("ServiceName") is not None:
        out["service_name"] = data["ServiceName"]
    else:
        out["service_name"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("QueryParameters") is not None:
        import capo_servicediscovery.types.attributes

        out["query_parameters"] = (
            capo_servicediscovery.types.attributes.deserialize_aws_json_1_1(
                data["QueryParameters"]
            )
        )
    if data.get("OptionalParameters") is not None:
        import capo_servicediscovery.types.attributes

        out["optional_parameters"] = (
            capo_servicediscovery.types.attributes.deserialize_aws_json_1_1(
                data["OptionalParameters"]
            )
        )
    if data.get("HealthStatus") is not None:
        import capo_servicediscovery.types.health_status_filter

        out["health_status"] = (
            capo_servicediscovery.types.health_status_filter.deserialize_aws_json_1_1(
                data["HealthStatus"]
            )
        )
    if data.get("OwnerAccount") is not None:
        out["owner_account"] = data["OwnerAccount"]
    return out
