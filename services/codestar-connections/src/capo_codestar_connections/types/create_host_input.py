"""Generated from Smithy shape ``com.amazonaws.codestarconnections#CreateHostInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.host_name
    import capo_codestar_connections.types.provider_type
    import capo_codestar_connections.types.tag_list
    import capo_codestar_connections.types.url
    import capo_codestar_connections.types.vpc_configuration


class CreateHostInput(TypedDict, closed=True):
    name: "capo_codestar_connections.types.host_name.HostName"
    """<p>The name of the host to be created.</p>"""
    provider_type: "capo_codestar_connections.types.provider_type.ProviderType"
    """<p>The name of the installed provider to be associated with your connection. The host resource represents the infrastructure where your provider type is installed. The valid provider type is GitHub Enterprise Server.</p>"""
    provider_endpoint: "capo_codestar_connections.types.url.Url"
    """<p>The endpoint of the infrastructure to be represented by the host after it is created.</p>"""
    vpc_configuration: NotRequired[
        "capo_codestar_connections.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>The VPC configuration to be provisioned for the host. A VPC must be configured and the infrastructure to be represented by the host must already be connected to the VPC.</p>"""
    tags: NotRequired["capo_codestar_connections.types.tag_list.TagList"]
    """<p>Tags for the host to be created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateHostInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_codestar_connections.types.provider_type

    out["ProviderType"] = (
        capo_codestar_connections.types.provider_type.serialize_aws_json_1_0(
            value["provider_type"]
        )
    )
    out["ProviderEndpoint"] = value["provider_endpoint"]
    if "vpc_configuration" in value:
        import capo_codestar_connections.types.vpc_configuration

        out["VpcConfiguration"] = (
            capo_codestar_connections.types.vpc_configuration.serialize_aws_json_1_0(
                value["vpc_configuration"]
            )
        )
    if "tags" in value:
        import capo_codestar_connections.types.tag_list

        out["Tags"] = capo_codestar_connections.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateHostInput:
    out: CreateHostInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ProviderType") is not None:
        import capo_codestar_connections.types.provider_type

        out["provider_type"] = (
            capo_codestar_connections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    else:
        import typing

        out["provider_type"] = typing.cast(
            "capo_codestar_connections.types.provider_type.ProviderType", ""
        )
    if data.get("ProviderEndpoint") is not None:
        out["provider_endpoint"] = data["ProviderEndpoint"]
    else:
        out["provider_endpoint"] = ""
    if data.get("VpcConfiguration") is not None:
        import capo_codestar_connections.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_codestar_connections.types.vpc_configuration.deserialize_aws_json_1_0(
                data["VpcConfiguration"]
            )
        )
    if data.get("Tags") is not None:
        import capo_codestar_connections.types.tag_list

        out["tags"] = capo_codestar_connections.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
