"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.sla_name
    import capo_connectcases.types.sla_status


class SlaFilter(TypedDict, closed=True):
    name: NotRequired["capo_connectcases.types.sla_name.SlaName"]
    """<p>Name of an SLA.</p>"""
    status: NotRequired["capo_connectcases.types.sla_status.SlaStatus"]
    """<p>Status of an SLA.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlaFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> SlaFilter:
    out: SlaFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out


def redact_sensitive(value: SlaFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
