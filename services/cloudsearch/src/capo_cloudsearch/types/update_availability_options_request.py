"""Generated from Smithy shape ``com.amazonaws.cloudsearch#UpdateAvailabilityOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.boolean
    import capo_cloudsearch.types.domain_name


class UpdateAvailabilityOptionsRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    multi_az: "capo_cloudsearch.types.boolean.Boolean"
    """<p>You expand an existing search domain to a second Availability Zone by setting the Multi-AZ option to true. Similarly, you can turn off the Multi-AZ option to downgrade the domain to a single Availability Zone by setting the Multi-AZ option to <code>false</code>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateAvailabilityOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))


def deserialize_query(el: Element) -> UpdateAvailabilityOptionsRequest:
    out: UpdateAvailabilityOptionsRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
    else:
        out["multi_az"] = False
    return out
