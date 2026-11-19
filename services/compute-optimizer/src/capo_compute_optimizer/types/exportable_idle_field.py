"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableIdleField``."""

from typing import Literal, TypeAlias, cast

ExportableIdleField: TypeAlias = Literal[
    "AccountId",
    "ResourceArn",
    "ResourceId",
    "ResourceType",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "SavingsOpportunity",
    "SavingsOpportunityAfterDiscount",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsNetworkOutBytesPerSecondMaximum",
    "UtilizationMetricsNetworkInBytesPerSecondMaximum",
    "UtilizationMetricsDatabaseConnectionsMaximum",
    "UtilizationMetricsEBSVolumeReadIOPSMaximum",
    "UtilizationMetricsEBSVolumeWriteIOPSMaximum",
    "UtilizationMetricsVolumeReadOpsPerSecondMaximum",
    "UtilizationMetricsVolumeWriteOpsPerSecondMaximum",
    "UtilizationMetricsActiveConnectionCountMaximum",
    "UtilizationMetricsPacketsInFromSourceMaximum",
    "UtilizationMetricsPacketsInFromDestinationMaximum",
    "UtilizationMetricsConsumedReadCapacityUnitsSum",
    "UtilizationMetricsConsumedWriteCapacityUnitsSum",
    "UtilizationMetricsNewConnectionsSum",
    "UtilizationMetricsEngineCPUUtilizationMaximum",
    "UtilizationMetricsCacheHitsSum",
    "UtilizationMetricsCacheMissesSum",
    "UtilizationMetricsKeyspaceHitsSum",
    "UtilizationMetricsKeyspaceMissesSum",
    "UtilizationMetricsIsIdleMinimum",
    "UtilizationMetricsUserConnectedSum",
    "UtilizationMetricsInvocationsSum",
    "UtilizationMetricsGetTypeCmdsSum",
    "UtilizationMetricsSetTypeCmdsSum",
    "UtilizationMetricsElastiCacheProcessingUnitsSum",
    "UtilizationMetricsCurrConnectionsSum",
    "UtilizationMetricsDatabaseConnectionsSum",
    "Finding",
    "FindingDescription",
    "Tags",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableIdleField) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportableIdleField:
    return cast(ExportableIdleField, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportableIdleField) -> str:
    return value


def deserialize_cbor(data: str) -> ExportableIdleField:
    return cast(ExportableIdleField, data)
