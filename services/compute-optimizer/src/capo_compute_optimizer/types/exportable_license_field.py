"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableLicenseField``."""

from typing import Literal, TypeAlias, cast

ExportableLicenseField: TypeAlias = Literal[
    "AccountId",
    "ResourceArn",
    "LookbackPeriodInDays",
    "LastRefreshTimestamp",
    "Finding",
    "FindingReasonCodes",
    "CurrentLicenseConfigurationNumberOfCores",
    "CurrentLicenseConfigurationInstanceType",
    "CurrentLicenseConfigurationOperatingSystem",
    "CurrentLicenseConfigurationLicenseName",
    "CurrentLicenseConfigurationLicenseEdition",
    "CurrentLicenseConfigurationLicenseModel",
    "CurrentLicenseConfigurationLicenseVersion",
    "CurrentLicenseConfigurationMetricsSource",
    "RecommendationOptionsOperatingSystem",
    "RecommendationOptionsLicenseEdition",
    "RecommendationOptionsLicenseModel",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "Tags",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableLicenseField) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportableLicenseField:
    return cast(ExportableLicenseField, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportableLicenseField) -> str:
    return value


def deserialize_cbor(data: str) -> ExportableLicenseField:
    return cast(ExportableLicenseField, data)
