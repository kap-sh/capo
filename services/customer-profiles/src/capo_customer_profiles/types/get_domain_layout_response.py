"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetDomainLayoutResponse``."""

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


class GetDomainLayoutResponse(TypedDict, closed=True):
    layout_definition_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the layout.</p>"""
    description: "capo_customer_profiles.types.sensitive_text.sensitiveText"
    """<p>The description of the layout</p>"""
    display_name: "capo_customer_profiles.types.display_name.displayName"
    """<p>The display name of the layout</p>"""
    is_default: "capo_customer_profiles.types.boolean.boolean"
    """<p>If set to true for a layout, this layout will be used by default to view data. If set to false, then the layout will not be used by default, but it can be used to view data by explicitly selecting it in the console.</p>"""
    layout_type: "capo_customer_profiles.types.layout_type.LayoutType"
    """<p>The type of layout that can be used to view data under a Customer Profiles domain.</p>"""
    layout: "capo_customer_profiles.types.sensitive_string1_to2000000.sensitiveString1To2000000"
    """<p>A customizable layout that can be used to view data under a Customer Profiles domain.</p>"""
    version: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The version used to create layout.</p>"""
    created_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the layout was created.</p>"""
    last_updated_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the layout was most recently updated.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainLayoutResponse) -> dict:
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
    import capo_customer_profiles.types.timestamp

    out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_customer_profiles.types.timestamp

    out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetDomainLayoutResponse:
    out: GetDomainLayoutResponse = {}  # type: ignore[typeddict-item]
    if data.get("LayoutDefinitionName") is not None:
        out["layout_definition_name"] = data["LayoutDefinitionName"]
    else:
        out["layout_definition_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    else:
        out["display_name"] = ""
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
        import typing

        out["layout_type"] = typing.cast(
            "capo_customer_profiles.types.layout_type.LayoutType", ""
        )
    if data.get("Layout") is not None:
        out["layout"] = data["Layout"]
    else:
        out["layout"] = ""
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = ""
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: GetDomainLayoutResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "layout" in value:
        out["layout"] = "*** Sensitive Data Redacted ***"
    return out
