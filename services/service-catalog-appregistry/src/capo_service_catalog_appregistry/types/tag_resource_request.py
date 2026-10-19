"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.arn
    import capo_service_catalog_appregistry.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_service_catalog_appregistry.types.arn.Arn"
    """<p>The Amazon resource name (ARN) that specifies the resource.</p>"""
    tags: "capo_service_catalog_appregistry.types.tags.Tags"
    """<p>The new or modified tags for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_service_catalog_appregistry.types.tags

    out["tags"] = capo_service_catalog_appregistry.types.tags.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_service_catalog_appregistry.types.tags

        out["tags"] = capo_service_catalog_appregistry.types.tags.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
