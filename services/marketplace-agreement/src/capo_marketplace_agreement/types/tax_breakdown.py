"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#TaxBreakdown``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.tax_breakdown_item

TaxBreakdown: TypeAlias = list[
    "capo_marketplace_agreement.types.tax_breakdown_item.TaxBreakdownItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaxBreakdown) -> list:
    import capo_marketplace_agreement.types.tax_breakdown_item

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.tax_breakdown_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TaxBreakdown:
    import capo_marketplace_agreement.types.tax_breakdown_item

    out: TaxBreakdown = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.tax_breakdown_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TaxBreakdown) -> list:
    import capo_marketplace_agreement.types.tax_breakdown_item

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.tax_breakdown_item.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> TaxBreakdown:
    import capo_marketplace_agreement.types.tax_breakdown_item

    out: TaxBreakdown = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.tax_breakdown_item.deserialize_cbor(item)
        )
    return out
