"""Generated from Smithy shape ``com.amazonaws.qconnect#ProfileCatalogItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_attribute_value
    import capo_qconnect.types.profile_catalog_item_attributes


class ProfileCatalogItem(TypedDict, closed=True):
    id: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The unique identifier of the catalog item.</p>"""
    name: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The name of the catalog item.</p>"""
    code: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The code of the catalog item.</p>"""
    type: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The type of the catalog item.</p>"""
    category: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The category of the catalog item.</p>"""
    description: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The description of the catalog item.</p>"""
    additional_information: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>Additional information about the catalog item.</p>"""
    image_link: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The URL of the image of the catalog item.</p>"""
    link: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The URL of the catalog item.</p>"""
    created_at: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The timestamp when the catalog item was created.</p>"""
    updated_at: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The timestamp when the catalog item was last updated.</p>"""
    price: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The price of the catalog item.</p>"""
    attributes: NotRequired[
        "capo_qconnect.types.profile_catalog_item_attributes.ProfileCatalogItemAttributes"
    ]
    """<p>The custom attributes of the catalog item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileCatalogItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "code" in value:
        out["code"] = value["code"]
    if "type" in value:
        out["type"] = value["type"]
    if "category" in value:
        out["category"] = value["category"]
    if "description" in value:
        out["description"] = value["description"]
    if "additional_information" in value:
        out["additionalInformation"] = value["additional_information"]
    if "image_link" in value:
        out["imageLink"] = value["image_link"]
    if "link" in value:
        out["link"] = value["link"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "updated_at" in value:
        out["updatedAt"] = value["updated_at"]
    if "price" in value:
        out["price"] = value["price"]
    if "attributes" in value:
        import capo_qconnect.types.profile_catalog_item_attributes

        out["attributes"] = (
            capo_qconnect.types.profile_catalog_item_attributes.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProfileCatalogItem:
    out: ProfileCatalogItem = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("category") is not None:
        out["category"] = data["category"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("additionalInformation") is not None:
        out["additional_information"] = data["additionalInformation"]
    if data.get("imageLink") is not None:
        out["image_link"] = data["imageLink"]
    if data.get("link") is not None:
        out["link"] = data["link"]
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    if data.get("updatedAt") is not None:
        out["updated_at"] = data["updatedAt"]
    if data.get("price") is not None:
        out["price"] = data["price"]
    if data.get("attributes") is not None:
        import capo_qconnect.types.profile_catalog_item_attributes

        out["attributes"] = (
            capo_qconnect.types.profile_catalog_item_attributes.deserialize_json(
                data["attributes"]
            )
        )
    return out


def redact_sensitive(value: ProfileCatalogItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "id" in value:
        out["id"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "code" in value:
        out["code"] = "*** Sensitive Data Redacted ***"
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    if "category" in value:
        out["category"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "additional_information" in value:
        out["additional_information"] = "*** Sensitive Data Redacted ***"
    if "image_link" in value:
        out["image_link"] = "*** Sensitive Data Redacted ***"
    if "link" in value:
        out["link"] = "*** Sensitive Data Redacted ***"
    if "created_at" in value:
        out["created_at"] = "*** Sensitive Data Redacted ***"
    if "updated_at" in value:
        out["updated_at"] = "*** Sensitive Data Redacted ***"
    if "price" in value:
        out["price"] = "*** Sensitive Data Redacted ***"
    if "attributes" in value:
        import capo_qconnect.types.profile_catalog_item_attributes

        out["attributes"] = (
            capo_qconnect.types.profile_catalog_item_attributes.redact_sensitive(
                value["attributes"]
            )
        )
    return out
