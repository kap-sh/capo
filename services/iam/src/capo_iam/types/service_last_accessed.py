"""Generated from Smithy shape ``com.amazonaws.iam#ServiceLastAccessed``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.date_type
    import capo_iam.types.integer_type
    import capo_iam.types.service_name_type
    import capo_iam.types.service_namespace_type
    import capo_iam.types.string_type
    import capo_iam.types.tracked_actions_last_accessed


class ServiceLastAccessed(TypedDict, closed=True):
    service_name: "capo_iam.types.service_name_type.serviceNameType"
    """<p>The name of the service in which access was attempted.</p>"""
    last_authenticated: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when an authenticated entity most recently attempted to access the service. Amazon Web Services does not report unauthenticated requests.</p> <p>This field is null if no IAM entities attempted to access the service within the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period">tracking period</a>.</p>"""
    service_namespace: "capo_iam.types.service_namespace_type.serviceNamespaceType"
    """<p>The namespace of the service in which access was attempted.</p> <p>To learn the service namespace of a service, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html">Actions, resources, and condition keys for Amazon Web Services services</a> in the <i>Service Authorization Reference</i>. Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, <code>(service prefix: a4b)</code>. For more information about service namespaces, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces">Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    last_authenticated_entity: NotRequired["capo_iam.types.arn_type.arnType"]
    """<p>The ARN of the authenticated entity (user or role) that last attempted to access the service. Amazon Web Services does not report unauthenticated requests.</p> <p>This field is null if no IAM entities attempted to access the service within the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period">tracking period</a>.</p>"""
    last_authenticated_region: NotRequired["capo_iam.types.string_type.stringType"]
    """<p>The Region from which the authenticated entity (user or role) last attempted to access the service. Amazon Web Services does not report unauthenticated requests.</p> <p>This field is null if no IAM entities attempted to access the service within the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period">tracking period</a>.</p>"""
    total_authenticated_entities: NotRequired["capo_iam.types.integer_type.integerType"]
    """<p>The total number of authenticated principals (root user, IAM users, or IAM roles) that have attempted to access the service.</p> <p>This field is null if no principals attempted to access the service within the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period">tracking period</a>.</p>"""
    tracked_actions_last_accessed: NotRequired[
        "capo_iam.types.tracked_actions_last_accessed.TrackedActionsLastAccessed"
    ]
    """<p>An object that contains details about the most recent attempt to access a tracked action within the service.</p> <p>This field is null if there no tracked actions or if the principal did not use the tracked actions within the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period">tracking period</a>. This field is also null if the report was generated at the service level and not the action level. For more information, see the <code>Granularity</code> field in <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateServiceLastAccessedDetails.html">GenerateServiceLastAccessedDetails</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceLastAccessed, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ServiceName", str(value["service_name"])))
    if "last_authenticated" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["last_authenticated"], pairs, f"{key_prefix}LastAuthenticated"
        )
    pairs.append((f"{key_prefix}ServiceNamespace", str(value["service_namespace"])))
    if "last_authenticated_entity" in value:
        pairs.append(
            (
                f"{key_prefix}LastAuthenticatedEntity",
                str(value["last_authenticated_entity"]),
            )
        )
    if "last_authenticated_region" in value:
        pairs.append(
            (
                f"{key_prefix}LastAuthenticatedRegion",
                str(value["last_authenticated_region"]),
            )
        )
    if "total_authenticated_entities" in value:
        pairs.append(
            (
                f"{key_prefix}TotalAuthenticatedEntities",
                str(value["total_authenticated_entities"]),
            )
        )
    if "tracked_actions_last_accessed" in value:
        import capo_iam.types.tracked_actions_last_accessed

        capo_iam.types.tracked_actions_last_accessed.serialize_query(
            value["tracked_actions_last_accessed"],
            pairs,
            f"{key_prefix}TrackedActionsLastAccessed",
        )


def deserialize_query(el: Element) -> ServiceLastAccessed:
    out: ServiceLastAccessed = {}  # type: ignore[typeddict-item]
    child_service_name = el.find("ServiceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    else:
        raise DeserializationError("ServiceLastAccessed.service_name required")
    child_last_authenticated = el.find("LastAuthenticated")
    if child_last_authenticated is not None:
        import capo_iam.types.date_type

        out["last_authenticated"] = capo_iam.types.date_type.deserialize_query(
            child_last_authenticated
        )
    child_service_namespace = el.find("ServiceNamespace")
    if child_service_namespace is not None:
        out["service_namespace"] = str(child_service_namespace.text or "")
    else:
        raise DeserializationError("ServiceLastAccessed.service_namespace required")
    child_last_authenticated_entity = el.find("LastAuthenticatedEntity")
    if child_last_authenticated_entity is not None:
        out["last_authenticated_entity"] = str(
            child_last_authenticated_entity.text or ""
        )
    child_last_authenticated_region = el.find("LastAuthenticatedRegion")
    if child_last_authenticated_region is not None:
        out["last_authenticated_region"] = str(
            child_last_authenticated_region.text or ""
        )
    child_total_authenticated_entities = el.find("TotalAuthenticatedEntities")
    if child_total_authenticated_entities is not None:
        out["total_authenticated_entities"] = int(
            child_total_authenticated_entities.text or ""
        )
    child_tracked_actions_last_accessed = el.find("TrackedActionsLastAccessed")
    if child_tracked_actions_last_accessed is not None:
        import capo_iam.types.tracked_actions_last_accessed

        out["tracked_actions_last_accessed"] = (
            capo_iam.types.tracked_actions_last_accessed.deserialize_query(
                child_tracked_actions_last_accessed
            )
        )
    return out
