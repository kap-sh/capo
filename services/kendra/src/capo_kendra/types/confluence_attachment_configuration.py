"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceAttachmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.confluence_attachment_field_mappings_list


class ConfluenceAttachmentConfiguration(TypedDict, closed=True):
    crawl_attachments: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index attachments of pages and blogs in Confluence.</p>"""
    attachment_field_mappings: NotRequired[
        "capo_kendra.types.confluence_attachment_field_mappings_list.ConfluenceAttachmentFieldMappingsList"
    ]
    """<p>Maps attributes or field names of Confluence attachments to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Confluence fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Confluence data source field names must exist in your Confluence custom metadata.</p> <p>If you specify the <code>AttachentFieldMappings</code> parameter, you must specify at least one field mapping.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluenceAttachmentConfiguration) -> dict:
    out: dict = {}
    out["CrawlAttachments"] = value.get("crawl_attachments", False)
    if "attachment_field_mappings" in value:
        import capo_kendra.types.confluence_attachment_field_mappings_list

        out["AttachmentFieldMappings"] = (
            capo_kendra.types.confluence_attachment_field_mappings_list.serialize_aws_json_1_1(
                value["attachment_field_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfluenceAttachmentConfiguration:
    out: ConfluenceAttachmentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CrawlAttachments") is not None:
        out["crawl_attachments"] = data["CrawlAttachments"]
    else:
        out["crawl_attachments"] = False
    if data.get("AttachmentFieldMappings") is not None:
        import capo_kendra.types.confluence_attachment_field_mappings_list

        out["attachment_field_mappings"] = (
            capo_kendra.types.confluence_attachment_field_mappings_list.deserialize_aws_json_1_1(
                data["AttachmentFieldMappings"]
            )
        )
    return out
