"""Generated from Smithy shape ``com.amazonaws.iam#AccessDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.date_type
    import capo_iam.types.integer_type
    import capo_iam.types.organizations_entity_path_type
    import capo_iam.types.service_name_type
    import capo_iam.types.service_namespace_type
    import capo_iam.types.string_type


class AccessDetail(TypedDict, closed=True):
    service_name: "capo_iam.types.service_name_type.serviceNameType"
    """<p>The name of the service in which access was attempted.</p>"""
    service_namespace: "capo_iam.types.service_namespace_type.serviceNamespaceType"
    """<p>The namespace of the service in which access was attempted.</p> <p>To learn the service namespace of a service, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html">Actions, resources, and condition keys for Amazon Web Services services</a> in the <i>Service Authorization Reference</i>. Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, <code>(service prefix: a4b)</code>. For more information about service namespaces, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces">Amazon Web Services service namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    region: NotRequired["capo_iam.types.string_type.stringType"]
    """<p>The Region where the last service access attempt occurred.</p> <p>This field is null if no principals in the reported Organizations entity attempted to access the service within the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period">tracking period</a>.</p>"""
    entity_path: NotRequired[
        "capo_iam.types.organizations_entity_path_type.organizationsEntityPathType"
    ]
    """<p>The path of the Organizations entity (root, organizational unit, or account) from which an authenticated principal last attempted to access the service. Amazon Web Services does not report unauthenticated requests.</p> <p>This field is null if no principals (IAM users, IAM roles, or root user) in the reported Organizations entity attempted to access the service within the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period">tracking period</a>.</p>"""
    last_authenticated_time: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when an authenticated principal most recently attempted to access the service. Amazon Web Services does not report unauthenticated requests.</p> <p>This field is null if no principals in the reported Organizations entity attempted to access the service within the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period">tracking period</a>.</p>"""
    total_authenticated_entities: NotRequired["capo_iam.types.integer_type.integerType"]
    """<p>The number of accounts with authenticated principals (root user, IAM users, and IAM roles) that attempted to access the service in the tracking period.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccessDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ServiceName", str(value["service_name"])))
    pairs.append((f"{key_prefix}ServiceNamespace", str(value["service_namespace"])))
    if "region" in value:
        pairs.append((f"{key_prefix}Region", str(value["region"])))
    if "entity_path" in value:
        pairs.append((f"{key_prefix}EntityPath", str(value["entity_path"])))
    if "last_authenticated_time" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["last_authenticated_time"],
            pairs,
            f"{key_prefix}LastAuthenticatedTime",
        )
    if "total_authenticated_entities" in value:
        pairs.append(
            (
                f"{key_prefix}TotalAuthenticatedEntities",
                str(value["total_authenticated_entities"]),
            )
        )


def deserialize_query(el: Element) -> AccessDetail:
    out: AccessDetail = {}  # type: ignore[typeddict-item]
    child_service_name = el.find("ServiceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    else:
        raise DeserializationError("AccessDetail.service_name required")
    child_service_namespace = el.find("ServiceNamespace")
    if child_service_namespace is not None:
        out["service_namespace"] = str(child_service_namespace.text or "")
    else:
        raise DeserializationError("AccessDetail.service_namespace required")
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    child_entity_path = el.find("EntityPath")
    if child_entity_path is not None:
        out["entity_path"] = str(child_entity_path.text or "")
    child_last_authenticated_time = el.find("LastAuthenticatedTime")
    if child_last_authenticated_time is not None:
        import capo_iam.types.date_type

        out["last_authenticated_time"] = capo_iam.types.date_type.deserialize_query(
            child_last_authenticated_time
        )
    child_total_authenticated_entities = el.find("TotalAuthenticatedEntities")
    if child_total_authenticated_entities is not None:
        out["total_authenticated_entities"] = int(
            child_total_authenticated_entities.text or ""
        )
    return out
