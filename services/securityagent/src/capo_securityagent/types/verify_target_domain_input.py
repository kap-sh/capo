"""Generated from Smithy shape ``com.amazonaws.securityagent#VerifyTargetDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.target_domain_id


class VerifyTargetDomainInput(TypedDict, closed=True):
    target_domain_id: "capo_securityagent.types.target_domain_id.TargetDomainId"
    """<p>The unique identifier of the target domain to verify.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyTargetDomainInput) -> dict:
    out: dict = {}
    out["targetDomainId"] = value["target_domain_id"]
    return out


def deserialize_json(data: dict) -> VerifyTargetDomainInput:
    out: VerifyTargetDomainInput = {}  # type: ignore[typeddict-item]
    if data.get("targetDomainId") is not None:
        out["target_domain_id"] = data["targetDomainId"]
    else:
        out["target_domain_id"] = ""
    return out
