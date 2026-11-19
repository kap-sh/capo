"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesApiCall``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.integer
    import capo_guardduty.types.string


class KubernetesApiCall(TypedDict, closed=True):
    cluster_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the cluster.</p>"""
    username: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Kubernetes user name of the caller.</p>"""
    user_groups: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Kubernetes groups of the caller.</p>"""
    user_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the caller.</p>"""
    verb: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Kubernetes API verb, such as <code>get</code> or <code>create</code>.</p>"""
    resource_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The type of the Kubernetes resource.</p>"""
    resource_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the Kubernetes resource.</p>"""
    namespace: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Kubernetes namespace of the resource.</p>"""
    request_uri: NotRequired["capo_guardduty.types.string.String"]
    """<p>The URI of the request.</p>"""
    status_code: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The status code of the API call.</p>"""
    source_ips: NotRequired["capo_guardduty.types.string.String"]
    """<p>The source IP addresses of the API call.</p>"""
    user_agent: NotRequired["capo_guardduty.types.string.String"]
    """<p>The user agent of the caller.</p>"""
    event_count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of matching API calls.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesApiCall) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "username" in value:
        out["username"] = value["username"]
    if "user_groups" in value:
        out["userGroups"] = value["user_groups"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "verb" in value:
        out["verb"] = value["verb"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "request_uri" in value:
        out["requestUri"] = value["request_uri"]
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "source_ips" in value:
        out["sourceIPs"] = value["source_ips"]
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    if "event_count" in value:
        out["eventCount"] = value["event_count"]
    return out


def deserialize_json(data: dict) -> KubernetesApiCall:
    out: KubernetesApiCall = {}  # type: ignore[typeddict-item]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("username") is not None:
        out["username"] = data["username"]
    if data.get("userGroups") is not None:
        out["user_groups"] = data["userGroups"]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("verb") is not None:
        out["verb"] = data["verb"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("requestUri") is not None:
        out["request_uri"] = data["requestUri"]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    if data.get("sourceIPs") is not None:
        out["source_ips"] = data["sourceIPs"]
    if data.get("userAgent") is not None:
        out["user_agent"] = data["userAgent"]
    if data.get("eventCount") is not None:
        out["event_count"] = data["eventCount"]
    return out
