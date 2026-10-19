"""Generated from Smithy shape ``com.amazonaws.iam#GenerateOrganizationsAccessReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.organizations_entity_path_type
    import capo_iam.types.organizations_policy_id_type


class GenerateOrganizationsAccessReportRequest(TypedDict, closed=True):
    entity_path: (
        "capo_iam.types.organizations_entity_path_type.organizationsEntityPathType"
    )
    """<p>The path of the Organizations entity (root, OU, or account). You can build an entity path using the known structure of your organization. For example, assume that your account ID is <code>123456789012</code> and its parent OU ID is <code>ou-rge0-awsabcde</code>. The organization root ID is <code>r-f6g7h8i9j0example</code> and your organization ID is <code>o-a1b2c3d4e5</code>. Your entity path is <code>o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-rge0-awsabcde/123456789012</code>.</p>"""
    organizations_policy_id: NotRequired[
        "capo_iam.types.organizations_policy_id_type.organizationsPolicyIdType"
    ]
    """<p>The identifier of the Organizations service control policy (SCP). This parameter is optional.</p> <p>This ID is used to generate information about when an account principal that is limited by the SCP attempted to access an Amazon Web Services service.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GenerateOrganizationsAccessReportRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}EntityPath", str(value["entity_path"])))
    if "organizations_policy_id" in value:
        pairs.append(
            (
                f"{key_prefix}OrganizationsPolicyId",
                str(value["organizations_policy_id"]),
            )
        )


def deserialize_query(el: Element) -> GenerateOrganizationsAccessReportRequest:
    out: GenerateOrganizationsAccessReportRequest = {}  # type: ignore[typeddict-item]
    child_entity_path = el.find("EntityPath")
    if child_entity_path is not None:
        out["entity_path"] = str(child_entity_path.text or "")
    else:
        out["entity_path"] = ""
    child_organizations_policy_id = el.find("OrganizationsPolicyId")
    if child_organizations_policy_id is not None:
        out["organizations_policy_id"] = str(child_organizations_policy_id.text or "")
    return out
