"""Generated from Smithy shape ``com.amazonaws.sagemaker#Workforce``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cognito_config
    import capo_sagemaker.types.oidc_config_for_response
    import capo_sagemaker.types.source_ip_config
    import capo_sagemaker.types.string
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.workforce_arn
    import capo_sagemaker.types.workforce_failure_reason
    import capo_sagemaker.types.workforce_ip_address_type
    import capo_sagemaker.types.workforce_name
    import capo_sagemaker.types.workforce_status
    import capo_sagemaker.types.workforce_vpc_config_response


class Workforce(TypedDict, closed=True):
    workforce_name: NotRequired["capo_sagemaker.types.workforce_name.WorkforceName"]
    """<p>The name of the private workforce.</p>"""
    workforce_arn: NotRequired["capo_sagemaker.types.workforce_arn.WorkforceArn"]
    """<p>The Amazon Resource Name (ARN) of the private workforce.</p>"""
    last_updated_date: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The most recent date that <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateWorkforce.html">UpdateWorkforce</a> was used to successfully add one or more IP address ranges (<a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html">CIDRs</a>) to a private workforce's allow list.</p>"""
    source_ip_config: NotRequired[
        "capo_sagemaker.types.source_ip_config.SourceIpConfig"
    ]
    """<p>A list of one to ten IP address ranges (<a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html">CIDRs</a>) to be added to the workforce allow list. By default, a workforce isn't restricted to specific IP addresses.</p>"""
    sub_domain: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The subdomain for your OIDC Identity Provider.</p>"""
    cognito_config: NotRequired["capo_sagemaker.types.cognito_config.CognitoConfig"]
    """<p>The configuration of an Amazon Cognito workforce. A single Cognito workforce is created using and corresponds to a single <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html"> Amazon Cognito user pool</a>.</p>"""
    oidc_config: NotRequired[
        "capo_sagemaker.types.oidc_config_for_response.OidcConfigForResponse"
    ]
    """<p>The configuration of an OIDC Identity Provider (IdP) private workforce.</p>"""
    create_date: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date that the workforce is created.</p>"""
    workforce_vpc_config: NotRequired[
        "capo_sagemaker.types.workforce_vpc_config_response.WorkforceVpcConfigResponse"
    ]
    """<p>The configuration of a VPC workforce.</p>"""
    status: NotRequired["capo_sagemaker.types.workforce_status.WorkforceStatus"]
    """<p>The status of your workforce.</p>"""
    failure_reason: NotRequired[
        "capo_sagemaker.types.workforce_failure_reason.WorkforceFailureReason"
    ]
    """<p>The reason your workforce failed.</p>"""
    ip_address_type: NotRequired[
        "capo_sagemaker.types.workforce_ip_address_type.WorkforceIpAddressType"
    ]
    """<p>The IP address type you specify - either <code>IPv4</code> only or <code>dualstack</code> (<code>IPv4</code> and <code>IPv6</code>) - to support your labeling workforce.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Workforce) -> dict:
    out: dict = {}
    if "workforce_name" in value:
        out["WorkforceName"] = value["workforce_name"]
    if "workforce_arn" in value:
        out["WorkforceArn"] = value["workforce_arn"]
    if "last_updated_date" in value:
        import capo_sagemaker.types.timestamp

        out["LastUpdatedDate"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_date"]
        )
    if "source_ip_config" in value:
        import capo_sagemaker.types.source_ip_config

        out["SourceIpConfig"] = (
            capo_sagemaker.types.source_ip_config.serialize_aws_json_1_1(
                value["source_ip_config"]
            )
        )
    if "sub_domain" in value:
        out["SubDomain"] = value["sub_domain"]
    if "cognito_config" in value:
        import capo_sagemaker.types.cognito_config

        out["CognitoConfig"] = (
            capo_sagemaker.types.cognito_config.serialize_aws_json_1_1(
                value["cognito_config"]
            )
        )
    if "oidc_config" in value:
        import capo_sagemaker.types.oidc_config_for_response

        out["OidcConfig"] = (
            capo_sagemaker.types.oidc_config_for_response.serialize_aws_json_1_1(
                value["oidc_config"]
            )
        )
    if "create_date" in value:
        import capo_sagemaker.types.timestamp

        out["CreateDate"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["create_date"]
        )
    if "workforce_vpc_config" in value:
        import capo_sagemaker.types.workforce_vpc_config_response

        out["WorkforceVpcConfig"] = (
            capo_sagemaker.types.workforce_vpc_config_response.serialize_aws_json_1_1(
                value["workforce_vpc_config"]
            )
        )
    if "status" in value:
        import capo_sagemaker.types.workforce_status

        out["Status"] = capo_sagemaker.types.workforce_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "ip_address_type" in value:
        import capo_sagemaker.types.workforce_ip_address_type

        out["IpAddressType"] = (
            capo_sagemaker.types.workforce_ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Workforce:
    out: Workforce = {}  # type: ignore[typeddict-item]
    if data.get("WorkforceName") is not None:
        out["workforce_name"] = data["WorkforceName"]
    if data.get("WorkforceArn") is not None:
        out["workforce_arn"] = data["WorkforceArn"]
    if data.get("LastUpdatedDate") is not None:
        import capo_sagemaker.types.timestamp

        out["last_updated_date"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedDate"]
            )
        )
    if data.get("SourceIpConfig") is not None:
        import capo_sagemaker.types.source_ip_config

        out["source_ip_config"] = (
            capo_sagemaker.types.source_ip_config.deserialize_aws_json_1_1(
                data["SourceIpConfig"]
            )
        )
    if data.get("SubDomain") is not None:
        out["sub_domain"] = data["SubDomain"]
    if data.get("CognitoConfig") is not None:
        import capo_sagemaker.types.cognito_config

        out["cognito_config"] = (
            capo_sagemaker.types.cognito_config.deserialize_aws_json_1_1(
                data["CognitoConfig"]
            )
        )
    if data.get("OidcConfig") is not None:
        import capo_sagemaker.types.oidc_config_for_response

        out["oidc_config"] = (
            capo_sagemaker.types.oidc_config_for_response.deserialize_aws_json_1_1(
                data["OidcConfig"]
            )
        )
    if data.get("CreateDate") is not None:
        import capo_sagemaker.types.timestamp

        out["create_date"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreateDate"]
        )
    if data.get("WorkforceVpcConfig") is not None:
        import capo_sagemaker.types.workforce_vpc_config_response

        out["workforce_vpc_config"] = (
            capo_sagemaker.types.workforce_vpc_config_response.deserialize_aws_json_1_1(
                data["WorkforceVpcConfig"]
            )
        )
    if data.get("Status") is not None:
        import capo_sagemaker.types.workforce_status

        out["status"] = capo_sagemaker.types.workforce_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("IpAddressType") is not None:
        import capo_sagemaker.types.workforce_ip_address_type

        out["ip_address_type"] = (
            capo_sagemaker.types.workforce_ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
            )
        )
    return out
