"""Generated from Smithy shape ``com.amazonaws.oam#UpdateLinkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_oam.types.include_tags
    import capo_oam.types.link_configuration
    import capo_oam.types.resource_identifier
    import capo_oam.types.resource_types_input


class UpdateLinkInput(TypedDict, closed=True):
    identifier: "capo_oam.types.resource_identifier.ResourceIdentifier"
    """<p>The ARN of the link that you want to update.</p>"""
    resource_types: "capo_oam.types.resource_types_input.ResourceTypesInput"
    """<p>An array of strings that define which types of data that the source account will send to the monitoring account.</p> <p>Your input here replaces the current set of data types that are shared.</p>"""
    link_configuration: NotRequired[
        "capo_oam.types.link_configuration.LinkConfiguration"
    ]
    """<p>Use this structure to filter which metric namespaces and which log groups are to be shared from the source account to the monitoring account.</p>"""
    include_tags: NotRequired["capo_oam.types.include_tags.IncludeTags"]
    """<p>Specifies whether to include the tags associated with the link in the response after the update operation. When <code>IncludeTags</code> is set to <code>true</code> and the caller has the required permission, <code>oam:ListTagsForResource</code>, the API will return the tags for the specified resource. If the caller doesn't have the required permission, <code>oam:ListTagsForResource</code>, the API will raise an exception. </p> <p>The default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkInput) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    import capo_oam.types.resource_types_input

    out["ResourceTypes"] = capo_oam.types.resource_types_input.serialize_json(
        value["resource_types"]
    )
    if "link_configuration" in value:
        import capo_oam.types.link_configuration

        out["LinkConfiguration"] = capo_oam.types.link_configuration.serialize_json(
            value["link_configuration"]
        )
    if "include_tags" in value:
        out["IncludeTags"] = value["include_tags"]
    return out


def deserialize_json(data: dict) -> UpdateLinkInput:
    out: UpdateLinkInput = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("ResourceTypes") is not None:
        import capo_oam.types.resource_types_input

        out["resource_types"] = capo_oam.types.resource_types_input.deserialize_json(
            data["ResourceTypes"]
        )
    else:
        out["resource_types"] = []
    if data.get("LinkConfiguration") is not None:
        import capo_oam.types.link_configuration

        out["link_configuration"] = capo_oam.types.link_configuration.deserialize_json(
            data["LinkConfiguration"]
        )
    if data.get("IncludeTags") is not None:
        out["include_tags"] = data["IncludeTags"]
    return out
