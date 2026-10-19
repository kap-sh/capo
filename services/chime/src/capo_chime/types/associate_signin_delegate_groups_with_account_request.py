"""Generated from Smithy shape ``com.amazonaws.chime#AssociateSigninDelegateGroupsWithAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string
    import capo_chime.types.signin_delegate_group_list


class AssociateSigninDelegateGroupsWithAccountRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    signin_delegate_groups: (
        "capo_chime.types.signin_delegate_group_list.SigninDelegateGroupList"
    )
    """<p>The sign-in delegate groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateSigninDelegateGroupsWithAccountRequest) -> dict:
    out: dict = {}
    import capo_chime.types.signin_delegate_group_list

    out["SigninDelegateGroups"] = (
        capo_chime.types.signin_delegate_group_list.serialize_json(
            value["signin_delegate_groups"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssociateSigninDelegateGroupsWithAccountRequest:
    out: AssociateSigninDelegateGroupsWithAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("SigninDelegateGroups") is not None:
        import capo_chime.types.signin_delegate_group_list

        out["signin_delegate_groups"] = (
            capo_chime.types.signin_delegate_group_list.deserialize_json(
                data["SigninDelegateGroups"]
            )
        )
    else:
        out["signin_delegate_groups"] = []
    return out
