"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceStandardObjectConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.data_source_field_name
    import capo_kendra.types.data_source_to_index_field_mapping_list
    import capo_kendra.types.salesforce_standard_object_name


class SalesforceStandardObjectConfiguration(TypedDict, closed=True):
    name: (
        "capo_kendra.types.salesforce_standard_object_name.SalesforceStandardObjectName"
    )
    """<p>The name of the standard object.</p>"""
    document_data_field_name: (
        "capo_kendra.types.data_source_field_name.DataSourceFieldName"
    )
    """<p>The name of the field in the standard object table that contains the document contents.</p>"""
    document_title_field_name: NotRequired[
        "capo_kendra.types.data_source_field_name.DataSourceFieldName"
    ]
    """<p>The name of the field in the standard object table that contains the document title.</p>"""
    field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>Maps attributes or field names of the standard object to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Salesforce fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Salesforce data source field names must exist in your Salesforce custom metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SalesforceStandardObjectConfiguration) -> dict:
    out: dict = {}
    import capo_kendra.types.salesforce_standard_object_name

    out["Name"] = (
        capo_kendra.types.salesforce_standard_object_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    out["DocumentDataFieldName"] = value["document_data_field_name"]
    if "document_title_field_name" in value:
        out["DocumentTitleFieldName"] = value["document_title_field_name"]
    if "field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["FieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["field_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SalesforceStandardObjectConfiguration:
    out: SalesforceStandardObjectConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_kendra.types.salesforce_standard_object_name

        out["name"] = (
            capo_kendra.types.salesforce_standard_object_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        raise DeserializationError(
            "SalesforceStandardObjectConfiguration.name required"
        )
    if data.get("DocumentDataFieldName") is not None:
        out["document_data_field_name"] = data["DocumentDataFieldName"]
    else:
        raise DeserializationError(
            "SalesforceStandardObjectConfiguration.document_data_field_name required"
        )
    if data.get("DocumentTitleFieldName") is not None:
        out["document_title_field_name"] = data["DocumentTitleFieldName"]
    if data.get("FieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["FieldMappings"]
            )
        )
    return out
