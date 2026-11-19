"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableECSServiceField``."""

from typing import Literal, TypeAlias, cast

ExportableECSServiceField: TypeAlias = Literal[
    "AccountId",
    "ServiceArn",
    "LookbackPeriodInDays",
    "LastRefreshTimestamp",
    "LaunchType",
    "CurrentPerformanceRisk",
    "CurrentServiceConfigurationMemory",
    "CurrentServiceConfigurationCpu",
    "CurrentServiceConfigurationTaskDefinitionArn",
    "CurrentServiceConfigurationAutoScalingConfiguration",
    "CurrentServiceContainerConfigurations",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsMemoryMaximum",
    "Finding",
    "FindingReasonCodes",
    "RecommendationOptionsMemory",
    "RecommendationOptionsCpu",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsContainerRecommendations",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "Tags",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "EffectiveRecommendationPreferencesLookBackPeriod",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableECSServiceField) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportableECSServiceField:
    return cast(ExportableECSServiceField, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportableECSServiceField) -> str:
    return value


def deserialize_cbor(data: str) -> ExportableECSServiceField:
    return cast(ExportableECSServiceField, data)
