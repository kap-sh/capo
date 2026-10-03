"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ChangeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.change_name
    import capo_marketplace_catalog.types.change_type
    import capo_marketplace_catalog.types.entity
    import capo_marketplace_catalog.types.error_detail_list
    import capo_marketplace_catalog.types.json
    import capo_marketplace_catalog.types.json_document_type


class ChangeSummary(TypedDict, closed=True):
    change_type: NotRequired["capo_marketplace_catalog.types.change_type.ChangeType"]
    """<p>The type of the change.</p>"""
    entity: NotRequired["capo_marketplace_catalog.types.entity.Entity"]
    """<p>The entity to be changed.</p>"""
    details: NotRequired["capo_marketplace_catalog.types.json.Json"]
    """<p>This object contains details specific to the change type of the requested change.</p>"""
    details_document: NotRequired[
        "capo_marketplace_catalog.types.json_document_type.JsonDocumentType"
    ]
    """<p>The JSON value of the details specific to the change type of the requested change.</p> <p>To download the "DetailsDocument" shapes, see the <a href="https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-python">Python</a> and <a href="https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-java/tree/main">Java</a> shapes on GitHub.</p>"""
    error_detail_list: NotRequired[
        "capo_marketplace_catalog.types.error_detail_list.ErrorDetailList"
    ]
    """<p>An array of <code>ErrorDetail</code> objects associated with the change.</p>"""
    change_name: NotRequired["capo_marketplace_catalog.types.change_name.ChangeName"]
    """<p>Optional name for the change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeSummary) -> dict:
    out: dict = {}
    if "change_type" in value:
        out["ChangeType"] = value["change_type"]
    if "entity" in value:
        import capo_marketplace_catalog.types.entity

        out["Entity"] = capo_marketplace_catalog.types.entity.serialize_json(
            value["entity"]
        )
    if "details" in value:
        out["Details"] = value["details"]
    if "details_document" in value:
        out["DetailsDocument"] = value["details_document"]
    if "error_detail_list" in value:
        import capo_marketplace_catalog.types.error_detail_list

        out["ErrorDetailList"] = (
            capo_marketplace_catalog.types.error_detail_list.serialize_json(
                value["error_detail_list"]
            )
        )
    if "change_name" in value:
        out["ChangeName"] = value["change_name"]
    return out


def deserialize_json(data: dict) -> ChangeSummary:
    out: ChangeSummary = {}  # type: ignore[typeddict-item]
    if data.get("ChangeType") is not None:
        out["change_type"] = data["ChangeType"]
    if data.get("Entity") is not None:
        import capo_marketplace_catalog.types.entity

        out["entity"] = capo_marketplace_catalog.types.entity.deserialize_json(
            data["Entity"]
        )
    if data.get("Details") is not None:
        out["details"] = data["Details"]
    if data.get("DetailsDocument") is not None:
        out["details_document"] = data["DetailsDocument"]
    if data.get("ErrorDetailList") is not None:
        import capo_marketplace_catalog.types.error_detail_list

        out["error_detail_list"] = (
            capo_marketplace_catalog.types.error_detail_list.deserialize_json(
                data["ErrorDetailList"]
            )
        )
    if data.get("ChangeName") is not None:
        out["change_name"] = data["ChangeName"]
    return out
