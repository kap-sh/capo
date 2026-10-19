"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.view_definition
    import capo_cloudwatchomni.types.view_description
    import capo_cloudwatchomni.types.view_name


class UpdateViewRequest(TypedDict, closed=True):
    name: "capo_cloudwatchomni.types.view_name.ViewName"
    """The name of the view to update."""
    definition: NotRequired["capo_cloudwatchomni.types.view_definition.ViewDefinition"]
    """The new SQL query that defines the view. Omit to leave unchanged."""
    description: NotRequired[
        "capo_cloudwatchomni.types.view_description.ViewDescription"
    ]
    """The new description of the view. Omit to leave unchanged."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateViewRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "definition" in value:
        out["definition"] = value["definition"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> UpdateViewRequest:
    out: UpdateViewRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
