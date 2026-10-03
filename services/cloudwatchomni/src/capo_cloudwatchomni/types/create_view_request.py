"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.tag_map
    import capo_cloudwatchomni.types.view_definition
    import capo_cloudwatchomni.types.view_description
    import capo_cloudwatchomni.types.view_name


class CreateViewRequest(TypedDict, closed=True):
    name: "capo_cloudwatchomni.types.view_name.ViewName"
    """The name of the view. Must begin with the "view." prefix. View names must be unique within the account and region."""
    definition: "capo_cloudwatchomni.types.view_definition.ViewDefinition"
    """The SQL query that defines the view."""
    description: NotRequired[
        "capo_cloudwatchomni.types.view_description.ViewDescription"
    ]
    """A description of the view."""
    tags: NotRequired["capo_cloudwatchomni.types.tag_map.TagMap"]
    """Resource tags."""
    client_token: NotRequired["str"]
    """Idempotency token for safe retries. Retrying with the same token returns the original view instead of creating a duplicate."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateViewRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["definition"] = value["definition"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.serialize_cbor(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> CreateViewRequest:
    out: CreateViewRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateViewRequest.name required")
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("CreateViewRequest.definition required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.deserialize_cbor(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
