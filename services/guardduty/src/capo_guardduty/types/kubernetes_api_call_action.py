"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesApiCallAction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.remote_ip_details
    import capo_guardduty.types.source_ips
    import capo_guardduty.types.string


class KubernetesApiCallAction(TypedDict, closed=True):
    request_uri: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Kubernetes API request URI.</p>"""
    verb: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Kubernetes API request HTTP verb.</p>"""
    resource: NotRequired["capo_guardduty.types.string.String"]
    """<p>The resource component in the Kubernetes API call action.</p>"""
    subresource: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the sub-resource in the Kubernetes API call action.</p>"""
    namespace: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the namespace where the Kubernetes API call action takes place.</p>"""
    resource_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the resource in the Kubernetes API call action.</p>"""
    source_ips: NotRequired["capo_guardduty.types.source_ips.SourceIps"]
    """<p>The IP of the Kubernetes API caller and the IPs of any proxies or load balancers between the caller and the API endpoint.</p>"""
    user_agent: NotRequired["capo_guardduty.types.string.String"]
    """<p>The user agent of the caller of the Kubernetes API.</p>"""
    remote_ip_details: NotRequired[
        "capo_guardduty.types.remote_ip_details.RemoteIpDetails"
    ]
    status_code: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The resulting HTTP response code of the Kubernetes API call action.</p>"""
    parameters: NotRequired["capo_guardduty.types.string.String"]
    """<p>Parameters related to the Kubernetes API call action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesApiCallAction) -> dict:
    out: dict = {}
    if "request_uri" in value:
        out["requestUri"] = value["request_uri"]
    if "verb" in value:
        out["verb"] = value["verb"]
    if "resource" in value:
        out["resource"] = value["resource"]
    if "subresource" in value:
        out["subresource"] = value["subresource"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "source_ips" in value:
        import capo_guardduty.types.source_ips

        out["sourceIPs"] = capo_guardduty.types.source_ips.serialize_json(
            value["source_ips"]
        )
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    if "remote_ip_details" in value:
        import capo_guardduty.types.remote_ip_details

        out["remoteIpDetails"] = capo_guardduty.types.remote_ip_details.serialize_json(
            value["remote_ip_details"]
        )
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "parameters" in value:
        out["parameters"] = value["parameters"]
    return out


def deserialize_json(data: dict) -> KubernetesApiCallAction:
    out: KubernetesApiCallAction = {}  # type: ignore[typeddict-item]
    if data.get("requestUri") is not None:
        out["request_uri"] = data["requestUri"]
    if data.get("verb") is not None:
        out["verb"] = data["verb"]
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    if data.get("subresource") is not None:
        out["subresource"] = data["subresource"]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    if data.get("sourceIPs") is not None:
        import capo_guardduty.types.source_ips

        out["source_ips"] = capo_guardduty.types.source_ips.deserialize_json(
            data["sourceIPs"]
        )
    if data.get("userAgent") is not None:
        out["user_agent"] = data["userAgent"]
    if data.get("remoteIpDetails") is not None:
        import capo_guardduty.types.remote_ip_details

        out["remote_ip_details"] = (
            capo_guardduty.types.remote_ip_details.deserialize_json(
                data["remoteIpDetails"]
            )
        )
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    if data.get("parameters") is not None:
        out["parameters"] = data["parameters"]
    return out


def redact_sensitive(value: KubernetesApiCallAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "remote_ip_details" in value:
        import capo_guardduty.types.remote_ip_details

        out["remote_ip_details"] = (
            capo_guardduty.types.remote_ip_details.redact_sensitive(
                value["remote_ip_details"]
            )
        )
    return out
