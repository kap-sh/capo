"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListCoreNetworkEndpointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.filters


class ListCoreNetworkEndpointsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to retrieve in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response.</p>"""
    filters: NotRequired["capo_route53globalresolver.types.filters.Filters"]
    """<p>Values to filter the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreNetworkEndpointsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCoreNetworkEndpointsInput:
    out: ListCoreNetworkEndpointsInput = {}  # type: ignore[typeddict-item]
    return out
