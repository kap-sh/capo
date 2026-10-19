"""Generated from Smithy shape ``com.amazonaws.oam#GetSinkPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_oam.types.resource_identifier


class GetSinkPolicyInput(TypedDict, closed=True):
    sink_identifier: "capo_oam.types.resource_identifier.ResourceIdentifier"
    """<p>The ARN of the sink to retrieve the policy of.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSinkPolicyInput) -> dict:
    out: dict = {}
    out["SinkIdentifier"] = value["sink_identifier"]
    return out


def deserialize_json(data: dict) -> GetSinkPolicyInput:
    out: GetSinkPolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("SinkIdentifier") is not None:
        out["sink_identifier"] = data["SinkIdentifier"]
    else:
        out["sink_identifier"] = ""
    return out
