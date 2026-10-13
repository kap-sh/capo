"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeResiliencyPolicyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.resiliency_policy


class DescribeResiliencyPolicyResponse(TypedDict, closed=True):
    policy: "capo_resiliencehub.types.resiliency_policy.ResiliencyPolicy"
    """<p>Information about the specific resiliency policy, returned as an object. This object includes creation time, data location constraints, its name, description, tags, the recovery time objective (RTO) and recovery point objective (RPO) in seconds, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResiliencyPolicyResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.resiliency_policy

    out["policy"] = capo_resiliencehub.types.resiliency_policy.serialize_json(
        value["policy"]
    )
    return out


def deserialize_json(data: dict) -> DescribeResiliencyPolicyResponse:
    out: DescribeResiliencyPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        import capo_resiliencehub.types.resiliency_policy

        out["policy"] = capo_resiliencehub.types.resiliency_policy.deserialize_json(
            data["policy"]
        )
    else:
        raise DeserializationError("DescribeResiliencyPolicyResponse.policy required")
    return out


def redact_sensitive(value: DescribeResiliencyPolicyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy" in value:
        import capo_resiliencehub.types.resiliency_policy

        out["policy"] = capo_resiliencehub.types.resiliency_policy.redact_sensitive(
            value["policy"]
        )
    return out
