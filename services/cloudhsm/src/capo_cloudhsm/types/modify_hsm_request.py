"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ModifyHsmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.external_id
    import capo_cloudhsm.types.hsm_arn
    import capo_cloudhsm.types.iam_role_arn
    import capo_cloudhsm.types.ip_address
    import capo_cloudhsm.types.subnet_id


class ModifyHsmRequest(TypedDict, closed=True):
    hsm_arn: "capo_cloudhsm.types.hsm_arn.HsmArn"
    """<p>The ARN of the HSM to modify.</p>"""
    subnet_id: NotRequired["capo_cloudhsm.types.subnet_id.SubnetId"]
    """<p>The new identifier of the subnet that the HSM is in. The new subnet must be in the same Availability Zone as the current subnet.</p>"""
    eni_ip: NotRequired["capo_cloudhsm.types.ip_address.IpAddress"]
    """<p>The new IP address for the elastic network interface (ENI) attached to the HSM.</p> <p>If the HSM is moved to a different subnet, and an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the new subnet.</p>"""
    iam_role_arn: NotRequired["capo_cloudhsm.types.iam_role_arn.IamRoleArn"]
    """<p>The new IAM role ARN.</p>"""
    external_id: NotRequired["capo_cloudhsm.types.external_id.ExternalId"]
    """<p>The new external ID.</p>"""
    syslog_ip: NotRequired["capo_cloudhsm.types.ip_address.IpAddress"]
    """<p>The new IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyHsmRequest) -> dict:
    out: dict = {}
    out["HsmArn"] = value["hsm_arn"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "eni_ip" in value:
        out["EniIp"] = value["eni_ip"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    if "syslog_ip" in value:
        out["SyslogIp"] = value["syslog_ip"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyHsmRequest:
    out: ModifyHsmRequest = {}  # type: ignore[typeddict-item]
    if data.get("HsmArn") is not None:
        out["hsm_arn"] = data["HsmArn"]
    else:
        out["hsm_arn"] = ""
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    if data.get("EniIp") is not None:
        out["eni_ip"] = data["EniIp"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("ExternalId") is not None:
        out["external_id"] = data["ExternalId"]
    if data.get("SyslogIp") is not None:
        out["syslog_ip"] = data["SyslogIp"]
    return out
