"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTablePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.resource_policy


class GetTablePolicyResponse(TypedDict, closed=True):
    resource_policy: "capo_s3tables.types.resource_policy.ResourcePolicy"
    """<p>The <code>JSON</code> that defines the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTablePolicyResponse) -> dict:
    out: dict = {}
    out["resourcePolicy"] = value["resource_policy"]
    return out


def deserialize_json(data: dict) -> GetTablePolicyResponse:
    out: GetTablePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourcePolicy") is not None:
        out["resource_policy"] = data["resourcePolicy"]
    else:
        out["resource_policy"] = ""
    return out
