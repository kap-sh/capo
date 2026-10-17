"""Generated from Smithy shape ``com.amazonaws.lakeformation#DeleteRLSPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.name_string


class DeleteRLSPolicyRequest(TypedDict, closed=True):
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name of the row-level security policy to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRLSPolicyRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteRLSPolicyRequest:
    out: DeleteRLSPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteRLSPolicyRequest.name required")
    return out
