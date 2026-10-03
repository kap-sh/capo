"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceBlogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.confluence_blog_field_mappings_list


class ConfluenceBlogConfiguration(TypedDict, closed=True):
    blog_field_mappings: NotRequired[
        "capo_kendra.types.confluence_blog_field_mappings_list.ConfluenceBlogFieldMappingsList"
    ]
    """<p>Maps attributes or field names of Confluence blogs to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Confluence fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Confluence data source field names must exist in your Confluence custom metadata.</p> <p>If you specify the <code>BlogFieldMappings</code> parameter, you must specify at least one field mapping.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluenceBlogConfiguration) -> dict:
    out: dict = {}
    if "blog_field_mappings" in value:
        import capo_kendra.types.confluence_blog_field_mappings_list

        out["BlogFieldMappings"] = (
            capo_kendra.types.confluence_blog_field_mappings_list.serialize_aws_json_1_1(
                value["blog_field_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfluenceBlogConfiguration:
    out: ConfluenceBlogConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("BlogFieldMappings") is not None:
        import capo_kendra.types.confluence_blog_field_mappings_list

        out["blog_field_mappings"] = (
            capo_kendra.types.confluence_blog_field_mappings_list.deserialize_aws_json_1_1(
                data["BlogFieldMappings"]
            )
        )
    return out
