"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateDomainLayoutResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.boolean
    import capo_customer_profiles.types.display_name
    import capo_customer_profiles.types.layout_type
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.sensitive_string1_to2000000
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp


class UpdateDomainLayoutResponse(TypedDict, closed=True):
    layout_definition_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The unique name of the layout.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the layout</p>"""
    display_name: NotRequired["capo_customer_profiles.types.display_name.displayName"]
    """<p>The display name of the layout</p>"""
    is_default: "capo_customer_profiles.types.boolean.boolean"
    """<p>If set to true for a layout, this layout will be used by default to view data. If set to false, then the layout will not be used by default, but it can be used to view data by explicitly selecting it in the console.</p>"""
    layout_type: NotRequired["capo_customer_profiles.types.layout_type.LayoutType"]
    """<p>The type of layout that can be used to view data under a Customer Profiles domain.</p>"""
    layout: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to2000000.sensitiveString1To2000000"
    ]
    """<p>A customizable layout that can be used to view data under a Customer Profiles domain.</p>"""
    version: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The version used to create layout.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the layout was created.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the layout was most recently updated.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainLayoutResponse) -> dict:
    out: dict = {}
    if "layout_definition_name" in value:
        out["LayoutDefinitionName"] = value["layout_definition_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    out["IsDefault"] = value.get("is_default", False)
    if "layout_type" in value:
        import capo_customer_profiles.types.layout_type

        out["LayoutType"] = capo_customer_profiles.types.layout_type.serialize_json(
            value["layout_type"]
        )
    if "layout" in value:
        out["Layout"] = value["layout"]
    if "version" in value:
        out["Version"] = value["version"]
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateDomainLayoutResponse:
    out: UpdateDomainLayoutResponse = {}  # type: ignore[typeddict-item]
    if data.get("LayoutDefinitionName") is not None:
        out["layout_definition_name"] = data["LayoutDefinitionName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("IsDefault") is not None:
        out["is_default"] = data["IsDefault"]
    else:
        out["is_default"] = False
    if data.get("LayoutType") is not None:
        import capo_customer_profiles.types.layout_type

        out["layout_type"] = capo_customer_profiles.types.layout_type.deserialize_json(
            data["LayoutType"]
        )
    if data.get("Layout") is not None:
        out["layout"] = data["Layout"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: UpdateDomainLayoutResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "layout" in value:
        out["layout"] = "*** Sensitive Data Redacted ***"
    return out
