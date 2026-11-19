"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationSmbResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.agent_arn_list
    import capo_datasync.types.cmk_secret_config
    import capo_datasync.types.custom_secret_config
    import capo_datasync.types.dns_ip_list
    import capo_datasync.types.kerberos_principal
    import capo_datasync.types.location_arn
    import capo_datasync.types.location_uri
    import capo_datasync.types.managed_secret_config
    import capo_datasync.types.smb_authentication_type
    import capo_datasync.types.smb_domain
    import capo_datasync.types.smb_mount_options
    import capo_datasync.types.smb_user
    import capo_datasync.types.time


class DescribeLocationSmbResponse(TypedDict, closed=True):
    location_arn: NotRequired["capo_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the SMB location.</p>"""
    location_uri: NotRequired["capo_datasync.types.location_uri.LocationUri"]
    """<p>The URI of the SMB location.</p>"""
    agent_arns: NotRequired["capo_datasync.types.agent_arn_list.AgentArnList"]
    """<p>The ARNs of the DataSync agents that can connect with your SMB file server.</p>"""
    user: NotRequired["capo_datasync.types.smb_user.SmbUser"]
    """<p>The user that can mount and access the files, folders, and file metadata in your SMB file server. This element applies only if <code>AuthenticationType</code> is set to <code>NTLM</code>.</p>"""
    domain: NotRequired["capo_datasync.types.smb_domain.SmbDomain"]
    """<p>The name of the Windows domain that the SMB file server belongs to. This element applies only if <code>AuthenticationType</code> is set to <code>NTLM</code>.</p>"""
    mount_options: NotRequired["capo_datasync.types.smb_mount_options.SmbMountOptions"]
    """<p>The SMB protocol version that DataSync uses to access your SMB file server.</p>"""
    creation_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time that the SMB location was created.</p>"""
    dns_ip_addresses: NotRequired["capo_datasync.types.dns_ip_list.DnsIpList"]
    """<p>The IPv4 or IPv6 addresses for the DNS servers that your SMB file server belongs to. This element applies only if <code>AuthenticationType</code> is set to <code>KERBEROS</code>.</p>"""
    kerberos_principal: NotRequired[
        "capo_datasync.types.kerberos_principal.KerberosPrincipal"
    ]
    """<p>The Kerberos principal that has permission to access the files, folders, and file metadata in your SMB file server.</p>"""
    authentication_type: NotRequired[
        "capo_datasync.types.smb_authentication_type.SmbAuthenticationType"
    ]
    """<p>The authentication protocol that DataSync uses to connect to your SMB file server.</p>"""
    managed_secret_config: NotRequired[
        "capo_datasync.types.managed_secret_config.ManagedSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as a <code>Password</code> or <code>KerberosKeytab</code> that DataSync uses to access a specific storage location. DataSync uses the default Amazon Web Services-managed KMS key to encrypt this secret in Secrets Manager.</p>"""
    cmk_secret_config: NotRequired[
        "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as a <code>Password</code> or <code>KerberosKeytab</code> that DataSync uses to access a specific storage location, with a customer-managed KMS key.</p>"""
    custom_secret_config: NotRequired[
        "capo_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Describes configuration information for a customer-managed secret, such as a <code>Password</code> or <code>KerberosKeytab</code> that DataSync uses to access a specific storage location, with a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationSmbResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "agent_arns" in value:
        import capo_datasync.types.agent_arn_list

        out["AgentArns"] = capo_datasync.types.agent_arn_list.serialize_aws_json_1_1(
            value["agent_arns"]
        )
    if "user" in value:
        out["User"] = value["user"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "mount_options" in value:
        import capo_datasync.types.smb_mount_options

        out["MountOptions"] = (
            capo_datasync.types.smb_mount_options.serialize_aws_json_1_1(
                value["mount_options"]
            )
        )
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "dns_ip_addresses" in value:
        import capo_datasync.types.dns_ip_list

        out["DnsIpAddresses"] = capo_datasync.types.dns_ip_list.serialize_aws_json_1_1(
            value["dns_ip_addresses"]
        )
    if "kerberos_principal" in value:
        out["KerberosPrincipal"] = value["kerberos_principal"]
    if "authentication_type" in value:
        import capo_datasync.types.smb_authentication_type

        out["AuthenticationType"] = (
            capo_datasync.types.smb_authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
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


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationSmbResponse:
    out: DescribeLocationSmbResponse = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    if data.get("AgentArns") is not None:
        import capo_datasync.types.agent_arn_list

        out["agent_arns"] = capo_datasync.types.agent_arn_list.deserialize_aws_json_1_1(
            data["AgentArns"]
        )
    if data.get("User") is not None:
        out["user"] = data["User"]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("MountOptions") is not None:
        import capo_datasync.types.smb_mount_options

        out["mount_options"] = (
            capo_datasync.types.smb_mount_options.deserialize_aws_json_1_1(
                data["MountOptions"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("DnsIpAddresses") is not None:
        import capo_datasync.types.dns_ip_list

        out["dns_ip_addresses"] = (
            capo_datasync.types.dns_ip_list.deserialize_aws_json_1_1(
                data["DnsIpAddresses"]
            )
        )
    if data.get("KerberosPrincipal") is not None:
        out["kerberos_principal"] = data["KerberosPrincipal"]
    if data.get("AuthenticationType") is not None:
        import capo_datasync.types.smb_authentication_type

        out["authentication_type"] = (
            capo_datasync.types.smb_authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
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
def serialize_cbor(value: DescribeLocationSmbResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "agent_arns" in value:
        import capo_datasync.types.agent_arn_list

        out["AgentArns"] = capo_datasync.types.agent_arn_list.serialize_cbor(
            value["agent_arns"]
        )
    if "user" in value:
        out["User"] = value["user"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "mount_options" in value:
        import capo_datasync.types.smb_mount_options

        out["MountOptions"] = capo_datasync.types.smb_mount_options.serialize_cbor(
            value["mount_options"]
        )
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_cbor(
            value["creation_time"]
        )
    if "dns_ip_addresses" in value:
        import capo_datasync.types.dns_ip_list

        out["DnsIpAddresses"] = capo_datasync.types.dns_ip_list.serialize_cbor(
            value["dns_ip_addresses"]
        )
    if "kerberos_principal" in value:
        out["KerberosPrincipal"] = value["kerberos_principal"]
    if "authentication_type" in value:
        import capo_datasync.types.smb_authentication_type

        out["AuthenticationType"] = (
            capo_datasync.types.smb_authentication_type.serialize_cbor(
                value["authentication_type"]
            )
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


def deserialize_cbor(data: dict) -> DescribeLocationSmbResponse:
    out: DescribeLocationSmbResponse = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    if data.get("AgentArns") is not None:
        import capo_datasync.types.agent_arn_list

        out["agent_arns"] = capo_datasync.types.agent_arn_list.deserialize_cbor(
            data["AgentArns"]
        )
    if data.get("User") is not None:
        out["user"] = data["User"]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("MountOptions") is not None:
        import capo_datasync.types.smb_mount_options

        out["mount_options"] = capo_datasync.types.smb_mount_options.deserialize_cbor(
            data["MountOptions"]
        )
    if data.get("CreationTime") is not None:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("DnsIpAddresses") is not None:
        import capo_datasync.types.dns_ip_list

        out["dns_ip_addresses"] = capo_datasync.types.dns_ip_list.deserialize_cbor(
            data["DnsIpAddresses"]
        )
    if data.get("KerberosPrincipal") is not None:
        out["kerberos_principal"] = data["KerberosPrincipal"]
    if data.get("AuthenticationType") is not None:
        import capo_datasync.types.smb_authentication_type

        out["authentication_type"] = (
            capo_datasync.types.smb_authentication_type.deserialize_cbor(
                data["AuthenticationType"]
            )
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
