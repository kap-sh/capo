"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.application_name
    import capo_qbusiness.types.description
    import capo_qbusiness.types.document_attribute_configurations
    import capo_qbusiness.types.index_capacity_configuration
    import capo_qbusiness.types.index_id


class UpdateIndexRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application connected to the index.</p>"""
    index_id: "capo_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the Amazon Q Business index.</p>"""
    display_name: NotRequired["capo_qbusiness.types.application_name.ApplicationName"]
    """<p>The name of the Amazon Q Business index.</p>"""
    description: NotRequired["capo_qbusiness.types.description.Description"]
    """<p>The description of the Amazon Q Business index.</p>"""
    capacity_configuration: NotRequired[
        "capo_qbusiness.types.index_capacity_configuration.IndexCapacityConfiguration"
    ]
    """<p>The storage capacity units you want to provision for your Amazon Q Business index. You can add and remove capacity to fit your usage needs.</p>"""
    document_attribute_configurations: NotRequired[
        "capo_qbusiness.types.document_attribute_configurations.DocumentAttributeConfigurations"
    ]
    """<p>Configuration information for document metadata or fields. Document metadata are fields or attributes associated with your documents. For example, the company department name associated with each document. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/business-use-dg/doc-attributes-types.html#doc-attributes">Understanding document attributes</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
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
    return out


def deserialize_json(data: dict) -> UpdateIndexRequest:
    out: UpdateIndexRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
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
    return out
