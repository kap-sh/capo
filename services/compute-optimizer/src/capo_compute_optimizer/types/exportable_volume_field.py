"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableVolumeField``."""

from typing import Literal, TypeAlias, cast

ExportableVolumeField: TypeAlias = Literal[
    "AccountId",
    "VolumeArn",
    "Finding",
    "UtilizationMetricsVolumeReadOpsPerSecondMaximum",
    "UtilizationMetricsVolumeWriteOpsPerSecondMaximum",
    "UtilizationMetricsVolumeReadBytesPerSecondMaximum",
    "UtilizationMetricsVolumeWriteBytesPerSecondMaximum",
    "UtilizationMetricsVolumeIOPSExceededMaximum",
    "UtilizationMetricsVolumeThroughputExceededMaximum",
    "LookbackPeriodInDays",
    "CurrentConfigurationVolumeType",
    "CurrentConfigurationVolumeBaselineIOPS",
    "CurrentConfigurationVolumeBaselineThroughput",
    "CurrentConfigurationVolumeBurstIOPS",
    "CurrentConfigurationVolumeBurstThroughput",
    "CurrentConfigurationVolumeSize",
    "CurrentMonthlyPrice",
    "RecommendationOptionsConfigurationVolumeType",
    "RecommendationOptionsConfigurationVolumeBaselineIOPS",
    "RecommendationOptionsConfigurationVolumeBaselineThroughput",
    "RecommendationOptionsConfigurationVolumeBurstIOPS",
    "RecommendationOptionsConfigurationVolumeBurstThroughput",
    "RecommendationOptionsConfigurationVolumeSize",
    "RecommendationOptionsMonthlyPrice",
    "RecommendationOptionsPerformanceRisk",
    "LastRefreshTimestamp",
    "CurrentPerformanceRisk",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "Tags",
    "RootVolume",
    "CurrentConfigurationRootVolume",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "EffectiveRecommendationPreferencesLookBackPeriod",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableVolumeField) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportableVolumeField:
    return cast(ExportableVolumeField, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportableVolumeField) -> str:
    return value


def deserialize_cbor(data: str) -> ExportableVolumeField:
    return cast(ExportableVolumeField, data)
