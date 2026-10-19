"""Generated from Smithy shape ``com.amazonaws.outposts#StartOutpostDecommissionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.outpost_identifier
    import capo_outposts.types.validate_only


class StartOutpostDecommissionInput(TypedDict, closed=True):
    outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>The ID or ARN of the Outpost that you want to decommission.</p>"""
    validate_only: NotRequired["capo_outposts.types.validate_only.ValidateOnly"]
    """<p>Validates the request without starting the decommission process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOutpostDecommissionInput) -> dict:
    out: dict = {}
    if "validate_only" in value:
        out["ValidateOnly"] = value["validate_only"]
    return out


def deserialize_json(data: dict) -> StartOutpostDecommissionInput:
    out: StartOutpostDecommissionInput = {}  # type: ignore[typeddict-item]
    if data.get("ValidateOnly") is not None:
        out["validate_only"] = data["ValidateOnly"]
    return out
