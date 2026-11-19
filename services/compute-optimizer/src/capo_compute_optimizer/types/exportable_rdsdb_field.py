"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableRDSDBField``."""

from typing import Literal, TypeAlias, cast

ExportableRDSDBField: TypeAlias = Literal[
    "ResourceArn",
    "AccountId",
    "Engine",
    "EngineVersion",
    "Idle",
    "MultiAZDBInstance",
    "ClusterWriter",
    "CurrentDBInstanceClass",
    "CurrentStorageConfigurationStorageType",
    "CurrentStorageConfigurationAllocatedStorage",
    "CurrentStorageConfigurationMaxAllocatedStorage",
    "CurrentStorageConfigurationIOPS",
    "CurrentStorageConfigurationStorageThroughput",
    "CurrentStorageEstimatedMonthlyVolumeIOPsCostVariation",
    "CurrentInstanceOnDemandHourlyPrice",
    "CurrentStorageOnDemandMonthlyPrice",
    "LookbackPeriodInDays",
    "CurrentStorageEstimatedClusterInstanceOnDemandMonthlyCost",
    "CurrentStorageEstimatedClusterStorageOnDemandMonthlyCost",
    "CurrentStorageEstimatedClusterStorageIOOnDemandMonthlyCost",
    "CurrentInstancePerformanceRisk",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsEBSVolumeStorageSpaceUtilizationMaximum",
    "UtilizationMetricsNetworkReceiveThroughputMaximum",
    "UtilizationMetricsNetworkTransmitThroughputMaximum",
    "UtilizationMetricsEBSVolumeReadIOPSMaximum",
    "UtilizationMetricsEBSVolumeWriteIOPSMaximum",
    "UtilizationMetricsEBSVolumeReadThroughputMaximum",
    "UtilizationMetricsEBSVolumeWriteThroughputMaximum",
    "UtilizationMetricsDatabaseConnectionsMaximum",
    "UtilizationMetricsStorageNetworkReceiveThroughputMaximum",
    "UtilizationMetricsStorageNetworkTransmitThroughputMaximum",
    "UtilizationMetricsAuroraMemoryHealthStateMaximum",
    "UtilizationMetricsAuroraMemoryNumDeclinedSqlTotalMaximum",
    "UtilizationMetricsAuroraMemoryNumKillConnTotalMaximum",
    "UtilizationMetricsAuroraMemoryNumKillQueryTotalMaximum",
    "UtilizationMetricsReadIOPSEphemeralStorageMaximum",
    "UtilizationMetricsWriteIOPSEphemeralStorageMaximum",
    "UtilizationMetricsVolumeBytesUsedAverage",
    "UtilizationMetricsVolumeReadIOPsAverage",
    "UtilizationMetricsVolumeWriteIOPsAverage",
    "InstanceFinding",
    "InstanceFindingReasonCodes",
    "StorageFinding",
    "StorageFindingReasonCodes",
    "InstanceRecommendationOptionsDBInstanceClass",
    "InstanceRecommendationOptionsRank",
    "InstanceRecommendationOptionsPerformanceRisk",
    "InstanceRecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "StorageRecommendationOptionsStorageType",
    "StorageRecommendationOptionsAllocatedStorage",
    "StorageRecommendationOptionsMaxAllocatedStorage",
    "StorageRecommendationOptionsIOPS",
    "StorageRecommendationOptionsStorageThroughput",
    "StorageRecommendationOptionsRank",
    "StorageRecommendationOptionsEstimatedMonthlyVolumeIOPsCostVariation",
    "InstanceRecommendationOptionsInstanceOnDemandHourlyPrice",
    "InstanceRecommendationOptionsSavingsOpportunityPercentage",
    "InstanceRecommendationOptionsEstimatedMonthlySavingsCurrency",
    "InstanceRecommendationOptionsEstimatedMonthlySavingsValue",
    "InstanceRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "InstanceRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "InstanceRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "StorageRecommendationOptionsOnDemandMonthlyPrice",
    "StorageRecommendationOptionsEstimatedClusterInstanceOnDemandMonthlyCost",
    "StorageRecommendationOptionsEstimatedClusterStorageOnDemandMonthlyCost",
    "StorageRecommendationOptionsEstimatedClusterStorageIOOnDemandMonthlyCost",
    "StorageRecommendationOptionsSavingsOpportunityPercentage",
    "StorageRecommendationOptionsEstimatedMonthlySavingsCurrency",
    "StorageRecommendationOptionsEstimatedMonthlySavingsValue",
    "StorageRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "StorageRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "StorageRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "EffectiveRecommendationPreferencesCpuVendorArchitectures",
    "EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics",
    "EffectiveRecommendationPreferencesLookBackPeriod",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "LastRefreshTimestamp",
    "Tags",
    "DBClusterIdentifier",
    "PromotionTier",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableRDSDBField) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportableRDSDBField:
    return cast(ExportableRDSDBField, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportableRDSDBField) -> str:
    return value


def deserialize_cbor(data: str) -> ExportableRDSDBField:
    return cast(ExportableRDSDBField, data)
