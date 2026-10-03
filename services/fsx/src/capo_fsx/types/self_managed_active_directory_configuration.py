"""Generated from Smithy shape ``com.amazonaws.fsx#SelfManagedActiveDirectoryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.active_directory_fully_qualified_name
    import capo_fsx.types.customer_secrets_manager_arn
    import capo_fsx.types.directory_password
    import capo_fsx.types.directory_user_name
    import capo_fsx.types.dns_ips
    import capo_fsx.types.file_system_administrators_group_name
    import capo_fsx.types.organizational_unit_distinguished_name


class SelfManagedActiveDirectoryConfiguration(TypedDict, closed=True):
    domain_name: NotRequired[
        "capo_fsx.types.active_directory_fully_qualified_name.ActiveDirectoryFullyQualifiedName"
    ]
    """<p>The fully qualified domain name of the self-managed AD directory, such as <code>corp.example.com</code>.</p>"""
    organizational_unit_distinguished_name: NotRequired[
        "capo_fsx.types.organizational_unit_distinguished_name.OrganizationalUnitDistinguishedName"
    ]
    """<p>(Optional) The fully qualified distinguished name of the organizational unit within your self-managed AD directory. Amazon FSx only accepts OU as the direct parent of the file system. An example is <code>OU=FSx,DC=yourdomain,DC=corp,DC=com</code>. To learn more, see <a href="https://tools.ietf.org/html/rfc2253">RFC 2253</a>. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. </p> <important> <p>Only Organizational Unit (OU) objects can be the direct parent of the file system that you're creating.</p> </important>"""
    file_system_administrators_group: NotRequired[
        "capo_fsx.types.file_system_administrators_group_name.FileSystemAdministratorsGroupName"
    ]
    """<p>(Optional) The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, setting audit controls (audit ACLs) on files and folders, and administering the file system remotely by using the FSx Remote PowerShell. The group that you specify must already exist in your domain. If you don't provide one, your AD domain's Domain Admins group is used.</p>"""
    user_name: NotRequired["capo_fsx.types.directory_user_name.DirectoryUserName"]
    """<p>The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain. This account must have the permission to join computers to the domain in the organizational unit provided in <code>OrganizationalUnitDistinguishedName</code>, or in the default location of your AD domain.</p>"""
    password: NotRequired["capo_fsx.types.directory_password.DirectoryPassword"]
    """<p>The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.</p>"""
    dns_ips: NotRequired["capo_fsx.types.dns_ips.DnsIps"]
    """<p>A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory. </p>"""
    domain_join_service_account_secret: NotRequired[
        "capo_fsx.types.customer_secrets_manager_arn.CustomerSecretsManagerARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret containing the self-managed Active Directory domain join service account credentials. When provided, Amazon FSx uses the credentials stored in this secret to join the file system to your self-managed Active Directory domain.</p> <p>The secret must contain two key-value pairs:</p> <ul> <li> <p> <code>CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME</code> - The username for the service account</p> </li> <li> <p> <code>CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD</code> - The password for the service account</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-manage-prereqs.html"> Using Amazon FSx for Windows with your self-managed Microsoft Active Directory</a> or <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/self-manage-prereqs.html"> Using Amazon FSx for ONTAP with your self-managed Microsoft Active Directory</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelfManagedActiveDirectoryConfiguration) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "organizational_unit_distinguished_name" in value:
        out["OrganizationalUnitDistinguishedName"] = value[
            "organizational_unit_distinguished_name"
        ]
    if "file_system_administrators_group" in value:
        out["FileSystemAdministratorsGroup"] = value["file_system_administrators_group"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "password" in value:
        out["Password"] = value["password"]
    if "dns_ips" in value:
        import capo_fsx.types.dns_ips

        out["DnsIps"] = capo_fsx.types.dns_ips.serialize_aws_json_1_1(value["dns_ips"])
    if "domain_join_service_account_secret" in value:
        out["DomainJoinServiceAccountSecret"] = value[
            "domain_join_service_account_secret"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> SelfManagedActiveDirectoryConfiguration:
    out: SelfManagedActiveDirectoryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("OrganizationalUnitDistinguishedName") is not None:
        out["organizational_unit_distinguished_name"] = data[
            "OrganizationalUnitDistinguishedName"
        ]
    if data.get("FileSystemAdministratorsGroup") is not None:
        out["file_system_administrators_group"] = data["FileSystemAdministratorsGroup"]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("DnsIps") is not None:
        import capo_fsx.types.dns_ips

        out["dns_ips"] = capo_fsx.types.dns_ips.deserialize_aws_json_1_1(data["DnsIps"])
    if data.get("DomainJoinServiceAccountSecret") is not None:
        out["domain_join_service_account_secret"] = data[
            "DomainJoinServiceAccountSecret"
        ]
    return out
