"""Generated from Smithy shape ``com.amazonaws.ec2#RemoveIpamOrganizationalUnitExclusion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class RemoveIpamOrganizationalUnitExclusion(TypedDict, closed=True):
    organizations_entity_path: NotRequired["capo_ec2.types.string.String"]
    """<p>An Amazon Web Services Organizations entity path. Build the path for the OU(s) using Amazon Web Services Organizations IDs separated by a <code>/</code>. Include all child OUs by ending the path with <code>/*</code>.</p> <ul> <li> <p>Example 1</p> <ul> <li> <p>Path to a child OU: <code>o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/ou-jkl0-awsddddd/</code> </p> </li> <li> <p>In this example, <code>o-a1b2c3d4e5</code> is the organization ID, <code>r-f6g7h8i9j0example</code> is the root ID , <code>ou-ghi0-awsccccc</code> is an OU ID, and <code>ou-jkl0-awsddddd</code> is a child OU ID.</p> </li> <li> <p>IPAM will not manage the IP addresses in accounts in the child OU.</p> </li> </ul> </li> <li> <p>Example 2</p> <ul> <li> <p>Path where all child OUs will be part of the exclusion: <code>o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/*</code> </p> </li> <li> <p>In this example, IPAM will not manage the IP addresses in accounts in the OU (<code>ou-ghi0-awsccccc</code>) or in accounts in any OUs that are children of the OU.</p> </li> </ul> </li> </ul> <p>For more information on how to construct an entity path, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_access-advisor-viewing-orgs-entity-path">Understand the Amazon Web Services Organizations entity path</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RemoveIpamOrganizationalUnitExclusion,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "organizations_entity_path" in value:
        pairs.append(
            (
                f"{key_prefix}OrganizationsEntityPath",
                str(value["organizations_entity_path"]),
            )
        )


def deserialize_ec2_query(el: Element) -> RemoveIpamOrganizationalUnitExclusion:
    out: RemoveIpamOrganizationalUnitExclusion = {}  # type: ignore[typeddict-item]
    child_organizations_entity_path = el.find("OrganizationsEntityPath")
    if child_organizations_entity_path is not None:
        out["organizations_entity_path"] = str(
            child_organizations_entity_path.text or ""
        )
    return out
