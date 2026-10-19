"""Generated from Smithy shape ``com.amazonaws.amp#RuleGroupsNamespaceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.rule_groups_namespace_status_code


class RuleGroupsNamespaceStatus(TypedDict, closed=True):
    status_code: (
        "capo_amp.types.rule_groups_namespace_status_code.RuleGroupsNamespaceStatusCode"
    )
    """<p>The current status of the namespace.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the failure, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupsNamespaceStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> RuleGroupsNamespaceStatus:
    out: RuleGroupsNamespaceStatus = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    else:
        out["status_code"] = ""
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
