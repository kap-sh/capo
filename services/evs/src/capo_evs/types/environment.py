"""Generated from Smithy shape ``com.amazonaws.evs#Environment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_evs.types.arn
    import capo_evs.types.check_result
    import capo_evs.types.checks_list
    import capo_evs.types.connectivity_info
    import capo_evs.types.environment_id
    import capo_evs.types.environment_name
    import capo_evs.types.environment_state
    import capo_evs.types.license_info_list
    import capo_evs.types.secret_list
    import capo_evs.types.service_access_security_groups
    import capo_evs.types.state_details
    import capo_evs.types.subnet_id
    import capo_evs.types.vcf_hostnames
    import capo_evs.types.vcf_version
    import capo_evs.types.vpc_id


class Environment(TypedDict, closed=True):
    environment_id: NotRequired["capo_evs.types.environment_id.EnvironmentId"]
    """<p>The unique ID for the environment.</p>"""
    environment_state: NotRequired["capo_evs.types.environment_state.EnvironmentState"]
    """<p>The state of an environment.</p>"""
    state_details: NotRequired["capo_evs.types.state_details.StateDetails"]
    """<p>A detailed description of the <code>environmentState</code> of an environment.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the environment was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p> The date and time that the environment was modified.</p>"""
    environment_arn: NotRequired["capo_evs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that is associated with the environment.</p>"""
    environment_name: NotRequired["capo_evs.types.environment_name.EnvironmentName"]
    """<p>The name of the environment.</p>"""
    vpc_id: NotRequired["capo_evs.types.vpc_id.VpcId"]
    """<p>The VPC associated with the environment.</p>"""
    service_access_subnet_id: NotRequired["capo_evs.types.subnet_id.SubnetId"]
    """<p> The subnet that is used to establish connectivity between the Amazon EVS control plane and VPC. Amazon EVS uses this subnet to perform validations and create the environment.</p>"""
    vcf_version: NotRequired["capo_evs.types.vcf_version.VcfVersion"]
    """<p>The VCF version of the environment.</p>"""
    terms_accepted: NotRequired["bool"]
    """<p>Customer confirmation that the customer has purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance. Amazon EVS does not validate license keys. To validate license keys, visit the Broadcom support portal. </p>"""
    license_info: NotRequired["capo_evs.types.license_info_list.LicenseInfoList"]
    """<p> The license information that Amazon EVS requires to create an environment. Amazon EVS requires two license keys: a VCF solution key and a vSAN license key. The VCF solution key must meet minimum core requirements, and the vSAN license key must meet minimum capacity requirements for your selected instance type.</p> <p>For information about minimum license requirements, see <a href="https://docs.aws.amazon.com/evs/latest/userguide/vcf-license-mgmt.html">the VCF subscriptions section</a> in the <i>Amazon EVS User Guide</i>.</p>"""
    site_id: NotRequired["str"]
    """<p>The Broadcom Site ID that is associated with your Amazon EVS environment. Amazon EVS uses the Broadcom Site ID that you provide to meet Broadcom VCF license usage reporting requirements for Amazon EVS.</p>"""
    environment_status: NotRequired["capo_evs.types.check_result.CheckResult"]
    """<p>Reports impaired functionality that stems from issues internal to the environment, such as impaired reachability.</p>"""
    checks: NotRequired["capo_evs.types.checks_list.ChecksList"]
    """<p>A check on the environment to identify connector health.</p>"""
    connectivity_info: NotRequired["capo_evs.types.connectivity_info.ConnectivityInfo"]
    """<p>The connectivity configuration for the environment. Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX uplink VLAN for connectivity to the NSX overlay network.</p>"""
    vcf_hostnames: NotRequired["capo_evs.types.vcf_hostnames.VcfHostnames"]
    """<p>The DNS hostnames to be used by the VCF management appliances in your environment.</p> <p>For environment creation to be successful, each hostname entry must resolve to a domain name that you've registered in your DNS service of choice and configured in the DHCP option set of your VPC. DNS hostnames cannot be changed after environment creation has started.</p>"""
    kms_key_id: NotRequired["str"]
    """<p>The Amazon Web Services KMS key ID that Amazon Web Services Secrets Manager uses to encrypt secrets that are associated with the environment. These secrets contain the VCF credentials that are needed to install vCenter Server, NSX, and SDDC Manager.</p> <p>By default, Amazon EVS use the Amazon Web Services Secrets Manager managed key <code>aws/secretsmanager</code>. You can also specify a customer managed key.</p>"""
    service_access_security_groups: NotRequired[
        "capo_evs.types.service_access_security_groups.ServiceAccessSecurityGroups"
    ]
    """<p>The security groups that allow traffic between the Amazon EVS control plane and your VPC for service access. If a security group is not specified, Amazon EVS uses the default security group in your account for service access.</p>"""
    credentials: NotRequired["capo_evs.types.secret_list.SecretList"]
    """<p>The VCF credentials that are stored as Amazon EVS managed secrets in Amazon Web Services Secrets Manager.</p> <p>Amazon EVS stores credentials that are needed to install vCenter Server, NSX, and SDDC Manager.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Environment) -> dict:
    out: dict = {}
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "environment_state" in value:
        import capo_evs.types.environment_state

        out["environmentState"] = (
            capo_evs.types.environment_state.serialize_aws_json_1_0(
                value["environment_state"]
            )
        )
    if "state_details" in value:
        out["stateDetails"] = value["state_details"]
    if "created_at" in value:
        import capo_evs.types._prelude.timestamp

        out["createdAt"] = capo_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "modified_at" in value:
        import capo_evs.types._prelude.timestamp

        out["modifiedAt"] = capo_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["modified_at"]
        )
    if "environment_arn" in value:
        out["environmentArn"] = value["environment_arn"]
    if "environment_name" in value:
        out["environmentName"] = value["environment_name"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "service_access_subnet_id" in value:
        out["serviceAccessSubnetId"] = value["service_access_subnet_id"]
    if "vcf_version" in value:
        import capo_evs.types.vcf_version

        out["vcfVersion"] = capo_evs.types.vcf_version.serialize_aws_json_1_0(
            value["vcf_version"]
        )
    if "terms_accepted" in value:
        out["termsAccepted"] = value["terms_accepted"]
    if "license_info" in value:
        import capo_evs.types.license_info_list

        out["licenseInfo"] = capo_evs.types.license_info_list.serialize_aws_json_1_0(
            value["license_info"]
        )
    if "site_id" in value:
        out["siteId"] = value["site_id"]
    if "environment_status" in value:
        import capo_evs.types.check_result

        out["environmentStatus"] = capo_evs.types.check_result.serialize_aws_json_1_0(
            value["environment_status"]
        )
    if "checks" in value:
        import capo_evs.types.checks_list

        out["checks"] = capo_evs.types.checks_list.serialize_aws_json_1_0(
            value["checks"]
        )
    if "connectivity_info" in value:
        import capo_evs.types.connectivity_info

        out["connectivityInfo"] = (
            capo_evs.types.connectivity_info.serialize_aws_json_1_0(
                value["connectivity_info"]
            )
        )
    if "vcf_hostnames" in value:
        import capo_evs.types.vcf_hostnames

        out["vcfHostnames"] = capo_evs.types.vcf_hostnames.serialize_aws_json_1_0(
            value["vcf_hostnames"]
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "service_access_security_groups" in value:
        import capo_evs.types.service_access_security_groups

        out["serviceAccessSecurityGroups"] = (
            capo_evs.types.service_access_security_groups.serialize_aws_json_1_0(
                value["service_access_security_groups"]
            )
        )
    if "credentials" in value:
        import capo_evs.types.secret_list

        out["credentials"] = capo_evs.types.secret_list.serialize_aws_json_1_0(
            value["credentials"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Environment:
    out: Environment = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    if data.get("environmentState") is not None:
        import capo_evs.types.environment_state

        out["environment_state"] = (
            capo_evs.types.environment_state.deserialize_aws_json_1_0(
                data["environmentState"]
            )
        )
    if data.get("stateDetails") is not None:
        out["state_details"] = data["stateDetails"]
    if data.get("createdAt") is not None:
        import capo_evs.types._prelude.timestamp

        out["created_at"] = capo_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    if data.get("modifiedAt") is not None:
        import capo_evs.types._prelude.timestamp

        out["modified_at"] = capo_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    if data.get("environmentArn") is not None:
        out["environment_arn"] = data["environmentArn"]
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    if data.get("serviceAccessSubnetId") is not None:
        out["service_access_subnet_id"] = data["serviceAccessSubnetId"]
    if data.get("vcfVersion") is not None:
        import capo_evs.types.vcf_version

        out["vcf_version"] = capo_evs.types.vcf_version.deserialize_aws_json_1_0(
            data["vcfVersion"]
        )
    if data.get("termsAccepted") is not None:
        out["terms_accepted"] = data["termsAccepted"]
    if data.get("licenseInfo") is not None:
        import capo_evs.types.license_info_list

        out["license_info"] = capo_evs.types.license_info_list.deserialize_aws_json_1_0(
            data["licenseInfo"]
        )
    if data.get("siteId") is not None:
        out["site_id"] = data["siteId"]
    if data.get("environmentStatus") is not None:
        import capo_evs.types.check_result

        out["environment_status"] = (
            capo_evs.types.check_result.deserialize_aws_json_1_0(
                data["environmentStatus"]
            )
        )
    if data.get("checks") is not None:
        import capo_evs.types.checks_list

        out["checks"] = capo_evs.types.checks_list.deserialize_aws_json_1_0(
            data["checks"]
        )
    if data.get("connectivityInfo") is not None:
        import capo_evs.types.connectivity_info

        out["connectivity_info"] = (
            capo_evs.types.connectivity_info.deserialize_aws_json_1_0(
                data["connectivityInfo"]
            )
        )
    if data.get("vcfHostnames") is not None:
        import capo_evs.types.vcf_hostnames

        out["vcf_hostnames"] = capo_evs.types.vcf_hostnames.deserialize_aws_json_1_0(
            data["vcfHostnames"]
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("serviceAccessSecurityGroups") is not None:
        import capo_evs.types.service_access_security_groups

        out["service_access_security_groups"] = (
            capo_evs.types.service_access_security_groups.deserialize_aws_json_1_0(
                data["serviceAccessSecurityGroups"]
            )
        )
    if data.get("credentials") is not None:
        import capo_evs.types.secret_list

        out["credentials"] = capo_evs.types.secret_list.deserialize_aws_json_1_0(
            data["credentials"]
        )
    return out
