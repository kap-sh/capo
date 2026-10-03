"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateWorkforceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cognito_config
    import capo_sagemaker.types.oidc_config
    import capo_sagemaker.types.source_ip_config
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.workforce_ip_address_type
    import capo_sagemaker.types.workforce_name
    import capo_sagemaker.types.workforce_vpc_config_request


class CreateWorkforceRequest(TypedDict, closed=True):
    cognito_config: NotRequired["capo_sagemaker.types.cognito_config.CognitoConfig"]
    """<p>Use this parameter to configure an Amazon Cognito private workforce. A single Cognito workforce is created using and corresponds to a single <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html"> Amazon Cognito user pool</a>.</p> <p>Do not use <code>OidcConfig</code> if you specify values for <code>CognitoConfig</code>.</p>"""
    oidc_config: NotRequired["capo_sagemaker.types.oidc_config.OidcConfig"]
    """<p>Use this parameter to configure a private workforce using your own OIDC Identity Provider.</p> <p>Do not use <code>CognitoConfig</code> if you specify values for <code>OidcConfig</code>.</p>"""
    source_ip_config: NotRequired[
        "capo_sagemaker.types.source_ip_config.SourceIpConfig"
    ]
    workforce_name: NotRequired["capo_sagemaker.types.workforce_name.WorkforceName"]
    """<p>The name of the private workforce.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs that contain metadata to help you categorize and organize our workforce. Each tag consists of a key and a value, both of which you define.</p>"""
    workforce_vpc_config: NotRequired[
        "capo_sagemaker.types.workforce_vpc_config_request.WorkforceVpcConfigRequest"
    ]
    """<p>Use this parameter to configure a workforce using VPC.</p>"""
    ip_address_type: NotRequired[
        "capo_sagemaker.types.workforce_ip_address_type.WorkforceIpAddressType"
    ]
    """<p>Use this parameter to specify whether you want <code>IPv4</code> only or <code>dualstack</code> (<code>IPv4</code> and <code>IPv6</code>) to support your labeling workforce.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkforceRequest) -> dict:
    out: dict = {}
    if "cognito_config" in value:
        import capo_sagemaker.types.cognito_config

        out["CognitoConfig"] = (
            capo_sagemaker.types.cognito_config.serialize_aws_json_1_1(
                value["cognito_config"]
            )
        )
    if "oidc_config" in value:
        import capo_sagemaker.types.oidc_config

        out["OidcConfig"] = capo_sagemaker.types.oidc_config.serialize_aws_json_1_1(
            value["oidc_config"]
        )
    if "source_ip_config" in value:
        import capo_sagemaker.types.source_ip_config

        out["SourceIpConfig"] = (
            capo_sagemaker.types.source_ip_config.serialize_aws_json_1_1(
                value["source_ip_config"]
            )
        )
    if "workforce_name" in value:
        out["WorkforceName"] = value["workforce_name"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "workforce_vpc_config" in value:
        import capo_sagemaker.types.workforce_vpc_config_request

        out["WorkforceVpcConfig"] = (
            capo_sagemaker.types.workforce_vpc_config_request.serialize_aws_json_1_1(
                value["workforce_vpc_config"]
            )
        )
    if "ip_address_type" in value:
        import capo_sagemaker.types.workforce_ip_address_type

        out["IpAddressType"] = (
            capo_sagemaker.types.workforce_ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkforceRequest:
    out: CreateWorkforceRequest = {}  # type: ignore[typeddict-item]
    if data.get("CognitoConfig") is not None:
        import capo_sagemaker.types.cognito_config

        out["cognito_config"] = (
            capo_sagemaker.types.cognito_config.deserialize_aws_json_1_1(
                data["CognitoConfig"]
            )
        )
    if data.get("OidcConfig") is not None:
        import capo_sagemaker.types.oidc_config

        out["oidc_config"] = capo_sagemaker.types.oidc_config.deserialize_aws_json_1_1(
            data["OidcConfig"]
        )
    if data.get("SourceIpConfig") is not None:
        import capo_sagemaker.types.source_ip_config

        out["source_ip_config"] = (
            capo_sagemaker.types.source_ip_config.deserialize_aws_json_1_1(
                data["SourceIpConfig"]
            )
        )
    if data.get("WorkforceName") is not None:
        out["workforce_name"] = data["WorkforceName"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("WorkforceVpcConfig") is not None:
        import capo_sagemaker.types.workforce_vpc_config_request

        out["workforce_vpc_config"] = (
            capo_sagemaker.types.workforce_vpc_config_request.deserialize_aws_json_1_1(
                data["WorkforceVpcConfig"]
            )
        )
    if data.get("IpAddressType") is not None:
        import capo_sagemaker.types.workforce_ip_address_type

        out["ip_address_type"] = (
            capo_sagemaker.types.workforce_ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
            )
        )
    return out
