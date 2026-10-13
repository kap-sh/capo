"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateDomainLayoutResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

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


class CreateDomainLayoutResponse(TypedDict, closed=True):
    layout_definition_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the layout.</p>"""
    description: "capo_customer_profiles.types.sensitive_text.sensitiveText"
    """<p>The description of the layout</p>"""
    display_name: "capo_customer_profiles.types.display_name.displayName"
    """<p>The display name of the layout</p>"""
    is_default: "capo_customer_profiles.types.boolean.boolean"
    """<p>If set to true for a layout, this layout will be used by default to view data. If set to false, then the layout will not be used by default, but it can be used to view data by explicitly selecting it in the console.</p>"""
    layout_type: "capo_customer_profiles.types.layout_type.LayoutType"
    """<p>The type of layout that can be used to view data under customer profiles domain.</p>"""
    layout: "capo_customer_profiles.types.sensitive_string1_to2000000.sensitiveString1To2000000"
    """<p>A customizable layout that can be used to view data under Customer Profiles domain.</p>"""
    version: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The version used to create layout.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    created_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the layout was created.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the layout was most recently updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainLayoutResponse) -> dict:
    out: dict = {}
    out["LayoutDefinitionName"] = value["layout_definition_name"]
    out["Description"] = value["description"]
    out["DisplayName"] = value["display_name"]
    out["IsDefault"] = value.get("is_default", False)
    import capo_customer_profiles.types.layout_type

    out["LayoutType"] = capo_customer_profiles.types.layout_type.serialize_json(
        value["layout_type"]
    )
    out["Layout"] = value["layout"]
    out["Version"] = value["version"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    import capo_customer_profiles.types.timestamp

    out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    if "last_updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> CreateDomainLayoutResponse:
    out: CreateDomainLayoutResponse = {}  # type: ignore[typeddict-item]
    if data.get("LayoutDefinitionName") is not None:
        out["layout_definition_name"] = data["LayoutDefinitionName"]
    else:
        raise DeserializationError(
            "CreateDomainLayoutResponse.layout_definition_name required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CreateDomainLayoutResponse.description required")
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError("CreateDomainLayoutResponse.display_name required")
    if data.get("IsDefault") is not None:
        out["is_default"] = data["IsDefault"]
    else:
        out["is_default"] = False
    if data.get("LayoutType") is not None:
        import capo_customer_profiles.types.layout_type

        out["layout_type"] = capo_customer_profiles.types.layout_type.deserialize_json(
            data["LayoutType"]
        )
    else:
        raise DeserializationError("CreateDomainLayoutResponse.layout_type required")
    if data.get("Layout") is not None:
        out["layout"] = data["Layout"]
    else:
        raise DeserializationError("CreateDomainLayoutResponse.layout required")
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("CreateDomainLayoutResponse.version required")
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("CreateDomainLayoutResponse.created_at required")
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    return out


def redact_sensitive(value: CreateDomainLayoutResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "layout" in value:
        out["layout"] = "*** Sensitive Data Redacted ***"
    return out
