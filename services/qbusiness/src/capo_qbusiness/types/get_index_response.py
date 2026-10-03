"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.description
    import capo_qbusiness.types.document_attribute_configurations
    import capo_qbusiness.types.error_detail
    import capo_qbusiness.types.index_arn
    import capo_qbusiness.types.index_capacity_configuration
    import capo_qbusiness.types.index_id
    import capo_qbusiness.types.index_name
    import capo_qbusiness.types.index_statistics
    import capo_qbusiness.types.index_status
    import capo_qbusiness.types.index_type
    import capo_qbusiness.types.timestamp


class GetIndexResponse(TypedDict, closed=True):
    application_id: NotRequired["capo_qbusiness.types.application_id.ApplicationId"]
    """<p>The identifier of the Amazon Q Business application associated with the index.</p>"""
    index_id: NotRequired["capo_qbusiness.types.index_id.IndexId"]
    """<p>The identifier of the Amazon Q Business index.</p>"""
    display_name: NotRequired["capo_qbusiness.types.index_name.IndexName"]
    """<p>The name of the Amazon Q Business index.</p>"""
    index_arn: NotRequired["capo_qbusiness.types.index_arn.IndexArn"]
    """<p> The Amazon Resource Name (ARN) of the Amazon Q Business index. </p>"""
    status: NotRequired["capo_qbusiness.types.index_status.IndexStatus"]
    """<p>The current status of the index. When the value is <code>ACTIVE</code>, the index is ready for use. If the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a message that explains why.</p>"""
    type: NotRequired["capo_qbusiness.types.index_type.IndexType"]
    """<p>The type of index attached to your Amazon Q Business application.</p>"""
    description: NotRequired["capo_qbusiness.types.description.Description"]
    """<p>The description for the Amazon Q Business index.</p>"""
    created_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business index was created.</p>"""
    updated_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business index was last updated.</p>"""
    capacity_configuration: NotRequired[
        "capo_qbusiness.types.index_capacity_configuration.IndexCapacityConfiguration"
    ]
    """<p>The storage capacity units chosen for your Amazon Q Business index.</p>"""
    document_attribute_configurations: NotRequired[
        "capo_qbusiness.types.document_attribute_configurations.DocumentAttributeConfigurations"
    ]
    """<p>Configuration information for document attributes or metadata. Document metadata are fields associated with your documents. For example, the company department name associated with each document. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/business-use-dg/doc-attributes-types.html#doc-attributes">Understanding document attributes</a>.</p>"""
    error: NotRequired["capo_qbusiness.types.error_detail.ErrorDetail"]
    """<p>When the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a message that explains why.</p>"""
    index_statistics: NotRequired[
        "capo_qbusiness.types.index_statistics.IndexStatistics"
    ]
    """<p>Provides information about the number of documents indexed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "index_id" in value:
        out["indexId"] = value["index_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    if "status" in value:
        import capo_qbusiness.types.index_status

        out["status"] = capo_qbusiness.types.index_status.serialize_json(
            value["status"]
        )
    if "type" in value:
        import capo_qbusiness.types.index_type

        out["type"] = capo_qbusiness.types.index_type.serialize_json(value["type"])
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_qbusiness.types.timestamp

        out["createdAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_qbusiness.types.timestamp

        out["updatedAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "capacity_configuration" in value:
        import capo_qbusiness.types.index_capacity_configuration

        out["capacityConfiguration"] = (
            capo_qbusiness.types.index_capacity_configuration.serialize_json(
                value["capacity_configuration"]
            )
        )
    if "document_attribute_configurations" in value:
        import capo_qbusiness.types.document_attribute_configurations

        out["documentAttributeConfigurations"] = (
            capo_qbusiness.types.document_attribute_configurations.serialize_json(
                value["document_attribute_configurations"]
            )
        )
    if "error" in value:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.serialize_json(value["error"])
    if "index_statistics" in value:
        import capo_qbusiness.types.index_statistics

        out["indexStatistics"] = capo_qbusiness.types.index_statistics.serialize_json(
            value["index_statistics"]
        )
    return out


def deserialize_json(data: dict) -> GetIndexResponse:
    out: GetIndexResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    if data.get("indexId") is not None:
        out["index_id"] = data["indexId"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("indexArn") is not None:
        out["index_arn"] = data["indexArn"]
    if data.get("status") is not None:
        import capo_qbusiness.types.index_status

        out["status"] = capo_qbusiness.types.index_status.deserialize_json(
            data["status"]
        )
    if data.get("type") is not None:
        import capo_qbusiness.types.index_type

        out["type"] = capo_qbusiness.types.index_type.deserialize_json(data["type"])
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_qbusiness.types.timestamp

        out["created_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_qbusiness.types.timestamp

        out["updated_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("capacityConfiguration") is not None:
        import capo_qbusiness.types.index_capacity_configuration

        out["capacity_configuration"] = (
            capo_qbusiness.types.index_capacity_configuration.deserialize_json(
                data["capacityConfiguration"]
            )
        )
    if data.get("documentAttributeConfigurations") is not None:
        import capo_qbusiness.types.document_attribute_configurations

        out["document_attribute_configurations"] = (
            capo_qbusiness.types.document_attribute_configurations.deserialize_json(
                data["documentAttributeConfigurations"]
            )
        )
    if data.get("error") is not None:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.deserialize_json(data["error"])
    if data.get("indexStatistics") is not None:
        import capo_qbusiness.types.index_statistics

        out["index_statistics"] = (
            capo_qbusiness.types.index_statistics.deserialize_json(
                data["indexStatistics"]
            )
        )
    return out
