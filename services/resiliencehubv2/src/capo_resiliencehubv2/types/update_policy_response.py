"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdatePolicyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.policy


class UpdatePolicyResponse(TypedDict, closed=True):
    policy: "capo_resiliencehubv2.types.policy.Policy"
    """<p>The updated policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePolicyResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.policy

    out["policy"] = capo_resiliencehubv2.types.policy.serialize_json(value["policy"])
    return out


def deserialize_json(data: dict) -> UpdatePolicyResponse:
    out: UpdatePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        import capo_resiliencehubv2.types.policy

        out["policy"] = capo_resiliencehubv2.types.policy.deserialize_json(
            data["policy"]
        )
    else:
        raise DeserializationError("UpdatePolicyResponse.policy required")
    return out


def redact_sensitive(value: UpdatePolicyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy" in value:
        import capo_resiliencehubv2.types.policy

        out["policy"] = capo_resiliencehubv2.types.policy.redact_sensitive(
            value["policy"]
        )
    return out
