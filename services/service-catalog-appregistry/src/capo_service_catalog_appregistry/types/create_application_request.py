"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.client_token
    import capo_service_catalog_appregistry.types.description
    import capo_service_catalog_appregistry.types.name
    import capo_service_catalog_appregistry.types.tags


class CreateApplicationRequest(TypedDict, closed=True):
    name: "capo_service_catalog_appregistry.types.name.Name"
    """<p>The name of the application. The name must be unique in the region in which you are creating the application.</p>"""
    description: NotRequired[
        "capo_service_catalog_appregistry.types.description.Description"
    ]
    """<p>The description of the application.</p>"""
    tags: NotRequired["capo_service_catalog_appregistry.types.tags.Tags"]
    """<p>Key-value pairs you can use to associate with the application.</p>"""
    client_token: "capo_service_catalog_appregistry.types.client_token.ClientToken"
    """<p>A unique identifier that you provide to ensure idempotency. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. If you retry a successful request using the same client token, but one or more of the parameters are different, the retry fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_service_catalog_appregistry.types.tags

        out["tags"] = capo_service_catalog_appregistry.types.tags.serialize_json(
            value["tags"]
        )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_service_catalog_appregistry.types.tags

        out["tags"] = capo_service_catalog_appregistry.types.tags.deserialize_json(
            data["tags"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    return out
