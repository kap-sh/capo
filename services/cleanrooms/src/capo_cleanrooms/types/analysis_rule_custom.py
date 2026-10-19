"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRuleCustom``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.additional_analyses
    import capo_cleanrooms.types.aggregation_threshold_list
    import capo_cleanrooms.types.allowed_additional_analyses
    import capo_cleanrooms.types.allowed_analyses_list
    import capo_cleanrooms.types.allowed_analysis_provider_list
    import capo_cleanrooms.types.allowed_result_receivers
    import capo_cleanrooms.types.analysis_rule_column_list
    import capo_cleanrooms.types.comparison_controls
    import capo_cleanrooms.types.differential_privacy_configuration


class AnalysisRuleCustom(TypedDict, closed=True):
    allowed_analyses: "capo_cleanrooms.types.allowed_analyses_list.AllowedAnalysesList"
    """<p>The ARN of the analysis templates that are allowed by the custom analysis rule.</p>"""
    allowed_analysis_providers: NotRequired[
        "capo_cleanrooms.types.allowed_analysis_provider_list.AllowedAnalysisProviderList"
    ]
    """<p>The IDs of the Amazon Web Services accounts that are allowed to query by the custom analysis rule. Required when <code>allowedAnalyses</code> is <code>ANY_QUERY</code>.</p>"""
    additional_analyses: NotRequired[
        "capo_cleanrooms.types.additional_analyses.AdditionalAnalyses"
    ]
    """<p> An indicator as to whether additional analyses (such as Clean Rooms ML) can be applied to the output of the direct query.</p>"""
    disallowed_output_columns: NotRequired[
        "capo_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    ]
    """<p> A list of columns that aren't allowed to be shown in the query output.</p>"""
    differential_privacy: NotRequired[
        "capo_cleanrooms.types.differential_privacy_configuration.DifferentialPrivacyConfiguration"
    ]
    """<p>The differential privacy configuration.</p>"""
    aggregation_thresholds: NotRequired[
        "capo_cleanrooms.types.aggregation_threshold_list.AggregationThresholdList"
    ]
    """<p>The aggregation thresholds that each query output group must satisfy. Clean Rooms filters out any group that represents fewer than the specified number of distinct identities. You can specify at most one threshold. You can't use aggregation thresholds with differential privacy, or when <code>allowedAnalyses</code> allows only jobs.</p>"""
    comparison_controls: NotRequired[
        "capo_cleanrooms.types.comparison_controls.ComparisonControls"
    ]
    """<p>The controls that restrict how a query can compare the columns in the configured table. You can't use comparison controls with differential privacy, or when <code>allowedAnalyses</code> allows only jobs.</p>"""
    allowed_result_receivers: NotRequired[
        "capo_cleanrooms.types.allowed_result_receivers.AllowedResultReceivers"
    ]
    """<p>The list of Amazon Web Services account IDs that are allowed to receive results from queries run on the configured table.</p>"""
    allowed_additional_analyses: NotRequired[
        "capo_cleanrooms.types.allowed_additional_analyses.AllowedAdditionalAnalyses"
    ]
    """<p>The list of allowed additional analyses for the custom analysis rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleCustom) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.allowed_analyses_list

    out["allowedAnalyses"] = capo_cleanrooms.types.allowed_analyses_list.serialize_json(
        value["allowed_analyses"]
    )
    if "allowed_analysis_providers" in value:
        import capo_cleanrooms.types.allowed_analysis_provider_list

        out["allowedAnalysisProviders"] = (
            capo_cleanrooms.types.allowed_analysis_provider_list.serialize_json(
                value["allowed_analysis_providers"]
            )
        )
    if "additional_analyses" in value:
        import capo_cleanrooms.types.additional_analyses

        out["additionalAnalyses"] = (
            capo_cleanrooms.types.additional_analyses.serialize_json(
                value["additional_analyses"]
            )
        )
    if "disallowed_output_columns" in value:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["disallowedOutputColumns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.serialize_json(
                value["disallowed_output_columns"]
            )
        )
    if "differential_privacy" in value:
        import capo_cleanrooms.types.differential_privacy_configuration

        out["differentialPrivacy"] = (
            capo_cleanrooms.types.differential_privacy_configuration.serialize_json(
                value["differential_privacy"]
            )
        )
    if "aggregation_thresholds" in value:
        import capo_cleanrooms.types.aggregation_threshold_list

        out["aggregationThresholds"] = (
            capo_cleanrooms.types.aggregation_threshold_list.serialize_json(
                value["aggregation_thresholds"]
            )
        )
    if "comparison_controls" in value:
        import capo_cleanrooms.types.comparison_controls

        out["comparisonControls"] = (
            capo_cleanrooms.types.comparison_controls.serialize_json(
                value["comparison_controls"]
            )
        )
    if "allowed_result_receivers" in value:
        import capo_cleanrooms.types.allowed_result_receivers

        out["allowedResultReceivers"] = (
            capo_cleanrooms.types.allowed_result_receivers.serialize_json(
                value["allowed_result_receivers"]
            )
        )
    if "allowed_additional_analyses" in value:
        import capo_cleanrooms.types.allowed_additional_analyses

        out["allowedAdditionalAnalyses"] = (
            capo_cleanrooms.types.allowed_additional_analyses.serialize_json(
                value["allowed_additional_analyses"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRuleCustom:
    out: AnalysisRuleCustom = {}  # type: ignore[typeddict-item]
    if data.get("allowedAnalyses") is not None:
        import capo_cleanrooms.types.allowed_analyses_list

        out["allowed_analyses"] = (
            capo_cleanrooms.types.allowed_analyses_list.deserialize_json(
                data["allowedAnalyses"]
            )
        )
    else:
        out["allowed_analyses"] = []
    if data.get("allowedAnalysisProviders") is not None:
        import capo_cleanrooms.types.allowed_analysis_provider_list

        out["allowed_analysis_providers"] = (
            capo_cleanrooms.types.allowed_analysis_provider_list.deserialize_json(
                data["allowedAnalysisProviders"]
            )
        )
    if data.get("additionalAnalyses") is not None:
        import capo_cleanrooms.types.additional_analyses

        out["additional_analyses"] = (
            capo_cleanrooms.types.additional_analyses.deserialize_json(
                data["additionalAnalyses"]
            )
        )
    if data.get("disallowedOutputColumns") is not None:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["disallowed_output_columns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["disallowedOutputColumns"]
            )
        )
    if data.get("differentialPrivacy") is not None:
        import capo_cleanrooms.types.differential_privacy_configuration

        out["differential_privacy"] = (
            capo_cleanrooms.types.differential_privacy_configuration.deserialize_json(
                data["differentialPrivacy"]
            )
        )
    if data.get("aggregationThresholds") is not None:
        import capo_cleanrooms.types.aggregation_threshold_list

        out["aggregation_thresholds"] = (
            capo_cleanrooms.types.aggregation_threshold_list.deserialize_json(
                data["aggregationThresholds"]
            )
        )
    if data.get("comparisonControls") is not None:
        import capo_cleanrooms.types.comparison_controls

        out["comparison_controls"] = (
            capo_cleanrooms.types.comparison_controls.deserialize_json(
                data["comparisonControls"]
            )
        )
    if data.get("allowedResultReceivers") is not None:
        import capo_cleanrooms.types.allowed_result_receivers

        out["allowed_result_receivers"] = (
            capo_cleanrooms.types.allowed_result_receivers.deserialize_json(
                data["allowedResultReceivers"]
            )
        )
    if data.get("allowedAdditionalAnalyses") is not None:
        import capo_cleanrooms.types.allowed_additional_analyses

        out["allowed_additional_analyses"] = (
            capo_cleanrooms.types.allowed_additional_analyses.deserialize_json(
                data["allowedAdditionalAnalyses"]
            )
        )
    return out
