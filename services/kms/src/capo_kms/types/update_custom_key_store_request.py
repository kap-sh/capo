"""Generated from Smithy shape ``com.amazonaws.kms#UpdateCustomKeyStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.account_id_type
    import capo_kms.types.cloud_hsm_cluster_id_type
    import capo_kms.types.custom_key_store_id_type
    import capo_kms.types.custom_key_store_name_type
    import capo_kms.types.key_store_password_type
    import capo_kms.types.xks_proxy_authentication_credential_type
    import capo_kms.types.xks_proxy_connectivity_type
    import capo_kms.types.xks_proxy_uri_endpoint_type
    import capo_kms.types.xks_proxy_uri_path_type
    import capo_kms.types.xks_proxy_vpc_endpoint_service_name_type


class UpdateCustomKeyStoreRequest(TypedDict, closed=True):
    custom_key_store_id: "capo_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    """<p>Identifies the custom key store that you want to update. Enter the ID of the custom key store. To find the ID of a custom key store, use the <a>DescribeCustomKeyStores</a> operation.</p>"""
    new_custom_key_store_name: NotRequired[
        "capo_kms.types.custom_key_store_name_type.CustomKeyStoreNameType"
    ]
    """<p>Changes the friendly name of the custom key store to the value that you specify. The custom key store name must be unique in the Amazon Web Services account.</p> <important> <p>Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <p>To change this value, the custom key store can be connected or disconnected.</p>"""
    key_store_password: NotRequired[
        "capo_kms.types.key_store_password_type.KeyStorePasswordType"
    ]
    """<p>Enter the current password of the <code>kmsuser</code> crypto user (CU) in the CloudHSM cluster that is associated with the custom key store. This parameter is valid only for custom key stores with a <code>CustomKeyStoreType</code> of <code>AWS_CLOUDHSM</code>.</p> <p>This parameter tells KMS the current password of the <code>kmsuser</code> crypto user (CU). It does not set or change the password of any users in the CloudHSM cluster.</p> <p>To change this value, the CloudHSM key store must be disconnected.</p>"""
    cloud_hsm_cluster_id: NotRequired[
        "capo_kms.types.cloud_hsm_cluster_id_type.CloudHsmClusterIdType"
    ]
    """<p>Associates the custom key store with a related CloudHSM cluster. This parameter is valid only for custom key stores with a <code>CustomKeyStoreType</code> of <code>AWS_CLOUDHSM</code>.</p> <p>Enter the cluster ID of the cluster that you used to create the custom key store or a cluster that shares a backup history and has the same cluster certificate as the original cluster. You cannot use this parameter to associate a custom key store with an unrelated cluster. In addition, the replacement cluster must <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html#before-keystore">fulfill the requirements</a> for a cluster associated with a custom key store. To view the cluster certificate of a cluster, use the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html">DescribeClusters</a> operation.</p> <p>To change this value, the CloudHSM key store must be disconnected.</p>"""
    xks_proxy_uri_endpoint: NotRequired[
        "capo_kms.types.xks_proxy_uri_endpoint_type.XksProxyUriEndpointType"
    ]
    """<p>Changes the URI endpoint that KMS uses to connect to your external key store proxy (XKS proxy). This parameter is valid only for custom key stores with a <code>CustomKeyStoreType</code> of <code>EXTERNAL_KEY_STORE</code>.</p> <p>For external key stores with an <code>XksProxyConnectivity</code> value of <code>PUBLIC_ENDPOINT</code>, the protocol must be HTTPS.</p> <p>For external key stores with an <code>XksProxyConnectivity</code> value of <code>VPC_ENDPOINT_SERVICE</code>, specify <code>https://</code> followed by the private DNS name associated with the VPC endpoint service. Each external key store must use a different private DNS name.</p> <p>The combined <code>XksProxyUriEndpoint</code> and <code>XksProxyUriPath</code> values must be unique in the Amazon Web Services account and Region.</p> <p>To change this value, the external key store must be disconnected.</p>"""
    xks_proxy_uri_path: NotRequired[
        "capo_kms.types.xks_proxy_uri_path_type.XksProxyUriPathType"
    ]
    """<p>Changes the base path to the proxy APIs for this external key store. To find this value, see the documentation for your external key manager and external key store proxy (XKS proxy). This parameter is valid only for custom key stores with a <code>CustomKeyStoreType</code> of <code>EXTERNAL_KEY_STORE</code>.</p> <p>The value must start with <code>/</code> and must end with <code>/kms/xks/v1</code>, where <code>v1</code> represents the version of the KMS external key store proxy API. You can include an optional prefix between the required elements such as <code>/<i>example</i>/kms/xks/v1</code>.</p> <p>The combined <code>XksProxyUriEndpoint</code> and <code>XksProxyUriPath</code> values must be unique in the Amazon Web Services account and Region.</p> <p>You can change this value when the external key store is connected or disconnected.</p>"""
    xks_proxy_vpc_endpoint_service_name: NotRequired[
        "capo_kms.types.xks_proxy_vpc_endpoint_service_name_type.XksProxyVpcEndpointServiceNameType"
    ]
    """<p>Changes the name that KMS uses to identify the Amazon VPC endpoint service for your external key store proxy (XKS proxy). This parameter is valid when the <code>CustomKeyStoreType</code> is <code>EXTERNAL_KEY_STORE</code> and the <code>XksProxyConnectivity</code> is <code>VPC_ENDPOINT_SERVICE</code>.</p> <p>To change this value, the external key store must be disconnected.</p>"""
    xks_proxy_vpc_endpoint_service_owner: NotRequired[
        "capo_kms.types.account_id_type.AccountIdType"
    ]
    """<p>Changes the Amazon Web Services account ID that KMS uses to identify the Amazon VPC endpoint service for your external key store proxy (XKS proxy). This parameter is optional. If not specified, the current Amazon Web Services account ID for the VPC endpoint service will not be updated.</p> <p>To change this value, the external key store must be disconnected.</p>"""
    xks_proxy_authentication_credential: NotRequired[
        "capo_kms.types.xks_proxy_authentication_credential_type.XksProxyAuthenticationCredentialType"
    ]
    """<p>Changes the credentials that KMS uses to sign requests to the external key store proxy (XKS proxy). This parameter is valid only for custom key stores with a <code>CustomKeyStoreType</code> of <code>EXTERNAL_KEY_STORE</code>.</p> <p>You must specify both the <code>AccessKeyId</code> and <code>SecretAccessKey</code> value in the authentication credential, even if you are only updating one value.</p> <p>This parameter doesn't establish or change your authentication credentials on the proxy. It just tells KMS the credential that you established with your external key store proxy. For example, if you rotate the credential on your external key store proxy, you can use this parameter to update the credential in KMS.</p> <p>You can change this value when the external key store is connected or disconnected.</p>"""
    xks_proxy_connectivity: NotRequired[
        "capo_kms.types.xks_proxy_connectivity_type.XksProxyConnectivityType"
    ]
    """<p>Changes the connectivity setting for the external key store. To indicate that the external key store proxy uses a Amazon VPC endpoint service to communicate with KMS, specify <code>VPC_ENDPOINT_SERVICE</code>. Otherwise, specify <code>PUBLIC_ENDPOINT</code>.</p> <p>If you change the <code>XksProxyConnectivity</code> to <code>VPC_ENDPOINT_SERVICE</code>, you must also change the <code>XksProxyUriEndpoint</code> and add an <code>XksProxyVpcEndpointServiceName</code> value. </p> <p>If you change the <code>XksProxyConnectivity</code> to <code>PUBLIC_ENDPOINT</code>, you must also change the <code>XksProxyUriEndpoint</code> and specify a null or empty string for the <code>XksProxyVpcEndpointServiceName</code> value.</p> <p>To change this value, the external key store must be disconnected.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCustomKeyStoreRequest) -> dict:
    out: dict = {}
    out["CustomKeyStoreId"] = value["custom_key_store_id"]
    if "new_custom_key_store_name" in value:
        out["NewCustomKeyStoreName"] = value["new_custom_key_store_name"]
    if "key_store_password" in value:
        out["KeyStorePassword"] = value["key_store_password"]
    if "cloud_hsm_cluster_id" in value:
        out["CloudHsmClusterId"] = value["cloud_hsm_cluster_id"]
    if "xks_proxy_uri_endpoint" in value:
        out["XksProxyUriEndpoint"] = value["xks_proxy_uri_endpoint"]
    if "xks_proxy_uri_path" in value:
        out["XksProxyUriPath"] = value["xks_proxy_uri_path"]
    if "xks_proxy_vpc_endpoint_service_name" in value:
        out["XksProxyVpcEndpointServiceName"] = value[
            "xks_proxy_vpc_endpoint_service_name"
        ]
    if "xks_proxy_vpc_endpoint_service_owner" in value:
        out["XksProxyVpcEndpointServiceOwner"] = value[
            "xks_proxy_vpc_endpoint_service_owner"
        ]
    if "xks_proxy_authentication_credential" in value:
        import capo_kms.types.xks_proxy_authentication_credential_type

        out["XksProxyAuthenticationCredential"] = (
            capo_kms.types.xks_proxy_authentication_credential_type.serialize_aws_json_1_1(
                value["xks_proxy_authentication_credential"]
            )
        )
    if "xks_proxy_connectivity" in value:
        import capo_kms.types.xks_proxy_connectivity_type

        out["XksProxyConnectivity"] = (
            capo_kms.types.xks_proxy_connectivity_type.serialize_aws_json_1_1(
                value["xks_proxy_connectivity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCustomKeyStoreRequest:
    out: UpdateCustomKeyStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("CustomKeyStoreId") is not None:
        out["custom_key_store_id"] = data["CustomKeyStoreId"]
    else:
        raise DeserializationError(
            "UpdateCustomKeyStoreRequest.custom_key_store_id required"
        )
    if data.get("NewCustomKeyStoreName") is not None:
        out["new_custom_key_store_name"] = data["NewCustomKeyStoreName"]
    if data.get("KeyStorePassword") is not None:
        out["key_store_password"] = data["KeyStorePassword"]
    if data.get("CloudHsmClusterId") is not None:
        out["cloud_hsm_cluster_id"] = data["CloudHsmClusterId"]
    if data.get("XksProxyUriEndpoint") is not None:
        out["xks_proxy_uri_endpoint"] = data["XksProxyUriEndpoint"]
    if data.get("XksProxyUriPath") is not None:
        out["xks_proxy_uri_path"] = data["XksProxyUriPath"]
    if data.get("XksProxyVpcEndpointServiceName") is not None:
        out["xks_proxy_vpc_endpoint_service_name"] = data[
            "XksProxyVpcEndpointServiceName"
        ]
    if data.get("XksProxyVpcEndpointServiceOwner") is not None:
        out["xks_proxy_vpc_endpoint_service_owner"] = data[
            "XksProxyVpcEndpointServiceOwner"
        ]
    if data.get("XksProxyAuthenticationCredential") is not None:
        import capo_kms.types.xks_proxy_authentication_credential_type

        out["xks_proxy_authentication_credential"] = (
            capo_kms.types.xks_proxy_authentication_credential_type.deserialize_aws_json_1_1(
                data["XksProxyAuthenticationCredential"]
            )
        )
    if data.get("XksProxyConnectivity") is not None:
        import capo_kms.types.xks_proxy_connectivity_type

        out["xks_proxy_connectivity"] = (
            capo_kms.types.xks_proxy_connectivity_type.deserialize_aws_json_1_1(
                data["XksProxyConnectivity"]
            )
        )
    return out
