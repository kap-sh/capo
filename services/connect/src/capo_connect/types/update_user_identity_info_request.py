"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserIdentityInfoRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.user_id
    import capo_connect.types.user_identity_info


class UpdateUserIdentityInfoRequest(TypedDict, closed=True):
    identity_info: "capo_connect.types.user_identity_info.UserIdentityInfo"
    """<p>The identity information for the user.</p>"""
    user_id: "capo_connect.types.user_id.UserId"
    """<p>The identifier of the user account.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserIdentityInfoRequest) -> dict:
    out: dict = {}
    import capo_connect.types.user_identity_info

    out["IdentityInfo"] = capo_connect.types.user_identity_info.serialize_json(
        value["identity_info"]
    )
    return out


def deserialize_json(data: dict) -> UpdateUserIdentityInfoRequest:
    out: UpdateUserIdentityInfoRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentityInfo") is not None:
        import capo_connect.types.user_identity_info

        out["identity_info"] = capo_connect.types.user_identity_info.deserialize_json(
            data["IdentityInfo"]
        )
    else:
        raise DeserializationError(
            "UpdateUserIdentityInfoRequest.identity_info required"
        )
    return out
