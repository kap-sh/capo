"""Generated from Smithy shape ``com.amazonaws.ses#ReceiptIpFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.cidr
    import capo_ses.types.receipt_filter_policy


class ReceiptIpFilter(TypedDict, closed=True):
    policy: "capo_ses.types.receipt_filter_policy.ReceiptFilterPolicy"
    """<p>Indicates whether to block or allow incoming mail from the specified IP addresses.</p>"""
    cidr: "capo_ses.types.cidr.Cidr"
    """<p>A single IP address or a range of IP addresses to block or allow, specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about CIDR notation, see <a href="https://tools.ietf.org/html/rfc2317">RFC 2317</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReceiptIpFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.receipt_filter_policy

    capo_ses.types.receipt_filter_policy.serialize_query(
        value["policy"], pairs, f"{key_prefix}Policy"
    )
    pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))


def deserialize_query(el: Element) -> ReceiptIpFilter:
    out: ReceiptIpFilter = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        import capo_ses.types.receipt_filter_policy

        out["policy"] = capo_ses.types.receipt_filter_policy.deserialize_query(
            child_policy
        )
    else:
        raise DeserializationError("ReceiptIpFilter.policy required")
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    else:
        raise DeserializationError("ReceiptIpFilter.cidr required")
    return out
