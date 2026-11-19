"""Generated from Smithy shape ``com.amazonaws.codeconnections#GetHostOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.host_name
    import capo_codeconnections.types.host_status
    import capo_codeconnections.types.provider_type
    import capo_codeconnections.types.url
    import capo_codeconnections.types.vpc_configuration


class GetHostOutput(TypedDict, closed=True):
    name: NotRequired["capo_codeconnections.types.host_name.HostName"]
    """<p>The name of the requested host.</p>"""
    status: NotRequired["capo_codeconnections.types.host_status.HostStatus"]
    """<p>The status of the requested host.</p>"""
    provider_type: NotRequired["capo_codeconnections.types.provider_type.ProviderType"]
    """<p>The provider type of the requested host, such as GitHub Enterprise Server.</p>"""
    provider_endpoint: NotRequired["capo_codeconnections.types.url.Url"]
    """<p>The endpoint of the infrastructure represented by the requested host.</p>"""
    vpc_configuration: NotRequired[
        "capo_codeconnections.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>The VPC configuration of the requested host.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetHostOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> GetHostOutput:
    out: GetHostOutput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
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
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetHostOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
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
    return out


def deserialize_cbor(data: dict) -> GetHostOutput:
    out: GetHostOutput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
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
    return out
