"""Generated from Smithy shape ``com.amazonaws.rtbfabric#EksEndpointsConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.base64_encoded_certificate_chain
    import capo_rtbfabric.types.kubernetes_cluster_name
    import capo_rtbfabric.types.kubernetes_endpoints_resource_name
    import capo_rtbfabric.types.kubernetes_namespace
    import capo_rtbfabric.types.uri


class EksEndpointsConfiguration(TypedDict, closed=True):
    endpoints_resource_name: "capo_rtbfabric.types.kubernetes_endpoints_resource_name.KubernetesEndpointsResourceName"
    """<p>The name of the endpoint resource.</p>"""
    endpoints_resource_namespace: (
        "capo_rtbfabric.types.kubernetes_namespace.KubernetesNamespace"
    )
    """<p>The namespace of the endpoint resource.</p>"""
    cluster_api_server_endpoint_uri: "capo_rtbfabric.types.uri.URI"
    """<p>The URI of the cluster API server endpoint.</p>"""
    cluster_api_server_ca_certificate_chain: "capo_rtbfabric.types.base64_encoded_certificate_chain.Base64EncodedCertificateChain"
    """<p>The CA certificate chain of the cluster API server.</p>"""
    cluster_name: "capo_rtbfabric.types.kubernetes_cluster_name.KubernetesClusterName"
    """<p>The name of the cluster.</p>"""
    role_arn: "str"
    """<p>The role ARN for the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksEndpointsConfiguration) -> dict:
    out: dict = {}
    out["endpointsResourceName"] = value["endpoints_resource_name"]
    out["endpointsResourceNamespace"] = value["endpoints_resource_namespace"]
    out["clusterApiServerEndpointUri"] = value["cluster_api_server_endpoint_uri"]
    out["clusterApiServerCaCertificateChain"] = value[
        "cluster_api_server_ca_certificate_chain"
    ]
    out["clusterName"] = value["cluster_name"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> EksEndpointsConfiguration:
    out: EksEndpointsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("endpointsResourceName") is not None:
        out["endpoints_resource_name"] = data["endpointsResourceName"]
    else:
        out["endpoints_resource_name"] = ""
    if data.get("endpointsResourceNamespace") is not None:
        out["endpoints_resource_namespace"] = data["endpointsResourceNamespace"]
    else:
        out["endpoints_resource_namespace"] = ""
    if data.get("clusterApiServerEndpointUri") is not None:
        out["cluster_api_server_endpoint_uri"] = data["clusterApiServerEndpointUri"]
    else:
        out["cluster_api_server_endpoint_uri"] = ""
    if data.get("clusterApiServerCaCertificateChain") is not None:
        out["cluster_api_server_ca_certificate_chain"] = data[
            "clusterApiServerCaCertificateChain"
        ]
    else:
        out["cluster_api_server_ca_certificate_chain"] = ""
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    else:
        out["cluster_name"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out


def redact_sensitive(value: EksEndpointsConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cluster_api_server_ca_certificate_chain" in value:
        out["cluster_api_server_ca_certificate_chain"] = (
            "*** Sensitive Data Redacted ***"
        )
    return out
