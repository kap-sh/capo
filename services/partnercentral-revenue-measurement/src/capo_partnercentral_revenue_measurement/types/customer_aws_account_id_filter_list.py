"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#CustomerAwsAccountIdFilterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.customer_aws_account_id

CustomerAwsAccountIdFilterList: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.customer_aws_account_id.CustomerAwsAccountId"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomerAwsAccountIdFilterList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> CustomerAwsAccountIdFilterList:
    return [item for item in data if item is not None]


def redact_sensitive(value: CustomerAwsAccountIdFilterList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
