"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetDatasetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.dataset_id
    import capo_connecthealth.types.domain_id


class GetDatasetInput(TypedDict, closed=True):
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p>The unique identifier of the parent Domain.</p>"""
    dataset_id: "capo_connecthealth.types.dataset_id.DatasetId"
    """<p>The unique identifier of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatasetInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDatasetInput:
    out: GetDatasetInput = {}  # type: ignore[typeddict-item]
    return out
