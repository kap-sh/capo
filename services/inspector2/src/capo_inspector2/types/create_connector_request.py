"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.connector_cloud_provider
    import capo_inspector2.types.connector_description
    import capo_inspector2.types.connector_name
    import capo_inspector2.types.connector_tag_map
    import capo_inspector2.types.provider_detail_create


class CreateConnectorRequest(TypedDict, closed=True):
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>"""
    name: "capo_inspector2.types.connector_name.ConnectorName"
    """<p>The name of the connector.</p>"""
    provider: "capo_inspector2.types.connector_cloud_provider.ConnectorCloudProvider"
    """<p>The cloud provider for the connector.</p>"""
    description: NotRequired[
        "capo_inspector2.types.connector_description.ConnectorDescription"
    ]
    """<p>A description of the connector.</p>"""
    provider_detail: "capo_inspector2.types.provider_detail_create.ProviderDetailCreate"
    """<p>The provider-specific configuration details for the connector.</p>"""
    tags: NotRequired["capo_inspector2.types.connector_tag_map.ConnectorTagMap"]
    """<p>The tags to apply to the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    import capo_inspector2.types.connector_cloud_provider

    out["provider"] = capo_inspector2.types.connector_cloud_provider.serialize_json(
        value["provider"]
    )
    if "description" in value:
        out["description"] = value["description"]
    import capo_inspector2.types.provider_detail_create

    out["providerDetail"] = capo_inspector2.types.provider_detail_create.serialize_json(
        value["provider_detail"]
    )
    if "tags" in value:
        import capo_inspector2.types.connector_tag_map

        out["tags"] = capo_inspector2.types.connector_tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateConnectorRequest:
    out: CreateConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("provider") is not None:
        import capo_inspector2.types.connector_cloud_provider

        out["provider"] = (
            capo_inspector2.types.connector_cloud_provider.deserialize_json(
                data["provider"]
            )
        )
    else:
        import typing

        out["provider"] = typing.cast(
            "capo_inspector2.types.connector_cloud_provider.ConnectorCloudProvider", ""
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("providerDetail") is not None:
        import capo_inspector2.types.provider_detail_create

        out["provider_detail"] = (
            capo_inspector2.types.provider_detail_create.deserialize_json(
                data["providerDetail"]
            )
        )
    else:
        out["provider_detail"] = {"$unknown": {"name": ""}}
    if data.get("tags") is not None:
        import capo_inspector2.types.connector_tag_map

        out["tags"] = capo_inspector2.types.connector_tag_map.deserialize_json(
            data["tags"]
        )
    return out
