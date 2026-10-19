"""Generated from Smithy shape ``com.amazonaws.oam#GetSinkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_oam.types.include_tags
    import capo_oam.types.resource_identifier


class GetSinkInput(TypedDict, closed=True):
    identifier: "capo_oam.types.resource_identifier.ResourceIdentifier"
    """<p>The ARN of the sink to retrieve information for.</p>"""
    include_tags: NotRequired["capo_oam.types.include_tags.IncludeTags"]
    """<p>Specifies whether to include the tags associated with the sink in the response. When <code>IncludeTags</code> is set to <code>true</code> and the caller has the required permission, <code>oam:ListTagsForResource</code>, the API will return the tags for the specified resource. If the caller doesn't have the required permission, <code>oam:ListTagsForResource</code>, the API will raise an exception.</p> <p>The default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSinkInput) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    if "include_tags" in value:
        out["IncludeTags"] = value["include_tags"]
    return out


def deserialize_json(data: dict) -> GetSinkInput:
    out: GetSinkInput = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("IncludeTags") is not None:
        out["include_tags"] = data["IncludeTags"]
    return out
