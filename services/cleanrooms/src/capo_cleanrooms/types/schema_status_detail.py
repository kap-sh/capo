"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaStatusDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule_type
    import capo_cleanrooms.types.analysis_type
    import capo_cleanrooms.types.schema_configuration_list
    import capo_cleanrooms.types.schema_status
    import capo_cleanrooms.types.schema_status_reason_list


class SchemaStatusDetail(TypedDict, closed=True):
    status: "capo_cleanrooms.types.schema_status.SchemaStatus"
    """<p>The status of the schema, indicating if it is ready to query.</p>"""
    reasons: NotRequired[
        "capo_cleanrooms.types.schema_status_reason_list.SchemaStatusReasonList"
    ]
    """<p>The reasons why the schema status is set to its current state.</p>"""
    analysis_rule_type: NotRequired[
        "capo_cleanrooms.types.analysis_rule_type.AnalysisRuleType"
    ]
    """<p>The analysis rule type for which the schema status has been evaluated.</p>"""
    configurations: NotRequired[
        "capo_cleanrooms.types.schema_configuration_list.SchemaConfigurationList"
    ]
    """<p>The configuration details of the schema analysis rule for the given type.</p>"""
    analysis_type: "capo_cleanrooms.types.analysis_type.AnalysisType"
    """<p>The type of analysis that can be performed on the schema.</p> <p>A schema can have an <code>analysisType</code> of <code>DIRECT_ANALYSIS</code>, <code>ADDITIONAL_ANALYSIS_FOR_AUDIENCE_GENERATION</code>, or both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaStatusDetail) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.schema_status

    out["status"] = capo_cleanrooms.types.schema_status.serialize_json(value["status"])
    if "reasons" in value:
        import capo_cleanrooms.types.schema_status_reason_list

        out["reasons"] = capo_cleanrooms.types.schema_status_reason_list.serialize_json(
            value["reasons"]
        )
    if "analysis_rule_type" in value:
        import capo_cleanrooms.types.analysis_rule_type

        out["analysisRuleType"] = (
            capo_cleanrooms.types.analysis_rule_type.serialize_json(
                value["analysis_rule_type"]
            )
        )
    if "configurations" in value:
        import capo_cleanrooms.types.schema_configuration_list

        out["configurations"] = (
            capo_cleanrooms.types.schema_configuration_list.serialize_json(
                value["configurations"]
            )
        )
    import capo_cleanrooms.types.analysis_type

    out["analysisType"] = capo_cleanrooms.types.analysis_type.serialize_json(
        value["analysis_type"]
    )
    return out


def deserialize_json(data: dict) -> SchemaStatusDetail:
    out: SchemaStatusDetail = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_cleanrooms.types.schema_status

        out["status"] = capo_cleanrooms.types.schema_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanrooms.types.schema_status.SchemaStatus", ""
        )
    if data.get("reasons") is not None:
        import capo_cleanrooms.types.schema_status_reason_list

        out["reasons"] = (
            capo_cleanrooms.types.schema_status_reason_list.deserialize_json(
                data["reasons"]
            )
        )
    if data.get("analysisRuleType") is not None:
        import capo_cleanrooms.types.analysis_rule_type

        out["analysis_rule_type"] = (
            capo_cleanrooms.types.analysis_rule_type.deserialize_json(
                data["analysisRuleType"]
            )
        )
    if data.get("configurations") is not None:
        import capo_cleanrooms.types.schema_configuration_list

        out["configurations"] = (
            capo_cleanrooms.types.schema_configuration_list.deserialize_json(
                data["configurations"]
            )
        )
    if data.get("analysisType") is not None:
        import capo_cleanrooms.types.analysis_type

        out["analysis_type"] = capo_cleanrooms.types.analysis_type.deserialize_json(
            data["analysisType"]
        )
    else:
        import typing

        out["analysis_type"] = typing.cast(
            "capo_cleanrooms.types.analysis_type.AnalysisType", ""
        )
    return out
