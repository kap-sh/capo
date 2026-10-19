"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CheckDNSAvailabilityMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.dns_cname_prefix


class CheckDNSAvailabilityMessage(TypedDict, closed=True):
    cname_prefix: "capo_elastic_beanstalk.types.dns_cname_prefix.DNSCnamePrefix"
    """<p>The prefix used when this CNAME is reserved.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CheckDNSAvailabilityMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}CNAMEPrefix", str(value["cname_prefix"])))


def deserialize_query(el: Element) -> CheckDNSAvailabilityMessage:
    out: CheckDNSAvailabilityMessage = {}  # type: ignore[typeddict-item]
    child_cname_prefix = el.find("CNAMEPrefix")
    if child_cname_prefix is not None:
        out["cname_prefix"] = str(child_cname_prefix.text or "")
    else:
        out["cname_prefix"] = ""
    return out
