"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CreateHsmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.client_token
    import capo_cloudhsm.types.external_id
    import capo_cloudhsm.types.iam_role_arn
    import capo_cloudhsm.types.ip_address
    import capo_cloudhsm.types.ssh_key
    import capo_cloudhsm.types.subnet_id
    import capo_cloudhsm.types.subscription_type


class CreateHsmRequest(TypedDict, closed=True):
    subnet_id: "capo_cloudhsm.types.subnet_id.SubnetId"
    """<p>The identifier of the subnet in your VPC in which to place the HSM.</p>"""
    ssh_key: "capo_cloudhsm.types.ssh_key.SshKey"
    """<p>The SSH public key to install on the HSM.</p>"""
    eni_ip: NotRequired["capo_cloudhsm.types.ip_address.IpAddress"]
    """<p>The IP address to assign to the HSM's ENI.</p> <p>If an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the subnet.</p>"""
    iam_role_arn: "capo_cloudhsm.types.iam_role_arn.IamRoleArn"
    """<p>The ARN of an IAM role to enable the AWS CloudHSM service to allocate an ENI on your behalf.</p>"""
    external_id: NotRequired["capo_cloudhsm.types.external_id.ExternalId"]
    """<p>The external ID from <code>IamRoleArn</code>, if present.</p>"""
    subscription_type: "capo_cloudhsm.types.subscription_type.SubscriptionType"
    client_token: NotRequired["capo_cloudhsm.types.client_token.ClientToken"]
    """<p>A user-defined token to ensure idempotence. Subsequent calls to this operation with the same token will be ignored.</p>"""
    syslog_ip: NotRequired["capo_cloudhsm.types.ip_address.IpAddress"]
    """<p>The IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHsmRequest) -> dict:
    out: dict = {}
    out["SubnetId"] = value["subnet_id"]
    out["SshKey"] = value["ssh_key"]
    if "eni_ip" in value:
        out["EniIp"] = value["eni_ip"]
    out["IamRoleArn"] = value["iam_role_arn"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    import capo_cloudhsm.types.subscription_type

    out["SubscriptionType"] = (
        capo_cloudhsm.types.subscription_type.serialize_aws_json_1_1(
            value["subscription_type"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "syslog_ip" in value:
        out["SyslogIp"] = value["syslog_ip"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHsmRequest:
    out: CreateHsmRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    else:
        out["subnet_id"] = ""
    if data.get("SshKey") is not None:
        out["ssh_key"] = data["SshKey"]
    else:
        out["ssh_key"] = ""
    if data.get("EniIp") is not None:
        out["eni_ip"] = data["EniIp"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        out["iam_role_arn"] = ""
    if data.get("ExternalId") is not None:
        out["external_id"] = data["ExternalId"]
    if data.get("SubscriptionType") is not None:
        import capo_cloudhsm.types.subscription_type

        out["subscription_type"] = (
            capo_cloudhsm.types.subscription_type.deserialize_aws_json_1_1(
                data["SubscriptionType"]
            )
        )
    else:
        import typing

        out["subscription_type"] = typing.cast(
            "capo_cloudhsm.types.subscription_type.SubscriptionType", ""
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("SyslogIp") is not None:
        out["syslog_ip"] = data["SyslogIp"]
    return out
