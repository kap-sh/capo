"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.account_id_type
    import capo_kms.types.xks_proxy_authentication_access_key_id_type
    import capo_kms.types.xks_proxy_connectivity_type
    import capo_kms.types.xks_proxy_uri_endpoint_type
    import capo_kms.types.xks_proxy_uri_path_type
    import capo_kms.types.xks_proxy_vpc_endpoint_service_name_type


class XksProxyConfigurationType(TypedDict, closed=True):
    connectivity: NotRequired[
        "capo_kms.types.xks_proxy_connectivity_type.XksProxyConnectivityType"
    ]
    """<p>Indicates whether the external key store proxy uses a public endpoint or an Amazon VPC endpoint service to communicate with KMS.</p>"""
    access_key_id: NotRequired[
        "capo_kms.types.xks_proxy_authentication_access_key_id_type.XksProxyAuthenticationAccessKeyIdType"
    ]
    """<p>The part of the external key store <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateCustomKeyStore.html#KMS-CreateCustomKeyStore-request-XksProxyAuthenticationCredential">proxy authentication credential</a> that uniquely identifies the secret access key.</p>"""
    uri_endpoint: NotRequired[
        "capo_kms.types.xks_proxy_uri_endpoint_type.XksProxyUriEndpointType"
    ]
    """<p>The URI endpoint for the external key store proxy.</p> <p>If the external key store proxy has a public endpoint, it is displayed here.</p> <p>If the external key store proxy uses an Amazon VPC endpoint service name, this field displays the private DNS name associated with the VPC endpoint service.</p>"""
    uri_path: NotRequired["capo_kms.types.xks_proxy_uri_path_type.XksProxyUriPathType"]
    """<p>The path to the external key store proxy APIs.</p>"""
    vpc_endpoint_service_name: NotRequired[
        "capo_kms.types.xks_proxy_vpc_endpoint_service_name_type.XksProxyVpcEndpointServiceNameType"
    ]
    """<p>The Amazon VPC endpoint service used to communicate with the external key store proxy. This field appears only when the external key store proxy uses an Amazon VPC endpoint service to communicate with KMS.</p>"""
    vpc_endpoint_service_owner: NotRequired[
        "capo_kms.types.account_id_type.AccountIdType"
    ]
    """<p>The Amazon Web Services account ID that owns the Amazon VPC endpoint service used to communicate with the external key store proxy (XKS). This field appears only when the XKS uses an VPC endpoint service to communicate with KMS.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XksProxyConfigurationType) -> dict:
    out: dict = {}
    if "connectivity" in value:
        import capo_kms.types.xks_proxy_connectivity_type

        out["Connectivity"] = (
            capo_kms.types.xks_proxy_connectivity_type.serialize_aws_json_1_1(
                value["connectivity"]
            )
        )
    if "access_key_id" in value:
        out["AccessKeyId"] = value["access_key_id"]
    if "uri_endpoint" in value:
        out["UriEndpoint"] = value["uri_endpoint"]
    if "uri_path" in value:
        out["UriPath"] = value["uri_path"]
    if "vpc_endpoint_service_name" in value:
        out["VpcEndpointServiceName"] = value["vpc_endpoint_service_name"]
    if "vpc_endpoint_service_owner" in value:
        out["VpcEndpointServiceOwner"] = value["vpc_endpoint_service_owner"]
    return out


def deserialize_aws_json_1_1(data: dict) -> XksProxyConfigurationType:
    out: XksProxyConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("Connectivity") is not None:
        import capo_kms.types.xks_proxy_connectivity_type

        out["connectivity"] = (
            capo_kms.types.xks_proxy_connectivity_type.deserialize_aws_json_1_1(
                data["Connectivity"]
            )
        )
    if data.get("AccessKeyId") is not None:
        out["access_key_id"] = data["AccessKeyId"]
    if data.get("UriEndpoint") is not None:
        out["uri_endpoint"] = data["UriEndpoint"]
    if data.get("UriPath") is not None:
        out["uri_path"] = data["UriPath"]
    if data.get("VpcEndpointServiceName") is not None:
        out["vpc_endpoint_service_name"] = data["VpcEndpointServiceName"]
    if data.get("VpcEndpointServiceOwner") is not None:
        out["vpc_endpoint_service_owner"] = data["VpcEndpointServiceOwner"]
    return out
