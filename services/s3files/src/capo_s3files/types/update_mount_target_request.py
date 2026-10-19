"""Generated from Smithy shape ``com.amazonaws.s3files#UpdateMountTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.mount_target_id
    import capo_s3files.types.security_groups


class UpdateMountTargetRequest(TypedDict, closed=True):
    mount_target_id: "capo_s3files.types.mount_target_id.MountTargetId"
    """<p>The ID of the mount target to update.</p>"""
    security_groups: "capo_s3files.types.security_groups.SecurityGroups"
    """<p>An array of VPC security group IDs to associate with the mount target's network interface. This replaces the existing security groups. All security groups must belong to the same VPC as the mount target's subnet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMountTargetRequest) -> dict:
    out: dict = {}
    import capo_s3files.types.security_groups

    out["securityGroups"] = capo_s3files.types.security_groups.serialize_json(
        value["security_groups"]
    )
    return out


def deserialize_json(data: dict) -> UpdateMountTargetRequest:
    out: UpdateMountTargetRequest = {}  # type: ignore[typeddict-item]
    if data.get("securityGroups") is not None:
        import capo_s3files.types.security_groups

        out["security_groups"] = capo_s3files.types.security_groups.deserialize_json(
            data["securityGroups"]
        )
    else:
        out["security_groups"] = []
    return out
