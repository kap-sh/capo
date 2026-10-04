"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.argo_cd_aws_idc_config_response
    import capo_eks.types.argo_cd_endpoint_prefix
    import capo_eks.types.argo_cd_network_access_config_response
    import capo_eks.types.argo_cd_role_mapping_list
    import capo_eks.types.string


class ArgoCdConfigResponse(TypedDict, closed=True):
    namespace: NotRequired["capo_eks.types.string.String"]
    """<p>The Kubernetes namespace where Argo CD resources are monitored by your Argo CD Capability.</p>"""
    aws_idc: NotRequired[
        "capo_eks.types.argo_cd_aws_idc_config_response.ArgoCdAwsIdcConfigResponse"
    ]
    """<p>The IAM Identity CenterIAM; Identity Center integration configuration.</p>"""
    rbac_role_mappings: NotRequired[
        "capo_eks.types.argo_cd_role_mapping_list.ArgoCdRoleMappingList"
    ]
    """<p>The list of role mappings that define which IAM Identity CenterIAM; Identity Center users or groups have which Argo CD roles.</p>"""
    network_access: NotRequired[
        "capo_eks.types.argo_cd_network_access_config_response.ArgoCdNetworkAccessConfigResponse"
    ]
    """<p>The network access configuration for the Argo CD capability's managed API server endpoint. If VPC endpoint IDs are specified, public access is blocked and the Argo CD server is only accessible through the specified VPC endpoints.</p>"""
    server_url: NotRequired["capo_eks.types.string.String"]
    """<p>The URL of the Argo CD server. Use this URL to access the Argo CD web interface and API.</p>"""
    endpoint_prefix: NotRequired[
        "capo_eks.types.argo_cd_endpoint_prefix.ArgoCdEndpointPrefix"
    ]
    """<p>The prefix that was configured for the hostname of the Argo CD server endpoint when the capability was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArgoCdConfigResponse) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "aws_idc" in value:
        import capo_eks.types.argo_cd_aws_idc_config_response

        out["awsIdc"] = capo_eks.types.argo_cd_aws_idc_config_response.serialize_json(
            value["aws_idc"]
        )
    if "rbac_role_mappings" in value:
        import capo_eks.types.argo_cd_role_mapping_list

        out["rbacRoleMappings"] = (
            capo_eks.types.argo_cd_role_mapping_list.serialize_json(
                value["rbac_role_mappings"]
            )
        )
    if "network_access" in value:
        import capo_eks.types.argo_cd_network_access_config_response

        out["networkAccess"] = (
            capo_eks.types.argo_cd_network_access_config_response.serialize_json(
                value["network_access"]
            )
        )
    if "server_url" in value:
        out["serverUrl"] = value["server_url"]
    if "endpoint_prefix" in value:
        out["endpointPrefix"] = value["endpoint_prefix"]
    return out


def deserialize_json(data: dict) -> ArgoCdConfigResponse:
    out: ArgoCdConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("awsIdc") is not None:
        import capo_eks.types.argo_cd_aws_idc_config_response

        out["aws_idc"] = (
            capo_eks.types.argo_cd_aws_idc_config_response.deserialize_json(
                data["awsIdc"]
            )
        )
    if data.get("rbacRoleMappings") is not None:
        import capo_eks.types.argo_cd_role_mapping_list

        out["rbac_role_mappings"] = (
            capo_eks.types.argo_cd_role_mapping_list.deserialize_json(
                data["rbacRoleMappings"]
            )
        )
    if data.get("networkAccess") is not None:
        import capo_eks.types.argo_cd_network_access_config_response

        out["network_access"] = (
            capo_eks.types.argo_cd_network_access_config_response.deserialize_json(
                data["networkAccess"]
            )
        )
    if data.get("serverUrl") is not None:
        out["server_url"] = data["serverUrl"]
    if data.get("endpointPrefix") is not None:
        out["endpoint_prefix"] = data["endpointPrefix"]
    return out
