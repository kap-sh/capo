"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.allowed_column_list
    import capo_cleanrooms.types.analysis_method
    import capo_cleanrooms.types.configured_table_analysis_rule_type_list
    import capo_cleanrooms.types.configured_table_arn
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.selected_analysis_methods
    import capo_cleanrooms.types.table_description
    import capo_cleanrooms.types.table_reference
    import capo_cleanrooms.types.uuid


class ConfiguredTable(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the configured table.</p>"""
    arn: "capo_cleanrooms.types.configured_table_arn.ConfiguredTableArn"
    """<p>The unique ARN for the configured table.</p>"""
    name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>A name for the configured table.</p>"""
    description: NotRequired["capo_cleanrooms.types.table_description.TableDescription"]
    """<p>A description for the configured table.</p>"""
    table_reference: "capo_cleanrooms.types.table_reference.TableReference"
    """<p>The table that this configured table represents.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the configured table was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the configured table was last updated</p>"""
    analysis_rule_types: "capo_cleanrooms.types.configured_table_analysis_rule_type_list.ConfiguredTableAnalysisRuleTypeList"
    """<p>The types of analysis rules associated with this configured table. Currently, only one analysis rule may be associated with a configured table.</p>"""
    analysis_method: "capo_cleanrooms.types.analysis_method.AnalysisMethod"
    """<p>The analysis method for the configured table.</p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>"""
    allowed_columns: "capo_cleanrooms.types.allowed_column_list.AllowedColumnList"
    """<p>The columns within the underlying Glue table that can be used within collaborations.</p>"""
    selected_analysis_methods: NotRequired[
        "capo_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
    ]
    """<p> The selected analysis methods for the configured table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTable) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cleanrooms.types.table_reference

    out["tableReference"] = capo_cleanrooms.types.table_reference.serialize_json(
        value["table_reference"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import capo_cleanrooms.types.configured_table_analysis_rule_type_list

    out["analysisRuleTypes"] = (
        capo_cleanrooms.types.configured_table_analysis_rule_type_list.serialize_json(
            value["analysis_rule_types"]
        )
    )
    import capo_cleanrooms.types.analysis_method

    out["analysisMethod"] = capo_cleanrooms.types.analysis_method.serialize_json(
        value["analysis_method"]
    )
    import capo_cleanrooms.types.allowed_column_list

    out["allowedColumns"] = capo_cleanrooms.types.allowed_column_list.serialize_json(
        value["allowed_columns"]
    )
    if "selected_analysis_methods" in value:
        import capo_cleanrooms.types.selected_analysis_methods

        out["selectedAnalysisMethods"] = (
            capo_cleanrooms.types.selected_analysis_methods.serialize_json(
                value["selected_analysis_methods"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfiguredTable:
    out: ConfiguredTable = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
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
        import capo_cleanrooms.types._unknown

        out["table_reference"] = capo_cleanrooms.types._unknown.UnknownUnionMember("")
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("analysisRuleTypes") is not None:
        import capo_cleanrooms.types.configured_table_analysis_rule_type_list

        out["analysis_rule_types"] = (
            capo_cleanrooms.types.configured_table_analysis_rule_type_list.deserialize_json(
                data["analysisRuleTypes"]
            )
        )
    else:
        out["analysis_rule_types"] = []
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
    if data.get("allowedColumns") is not None:
        import capo_cleanrooms.types.allowed_column_list

        out["allowed_columns"] = (
            capo_cleanrooms.types.allowed_column_list.deserialize_json(
                data["allowedColumns"]
            )
        )
    else:
        out["allowed_columns"] = []
    if data.get("selectedAnalysisMethods") is not None:
        import capo_cleanrooms.types.selected_analysis_methods

        out["selected_analysis_methods"] = (
            capo_cleanrooms.types.selected_analysis_methods.deserialize_json(
                data["selectedAnalysisMethods"]
            )
        )
    return out
