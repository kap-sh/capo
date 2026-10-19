"""Generated from Smithy shape ``com.amazonaws.storagegateway#JoinDomainInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.domain_name
    import capo_storage_gateway.types.domain_user_name
    import capo_storage_gateway.types.domain_user_password
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.hosts
    import capo_storage_gateway.types.organizational_unit
    import capo_storage_gateway.types.timeout_in_seconds


class JoinDomainInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    """<p>The Amazon Resource Name (ARN) of the gateway. Use the <code>ListGateways</code> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
    domain_name: "capo_storage_gateway.types.domain_name.DomainName"
    """<p>The name of the domain that you want the gateway to join.</p>"""
    organizational_unit: NotRequired[
        "capo_storage_gateway.types.organizational_unit.OrganizationalUnit"
    ]
    """<p>The organizational unit (OU) is a container in an Active Directory that can hold users, groups, computers, and other OUs and this parameter specifies the OU that the gateway will join within the AD domain.</p>"""
    domain_controllers: NotRequired["capo_storage_gateway.types.hosts.Hosts"]
    """<p>List of IP addresses, NetBIOS names, or host names of your domain server. If you need to specify the port number include it after the colon (“:”). For example, <code>mydc.mydomain.com:389</code>.</p> <note> <p>S3 File Gateway supports IPv6 addresses in addition to IPv4 and other existing formats.</p> <p>FSx File Gateway does not support IPv6.</p> </note>"""
    timeout_in_seconds: NotRequired[
        "capo_storage_gateway.types.timeout_in_seconds.TimeoutInSeconds"
    ]
    """<p>Specifies the time in seconds, in which the <code>JoinDomain</code> operation must complete. The default is 20 seconds.</p>"""
    user_name: "capo_storage_gateway.types.domain_user_name.DomainUserName"
    """<p>Sets the user name of user who has permission to add the gateway to the Active Directory domain. The domain user account should be enabled to join computers to the domain. For example, you can use the domain administrator account or an account with delegated permissions to join computers to the domain.</p>"""
    password: "capo_storage_gateway.types.domain_user_password.DomainUserPassword"
    """<p>Sets the password of the user who has permission to add the gateway to the Active Directory domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JoinDomainInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["DomainName"] = value["domain_name"]
    if "organizational_unit" in value:
        out["OrganizationalUnit"] = value["organizational_unit"]
    if "domain_controllers" in value:
        import capo_storage_gateway.types.hosts

        out["DomainControllers"] = (
            capo_storage_gateway.types.hosts.serialize_aws_json_1_1(
                value["domain_controllers"]
            )
        )
    if "timeout_in_seconds" in value:
        out["TimeoutInSeconds"] = value["timeout_in_seconds"]
    out["UserName"] = value["user_name"]
    out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JoinDomainInput:
    out: JoinDomainInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("OrganizationalUnit") is not None:
        out["organizational_unit"] = data["OrganizationalUnit"]
    if data.get("DomainControllers") is not None:
        import capo_storage_gateway.types.hosts

        out["domain_controllers"] = (
            capo_storage_gateway.types.hosts.deserialize_aws_json_1_1(
                data["DomainControllers"]
            )
        )
    if data.get("TimeoutInSeconds") is not None:
        out["timeout_in_seconds"] = data["TimeoutInSeconds"]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    else:
        out["user_name"] = ""
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        out["password"] = ""
    return out


def redact_sensitive(value: JoinDomainInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
