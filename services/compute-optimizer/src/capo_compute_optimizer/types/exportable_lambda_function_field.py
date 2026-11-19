"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableLambdaFunctionField``."""

from typing import Literal, TypeAlias, cast

ExportableLambdaFunctionField: TypeAlias = Literal[
    "AccountId",
    "FunctionArn",
    "FunctionVersion",
    "Finding",
    "FindingReasonCodes",
    "NumberOfInvocations",
    "UtilizationMetricsDurationMaximum",
    "UtilizationMetricsDurationAverage",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsMemoryAverage",
    "LookbackPeriodInDays",
    "CurrentConfigurationMemorySize",
    "CurrentConfigurationTimeout",
    "CurrentCostTotal",
    "CurrentCostAverage",
    "RecommendationOptionsConfigurationMemorySize",
    "RecommendationOptionsCostLow",
    "RecommendationOptionsCostHigh",
    "RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound",
    "RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound",
    "RecommendationOptionsProjectedUtilizationMetricsDurationExpected",
    "LastRefreshTimestamp",
    "CurrentPerformanceRisk",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "Tags",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableLambdaFunctionField) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportableLambdaFunctionField:
    return cast(ExportableLambdaFunctionField, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportableLambdaFunctionField) -> str:
    return value


def deserialize_cbor(data: str) -> ExportableLambdaFunctionField:
    return cast(ExportableLambdaFunctionField, data)
