"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetRLSPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.name_string


class GetRLSPolicyRequest(TypedDict, closed=True):
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name of the row-level security policy to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRLSPolicyRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> GetRLSPolicyRequest:
    out: GetRLSPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
