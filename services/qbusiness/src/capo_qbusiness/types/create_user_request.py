"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.string
    import capo_qbusiness.types.user_aliases


class CreateUserRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application for which the user mapping will be created.</p>"""
    user_id: "capo_qbusiness.types.string.String"
    """<p>The user emails attached to a user mapping.</p>"""
    user_aliases: NotRequired["capo_qbusiness.types.user_aliases.UserAliases"]
    """<p>The list of user aliases in the mapping.</p>"""
    client_token: NotRequired["capo_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the request to create your Amazon Q Business user mapping.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserRequest) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    if "user_aliases" in value:
        import capo_qbusiness.types.user_aliases

        out["userAliases"] = capo_qbusiness.types.user_aliases.serialize_json(
            value["user_aliases"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    if data.get("userAliases") is not None:
        import capo_qbusiness.types.user_aliases

        out["user_aliases"] = capo_qbusiness.types.user_aliases.deserialize_json(
            data["userAliases"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
