"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamInternetRegistryAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_id
    import capo_ec2.types.rir
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateIpamInternetRegistryAssociationRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_id: NotRequired["capo_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM to associate with the internet registry.</p>"""
    rir: NotRequired["capo_ec2.types.rir.Rir"]
    """<p>The internet registry to associate with. Possible values:</p> <ul> <li> <p> <code>ripe</code> - RIPE NCC (Europe, the Middle East, and Central Asia).</p> </li> <li> <p> <code>apnic</code> - APNIC (Asia Pacific).</p> </li> <li> <p> <code>arin</code> - ARIN (North America).</p> </li> <li> <p> <code>lacnic</code> - LACNIC (Latin America and the Caribbean).</p> </li> <li> <p> <code>nicbr</code> - NIC.br (Brazil).</p> </li> </ul>"""
    organization_handle: NotRequired["capo_ec2.types.string.String"]
    """<p>The organization handle at the internet registry (for example, a RIPE NCC organization ID or ARIN Org ID).</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the internet registry association.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the internet registry association.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the operation ignores the request, but does not return an error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateIpamInternetRegistryAssociationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_id" in value:
        pairs.append((f"{key_prefix}IpamId", str(value["ipam_id"])))
    if "rir" in value:
        import capo_ec2.types.rir

        capo_ec2.types.rir.serialize_ec2_query(value["rir"], pairs, f"{key_prefix}Rir")
    if "organization_handle" in value:
        pairs.append(
            (f"{key_prefix}OrganizationHandle", str(value["organization_handle"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateIpamInternetRegistryAssociationRequest:
    out: CreateIpamInternetRegistryAssociationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_rir = el.find("Rir")
    if child_rir is not None:
        import capo_ec2.types.rir

        out["rir"] = capo_ec2.types.rir.deserialize_ec2_query(child_rir)
    child_organization_handle = el.find("OrganizationHandle")
    if child_organization_handle is not None:
        out["organization_handle"] = str(child_organization_handle.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
