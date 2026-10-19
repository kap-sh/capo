"""Generated from Smithy shape ``com.amazonaws.cloudsearch#UpdateServiceAccessPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_name
    import capo_cloudsearch.types.policy_document


class UpdateServiceAccessPoliciesRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    access_policies: "capo_cloudsearch.types.policy_document.PolicyDocument"
    """<p>The access rules you want to configure. These rules replace any existing rules. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateServiceAccessPoliciesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    pairs.append((f"{key_prefix}AccessPolicies", str(value["access_policies"])))


def deserialize_query(el: Element) -> UpdateServiceAccessPoliciesRequest:
    out: UpdateServiceAccessPoliciesRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_access_policies = el.find("AccessPolicies")
    if child_access_policies is not None:
        out["access_policies"] = str(child_access_policies.text or "")
    else:
        out["access_policies"] = ""
    return out
