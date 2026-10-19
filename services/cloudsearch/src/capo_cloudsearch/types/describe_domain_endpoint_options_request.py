"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeDomainEndpointOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.boolean
    import capo_cloudsearch.types.domain_name


class DescribeDomainEndpointOptionsRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    """<p>A string that represents the name of a domain.</p>"""
    deployed: NotRequired["capo_cloudsearch.types.boolean.Boolean"]
    """<p>Whether to retrieve the latest configuration (which might be in a Processing state) or the current, active configuration. Defaults to <code>false</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDomainEndpointOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    if "deployed" in value:
        pairs.append(
            (f"{key_prefix}Deployed", "true" if value["deployed"] else "false")
        )


def deserialize_query(el: Element) -> DescribeDomainEndpointOptionsRequest:
    out: DescribeDomainEndpointOptionsRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_deployed = el.find("Deployed")
    if child_deployed is not None:
        out["deployed"] = (child_deployed.text or "").lower() == "true"
    return out
