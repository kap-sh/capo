"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#Change``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.change_name
    import capo_marketplace_catalog.types.change_type
    import capo_marketplace_catalog.types.entity
    import capo_marketplace_catalog.types.json
    import capo_marketplace_catalog.types.json_document_type
    import capo_marketplace_catalog.types.tag_list


class Change(TypedDict, closed=True):
    change_type: "capo_marketplace_catalog.types.change_type.ChangeType"
    """<p>Change types are single string values that describe your intention for the change. Each change type is unique for each <code>EntityType</code> provided in the change's scope. For more information about change types available for single-AMI products, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#working-with-single-AMI-products">Working with single-AMI products</a>. Also, for more information about change types available for container-based products, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#working-with-container-products">Working with container products</a>.</p>"""
    entity: "capo_marketplace_catalog.types.entity.Entity"
    """<p>The entity to be changed.</p>"""
    entity_tags: NotRequired["capo_marketplace_catalog.types.tag_list.TagList"]
    """<p>The tags associated with the change.</p>"""
    details: NotRequired["capo_marketplace_catalog.types.json.Json"]
    """<p>This object contains details specific to the change type of the requested change. For more information about change types available for single-AMI products, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#working-with-single-AMI-products">Working with single-AMI products</a>. Also, for more information about change types available for container-based products, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#working-with-container-products">Working with container products</a>.</p>"""
    details_document: NotRequired[
        "capo_marketplace_catalog.types.json_document_type.JsonDocumentType"
    ]
    """<p>Alternative field that accepts a JSON value instead of a string for <code>ChangeType</code> details. You can use either <code>Details</code> or <code>DetailsDocument</code>, but not both.</p> <p>To download the "DetailsDocument" shapes, see the <a href="https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-python">Python</a> and <a href="https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-java/tree/main">Java</a> shapes on GitHub.</p>"""
    change_name: NotRequired["capo_marketplace_catalog.types.change_name.ChangeName"]
    """<p>Optional name for the change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Change) -> dict:
    out: dict = {}
    out["ChangeType"] = value["change_type"]
    import capo_marketplace_catalog.types.entity

    out["Entity"] = capo_marketplace_catalog.types.entity.serialize_json(
        value["entity"]
    )
    if "entity_tags" in value:
        import capo_marketplace_catalog.types.tag_list

        out["EntityTags"] = capo_marketplace_catalog.types.tag_list.serialize_json(
            value["entity_tags"]
        )
    if "details" in value:
        out["Details"] = value["details"]
    if "details_document" in value:
        out["DetailsDocument"] = value["details_document"]
    if "change_name" in value:
        out["ChangeName"] = value["change_name"]
    return out


def deserialize_json(data: dict) -> Change:
    out: Change = {}  # type: ignore[typeddict-item]
    if data.get("ChangeType") is not None:
        out["change_type"] = data["ChangeType"]
    else:
        raise DeserializationError("Change.change_type required")
    if data.get("Entity") is not None:
        import capo_marketplace_catalog.types.entity

        out["entity"] = capo_marketplace_catalog.types.entity.deserialize_json(
            data["Entity"]
        )
    else:
        raise DeserializationError("Change.entity required")
    if data.get("EntityTags") is not None:
        import capo_marketplace_catalog.types.tag_list

        out["entity_tags"] = capo_marketplace_catalog.types.tag_list.deserialize_json(
            data["EntityTags"]
        )
    if data.get("Details") is not None:
        out["details"] = data["Details"]
    if data.get("DetailsDocument") is not None:
        out["details_document"] = data["DetailsDocument"]
    if data.get("ChangeName") is not None:
        out["change_name"] = data["ChangeName"]
    return out
