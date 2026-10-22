"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteDesignationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.designation_id
    import capo_datazone.types.domain_id


class DeleteDesignationInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain that contains the designation to delete.</p>"""
    identifier: "capo_datazone.types.designation_id.DesignationId"
    """<p>The unique ID of the designation to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDesignationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDesignationInput:
    out: DeleteDesignationInput = {}  # type: ignore[typeddict-item]
    return out
