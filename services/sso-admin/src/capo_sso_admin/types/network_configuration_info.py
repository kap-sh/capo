"""Generated from Smithy shape ``com.amazonaws.ssoadmin#NetworkConfigurationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn_list
    import capo_sso_admin.types.ip_cidr_list
    import capo_sso_admin.types.vpc_arn_list


class NetworkConfigurationInfo(TypedDict, closed=True):
    vpce_access_required: "bool"
    """<p>Specifies whether access to your Identity Center instance and to applications must originate from a VPC endpoint. When this value is <code>true</code> and no other field is specified, access is allowed from any VPC in your organization, or from any VPC in the Amazon Web Services account for an account instance, and applies to all applications. When this value is <code>false</code>, no network access control is enforced and the values of <code>RestrictSourceVpcs</code>, <code>AllowSourceIps</code>, and <code>ExcludeApplicationArns</code> are cleared.</p>"""
    restrict_source_vpcs: NotRequired["capo_sso_admin.types.vpc_arn_list.VpcArnList"]
    """<p>Limits access to the VPC endpoints in the VPCs that you specify. These VPCs must be in your organization, or in the Amazon Web Services account for an account instance. If you don't specify this value, access is allowed from any VPC in your organization or Amazon Web Services account.</p>"""
    allow_source_ips: NotRequired["capo_sso_admin.types.ip_cidr_list.IpCidrList"]
    """<p>Allows access from the IPv4 or IPv6 CIDR blocks that you specify, in addition to the VPCs allowed by <code>RestrictSourceVpcs</code>. If you don't specify this value, no additional IP address ranges are allowed.</p>"""
    exclude_application_arns: NotRequired[
        "capo_sso_admin.types.application_arn_list.ApplicationArnList"
    ]
    """<p>Exempts the applications that you specify from the network access control, so that access to them is unchanged. You can specify both Amazon Web Services managed applications and customer managed applications, and you can use wildcards. These applications are not restricted by <code>RestrictSourceVpcs</code> or <code>AllowSourceIps</code>. If you don't specify this value, the controls apply to all applications.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkConfigurationInfo) -> dict:
    out: dict = {}
    out["VpceAccessRequired"] = value["vpce_access_required"]
    if "restrict_source_vpcs" in value:
        import capo_sso_admin.types.vpc_arn_list

        out["RestrictSourceVpcs"] = (
            capo_sso_admin.types.vpc_arn_list.serialize_aws_json_1_1(
                value["restrict_source_vpcs"]
            )
        )
    if "allow_source_ips" in value:
        import capo_sso_admin.types.ip_cidr_list

        out["AllowSourceIps"] = (
            capo_sso_admin.types.ip_cidr_list.serialize_aws_json_1_1(
                value["allow_source_ips"]
            )
        )
    if "exclude_application_arns" in value:
        import capo_sso_admin.types.application_arn_list

        out["ExcludeApplicationArns"] = (
            capo_sso_admin.types.application_arn_list.serialize_aws_json_1_1(
                value["exclude_application_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkConfigurationInfo:
    out: NetworkConfigurationInfo = {}  # type: ignore[typeddict-item]
    if data.get("VpceAccessRequired") is not None:
        out["vpce_access_required"] = data["VpceAccessRequired"]
    else:
        out["vpce_access_required"] = False
    if data.get("RestrictSourceVpcs") is not None:
        import capo_sso_admin.types.vpc_arn_list

        out["restrict_source_vpcs"] = (
            capo_sso_admin.types.vpc_arn_list.deserialize_aws_json_1_1(
                data["RestrictSourceVpcs"]
            )
        )
    if data.get("AllowSourceIps") is not None:
        import capo_sso_admin.types.ip_cidr_list

        out["allow_source_ips"] = (
            capo_sso_admin.types.ip_cidr_list.deserialize_aws_json_1_1(
                data["AllowSourceIps"]
            )
        )
    if data.get("ExcludeApplicationArns") is not None:
        import capo_sso_admin.types.application_arn_list

        out["exclude_application_arns"] = (
            capo_sso_admin.types.application_arn_list.deserialize_aws_json_1_1(
                data["ExcludeApplicationArns"]
            )
        )
    return out
