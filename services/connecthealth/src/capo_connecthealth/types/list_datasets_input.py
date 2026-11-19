"""Generated from Smithy shape ``com.amazonaws.connecthealth#ListDatasetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.dataset_type
    import capo_connecthealth.types.domain_id


class ListDatasetsInput(TypedDict, closed=True):
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p>The unique identifier of the parent Domain.</p>"""
    type: NotRequired["capo_connecthealth.types.dataset_type.DatasetType"]
    """<p>Returns only datasets of this type.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next page of results, from a previous ListDatasets response. If you don't specify a value, the operation returns the first page of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of datasets to return in one page. The default is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatasetsInput:
    out: ListDatasetsInput = {}  # type: ignore[typeddict-item]
    return out
