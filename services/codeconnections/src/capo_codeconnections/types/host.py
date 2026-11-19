"""Generated from Smithy shape ``com.amazonaws.codeconnections#Host``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.host_arn
    import capo_codeconnections.types.host_name
    import capo_codeconnections.types.host_status
    import capo_codeconnections.types.host_status_message
    import capo_codeconnections.types.provider_type
    import capo_codeconnections.types.url
    import capo_codeconnections.types.vpc_configuration


class Host(TypedDict, closed=True):
    name: NotRequired["capo_codeconnections.types.host_name.HostName"]
    """<p>The name of the host.</p>"""
    host_arn: NotRequired["capo_codeconnections.types.host_arn.HostArn"]
    """<p>The Amazon Resource Name (ARN) of the host.</p>"""
    provider_type: NotRequired["capo_codeconnections.types.provider_type.ProviderType"]
    """<p>The name of the installed provider to be associated with your connection. The host resource represents the infrastructure where your provider type is installed. The valid provider type is GitHub Enterprise Server.</p>"""
    provider_endpoint: NotRequired["capo_codeconnections.types.url.Url"]
    """<p>The endpoint of the infrastructure where your provider type is installed.</p>"""
    vpc_configuration: NotRequired[
        "capo_codeconnections.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>The VPC configuration provisioned for the host.</p>"""
    status: NotRequired["capo_codeconnections.types.host_status.HostStatus"]
    """<p>The status of the host, such as PENDING, AVAILABLE, VPC_CONFIG_DELETING, VPC_CONFIG_INITIALIZING, and VPC_CONFIG_FAILED_INITIALIZATION.</p>"""
    status_message: NotRequired[
        "capo_codeconnections.types.host_status_message.HostStatusMessage"
    ]
    """<p>The status description for the host.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Host) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "host_arn" in value:
        out["HostArn"] = value["host_arn"]
    if "provider_type" in value:
        import capo_codeconnections.types.provider_type

        out["ProviderType"] = (
            capo_codeconnections.types.provider_type.serialize_aws_json_1_0(
                value["provider_type"]
            )
        )
    if "provider_endpoint" in value:
        out["ProviderEndpoint"] = value["provider_endpoint"]
    if "vpc_configuration" in value:
        import capo_codeconnections.types.vpc_configuration

        out["VpcConfiguration"] = (
            capo_codeconnections.types.vpc_configuration.serialize_aws_json_1_0(
                value["vpc_configuration"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Host:
    out: Host = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("HostArn") is not None:
        out["host_arn"] = data["HostArn"]
    if data.get("ProviderType") is not None:
        import capo_codeconnections.types.provider_type

        out["provider_type"] = (
            capo_codeconnections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    if data.get("ProviderEndpoint") is not None:
        out["provider_endpoint"] = data["ProviderEndpoint"]
    if data.get("VpcConfiguration") is not None:
        import capo_codeconnections.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_codeconnections.types.vpc_configuration.deserialize_aws_json_1_0(
                data["VpcConfiguration"]
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Host) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "host_arn" in value:
        out["HostArn"] = value["host_arn"]
    if "provider_type" in value:
        import capo_codeconnections.types.provider_type

        out["ProviderType"] = capo_codeconnections.types.provider_type.serialize_cbor(
            value["provider_type"]
        )
    if "provider_endpoint" in value:
        out["ProviderEndpoint"] = value["provider_endpoint"]
    if "vpc_configuration" in value:
        import capo_codeconnections.types.vpc_configuration

        out["VpcConfiguration"] = (
            capo_codeconnections.types.vpc_configuration.serialize_cbor(
                value["vpc_configuration"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_cbor(data: dict) -> Host:
    out: Host = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("HostArn") is not None:
        out["host_arn"] = data["HostArn"]
    if data.get("ProviderType") is not None:
        import capo_codeconnections.types.provider_type

        out["provider_type"] = (
            capo_codeconnections.types.provider_type.deserialize_cbor(
                data["ProviderType"]
            )
        )
    if data.get("ProviderEndpoint") is not None:
        out["provider_endpoint"] = data["ProviderEndpoint"]
    if data.get("VpcConfiguration") is not None:
        import capo_codeconnections.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_codeconnections.types.vpc_configuration.deserialize_cbor(
                data["VpcConfiguration"]
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
