"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CatalogItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.attributes
    import capo_customer_profiles.types.sensitive_string1_to255
    import capo_customer_profiles.types.sensitive_string1_to1000
    import capo_customer_profiles.types.timestamp


class CatalogItem(TypedDict, closed=True):
    id: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The unique identifier for the catalog item.</p>"""
    name: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The display name of the catalog item.</p>"""
    code: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The product code or SKU of the catalog item.</p>"""
    type: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The type classification of the catalog item.</p>"""
    category: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The category to which the catalog item belongs.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>A detailed description of the catalog item.</p>"""
    additional_information: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to1000.sensitiveString1To1000"
    ]
    """<p>Supplementary information about the catalog item beyond the basic description.</p>"""
    image_link: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to1000.sensitiveString1To1000"
    ]
    """<p>The URL link to the item's image.</p>"""
    link: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to1000.sensitiveString1To1000"
    ]
    """<p>The URL link to the item's detailed page or external resource.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the catalog item was created.</p>"""
    updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when the catalog item was last updated.</p>"""
    price: NotRequired[
        "capo_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The price of the catalog item.</p>"""
    attributes: NotRequired["capo_customer_profiles.types.attributes.Attributes"]
    """<p>Additional attributes or properties associated with the catalog item stored as key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CatalogItem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "code" in value:
        out["Code"] = value["code"]
    if "type" in value:
        out["Type"] = value["type"]
    if "category" in value:
        out["Category"] = value["category"]
    if "description" in value:
        out["Description"] = value["description"]
    if "additional_information" in value:
        out["AdditionalInformation"] = value["additional_information"]
    if "image_link" in value:
        out["ImageLink"] = value["image_link"]
    if "link" in value:
        out["Link"] = value["link"]
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["UpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "price" in value:
        out["Price"] = value["price"]
    if "attributes" in value:
        import capo_customer_profiles.types.attributes

        out["Attributes"] = capo_customer_profiles.types.attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> CatalogItem:
    out: CatalogItem = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AdditionalInformation") is not None:
        out["additional_information"] = data["AdditionalInformation"]
    if data.get("ImageLink") is not None:
        out["image_link"] = data["ImageLink"]
    if data.get("Link") is not None:
        out["link"] = data["Link"]
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["updated_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if data.get("Price") is not None:
        out["price"] = data["Price"]
    if data.get("Attributes") is not None:
        import capo_customer_profiles.types.attributes

        out["attributes"] = capo_customer_profiles.types.attributes.deserialize_json(
            data["Attributes"]
        )
    return out


def redact_sensitive(value: CatalogItem) -> dict[str, Any]:
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
    if "price" in value:
        out["price"] = "*** Sensitive Data Redacted ***"
    if "attributes" in value:
        out["attributes"] = "*** Sensitive Data Redacted ***"
    return out
