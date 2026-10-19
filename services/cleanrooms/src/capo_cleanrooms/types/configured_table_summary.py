"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.analysis_method
    import capo_cleanrooms.types.configured_table_analysis_rule_type_list
    import capo_cleanrooms.types.configured_table_arn
    import capo_cleanrooms.types.configured_table_identifier
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.selected_analysis_methods


class ConfiguredTableSummary(TypedDict, closed=True):
    id: "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier"
    """<p>The unique ID of the configured table.</p>"""
    arn: "capo_cleanrooms.types.configured_table_arn.ConfiguredTableArn"
    """<p>The unique ARN of the configured table.</p>"""
    name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The name of the configured table.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the configured table was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the configured table was last updated.</p>"""
    analysis_rule_types: "capo_cleanrooms.types.configured_table_analysis_rule_type_list.ConfiguredTableAnalysisRuleTypeList"
    """<p>The types of analysis rules associated with this configured table.</p>"""
    analysis_method: "capo_cleanrooms.types.analysis_method.AnalysisMethod"
    """<p>The analysis method for the configured tables. </p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>"""
    selected_analysis_methods: NotRequired[
        "capo_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
    ]
    """<p> The selected analysis methods for the configured table summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
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
    if "selected_analysis_methods" in value:
        import capo_cleanrooms.types.selected_analysis_methods

        out["selectedAnalysisMethods"] = (
            capo_cleanrooms.types.selected_analysis_methods.serialize_json(
                value["selected_analysis_methods"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfiguredTableSummary:
    out: ConfiguredTableSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("selectedAnalysisMethods") is not None:
        import capo_cleanrooms.types.selected_analysis_methods

        out["selected_analysis_methods"] = (
            capo_cleanrooms.types.selected_analysis_methods.deserialize_json(
                data["selectedAnalysisMethods"]
            )
        )
    return out
