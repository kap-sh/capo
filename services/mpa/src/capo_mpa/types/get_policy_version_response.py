"""Generated from Smithy shape ``com.amazonaws.mpa#GetPolicyVersionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mpa.types.policy_version


class GetPolicyVersionResponse(TypedDict, closed=True):
    policy_version: "capo_mpa.types.policy_version.PolicyVersion"
    """<p>A <code>PolicyVersion</code> object. Contains details for the version of the policy. Policies define the permissions for team resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyVersionResponse) -> dict:
    out: dict = {}
    import capo_mpa.types.policy_version

    out["PolicyVersion"] = capo_mpa.types.policy_version.serialize_json(
        value["policy_version"]
    )
    return out


def deserialize_json(data: dict) -> GetPolicyVersionResponse:
    out: GetPolicyVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("PolicyVersion") is not None:
        import capo_mpa.types.policy_version

        out["policy_version"] = capo_mpa.types.policy_version.deserialize_json(
            data["PolicyVersion"]
        )
    else:
        raise DeserializationError("GetPolicyVersionResponse.policy_version required")
    return out


def redact_sensitive(value: GetPolicyVersionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy_version" in value:
        import capo_mpa.types.policy_version

        out["policy_version"] = capo_mpa.types.policy_version.redact_sensitive(
            value["policy_version"]
        )
    return out
