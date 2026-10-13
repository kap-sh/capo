"""Generated from Smithy shape ``com.amazonaws.fsx#SelfManagedActiveDirectoryConfigurationUpdates``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.active_directory_fully_qualified_name
    import capo_fsx.types.customer_secrets_manager_arn
    import capo_fsx.types.directory_password
    import capo_fsx.types.directory_user_name
    import capo_fsx.types.dns_ips
    import capo_fsx.types.file_system_administrators_group_name
    import capo_fsx.types.organizational_unit_distinguished_name


class SelfManagedActiveDirectoryConfigurationUpdates(TypedDict, closed=True):
    user_name: NotRequired["capo_fsx.types.directory_user_name.DirectoryUserName"]
    """<p>Specifies the updated user name for the service account on your self-managed Active Directory domain. Amazon FSx uses this account to join to your self-managed Active Directory domain.</p> <p>This account must have the permissions required to join computers to the domain in the organizational unit provided in <code>OrganizationalUnitDistinguishedName</code>.</p>"""
    password: NotRequired["capo_fsx.types.directory_password.DirectoryPassword"]
    """<p>Specifies the updated password for the service account on your self-managed Active Directory domain. Amazon FSx uses this account to join to your self-managed Active Directory domain.</p>"""
    dns_ips: NotRequired["capo_fsx.types.dns_ips.DnsIps"]
    """<p>A list of up to three DNS server or domain controller IP addresses in your self-managed Active Directory domain.</p>"""
    domain_name: NotRequired[
        "capo_fsx.types.active_directory_fully_qualified_name.ActiveDirectoryFullyQualifiedName"
    ]
    """<p>Specifies an updated fully qualified domain name of your self-managed Active Directory configuration.</p>"""
    organizational_unit_distinguished_name: NotRequired[
        "capo_fsx.types.organizational_unit_distinguished_name.OrganizationalUnitDistinguishedName"
    ]
    """<p>Specifies an updated fully qualified distinguished name of the organization unit within your self-managed Active Directory.</p>"""
    file_system_administrators_group: NotRequired[
        "capo_fsx.types.file_system_administrators_group_name.FileSystemAdministratorsGroupName"
    ]
    """<p>For FSx for ONTAP file systems only - Specifies the updated name of the self-managed Active Directory domain group whose members are granted administrative privileges for the Amazon FSx resource.</p>"""
    domain_join_service_account_secret: NotRequired[
        "capo_fsx.types.customer_secrets_manager_arn.CustomerSecretsManagerARN"
    ]
    """<p>Specifies the updated Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret containing the self-managed Active Directory domain join service account credentials. Amazon FSx uses this account to join to your self-managed Active Directory domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: SelfManagedActiveDirectoryConfigurationUpdates,
) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "password" in value:
        out["Password"] = value["password"]
    if "dns_ips" in value:
        import capo_fsx.types.dns_ips

        out["DnsIps"] = capo_fsx.types.dns_ips.serialize_aws_json_1_1(value["dns_ips"])
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "organizational_unit_distinguished_name" in value:
        out["OrganizationalUnitDistinguishedName"] = value[
            "organizational_unit_distinguished_name"
        ]
    if "file_system_administrators_group" in value:
        out["FileSystemAdministratorsGroup"] = value["file_system_administrators_group"]
    if "domain_join_service_account_secret" in value:
        out["DomainJoinServiceAccountSecret"] = value[
            "domain_join_service_account_secret"
        ]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> SelfManagedActiveDirectoryConfigurationUpdates:
    out: SelfManagedActiveDirectoryConfigurationUpdates = {}  # type: ignore[typeddict-item]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("DnsIps") is not None:
        import capo_fsx.types.dns_ips

        out["dns_ips"] = capo_fsx.types.dns_ips.deserialize_aws_json_1_1(data["DnsIps"])
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("OrganizationalUnitDistinguishedName") is not None:
        out["organizational_unit_distinguished_name"] = data[
            "OrganizationalUnitDistinguishedName"
        ]
    if data.get("FileSystemAdministratorsGroup") is not None:
        out["file_system_administrators_group"] = data["FileSystemAdministratorsGroup"]
    if data.get("DomainJoinServiceAccountSecret") is not None:
        out["domain_join_service_account_secret"] = data[
            "DomainJoinServiceAccountSecret"
        ]
    return out


def redact_sensitive(
    value: SelfManagedActiveDirectoryConfigurationUpdates,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
