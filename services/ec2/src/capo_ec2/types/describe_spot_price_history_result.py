"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotPriceHistoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.spot_price_history_list
    import capo_ec2.types.string


class DescribeSpotPriceHistoryResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is an empty string (<code>""</code>) or <code>null</code> when there are no more items to return.</p>"""
    spot_price_history: NotRequired[
        "capo_ec2.types.spot_price_history_list.SpotPriceHistoryList"
    ]
    """<p>The historical Spot prices.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSpotPriceHistoryResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "spot_price_history" in value:
        import capo_ec2.types.spot_price_history_list

        capo_ec2.types.spot_price_history_list.serialize_ec2_query(
            value["spot_price_history"], pairs, f"{key_prefix}SpotPriceHistorySet"
        )


def deserialize_ec2_query(el: Element) -> DescribeSpotPriceHistoryResult:
    out: DescribeSpotPriceHistoryResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_spot_price_history = el.find("spotPriceHistorySet")
    if child_spot_price_history is not None:
        import capo_ec2.types.spot_price_history_list

        out["spot_price_history"] = (
            capo_ec2.types.spot_price_history_list.deserialize_ec2_query(
                child_spot_price_history
            )
        )
    return out
