"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DescribeEntityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.arn
    import capo_marketplace_catalog.types.date_time_iso8601
    import capo_marketplace_catalog.types.entity_type
    import capo_marketplace_catalog.types.identifier
    import capo_marketplace_catalog.types.json
    import capo_marketplace_catalog.types.json_document_type


class DescribeEntityResponse(TypedDict, closed=True):
    entity_type: NotRequired["capo_marketplace_catalog.types.entity_type.EntityType"]
    """<p>The named type of the entity, in the format of <code>EntityType@Version</code>.</p>"""
    entity_identifier: NotRequired[
        "capo_marketplace_catalog.types.identifier.Identifier"
    ]
    """<p>The identifier of the entity, in the format of <code>EntityId@RevisionId</code>.</p>"""
    entity_arn: NotRequired["capo_marketplace_catalog.types.arn.ARN"]
    """<p>The ARN associated to the unique identifier for the entity referenced in this request.</p>"""
    last_modified_date: NotRequired[
        "capo_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The last modified date of the entity, in ISO 8601 format (2018-02-27T13:45:22Z).</p>"""
    details: NotRequired["capo_marketplace_catalog.types.json.Json"]
    """<p>This stringified JSON object includes the details of the entity.</p>"""
    details_document: NotRequired[
        "capo_marketplace_catalog.types.json_document_type.JsonDocumentType"
    ]
    """<p>The JSON value of the details specific to the entity.</p> <p>To download "DetailsDocument" shapes, see the <a href="https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-python">Python</a> and <a href="https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-java/tree/main">Java</a> shapes on GitHub.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEntityResponse) -> dict:
    out: dict = {}
    if "entity_type" in value:
        out["EntityType"] = value["entity_type"]
    if "entity_identifier" in value:
        out["EntityIdentifier"] = value["entity_identifier"]
    if "entity_arn" in value:
        out["EntityArn"] = value["entity_arn"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "details" in value:
        out["Details"] = value["details"]
    if "details_document" in value:
        out["DetailsDocument"] = value["details_document"]
    return out


def deserialize_json(data: dict) -> DescribeEntityResponse:
    out: DescribeEntityResponse = {}  # type: ignore[typeddict-item]
    if data.get("EntityType") is not None:
        out["entity_type"] = data["EntityType"]
    if data.get("EntityIdentifier") is not None:
        out["entity_identifier"] = data["EntityIdentifier"]
    if data.get("EntityArn") is not None:
        out["entity_arn"] = data["EntityArn"]
    if data.get("LastModifiedDate") is not None:
        out["last_modified_date"] = data["LastModifiedDate"]
    if data.get("Details") is not None:
        out["details"] = data["Details"]
    if data.get("DetailsDocument") is not None:
        out["details_document"] = data["DetailsDocument"]
    return out
