"""Generated from Smithy shape ``com.amazonaws.iam#ListPoliciesGrantingServiceAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.marker_type
    import capo_iam.types.service_namespace_list_type


class ListPoliciesGrantingServiceAccessRequest(TypedDict, closed=True):
    marker: NotRequired["capo_iam.types.marker_type.markerType"]
    """<p>Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the <code>Marker</code> element in the response that you received to indicate where the next call should start.</p>"""
    arn: "capo_iam.types.arn_type.arnType"
    """<p>The ARN of the IAM identity (user, group, or role) whose policies you want to list.</p>"""
    service_namespaces: (
        "capo_iam.types.service_namespace_list_type.serviceNamespaceListType"
    )
    """<p>The service namespace for the Amazon Web Services services whose policies you want to list.</p> <p>To learn the service namespace for a service, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html">Actions, resources, and condition keys for Amazon Web Services services</a> in the <i>IAM User Guide</i>. Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, <code>(service prefix: a4b)</code>. For more information about service namespaces, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces">Amazon Web Services service namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPoliciesGrantingServiceAccessRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    import capo_iam.types.service_namespace_list_type

    capo_iam.types.service_namespace_list_type.serialize_query(
        value["service_namespaces"], pairs, f"{key_prefix}ServiceNamespaces"
    )


def deserialize_query(el: Element) -> ListPoliciesGrantingServiceAccessRequest:
    out: ListPoliciesGrantingServiceAccessRequest = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError(
            "ListPoliciesGrantingServiceAccessRequest.arn required"
        )
    child_service_namespaces = el.find("ServiceNamespaces")
    if child_service_namespaces is not None:
        import capo_iam.types.service_namespace_list_type

        out["service_namespaces"] = (
            capo_iam.types.service_namespace_list_type.deserialize_query(
                child_service_namespaces
            )
        )
    else:
        raise DeserializationError(
            "ListPoliciesGrantingServiceAccessRequest.service_namespaces required"
        )
    return out
