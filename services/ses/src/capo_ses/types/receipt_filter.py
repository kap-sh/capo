"""Generated from Smithy shape ``com.amazonaws.ses#ReceiptFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.receipt_filter_name
    import capo_ses.types.receipt_ip_filter


class ReceiptFilter(TypedDict, closed=True):
    name: "capo_ses.types.receipt_filter_name.ReceiptFilterName"
    """<p>The name of the IP address filter. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Start and end with a letter or number.</p> </li> <li> <p>Contain 64 characters or fewer.</p> </li> </ul>"""
    ip_filter: "capo_ses.types.receipt_ip_filter.ReceiptIpFilter"
    """<p>A structure that provides the IP addresses to block or allow, and whether to block or allow incoming mail from them.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReceiptFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Name", str(value["name"])))
    import capo_ses.types.receipt_ip_filter

    capo_ses.types.receipt_ip_filter.serialize_query(
        value["ip_filter"], pairs, f"{key_prefix}IpFilter"
    )


def deserialize_query(el: Element) -> ReceiptFilter:
    out: ReceiptFilter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_ip_filter = el.find("IpFilter")
    if child_ip_filter is not None:
        import capo_ses.types.receipt_ip_filter

        out["ip_filter"] = capo_ses.types.receipt_ip_filter.deserialize_query(
            child_ip_filter
        )
    else:
        raise DeserializationError("ReceiptFilter.ip_filter required")
    return out
