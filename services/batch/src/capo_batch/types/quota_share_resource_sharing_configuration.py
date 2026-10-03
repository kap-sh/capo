"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareResourceSharingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.quota_share_resource_sharing_strategy


class QuotaShareResourceSharingConfiguration(TypedDict, closed=True):
    strategy: NotRequired[
        "capo_batch.types.quota_share_resource_sharing_strategy.QuotaShareResourceSharingStrategy"
    ]
    """<p>The resource sharing strategy for the quota share. The <code>RESERVE</code> strategy allows a quota share to reserve idle capacity for itself. <code>LEND</code> configures the share to lend its idle capacity to another share in need of capacity. The <code>LEND_AND_BORROW</code> strategy configures the share to borrow idle capacity from an underutilized share, as well as lend to another share.</p>"""
    borrow_limit: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The maximum percentage of additional capacity that the quota share can borrow from other shares. <code>borrowLimit</code> can only be applied to quota shares with a strategy of <code>LEND_AND_BORROW</code>. This value is expressed as a percentage of the quota share's configured <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_QuotaShareCapacityLimit.html">CapacityLimits</a>.</p> <p>The <code>borrowLimit</code> is applied uniformly across all capacity units. For example, if the <code>borrowLimit</code> is 200, the quota share can borrow up to 200% of its configured <code>maxCapacity</code> for each capacity unit. The default <code>borrowLimit</code> is -1, which indicates unlimited borrowing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareResourceSharingConfiguration) -> dict:
    out: dict = {}
    if "strategy" in value:
        import capo_batch.types.quota_share_resource_sharing_strategy

        out["strategy"] = (
            capo_batch.types.quota_share_resource_sharing_strategy.serialize_json(
                value["strategy"]
            )
        )
    if "borrow_limit" in value:
        out["borrowLimit"] = value["borrow_limit"]
    return out


def deserialize_json(data: dict) -> QuotaShareResourceSharingConfiguration:
    out: QuotaShareResourceSharingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("strategy") is not None:
        import capo_batch.types.quota_share_resource_sharing_strategy

        out["strategy"] = (
            capo_batch.types.quota_share_resource_sharing_strategy.deserialize_json(
                data["strategy"]
            )
        )
    if data.get("borrowLimit") is not None:
        out["borrow_limit"] = data["borrowLimit"]
    return out
