"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetRLSPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.rls_policy


class GetRLSPolicyResponse(TypedDict, closed=True):
    rls_policy: NotRequired["capo_lakeformation.types.rls_policy.RLSPolicy"]
    """<p>An <code>RLSPolicy</code> structure containing the definition of the requested row-level security policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRLSPolicyResponse) -> dict:
    out: dict = {}
    if "rls_policy" in value:
        import capo_lakeformation.types.rls_policy

        out["RLSPolicy"] = capo_lakeformation.types.rls_policy.serialize_json(
            value["rls_policy"]
        )
    return out


def deserialize_json(data: dict) -> GetRLSPolicyResponse:
    out: GetRLSPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("RLSPolicy") is not None:
        import capo_lakeformation.types.rls_policy

        out["rls_policy"] = capo_lakeformation.types.rls_policy.deserialize_json(
            data["RLSPolicy"]
        )
    return out
