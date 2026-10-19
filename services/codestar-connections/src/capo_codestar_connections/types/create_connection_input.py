"""Generated from Smithy shape ``com.amazonaws.codestarconnections#CreateConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.connection_name
    import capo_codestar_connections.types.host_arn
    import capo_codestar_connections.types.provider_type
    import capo_codestar_connections.types.tag_list


class CreateConnectionInput(TypedDict, closed=True):
    provider_type: NotRequired[
        "capo_codestar_connections.types.provider_type.ProviderType"
    ]
    """<p>The name of the external provider where your third-party code repository is configured.</p>"""
    connection_name: "capo_codestar_connections.types.connection_name.ConnectionName"
    """<p>The name of the connection to be created.</p>"""
    tags: NotRequired["capo_codestar_connections.types.tag_list.TagList"]
    """<p>The key-value pair to use when tagging the resource.</p>"""
    host_arn: NotRequired["capo_codestar_connections.types.host_arn.HostArn"]
    """<p>The Amazon Resource Name (ARN) of the host associated with the connection to be created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConnectionInput) -> dict:
    out: dict = {}
    if "provider_type" in value:
        import capo_codestar_connections.types.provider_type

        out["ProviderType"] = (
            capo_codestar_connections.types.provider_type.serialize_aws_json_1_0(
                value["provider_type"]
            )
        )
    out["ConnectionName"] = value["connection_name"]
    if "tags" in value:
        import capo_codestar_connections.types.tag_list

        out["Tags"] = capo_codestar_connections.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "host_arn" in value:
        out["HostArn"] = value["host_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateConnectionInput:
    out: CreateConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("ProviderType") is not None:
        import capo_codestar_connections.types.provider_type

        out["provider_type"] = (
            capo_codestar_connections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    else:
        out["connection_name"] = ""
    if data.get("Tags") is not None:
        import capo_codestar_connections.types.tag_list

        out["tags"] = capo_codestar_connections.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("HostArn") is not None:
        out["host_arn"] = data["HostArn"]
    return out
