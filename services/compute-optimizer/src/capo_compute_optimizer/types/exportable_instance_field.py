"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableInstanceField``."""

from typing import Literal, TypeAlias, cast

ExportableInstanceField: TypeAlias = Literal[
    "AccountId",
    "InstanceArn",
    "InstanceName",
    "Finding",
    "FindingReasonCodes",
    "LookbackPeriodInDays",
    "CurrentInstanceType",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsEbsReadOpsPerSecondMaximum",
    "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
    "UtilizationMetricsEbsReadBytesPerSecondMaximum",
    "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
    "UtilizationMetricsDiskReadOpsPerSecondMaximum",
    "UtilizationMetricsDiskWriteOpsPerSecondMaximum",
    "UtilizationMetricsDiskReadBytesPerSecondMaximum",
    "UtilizationMetricsDiskWriteBytesPerSecondMaximum",
    "UtilizationMetricsNetworkInBytesPerSecondMaximum",
    "UtilizationMetricsNetworkOutBytesPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsInPerSecondMaximum",
    "UtilizationMetricsNetworkPacketsOutPerSecondMaximum",
    "CurrentOnDemandPrice",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentVCpus",
    "CurrentMemory",
    "CurrentStorage",
    "CurrentNetwork",
    "RecommendationOptionsInstanceType",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsPlatformDifferences",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsVcpus",
    "RecommendationOptionsMemory",
    "RecommendationOptionsStorage",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationsSourcesRecommendationSourceArn",
    "RecommendationsSourcesRecommendationSourceType",
    "LastRefreshTimestamp",
    "CurrentPerformanceRisk",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "EffectiveRecommendationPreferencesCpuVendorArchitectures",
    "EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics",
    "EffectiveRecommendationPreferencesInferredWorkloadTypes",
    "InferredWorkloadTypes",
    "RecommendationOptionsMigrationEffort",
    "EffectiveRecommendationPreferencesExternalMetricsSource",
    "Tags",
    "InstanceState",
    "ExternalMetricStatusCode",
    "ExternalMetricStatusReason",
    "CurrentInstanceGpuInfo",
    "RecommendationOptionsInstanceGpuInfo",
    "UtilizationMetricsGpuPercentageMaximum",
    "UtilizationMetricsGpuMemoryPercentageMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsGpuPercentageMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsGpuMemoryPercentageMaximum",
    "Idle",
    "EffectiveRecommendationPreferencesPreferredResources",
    "EffectiveRecommendationPreferencesLookBackPeriod",
    "EffectiveRecommendationPreferencesUtilizationPreferences",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableInstanceField) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportableInstanceField:
    return cast(ExportableInstanceField, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportableInstanceField) -> str:
    return value


def deserialize_cbor(data: str) -> ExportableInstanceField:
    return cast(ExportableInstanceField, data)
