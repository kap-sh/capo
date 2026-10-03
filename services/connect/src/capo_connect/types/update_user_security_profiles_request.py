"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserSecurityProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.security_profile_ids
    import capo_connect.types.user_id


class UpdateUserSecurityProfilesRequest(TypedDict, closed=True):
    security_profile_ids: "capo_connect.types.security_profile_ids.SecurityProfileIds"
    """<p>The identifiers of the security profiles for the user.</p>"""
    user_id: "capo_connect.types.user_id.UserId"
    """<p>The identifier of the user account.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserSecurityProfilesRequest) -> dict:
    out: dict = {}
    import capo_connect.types.security_profile_ids

    out["SecurityProfileIds"] = capo_connect.types.security_profile_ids.serialize_json(
        value["security_profile_ids"]
    )
    return out


def deserialize_json(data: dict) -> UpdateUserSecurityProfilesRequest:
    out: UpdateUserSecurityProfilesRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecurityProfileIds") is not None:
        import capo_connect.types.security_profile_ids

        out["security_profile_ids"] = (
            capo_connect.types.security_profile_ids.deserialize_json(
                data["SecurityProfileIds"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateUserSecurityProfilesRequest.security_profile_ids required"
        )
    return out
