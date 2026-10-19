"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteTargetDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.target_domain_id


class DeleteTargetDomainInput(TypedDict, closed=True):
    target_domain_id: "capo_securityagent.types.target_domain_id.TargetDomainId"
    """<p>The unique identifier of the target domain to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTargetDomainInput) -> dict:
    out: dict = {}
    out["targetDomainId"] = value["target_domain_id"]
    return out


def deserialize_json(data: dict) -> DeleteTargetDomainInput:
    out: DeleteTargetDomainInput = {}  # type: ignore[typeddict-item]
    if data.get("targetDomainId") is not None:
        out["target_domain_id"] = data["targetDomainId"]
    else:
        out["target_domain_id"] = ""
    return out
