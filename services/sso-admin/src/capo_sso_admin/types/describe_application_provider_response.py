"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeApplicationProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_provider_arn
    import capo_sso_admin.types.display_data
    import capo_sso_admin.types.federation_protocol
    import capo_sso_admin.types.resource_server_config


class DescribeApplicationProviderResponse(TypedDict, closed=True):
    application_provider_arn: (
        "capo_sso_admin.types.application_provider_arn.ApplicationProviderArn"
    )
    """<p>The ARN of the application provider.</p>"""
    federation_protocol: NotRequired[
        "capo_sso_admin.types.federation_protocol.FederationProtocol"
    ]
    """<p>The protocol used to federate to the application provider.</p>"""
    display_data: NotRequired["capo_sso_admin.types.display_data.DisplayData"]
    """<p>A structure with details about the display data for the application provider.</p>"""
    resource_server_config: NotRequired[
        "capo_sso_admin.types.resource_server_config.ResourceServerConfig"
    ]
    """<p>A structure with details about the receiving application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationProviderResponse) -> dict:
    out: dict = {}
    out["ApplicationProviderArn"] = value["application_provider_arn"]
    if "federation_protocol" in value:
        import capo_sso_admin.types.federation_protocol

        out["FederationProtocol"] = (
            capo_sso_admin.types.federation_protocol.serialize_aws_json_1_1(
                value["federation_protocol"]
            )
        )
    if "display_data" in value:
        import capo_sso_admin.types.display_data

        out["DisplayData"] = capo_sso_admin.types.display_data.serialize_aws_json_1_1(
            value["display_data"]
        )
    if "resource_server_config" in value:
        import capo_sso_admin.types.resource_server_config

        out["ResourceServerConfig"] = (
            capo_sso_admin.types.resource_server_config.serialize_aws_json_1_1(
                value["resource_server_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationProviderResponse:
    out: DescribeApplicationProviderResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationProviderArn") is not None:
        out["application_provider_arn"] = data["ApplicationProviderArn"]
    else:
        out["application_provider_arn"] = ""
    if data.get("FederationProtocol") is not None:
        import capo_sso_admin.types.federation_protocol

        out["federation_protocol"] = (
            capo_sso_admin.types.federation_protocol.deserialize_aws_json_1_1(
                data["FederationProtocol"]
            )
        )
    if data.get("DisplayData") is not None:
        import capo_sso_admin.types.display_data

        out["display_data"] = (
            capo_sso_admin.types.display_data.deserialize_aws_json_1_1(
                data["DisplayData"]
            )
        )
    if data.get("ResourceServerConfig") is not None:
        import capo_sso_admin.types.resource_server_config

        out["resource_server_config"] = (
            capo_sso_admin.types.resource_server_config.deserialize_aws_json_1_1(
                data["ResourceServerConfig"]
            )
        )
    return out
