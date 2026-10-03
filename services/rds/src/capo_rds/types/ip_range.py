"""Generated from Smithy shape ``com.amazonaws.rds#IPRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class IPRange(TypedDict, closed=True):
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the IP range. Status can be "authorizing", "authorized", "revoking", and "revoked".</p>"""
    cidrip: NotRequired["capo_rds.types.string.String"]
    """<p>The IP range.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: IPRange, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "cidrip" in value:
        pairs.append((f"{key_prefix}CIDRIP", str(value["cidrip"])))


def deserialize_query(el: Element) -> IPRange:
    out: IPRange = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_cidrip = el.find("CIDRIP")
    if child_cidrip is not None:
        out["cidrip"] = str(child_cidrip.text or "")
    return out
