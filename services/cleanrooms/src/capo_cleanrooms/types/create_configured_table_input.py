"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateConfiguredTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.allowed_column_list
    import capo_cleanrooms.types.analysis_method
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.selected_analysis_methods
    import capo_cleanrooms.types.table_description
    import capo_cleanrooms.types.table_reference
    import capo_cleanrooms.types.tag_map


class CreateConfiguredTableInput(TypedDict, closed=True):
    name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The name of the configured table.</p>"""
    description: NotRequired["capo_cleanrooms.types.table_description.TableDescription"]
    """<p>A description for the configured table.</p>"""
    table_reference: "capo_cleanrooms.types.table_reference.TableReference"
    """<p>A reference to the table being configured.</p>"""
    allowed_columns: "capo_cleanrooms.types.allowed_column_list.AllowedColumnList"
    """<p>The columns of the underlying table that can be used by collaborations or analysis rules.</p>"""
    analysis_method: "capo_cleanrooms.types.analysis_method.AnalysisMethod"
    """<p>The analysis method allowed for the configured tables.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>"""
    selected_analysis_methods: NotRequired[
        "capo_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
    ]
    """<p> The analysis methods to enable for the configured table. When configured, you must specify at least two analysis methods.</p>"""
    tags: NotRequired["capo_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredTableInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cleanrooms.types.table_reference

    out["tableReference"] = capo_cleanrooms.types.table_reference.serialize_json(
        value["table_reference"]
    )
    import capo_cleanrooms.types.allowed_column_list

    out["allowedColumns"] = capo_cleanrooms.types.allowed_column_list.serialize_json(
        value["allowed_columns"]
    )
    import capo_cleanrooms.types.analysis_method

    out["analysisMethod"] = capo_cleanrooms.types.analysis_method.serialize_json(
        value["analysis_method"]
    )
    if "selected_analysis_methods" in value:
        import capo_cleanrooms.types.selected_analysis_methods

        out["selectedAnalysisMethods"] = (
            capo_cleanrooms.types.selected_analysis_methods.serialize_json(
                value["selected_analysis_methods"]
            )
        )
    if "tags" in value:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConfiguredTableInput:
    out: CreateConfiguredTableInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tableReference") is not None:
        import capo_cleanrooms.types.table_reference

        out["table_reference"] = capo_cleanrooms.types.table_reference.deserialize_json(
            data["tableReference"]
        )
    else:
        out["table_reference"] = {"$unknown": {"name": ""}}
    if data.get("allowedColumns") is not None:
        import capo_cleanrooms.types.allowed_column_list

        out["allowed_columns"] = (
            capo_cleanrooms.types.allowed_column_list.deserialize_json(
                data["allowedColumns"]
            )
        )
    else:
        out["allowed_columns"] = []
    if data.get("analysisMethod") is not None:
        import capo_cleanrooms.types.analysis_method

        out["analysis_method"] = capo_cleanrooms.types.analysis_method.deserialize_json(
            data["analysisMethod"]
        )
    else:
        import typing

        out["analysis_method"] = typing.cast(
            "capo_cleanrooms.types.analysis_method.AnalysisMethod", ""
        )
    if data.get("selectedAnalysisMethods") is not None:
        import capo_cleanrooms.types.selected_analysis_methods

        out["selected_analysis_methods"] = (
            capo_cleanrooms.types.selected_analysis_methods.deserialize_json(
                data["selectedAnalysisMethods"]
            )
        )
    if data.get("tags") is not None:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    return out
