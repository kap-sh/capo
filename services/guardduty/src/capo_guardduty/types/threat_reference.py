"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.mitre_threat_id
    import capo_guardduty.types.string


class ThreatReference(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the tactic or technique.</p>"""
    uid: NotRequired["capo_guardduty.types.mitre_threat_id.MitreThreatId"]
    """<p>The MITRE ATT&amp;CK identifier of the tactic or technique, such as <code>TA0002</code> or <code>T1059.004</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatReference) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "uid" in value:
        out["uid"] = value["uid"]
    return out


def deserialize_json(data: dict) -> ThreatReference:
    out: ThreatReference = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("uid") is not None:
        out["uid"] = data["uid"]
    return out
