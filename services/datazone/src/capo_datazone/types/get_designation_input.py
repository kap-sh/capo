"""Generated from Smithy shape ``com.amazonaws.datazone#GetDesignationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.designation_id
    import capo_datazone.types.domain_id


class GetDesignationInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain that contains the designation.</p>"""
    identifier: "capo_datazone.types.designation_id.DesignationId"
    """<p>The unique ID of the designation to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDesignationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDesignationInput:
    out: GetDesignationInput = {}  # type: ignore[typeddict-item]
    return out
