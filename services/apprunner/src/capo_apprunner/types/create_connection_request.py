"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.connection_name
    import capo_apprunner.types.provider_type
    import capo_apprunner.types.tag_list


class CreateConnectionRequest(TypedDict, closed=True):
    connection_name: "capo_apprunner.types.connection_name.ConnectionName"
    """<p>A name for the new connection. It must be unique across all App Runner connections for the Amazon Web Services account in the Amazon Web Services Region.</p>"""
    provider_type: "capo_apprunner.types.provider_type.ProviderType"
    """<p>The source repository provider.</p>"""
    tags: NotRequired["capo_apprunner.types.tag_list.TagList"]
    """<p>A list of metadata items that you can associate with your connection resource. A tag is a key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConnectionRequest) -> dict:
    out: dict = {}
    out["ConnectionName"] = value["connection_name"]
    import capo_apprunner.types.provider_type

    out["ProviderType"] = capo_apprunner.types.provider_type.serialize_aws_json_1_0(
        value["provider_type"]
    )
    if "tags" in value:
        import capo_apprunner.types.tag_list

        out["Tags"] = capo_apprunner.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateConnectionRequest:
    out: CreateConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    else:
        out["connection_name"] = ""
    if data.get("ProviderType") is not None:
        import capo_apprunner.types.provider_type

        out["provider_type"] = (
            capo_apprunner.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    else:
        import typing

        out["provider_type"] = typing.cast(
            "capo_apprunner.types.provider_type.ProviderType", ""
        )
    if data.get("Tags") is not None:
        import capo_apprunner.types.tag_list

        out["tags"] = capo_apprunner.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
