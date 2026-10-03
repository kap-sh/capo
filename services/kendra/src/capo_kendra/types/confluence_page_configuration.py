"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluencePageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.confluence_page_field_mappings_list


class ConfluencePageConfiguration(TypedDict, closed=True):
    page_field_mappings: NotRequired[
        "capo_kendra.types.confluence_page_field_mappings_list.ConfluencePageFieldMappingsList"
    ]
    """<p>Maps attributes or field names of Confluence pages to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Confluence fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Confluence data source field names must exist in your Confluence custom metadata.</p> <p>If you specify the <code>PageFieldMappings</code> parameter, you must specify at least one field mapping.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluencePageConfiguration) -> dict:
    out: dict = {}
    if "page_field_mappings" in value:
        import capo_kendra.types.confluence_page_field_mappings_list

        out["PageFieldMappings"] = (
            capo_kendra.types.confluence_page_field_mappings_list.serialize_aws_json_1_1(
                value["page_field_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfluencePageConfiguration:
    out: ConfluencePageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("PageFieldMappings") is not None:
        import capo_kendra.types.confluence_page_field_mappings_list

        out["page_field_mappings"] = (
            capo_kendra.types.confluence_page_field_mappings_list.deserialize_aws_json_1_1(
                data["PageFieldMappings"]
            )
        )
    return out
