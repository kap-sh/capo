"""Generated from Smithy shape ``com.amazonaws.kendra#ColumnConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.change_detecting_columns
    import capo_kendra.types.column_name
    import capo_kendra.types.data_source_to_index_field_mapping_list


class ColumnConfiguration(TypedDict, closed=True):
    document_id_column_name: "capo_kendra.types.column_name.ColumnName"
    """<p>The column that provides the document's identifier.</p>"""
    document_data_column_name: "capo_kendra.types.column_name.ColumnName"
    """<p>The column that contains the contents of the document.</p>"""
    document_title_column_name: NotRequired["capo_kendra.types.column_name.ColumnName"]
    """<p>The column that contains the title of the document.</p>"""
    field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>An array of objects that map database column names to the corresponding fields in an index. You must first create the fields in the index using the <code>UpdateIndex</code> API.</p>"""
    change_detecting_columns: (
        "capo_kendra.types.change_detecting_columns.ChangeDetectingColumns"
    )
    """<p>One to five columns that indicate when a document in the database has changed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnConfiguration) -> dict:
    out: dict = {}
    out["DocumentIdColumnName"] = value["document_id_column_name"]
    out["DocumentDataColumnName"] = value["document_data_column_name"]
    if "document_title_column_name" in value:
        out["DocumentTitleColumnName"] = value["document_title_column_name"]
    if "field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["FieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["field_mappings"]
            )
        )
    import capo_kendra.types.change_detecting_columns

    out["ChangeDetectingColumns"] = (
        capo_kendra.types.change_detecting_columns.serialize_aws_json_1_1(
            value["change_detecting_columns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnConfiguration:
    out: ColumnConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DocumentIdColumnName") is not None:
        out["document_id_column_name"] = data["DocumentIdColumnName"]
    else:
        out["document_id_column_name"] = ""
    if data.get("DocumentDataColumnName") is not None:
        out["document_data_column_name"] = data["DocumentDataColumnName"]
    else:
        out["document_data_column_name"] = ""
    if data.get("DocumentTitleColumnName") is not None:
        out["document_title_column_name"] = data["DocumentTitleColumnName"]
    if data.get("FieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["FieldMappings"]
            )
        )
    if data.get("ChangeDetectingColumns") is not None:
        import capo_kendra.types.change_detecting_columns

        out["change_detecting_columns"] = (
            capo_kendra.types.change_detecting_columns.deserialize_aws_json_1_1(
                data["ChangeDetectingColumns"]
            )
        )
    else:
        out["change_detecting_columns"] = []
    return out
