"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.argo_cd_aws_idc_config_request
    import capo_eks.types.argo_cd_endpoint_prefix
    import capo_eks.types.argo_cd_network_access_config_request
    import capo_eks.types.argo_cd_role_mapping_list
    import capo_eks.types.string


class ArgoCdConfigRequest(TypedDict, closed=True):
    namespace: NotRequired["capo_eks.types.string.String"]
    """<p>The Kubernetes namespace where Argo CD resources will be created. If not specified, the default namespace is used.</p>"""
    aws_idc: "capo_eks.types.argo_cd_aws_idc_config_request.ArgoCdAwsIdcConfigRequest"
    """<p>Configuration for IAM Identity CenterIAM; Identity Center integration. When configured, users can authenticate to Argo CD using their IAM Identity CenterIAM; Identity Center credentials.</p>"""
    rbac_role_mappings: NotRequired[
        "capo_eks.types.argo_cd_role_mapping_list.ArgoCdRoleMappingList"
    ]
    """<p>A list of role mappings that define which IAM Identity CenterIAM; Identity Center users or groups have which Argo CD roles. Each mapping associates an Argo CD role (<code>ADMIN</code>, <code>EDITOR</code>, or <code>VIEWER</code>) with one or more IAM Identity CenterIAM; Identity Center identities.</p>"""
    network_access: NotRequired[
        "capo_eks.types.argo_cd_network_access_config_request.ArgoCdNetworkAccessConfigRequest"
    ]
    """<p>Configuration for network access to the Argo CD capability's managed API server endpoint. By default, the Argo CD server is accessible via a public endpoint. You can optionally specify one or more VPC endpoint IDs to enable private connectivity from your VPCs. When VPC endpoints are configured, public access is blocked and the Argo CD server is only accessible through the specified VPC endpoints.</p>"""
    endpoint_prefix: NotRequired[
        "capo_eks.types.argo_cd_endpoint_prefix.ArgoCdEndpointPrefix"
    ]
    """<p>An optional prefix used to construct the hostname of the Argo CD server endpoint. If not specified, Amazon EKS automatically generates the endpoint. This value can't be changed after the capability is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArgoCdConfigRequest) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    import capo_eks.types.argo_cd_aws_idc_config_request

    out["awsIdc"] = capo_eks.types.argo_cd_aws_idc_config_request.serialize_json(
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
        import capo_eks.types.argo_cd_network_access_config_request

        out["networkAccess"] = (
            capo_eks.types.argo_cd_network_access_config_request.serialize_json(
                value["network_access"]
            )
        )
    if "endpoint_prefix" in value:
        out["endpointPrefix"] = value["endpoint_prefix"]
    return out


def deserialize_json(data: dict) -> ArgoCdConfigRequest:
    out: ArgoCdConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("awsIdc") is not None:
        import capo_eks.types.argo_cd_aws_idc_config_request

        out["aws_idc"] = capo_eks.types.argo_cd_aws_idc_config_request.deserialize_json(
            data["awsIdc"]
        )
    else:
        raise DeserializationError("ArgoCdConfigRequest.aws_idc required")
    if data.get("rbacRoleMappings") is not None:
        import capo_eks.types.argo_cd_role_mapping_list

        out["rbac_role_mappings"] = (
            capo_eks.types.argo_cd_role_mapping_list.deserialize_json(
                data["rbacRoleMappings"]
            )
        )
    if data.get("networkAccess") is not None:
        import capo_eks.types.argo_cd_network_access_config_request

        out["network_access"] = (
            capo_eks.types.argo_cd_network_access_config_request.deserialize_json(
                data["networkAccess"]
            )
        )
    if data.get("endpointPrefix") is not None:
        out["endpoint_prefix"] = data["endpointPrefix"]
    return out
