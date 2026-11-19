"""Generated from Smithy shape ``com.amazonaws.servicecatalog#PortfolioShareDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.portfolio_share_detail

PortfolioShareDetails: TypeAlias = list[
    "capo_service_catalog.types.portfolio_share_detail.PortfolioShareDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortfolioShareDetails) -> list:
    import capo_service_catalog.types.portfolio_share_detail

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.portfolio_share_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PortfolioShareDetails:
    import capo_service_catalog.types.portfolio_share_detail

    out: PortfolioShareDetails = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.portfolio_share_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PortfolioShareDetails) -> list:
    import capo_service_catalog.types.portfolio_share_detail

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.portfolio_share_detail.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> PortfolioShareDetails:
    import capo_service_catalog.types.portfolio_share_detail

    out: PortfolioShareDetails = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.portfolio_share_detail.deserialize_cbor(item)
        )
    return out
