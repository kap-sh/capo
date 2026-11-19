"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableAutoScalingGroupField``."""

from typing import Literal, TypeAlias, cast

ExportableAutoScalingGroupField: TypeAlias = Literal[
    "AccountId",
    "AutoScalingGroupArn",
    "AutoScalingGroupName",
    "Finding",
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
    "LookbackPeriodInDays",
    "CurrentConfigurationInstanceType",
    "CurrentConfigurationDesiredCapacity",
    "CurrentConfigurationMinSize",
    "CurrentConfigurationMaxSize",
    "CurrentConfigurationAllocationStrategy",
    "CurrentConfigurationMixedInstanceTypes",
    "CurrentConfigurationType",
    "CurrentOnDemandPrice",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentVCpus",
    "CurrentMemory",
    "CurrentStorage",
    "CurrentNetwork",
    "RecommendationOptionsConfigurationInstanceType",
    "RecommendationOptionsConfigurationDesiredCapacity",
    "RecommendationOptionsConfigurationMinSize",
    "RecommendationOptionsConfigurationMaxSize",
    "RecommendationOptionsConfigurationEstimatedInstanceHourReductionPercentage",
    "RecommendationOptionsConfigurationAllocationStrategy",
    "RecommendationOptionsConfigurationMixedInstanceTypes",
    "RecommendationOptionsConfigurationType",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationOptionsVcpus",
    "RecommendationOptionsMemory",
    "RecommendationOptionsStorage",
    "RecommendationOptionsNetwork",
    "LastRefreshTimestamp",
    "CurrentPerformanceRisk",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "EffectiveRecommendationPreferencesCpuVendorArchitectures",
    "EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics",
    "EffectiveRecommendationPreferencesInferredWorkloadTypes",
    "EffectiveRecommendationPreferencesPreferredResources",
    "EffectiveRecommendationPreferencesLookBackPeriod",
    "InferredWorkloadTypes",
    "RecommendationOptionsMigrationEffort",
    "CurrentInstanceGpuInfo",
    "RecommendationOptionsInstanceGpuInfo",
    "UtilizationMetricsGpuPercentageMaximum",
    "UtilizationMetricsGpuMemoryPercentageMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsGpuPercentageMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsGpuMemoryPercentageMaximum",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableAutoScalingGroupField) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportableAutoScalingGroupField:
    return cast(ExportableAutoScalingGroupField, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportableAutoScalingGroupField) -> str:
    return value


def deserialize_cbor(data: str) -> ExportableAutoScalingGroupField:
    return cast(ExportableAutoScalingGroupField, data)
