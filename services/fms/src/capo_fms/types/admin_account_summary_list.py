"""Generated from Smithy shape ``com.amazonaws.fms#AdminAccountSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.admin_account_summary

AdminAccountSummaryList: TypeAlias = list[
    "capo_fms.types.admin_account_summary.AdminAccountSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminAccountSummaryList) -> list:
    import capo_fms.types.admin_account_summary

    out: list = []
    for item in value:
        out.append(capo_fms.types.admin_account_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AdminAccountSummaryList:
    import capo_fms.types.admin_account_summary

    out: AdminAccountSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.admin_account_summary.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AdminAccountSummaryList) -> list:
    import capo_fms.types.admin_account_summary

    out: list = []
    for item in value:
        out.append(capo_fms.types.admin_account_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AdminAccountSummaryList:
    import capo_fms.types.admin_account_summary

    out: AdminAccountSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.admin_account_summary.deserialize_cbor(item))
    return out
