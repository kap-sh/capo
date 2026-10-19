"""Generated from Smithy shape ``com.amazonaws.chime#DisassociateSigninDelegateGroupsFromAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string
    import capo_chime.types.non_empty_string_list


class DisassociateSigninDelegateGroupsFromAccountRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    group_names: "capo_chime.types.non_empty_string_list.NonEmptyStringList"
    """<p>The sign-in delegate group names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateSigninDelegateGroupsFromAccountRequest) -> dict:
    out: dict = {}
    import capo_chime.types.non_empty_string_list

    out["GroupNames"] = capo_chime.types.non_empty_string_list.serialize_json(
        value["group_names"]
    )
    return out


def deserialize_json(data: dict) -> DisassociateSigninDelegateGroupsFromAccountRequest:
    out: DisassociateSigninDelegateGroupsFromAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("GroupNames") is not None:
        import capo_chime.types.non_empty_string_list

        out["group_names"] = capo_chime.types.non_empty_string_list.deserialize_json(
            data["GroupNames"]
        )
    else:
        out["group_names"] = []
    return out
