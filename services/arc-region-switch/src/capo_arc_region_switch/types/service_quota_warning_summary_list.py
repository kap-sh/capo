"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ServiceQuotaWarningSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.service_quota_warning_summary

ServiceQuotaWarningSummaryList: TypeAlias = list[
    "capo_arc_region_switch.types.service_quota_warning_summary.ServiceQuotaWarningSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceQuotaWarningSummaryList) -> list:
    import capo_arc_region_switch.types.service_quota_warning_summary

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.service_quota_warning_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ServiceQuotaWarningSummaryList:
    import capo_arc_region_switch.types.service_quota_warning_summary

    out: ServiceQuotaWarningSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.service_quota_warning_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceQuotaWarningSummaryList) -> list:
    import capo_arc_region_switch.types.service_quota_warning_summary

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.service_quota_warning_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ServiceQuotaWarningSummaryList:
    import capo_arc_region_switch.types.service_quota_warning_summary

    out: ServiceQuotaWarningSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.service_quota_warning_summary.deserialize_cbor(
                item
            )
        )
    return out
