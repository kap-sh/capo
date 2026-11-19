"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Sort``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.sort_by
    import capo_marketplace_agreement.types.sort_order


class Sort(TypedDict, closed=True):
    sort_by: NotRequired["capo_marketplace_agreement.types.sort_by.SortBy"]
    """<p>The attribute on which the data is grouped, which can be <code>EndTime</code>, <code>StartTime</code>, or <code>LastUpdateTime</code>. <code>StartTime</code> and <code>LastUpdateTime</code> are supported only when <code>PartyType</code> is <code>Proposer</code>. The default value is <code>EndTime</code>.</p>"""
    sort_order: NotRequired["capo_marketplace_agreement.types.sort_order.SortOrder"]
    """<p>The sorting order, which can be <code>ASCENDING</code> or <code>DESCENDING</code>. The default value is <code>ASCENDING</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Sort) -> dict:
    out: dict = {}
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    if "sort_order" in value:
        import capo_marketplace_agreement.types.sort_order

        out["sortOrder"] = (
            capo_marketplace_agreement.types.sort_order.serialize_aws_json_1_0(
                value["sort_order"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Sort:
    out: Sort = {}  # type: ignore[typeddict-item]
    if data.get("sortBy") is not None:
        out["sort_by"] = data["sortBy"]
    if data.get("sortOrder") is not None:
        import capo_marketplace_agreement.types.sort_order

        out["sort_order"] = (
            capo_marketplace_agreement.types.sort_order.deserialize_aws_json_1_0(
                data["sortOrder"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Sort) -> dict:
    out: dict = {}
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    if "sort_order" in value:
        import capo_marketplace_agreement.types.sort_order

        out["sortOrder"] = capo_marketplace_agreement.types.sort_order.serialize_cbor(
            value["sort_order"]
        )
    return out


def deserialize_cbor(data: dict) -> Sort:
    out: Sort = {}  # type: ignore[typeddict-item]
    if data.get("sortBy") is not None:
        out["sort_by"] = data["sortBy"]
    if data.get("sortOrder") is not None:
        import capo_marketplace_agreement.types.sort_order

        out["sort_order"] = (
            capo_marketplace_agreement.types.sort_order.deserialize_cbor(
                data["sortOrder"]
            )
        )
    return out
