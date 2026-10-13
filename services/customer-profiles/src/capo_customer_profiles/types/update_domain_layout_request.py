"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateDomainLayoutRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.boolean
    import capo_customer_profiles.types.display_name
    import capo_customer_profiles.types.layout_type
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.sensitive_string1_to2000000
    import capo_customer_profiles.types.sensitive_text


class UpdateDomainLayoutRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    layout_definition_name: "capo_customer_profiles.types.name.name"
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


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainLayoutRequest) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> UpdateDomainLayoutRequest:
    out: UpdateDomainLayoutRequest = {}  # type: ignore[typeddict-item]
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
    return out


def redact_sensitive(value: UpdateDomainLayoutRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "layout" in value:
        out["layout"] = "*** Sensitive Data Redacted ***"
    return out
