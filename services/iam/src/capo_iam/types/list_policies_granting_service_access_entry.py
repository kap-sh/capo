"""Generated from Smithy shape ``com.amazonaws.iam#ListPoliciesGrantingServiceAccessEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.policy_granting_service_access_list_type
    import capo_iam.types.service_namespace_type


class ListPoliciesGrantingServiceAccessEntry(TypedDict, closed=True):
    service_namespace: NotRequired[
        "capo_iam.types.service_namespace_type.serviceNamespaceType"
    ]
    """<p>The namespace of the service that was accessed.</p> <p>To learn the service namespace of a service, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html">Actions, resources, and condition keys for Amazon Web Services services</a> in the <i>Service Authorization Reference</i>. Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, <code>(service prefix: a4b)</code>. For more information about service namespaces, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces">Amazon Web Services service namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    policies: NotRequired[
        "capo_iam.types.policy_granting_service_access_list_type.policyGrantingServiceAccessListType"
    ]
    """<p>The <code>PoliciesGrantingServiceAccess</code> object that contains details about the policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPoliciesGrantingServiceAccessEntry,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "service_namespace" in value:
        pairs.append((f"{key_prefix}ServiceNamespace", str(value["service_namespace"])))
    if "policies" in value:
        import capo_iam.types.policy_granting_service_access_list_type

        capo_iam.types.policy_granting_service_access_list_type.serialize_query(
            value["policies"], pairs, f"{key_prefix}Policies"
        )


def deserialize_query(el: Element) -> ListPoliciesGrantingServiceAccessEntry:
    out: ListPoliciesGrantingServiceAccessEntry = {}  # type: ignore[typeddict-item]
    child_service_namespace = el.find("ServiceNamespace")
    if child_service_namespace is not None:
        out["service_namespace"] = str(child_service_namespace.text or "")
    child_policies = el.find("Policies")
    if child_policies is not None:
        import capo_iam.types.policy_granting_service_access_list_type

        out["policies"] = (
            capo_iam.types.policy_granting_service_access_list_type.deserialize_query(
                child_policies
            )
        )
    return out
