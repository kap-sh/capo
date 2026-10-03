"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationObjectStorageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.agent_arn_list
    import capo_datasync.types.cmk_secret_config
    import capo_datasync.types.custom_secret_config
    import capo_datasync.types.input_tag_list
    import capo_datasync.types.object_storage_access_key
    import capo_datasync.types.object_storage_bucket_name
    import capo_datasync.types.object_storage_certificate
    import capo_datasync.types.object_storage_secret_key
    import capo_datasync.types.object_storage_server_port
    import capo_datasync.types.object_storage_server_protocol
    import capo_datasync.types.s3_subdirectory
    import capo_datasync.types.server_hostname


class CreateLocationObjectStorageRequest(TypedDict, closed=True):
    server_hostname: "capo_datasync.types.server_hostname.ServerHostname"
    """<p>Specifies the domain name or IP address (IPv4 or IPv6) of the object storage server that your DataSync agent connects to.</p>"""
    server_port: NotRequired[
        "capo_datasync.types.object_storage_server_port.ObjectStorageServerPort"
    ]
    """<p>Specifies the port that your object storage server accepts inbound network traffic on (for example, port 443).</p>"""
    server_protocol: NotRequired[
        "capo_datasync.types.object_storage_server_protocol.ObjectStorageServerProtocol"
    ]
    """<p>Specifies the protocol that your object storage server uses to communicate. If not specified, the default value is <code>HTTPS</code>.</p>"""
    subdirectory: NotRequired["capo_datasync.types.s3_subdirectory.S3Subdirectory"]
    """<p>Specifies the object prefix for your object storage server. If this is a source location, DataSync only copies objects with this prefix. If this is a destination location, DataSync writes all objects with this prefix. </p>"""
    bucket_name: (
        "capo_datasync.types.object_storage_bucket_name.ObjectStorageBucketName"
    )
    """<p>Specifies the name of the object storage bucket involved in the transfer.</p>"""
    access_key: NotRequired[
        "capo_datasync.types.object_storage_access_key.ObjectStorageAccessKey"
    ]
    """<p>Specifies the access key (for example, a user name) if credentials are required to authenticate with the object storage server.</p>"""
    secret_key: NotRequired[
        "capo_datasync.types.object_storage_secret_key.ObjectStorageSecretKey"
    ]
    """<p>Specifies the secret key (for example, a password) if credentials are required to authenticate with the object storage server.</p> <note> <p>If you provide a secret using <code>SecretKey</code>, but do not provide secret configuration details using <code>CmkSecretConfig</code> or <code>CustomSecretConfig</code>, then DataSync stores the token using your Amazon Web Services account's Secrets Manager secret.</p> </note>"""
    agent_arns: NotRequired["capo_datasync.types.agent_arn_list.AgentArnList"]
    """<p>(Optional) Specifies the Amazon Resource Names (ARNs) of the DataSync agents that can connect with your object storage system. If you are setting up an agentless cross-cloud transfer, you do not need to specify a value for this parameter.</p> <note> <p>Make sure you configure this parameter correctly when you first create your storage location. You cannot add or remove agents from a storage location after you create it.</p> </note>"""
    tags: NotRequired["capo_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies the key-value pair that represents a tag that you want to add to the resource. Tags can help you manage, filter, and search for your resources. We recommend creating a name tag for your location.</p>"""
    server_certificate: NotRequired[
        "capo_datasync.types.object_storage_certificate.ObjectStorageCertificate"
    ]
    """<p>Specifies a certificate chain for DataSync to authenticate with your object storage system if the system uses a private or self-signed certificate authority (CA). You must specify a single <code>.pem</code> file with a full certificate chain (for example, <code>file:///home/user/.ssh/object_storage_certificates.pem</code>).</p> <p>The certificate chain might include:</p> <ul> <li> <p>The object storage system's certificate</p> </li> <li> <p>All intermediate certificates (if there are any)</p> </li> <li> <p>The root certificate of the signing CA</p> </li> </ul> <p>You can concatenate your certificates into a <code>.pem</code> file (which can be up to 32768 bytes before base64 encoding). The following example <code>cat</code> command creates an <code>object_storage_certificates.pem</code> file that includes three certificates:</p> <p> <code>cat object_server_certificate.pem intermediate_certificate.pem ca_root_certificate.pem > object_storage_certificates.pem</code> </p> <p>To use this parameter, configure <code>ServerProtocol</code> to <code>HTTPS</code>.</p>"""
    cmk_secret_config: NotRequired[
        "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Specifies configuration information for a DataSync-managed secret, which includes the <code>SecretKey</code> that DataSync uses to access a specific object storage location, with a customer-managed KMS key.</p> <p>When you include this parameter as part of a <code>CreateLocationObjectStorage</code> request, you provide only the KMS key ARN. DataSync uses this KMS key together with the value you specify for the <code>SecretKey</code> parameter to create a DataSync-managed secret to store the location access credentials.</p> <p>Make sure that DataSync has permission to access the KMS key that you specify. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key"> Using a service-managed secret encrypted with a custom KMS key</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>SecretKey</code>) or <code>CustomSecretConfig</code> (without <code>SecretKey</code>) to provide credentials for a <code>CreateLocationObjectStorage</code> request. Do not provide both parameters for the same request.</p> </note>"""
    custom_secret_config: NotRequired[
        "capo_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Specifies configuration information for a customer-managed Secrets Manager secret where the secret key for a specific object storage location is stored in plain text, in Secrets Manager. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key"> Using a secret that you manage</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>SecretKey</code>) or <code>CustomSecretConfig</code> (without <code>SecretKey</code>) to provide credentials for a <code>CreateLocationObjectStorage</code> request. Do not provide both parameters for the same request.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationObjectStorageRequest) -> dict:
    out: dict = {}
    out["ServerHostname"] = value["server_hostname"]
    if "server_port" in value:
        out["ServerPort"] = value["server_port"]
    if "server_protocol" in value:
        import capo_datasync.types.object_storage_server_protocol

        out["ServerProtocol"] = (
            capo_datasync.types.object_storage_server_protocol.serialize_aws_json_1_1(
                value["server_protocol"]
            )
        )
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    out["BucketName"] = value["bucket_name"]
    if "access_key" in value:
        out["AccessKey"] = value["access_key"]
    if "secret_key" in value:
        out["SecretKey"] = value["secret_key"]
    if "agent_arns" in value:
        import capo_datasync.types.agent_arn_list

        out["AgentArns"] = capo_datasync.types.agent_arn_list.serialize_aws_json_1_1(
            value["agent_arns"]
        )
    if "tags" in value:
        import capo_datasync.types.input_tag_list

        out["Tags"] = capo_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "server_certificate" in value:
        import capo_datasync.types.object_storage_certificate

        out["ServerCertificate"] = (
            capo_datasync.types.object_storage_certificate.serialize_aws_json_1_1(
                value["server_certificate"]
            )
        )
    if "cmk_secret_config" in value:
        import capo_datasync.types.cmk_secret_config

        out["CmkSecretConfig"] = (
            capo_datasync.types.cmk_secret_config.serialize_aws_json_1_1(
                value["cmk_secret_config"]
            )
        )
    if "custom_secret_config" in value:
        import capo_datasync.types.custom_secret_config

        out["CustomSecretConfig"] = (
            capo_datasync.types.custom_secret_config.serialize_aws_json_1_1(
                value["custom_secret_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationObjectStorageRequest:
    out: CreateLocationObjectStorageRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServerHostname") is not None:
        out["server_hostname"] = data["ServerHostname"]
    else:
        raise DeserializationError(
            "CreateLocationObjectStorageRequest.server_hostname required"
        )
    if data.get("ServerPort") is not None:
        out["server_port"] = data["ServerPort"]
    if data.get("ServerProtocol") is not None:
        import capo_datasync.types.object_storage_server_protocol

        out["server_protocol"] = (
            capo_datasync.types.object_storage_server_protocol.deserialize_aws_json_1_1(
                data["ServerProtocol"]
            )
        )
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError(
            "CreateLocationObjectStorageRequest.bucket_name required"
        )
    if data.get("AccessKey") is not None:
        out["access_key"] = data["AccessKey"]
    if data.get("SecretKey") is not None:
        out["secret_key"] = data["SecretKey"]
    if data.get("AgentArns") is not None:
        import capo_datasync.types.agent_arn_list

        out["agent_arns"] = capo_datasync.types.agent_arn_list.deserialize_aws_json_1_1(
            data["AgentArns"]
        )
    if data.get("Tags") is not None:
        import capo_datasync.types.input_tag_list

        out["tags"] = capo_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ServerCertificate") is not None:
        import capo_datasync.types.object_storage_certificate

        out["server_certificate"] = (
            capo_datasync.types.object_storage_certificate.deserialize_aws_json_1_1(
                data["ServerCertificate"]
            )
        )
    if data.get("CmkSecretConfig") is not None:
        import capo_datasync.types.cmk_secret_config

        out["cmk_secret_config"] = (
            capo_datasync.types.cmk_secret_config.deserialize_aws_json_1_1(
                data["CmkSecretConfig"]
            )
        )
    if data.get("CustomSecretConfig") is not None:
        import capo_datasync.types.custom_secret_config

        out["custom_secret_config"] = (
            capo_datasync.types.custom_secret_config.deserialize_aws_json_1_1(
                data["CustomSecretConfig"]
            )
        )
    return out
