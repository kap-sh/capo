"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeAvailabilityOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.boolean
    import capo_cloudsearch.types.domain_name


class DescribeAvailabilityOptionsRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    """<p>The name of the domain you want to describe.</p>"""
    deployed: NotRequired["capo_cloudsearch.types.boolean.Boolean"]
    """<p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAvailabilityOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    if "deployed" in value:
        pairs.append(
            (f"{key_prefix}Deployed", "true" if value["deployed"] else "false")
        )


def deserialize_query(el: Element) -> DescribeAvailabilityOptionsRequest:
    out: DescribeAvailabilityOptionsRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_deployed = el.find("Deployed")
    if child_deployed is not None:
        out["deployed"] = (child_deployed.text or "").lower() == "true"
    return out
