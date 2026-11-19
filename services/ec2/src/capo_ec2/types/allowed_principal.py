"""Generated from Smithy shape ``com.amazonaws.ec2#AllowedPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.permission_type
    import capo_ec2.types.principal_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class AllowedPrincipal(TypedDict, closed=True):
    principal_type: NotRequired["capo_ec2.types.principal_type.PrincipalType"]
    """<p>The type of principal.</p>"""
    principal: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the principal.</p>"""
    service_permission_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the service permission.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    service_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the service.</p>"""
    permission_type: NotRequired["capo_ec2.types.permission_type.PermissionType"]
    """<p>The type of permission granted to the principal.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AllowedPrincipal, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "principal_type" in value:
        import capo_ec2.types.principal_type

        capo_ec2.types.principal_type.serialize_ec2_query(
            value["principal_type"], pairs, f"{key_prefix}PrincipalType"
        )
    if "principal" in value:
        pairs.append((f"{key_prefix}Principal", str(value["principal"])))
    if "service_permission_id" in value:
        pairs.append(
            (f"{key_prefix}ServicePermissionId", str(value["service_permission_id"]))
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "service_id" in value:
        pairs.append((f"{key_prefix}ServiceId", str(value["service_id"])))
    if "permission_type" in value:
        import capo_ec2.types.permission_type

        capo_ec2.types.permission_type.serialize_ec2_query(
            value["permission_type"], pairs, f"{key_prefix}PermissionType"
        )


def deserialize_ec2_query(el: Element) -> AllowedPrincipal:
    out: AllowedPrincipal = {}  # type: ignore[typeddict-item]
    child_principal_type = el.find("principalType")
    if child_principal_type is not None:
        import capo_ec2.types.principal_type

        out["principal_type"] = capo_ec2.types.principal_type.deserialize_ec2_query(
            child_principal_type
        )
    child_principal = el.find("principal")
    if child_principal is not None:
        out["principal"] = str(child_principal.text or "")
    child_service_permission_id = el.find("servicePermissionId")
    if child_service_permission_id is not None:
        out["service_permission_id"] = str(child_service_permission_id.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_service_id = el.find("serviceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    child_permission_type = el.find("permissionType")
    if child_permission_type is not None:
        import capo_ec2.types.permission_type

        out["permission_type"] = capo_ec2.types.permission_type.deserialize_ec2_query(
            child_permission_type
        )
    return out
