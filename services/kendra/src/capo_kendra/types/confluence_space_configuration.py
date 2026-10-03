"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceSpaceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.confluence_space_field_mappings_list
    import capo_kendra.types.confluence_space_list


class ConfluenceSpaceConfiguration(TypedDict, closed=True):
    crawl_personal_spaces: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index personal spaces. You can add restrictions to items in personal spaces. If personal spaces are indexed, queries without user context information may return restricted items from a personal space in their results. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html">Filtering on user context</a>.</p>"""
    crawl_archived_spaces: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index archived spaces.</p>"""
    include_spaces: NotRequired[
        "capo_kendra.types.confluence_space_list.ConfluenceSpaceList"
    ]
    """<p>A list of space keys for Confluence spaces. If you include a key, the blogs, documents, and attachments in the space are indexed. Spaces that aren't in the list aren't indexed. A space in the list must exist. Otherwise, Amazon Kendra logs an error when the data source is synchronized. If a space is in both the <code>IncludeSpaces</code> and the <code>ExcludeSpaces</code> list, the space is excluded.</p>"""
    exclude_spaces: NotRequired[
        "capo_kendra.types.confluence_space_list.ConfluenceSpaceList"
    ]
    """<p>A list of space keys of Confluence spaces. If you include a key, the blogs, documents, and attachments in the space are not indexed. If a space is in both the <code>ExcludeSpaces</code> and the <code>IncludeSpaces</code> list, the space is excluded.</p>"""
    space_field_mappings: NotRequired[
        "capo_kendra.types.confluence_space_field_mappings_list.ConfluenceSpaceFieldMappingsList"
    ]
    """<p>Maps attributes or field names of Confluence spaces to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Confluence fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Confluence data source field names must exist in your Confluence custom metadata.</p> <p>If you specify the <code>SpaceFieldMappings</code> parameter, you must specify at least one field mapping.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluenceSpaceConfiguration) -> dict:
    out: dict = {}
    out["CrawlPersonalSpaces"] = value.get("crawl_personal_spaces", False)
    out["CrawlArchivedSpaces"] = value.get("crawl_archived_spaces", False)
    if "include_spaces" in value:
        import capo_kendra.types.confluence_space_list

        out["IncludeSpaces"] = (
            capo_kendra.types.confluence_space_list.serialize_aws_json_1_1(
                value["include_spaces"]
            )
        )
    if "exclude_spaces" in value:
        import capo_kendra.types.confluence_space_list

        out["ExcludeSpaces"] = (
            capo_kendra.types.confluence_space_list.serialize_aws_json_1_1(
                value["exclude_spaces"]
            )
        )
    if "space_field_mappings" in value:
        import capo_kendra.types.confluence_space_field_mappings_list

        out["SpaceFieldMappings"] = (
            capo_kendra.types.confluence_space_field_mappings_list.serialize_aws_json_1_1(
                value["space_field_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfluenceSpaceConfiguration:
    out: ConfluenceSpaceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CrawlPersonalSpaces") is not None:
        out["crawl_personal_spaces"] = data["CrawlPersonalSpaces"]
    else:
        out["crawl_personal_spaces"] = False
    if data.get("CrawlArchivedSpaces") is not None:
        out["crawl_archived_spaces"] = data["CrawlArchivedSpaces"]
    else:
        out["crawl_archived_spaces"] = False
    if data.get("IncludeSpaces") is not None:
        import capo_kendra.types.confluence_space_list

        out["include_spaces"] = (
            capo_kendra.types.confluence_space_list.deserialize_aws_json_1_1(
                data["IncludeSpaces"]
            )
        )
    if data.get("ExcludeSpaces") is not None:
        import capo_kendra.types.confluence_space_list

        out["exclude_spaces"] = (
            capo_kendra.types.confluence_space_list.deserialize_aws_json_1_1(
                data["ExcludeSpaces"]
            )
        )
    if data.get("SpaceFieldMappings") is not None:
        import capo_kendra.types.confluence_space_field_mappings_list

        out["space_field_mappings"] = (
            capo_kendra.types.confluence_space_field_mappings_list.deserialize_aws_json_1_1(
                data["SpaceFieldMappings"]
            )
        )
    return out
