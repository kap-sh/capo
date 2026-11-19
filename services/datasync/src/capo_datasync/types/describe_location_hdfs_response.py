"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationHdfsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.agent_arn_list
    import capo_datasync.types.cmk_secret_config
    import capo_datasync.types.custom_secret_config
    import capo_datasync.types.hdfs_authentication_type
    import capo_datasync.types.hdfs_block_size
    import capo_datasync.types.hdfs_name_node_list
    import capo_datasync.types.hdfs_replication_factor
    import capo_datasync.types.hdfs_user
    import capo_datasync.types.kerberos_principal
    import capo_datasync.types.kms_key_provider_uri
    import capo_datasync.types.location_arn
    import capo_datasync.types.location_uri
    import capo_datasync.types.managed_secret_config
    import capo_datasync.types.qop_configuration
    import capo_datasync.types.time


class DescribeLocationHdfsResponse(TypedDict, closed=True):
    location_arn: NotRequired["capo_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the HDFS location.</p>"""
    location_uri: NotRequired["capo_datasync.types.location_uri.LocationUri"]
    """<p>The URI of the HDFS location.</p>"""
    name_nodes: NotRequired["capo_datasync.types.hdfs_name_node_list.HdfsNameNodeList"]
    """<p>The NameNode that manages the HDFS namespace. </p>"""
    block_size: NotRequired["capo_datasync.types.hdfs_block_size.HdfsBlockSize"]
    """<p>The size of the data blocks to write into the HDFS cluster. </p>"""
    replication_factor: NotRequired[
        "capo_datasync.types.hdfs_replication_factor.HdfsReplicationFactor"
    ]
    """<p>The number of DataNodes to replicate the data to when writing to the HDFS cluster. </p>"""
    kms_key_provider_uri: NotRequired[
        "capo_datasync.types.kms_key_provider_uri.KmsKeyProviderUri"
    ]
    """<p> The URI of the HDFS cluster's Key Management Server (KMS). </p>"""
    qop_configuration: NotRequired[
        "capo_datasync.types.qop_configuration.QopConfiguration"
    ]
    """<p>The Quality of Protection (QOP) configuration, which specifies the Remote Procedure Call (RPC) and data transfer protection settings configured on the HDFS cluster. </p>"""
    authentication_type: NotRequired[
        "capo_datasync.types.hdfs_authentication_type.HdfsAuthenticationType"
    ]
    """<p>The type of authentication used to determine the identity of the user. </p>"""
    simple_user: NotRequired["capo_datasync.types.hdfs_user.HdfsUser"]
    """<p>The user name to identify the client on the host operating system. This parameter is used if the <code>AuthenticationType</code> is defined as <code>SIMPLE</code>.</p>"""
    kerberos_principal: NotRequired[
        "capo_datasync.types.kerberos_principal.KerberosPrincipal"
    ]
    """<p>The Kerberos principal with access to the files and folders on the HDFS cluster. This parameter is used if the <code>AuthenticationType</code> is defined as <code>KERBEROS</code>.</p>"""
    agent_arns: NotRequired["capo_datasync.types.agent_arn_list.AgentArnList"]
    """<p>The ARNs of the DataSync agents that can connect with your HDFS cluster.</p>"""
    creation_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time that the HDFS location was created.</p>"""
    managed_secret_config: NotRequired[
        "capo_datasync.types.managed_secret_config.ManagedSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as a <code>KerberosKeytab</code> that DataSync uses to access a specific storage location. DataSync uses the default Amazon Web Services-managed KMS key to encrypt this secret in Secrets Manager.</p>"""
    cmk_secret_config: NotRequired[
        "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as a <code>KerberosKeytab</code> that DataSync uses to access a specific storage location, with a customer-managed KMS key.</p>"""
    custom_secret_config: NotRequired[
        "capo_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Describes configuration information for a customer-managed secret, such as a <code>KerberosKeytab</code> that DataSync uses to access a specific storage location, with a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationHdfsResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "name_nodes" in value:
        import capo_datasync.types.hdfs_name_node_list

        out["NameNodes"] = (
            capo_datasync.types.hdfs_name_node_list.serialize_aws_json_1_1(
                value["name_nodes"]
            )
        )
    if "block_size" in value:
        out["BlockSize"] = value["block_size"]
    if "replication_factor" in value:
        out["ReplicationFactor"] = value["replication_factor"]
    if "kms_key_provider_uri" in value:
        out["KmsKeyProviderUri"] = value["kms_key_provider_uri"]
    if "qop_configuration" in value:
        import capo_datasync.types.qop_configuration

        out["QopConfiguration"] = (
            capo_datasync.types.qop_configuration.serialize_aws_json_1_1(
                value["qop_configuration"]
            )
        )
    if "authentication_type" in value:
        import capo_datasync.types.hdfs_authentication_type

        out["AuthenticationType"] = (
            capo_datasync.types.hdfs_authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "simple_user" in value:
        out["SimpleUser"] = value["simple_user"]
    if "kerberos_principal" in value:
        out["KerberosPrincipal"] = value["kerberos_principal"]
    if "agent_arns" in value:
        import capo_datasync.types.agent_arn_list

        out["AgentArns"] = capo_datasync.types.agent_arn_list.serialize_aws_json_1_1(
            value["agent_arns"]
        )
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "managed_secret_config" in value:
        import capo_datasync.types.managed_secret_config

        out["ManagedSecretConfig"] = (
            capo_datasync.types.managed_secret_config.serialize_aws_json_1_1(
                value["managed_secret_config"]
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


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationHdfsResponse:
    out: DescribeLocationHdfsResponse = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    if data.get("NameNodes") is not None:
        import capo_datasync.types.hdfs_name_node_list

        out["name_nodes"] = (
            capo_datasync.types.hdfs_name_node_list.deserialize_aws_json_1_1(
                data["NameNodes"]
            )
        )
    if data.get("BlockSize") is not None:
        out["block_size"] = data["BlockSize"]
    if data.get("ReplicationFactor") is not None:
        out["replication_factor"] = data["ReplicationFactor"]
    if data.get("KmsKeyProviderUri") is not None:
        out["kms_key_provider_uri"] = data["KmsKeyProviderUri"]
    if data.get("QopConfiguration") is not None:
        import capo_datasync.types.qop_configuration

        out["qop_configuration"] = (
            capo_datasync.types.qop_configuration.deserialize_aws_json_1_1(
                data["QopConfiguration"]
            )
        )
    if data.get("AuthenticationType") is not None:
        import capo_datasync.types.hdfs_authentication_type

        out["authentication_type"] = (
            capo_datasync.types.hdfs_authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if data.get("SimpleUser") is not None:
        out["simple_user"] = data["SimpleUser"]
    if data.get("KerberosPrincipal") is not None:
        out["kerberos_principal"] = data["KerberosPrincipal"]
    if data.get("AgentArns") is not None:
        import capo_datasync.types.agent_arn_list

        out["agent_arns"] = capo_datasync.types.agent_arn_list.deserialize_aws_json_1_1(
            data["AgentArns"]
        )
    if data.get("CreationTime") is not None:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("ManagedSecretConfig") is not None:
        import capo_datasync.types.managed_secret_config

        out["managed_secret_config"] = (
            capo_datasync.types.managed_secret_config.deserialize_aws_json_1_1(
                data["ManagedSecretConfig"]
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


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeLocationHdfsResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "name_nodes" in value:
        import capo_datasync.types.hdfs_name_node_list

        out["NameNodes"] = capo_datasync.types.hdfs_name_node_list.serialize_cbor(
            value["name_nodes"]
        )
    if "block_size" in value:
        out["BlockSize"] = value["block_size"]
    if "replication_factor" in value:
        out["ReplicationFactor"] = value["replication_factor"]
    if "kms_key_provider_uri" in value:
        out["KmsKeyProviderUri"] = value["kms_key_provider_uri"]
    if "qop_configuration" in value:
        import capo_datasync.types.qop_configuration

        out["QopConfiguration"] = capo_datasync.types.qop_configuration.serialize_cbor(
            value["qop_configuration"]
        )
    if "authentication_type" in value:
        import capo_datasync.types.hdfs_authentication_type

        out["AuthenticationType"] = (
            capo_datasync.types.hdfs_authentication_type.serialize_cbor(
                value["authentication_type"]
            )
        )
    if "simple_user" in value:
        out["SimpleUser"] = value["simple_user"]
    if "kerberos_principal" in value:
        out["KerberosPrincipal"] = value["kerberos_principal"]
    if "agent_arns" in value:
        import capo_datasync.types.agent_arn_list

        out["AgentArns"] = capo_datasync.types.agent_arn_list.serialize_cbor(
            value["agent_arns"]
        )
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_cbor(
            value["creation_time"]
        )
    if "managed_secret_config" in value:
        import capo_datasync.types.managed_secret_config

        out["ManagedSecretConfig"] = (
            capo_datasync.types.managed_secret_config.serialize_cbor(
                value["managed_secret_config"]
            )
        )
    if "cmk_secret_config" in value:
        import capo_datasync.types.cmk_secret_config

        out["CmkSecretConfig"] = capo_datasync.types.cmk_secret_config.serialize_cbor(
            value["cmk_secret_config"]
        )
    if "custom_secret_config" in value:
        import capo_datasync.types.custom_secret_config

        out["CustomSecretConfig"] = (
            capo_datasync.types.custom_secret_config.serialize_cbor(
                value["custom_secret_config"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeLocationHdfsResponse:
    out: DescribeLocationHdfsResponse = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    if data.get("NameNodes") is not None:
        import capo_datasync.types.hdfs_name_node_list

        out["name_nodes"] = capo_datasync.types.hdfs_name_node_list.deserialize_cbor(
            data["NameNodes"]
        )
    if data.get("BlockSize") is not None:
        out["block_size"] = data["BlockSize"]
    if data.get("ReplicationFactor") is not None:
        out["replication_factor"] = data["ReplicationFactor"]
    if data.get("KmsKeyProviderUri") is not None:
        out["kms_key_provider_uri"] = data["KmsKeyProviderUri"]
    if data.get("QopConfiguration") is not None:
        import capo_datasync.types.qop_configuration

        out["qop_configuration"] = (
            capo_datasync.types.qop_configuration.deserialize_cbor(
                data["QopConfiguration"]
            )
        )
    if data.get("AuthenticationType") is not None:
        import capo_datasync.types.hdfs_authentication_type

        out["authentication_type"] = (
            capo_datasync.types.hdfs_authentication_type.deserialize_cbor(
                data["AuthenticationType"]
            )
        )
    if data.get("SimpleUser") is not None:
        out["simple_user"] = data["SimpleUser"]
    if data.get("KerberosPrincipal") is not None:
        out["kerberos_principal"] = data["KerberosPrincipal"]
    if data.get("AgentArns") is not None:
        import capo_datasync.types.agent_arn_list

        out["agent_arns"] = capo_datasync.types.agent_arn_list.deserialize_cbor(
            data["AgentArns"]
        )
    if data.get("CreationTime") is not None:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("ManagedSecretConfig") is not None:
        import capo_datasync.types.managed_secret_config

        out["managed_secret_config"] = (
            capo_datasync.types.managed_secret_config.deserialize_cbor(
                data["ManagedSecretConfig"]
            )
        )
    if data.get("CmkSecretConfig") is not None:
        import capo_datasync.types.cmk_secret_config

        out["cmk_secret_config"] = (
            capo_datasync.types.cmk_secret_config.deserialize_cbor(
                data["CmkSecretConfig"]
            )
        )
    if data.get("CustomSecretConfig") is not None:
        import capo_datasync.types.custom_secret_config

        out["custom_secret_config"] = (
            capo_datasync.types.custom_secret_config.deserialize_cbor(
                data["CustomSecretConfig"]
            )
        )
    return out
