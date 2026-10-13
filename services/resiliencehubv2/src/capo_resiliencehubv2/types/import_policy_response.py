"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ImportPolicyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.policy


class ImportPolicyResponse(TypedDict, closed=True):
    policy: "capo_resiliencehubv2.types.policy.Policy"
    """<p>The imported policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportPolicyResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.policy

    out["policy"] = capo_resiliencehubv2.types.policy.serialize_json(value["policy"])
    return out


def deserialize_json(data: dict) -> ImportPolicyResponse:
    out: ImportPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        import capo_resiliencehubv2.types.policy

        out["policy"] = capo_resiliencehubv2.types.policy.deserialize_json(
            data["policy"]
        )
    else:
        raise DeserializationError("ImportPolicyResponse.policy required")
    return out


def redact_sensitive(value: ImportPolicyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy" in value:
        import capo_resiliencehubv2.types.policy

        out["policy"] = capo_resiliencehubv2.types.policy.redact_sensitive(
            value["policy"]
        )
    return out
