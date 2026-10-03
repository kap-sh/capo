"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceCustomKnowledgeArticleTypeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.data_source_field_name
    import capo_kendra.types.data_source_to_index_field_mapping_list
    import capo_kendra.types.salesforce_custom_knowledge_article_type_name


class SalesforceCustomKnowledgeArticleTypeConfiguration(TypedDict, closed=True):
    name: "capo_kendra.types.salesforce_custom_knowledge_article_type_name.SalesforceCustomKnowledgeArticleTypeName"
    """<p>The name of the configuration.</p>"""
    document_data_field_name: (
        "capo_kendra.types.data_source_field_name.DataSourceFieldName"
    )
    """<p>The name of the field in the custom knowledge article that contains the document data to index.</p>"""
    document_title_field_name: NotRequired[
        "capo_kendra.types.data_source_field_name.DataSourceFieldName"
    ]
    """<p>The name of the field in the custom knowledge article that contains the document title.</p>"""
    field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>Maps attributes or field names of the custom knowledge article to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Salesforce fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Salesforce data source field names must exist in your Salesforce custom metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: SalesforceCustomKnowledgeArticleTypeConfiguration,
) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
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


def deserialize_aws_json_1_1(
    data: dict,
) -> SalesforceCustomKnowledgeArticleTypeConfiguration:
    out: SalesforceCustomKnowledgeArticleTypeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError(
            "SalesforceCustomKnowledgeArticleTypeConfiguration.name required"
        )
    if data.get("DocumentDataFieldName") is not None:
        out["document_data_field_name"] = data["DocumentDataFieldName"]
    else:
        raise DeserializationError(
            "SalesforceCustomKnowledgeArticleTypeConfiguration.document_data_field_name required"
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
