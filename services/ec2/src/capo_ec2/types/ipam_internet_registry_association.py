"""Generated from Smithy shape ``com.amazonaws.ec2#IpamInternetRegistryAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_id
    import capo_ec2.types.ipam_internet_registry_association_id
    import capo_ec2.types.ipam_internet_registry_association_state
    import capo_ec2.types.resource_arn
    import capo_ec2.types.rir
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class IpamInternetRegistryAssociation(TypedDict, closed=True):
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the internet registry association.</p>"""
    ipam_internet_registry_association_id: NotRequired[
        "capo_ec2.types.ipam_internet_registry_association_id.IpamInternetRegistryAssociationId"
    ]
    """<p>The ID of the internet registry association.</p>"""
    ipam_internet_registry_association_arn: NotRequired[
        "capo_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the internet registry association.</p>"""
    ipam_id: NotRequired["capo_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the associated IPAM.</p>"""
    ipam_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the IPAM.</p>"""
    rir: NotRequired["capo_ec2.types.rir.Rir"]
    """<p>The internet registry. Possible values:</p> <ul> <li> <p> <code>ripe</code> - RIPE NCC (Europe, the Middle East, and Central Asia).</p> </li> <li> <p> <code>apnic</code> - APNIC (Asia Pacific).</p> </li> <li> <p> <code>arin</code> - ARIN (North America).</p> </li> <li> <p> <code>lacnic</code> - LACNIC (Latin America and the Caribbean).</p> </li> <li> <p> <code>nicbr</code> - NIC.br (Brazil).</p> </li> </ul>"""
    organization_handle: NotRequired["capo_ec2.types.string.String"]
    """<p>The organization handle at the internet registry.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the internet registry association.</p>"""
    state: NotRequired[
        "capo_ec2.types.ipam_internet_registry_association_state.IpamInternetRegistryAssociationState"
    ]
    """<p>The state of the internet registry association. Valid values: <code>pending-enable</code> | <code>create-in-progress</code> | <code>create-failed</code> | <code>enable-in-progress</code> | <code>enable-complete</code> | <code>enable-failed</code> | <code>disable-in-progress</code> | <code>disable-complete</code> | <code>disable-failed</code> | <code>delete-in-progress</code> | <code>delete-complete</code> | <code>delete-failed</code>.</p>"""
    state_message: NotRequired["capo_ec2.types.string.String"]
    """<p>A message describing the current state of the internet registry association, including additional details such as the reason for a failure.</p>"""
    child_request_xml: NotRequired["capo_ec2.types.string.String"]
    """<p>The XML content for the child request to be submitted to the internet registry to complete the BPKI setup.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the internet registry association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamInternetRegistryAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "ipam_internet_registry_association_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamInternetRegistryAssociationId",
                str(value["ipam_internet_registry_association_id"]),
            )
        )
    if "ipam_internet_registry_association_arn" in value:
        pairs.append(
            (
                f"{key_prefix}IpamInternetRegistryAssociationArn",
                str(value["ipam_internet_registry_association_arn"]),
            )
        )
    if "ipam_id" in value:
        pairs.append((f"{key_prefix}IpamId", str(value["ipam_id"])))
    if "ipam_region" in value:
        pairs.append((f"{key_prefix}IpamRegion", str(value["ipam_region"])))
    if "rir" in value:
        import capo_ec2.types.rir

        capo_ec2.types.rir.serialize_ec2_query(value["rir"], pairs, f"{key_prefix}Rir")
    if "organization_handle" in value:
        pairs.append(
            (f"{key_prefix}OrganizationHandle", str(value["organization_handle"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "state" in value:
        import capo_ec2.types.ipam_internet_registry_association_state

        capo_ec2.types.ipam_internet_registry_association_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "state_message" in value:
        pairs.append((f"{key_prefix}StateMessage", str(value["state_message"])))
    if "child_request_xml" in value:
        pairs.append((f"{key_prefix}ChildRequestXml", str(value["child_request_xml"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> IpamInternetRegistryAssociation:
    out: IpamInternetRegistryAssociation = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_ipam_internet_registry_association_id = el.find(
        "ipamInternetRegistryAssociationId"
    )
    if child_ipam_internet_registry_association_id is not None:
        out["ipam_internet_registry_association_id"] = str(
            child_ipam_internet_registry_association_id.text or ""
        )
    child_ipam_internet_registry_association_arn = el.find(
        "ipamInternetRegistryAssociationArn"
    )
    if child_ipam_internet_registry_association_arn is not None:
        out["ipam_internet_registry_association_arn"] = str(
            child_ipam_internet_registry_association_arn.text or ""
        )
    child_ipam_id = el.find("ipamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_ipam_region = el.find("ipamRegion")
    if child_ipam_region is not None:
        out["ipam_region"] = str(child_ipam_region.text or "")
    child_rir = el.find("rir")
    if child_rir is not None:
        import capo_ec2.types.rir

        out["rir"] = capo_ec2.types.rir.deserialize_ec2_query(child_rir)
    child_organization_handle = el.find("organizationHandle")
    if child_organization_handle is not None:
        out["organization_handle"] = str(child_organization_handle.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.ipam_internet_registry_association_state

        out["state"] = (
            capo_ec2.types.ipam_internet_registry_association_state.deserialize_ec2_query(
                child_state
            )
        )
    child_state_message = el.find("stateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    child_child_request_xml = el.find("childRequestXml")
    if child_child_request_xml is not None:
        out["child_request_xml"] = str(child_child_request_xml.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
