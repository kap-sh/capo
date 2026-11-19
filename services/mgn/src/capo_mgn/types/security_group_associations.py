"""Generated from Smithy shape ``com.amazonaws.mgn#SecurityGroupAssociations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.association_cidr_list
    import capo_mgn.types.association_user_provided_id_list
    import capo_mgn.types.association_vm_uuid_list


class SecurityGroupAssociations(TypedDict, closed=True):
    cidrs: NotRequired["capo_mgn.types.association_cidr_list.AssociationCidrList"]
    """<p>The CIDR ranges associated with the security group. A provided list replaces the stored list; an empty list clears it, and omitting the field leaves it unchanged.</p>"""
    vm_uui_ds: NotRequired[
        "capo_mgn.types.association_vm_uuid_list.AssociationVmUUIDList"
    ]
    """<p>The UUIDs of the source machines associated with the security group.</p>"""
    user_provided_i_ds: NotRequired[
        "capo_mgn.types.association_user_provided_id_list.AssociationUserProvidedIDList"
    ]
    """<p>The user-provided identifiers of the source machines associated with the security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupAssociations) -> dict:
    out: dict = {}
    if "cidrs" in value:
        import capo_mgn.types.association_cidr_list

        out["cidrs"] = capo_mgn.types.association_cidr_list.serialize_json(
            value["cidrs"]
        )
    if "vm_uui_ds" in value:
        import capo_mgn.types.association_vm_uuid_list

        out["vmUUIDs"] = capo_mgn.types.association_vm_uuid_list.serialize_json(
            value["vm_uui_ds"]
        )
    if "user_provided_i_ds" in value:
        import capo_mgn.types.association_user_provided_id_list

        out["userProvidedIDs"] = (
            capo_mgn.types.association_user_provided_id_list.serialize_json(
                value["user_provided_i_ds"]
            )
        )
    return out


def deserialize_json(data: dict) -> SecurityGroupAssociations:
    out: SecurityGroupAssociations = {}  # type: ignore[typeddict-item]
    if data.get("cidrs") is not None:
        import capo_mgn.types.association_cidr_list

        out["cidrs"] = capo_mgn.types.association_cidr_list.deserialize_json(
            data["cidrs"]
        )
    if data.get("vmUUIDs") is not None:
        import capo_mgn.types.association_vm_uuid_list

        out["vm_uui_ds"] = capo_mgn.types.association_vm_uuid_list.deserialize_json(
            data["vmUUIDs"]
        )
    if data.get("userProvidedIDs") is not None:
        import capo_mgn.types.association_user_provided_id_list

        out["user_provided_i_ds"] = (
            capo_mgn.types.association_user_provided_id_list.deserialize_json(
                data["userProvidedIDs"]
            )
        )
    return out
