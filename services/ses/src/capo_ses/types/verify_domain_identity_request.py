"""Generated from Smithy shape ``com.amazonaws.ses#VerifyDomainIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.domain


class VerifyDomainIdentityRequest(TypedDict, closed=True):
    domain: "capo_ses.types.domain.Domain"
    """<p>The domain to be verified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VerifyDomainIdentityRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Domain", str(value["domain"])))


def deserialize_query(el: Element) -> VerifyDomainIdentityRequest:
    out: VerifyDomainIdentityRequest = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    else:
        out["domain"] = ""
    return out
