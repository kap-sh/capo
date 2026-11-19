"""Generated from Smithy shape ``com.amazonaws.route53domains#BillingRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route_53_domains.types.billing_record

BillingRecords: TypeAlias = list[
    "capo_route_53_domains.types.billing_record.BillingRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BillingRecords) -> list:
    import capo_route_53_domains.types.billing_record

    out: list = []
    for item in value:
        out.append(
            capo_route_53_domains.types.billing_record.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BillingRecords:
    import capo_route_53_domains.types.billing_record

    out: BillingRecords = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route_53_domains.types.billing_record.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BillingRecords) -> list:
    import capo_route_53_domains.types.billing_record

    out: list = []
    for item in value:
        out.append(capo_route_53_domains.types.billing_record.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> BillingRecords:
    import capo_route_53_domains.types.billing_record

    out: BillingRecords = []
    for item in data:
        if item is None:
            continue
        out.append(capo_route_53_domains.types.billing_record.deserialize_cbor(item))
    return out
