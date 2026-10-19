"""Generated from Smithy shape ``com.amazonaws.connect#DisassociateUserProficienciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.user_id
    import capo_connect.types.user_proficiency_disassociate_list


class DisassociateUserProficienciesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.</p>"""
    user_id: "capo_connect.types.user_id.UserId"
    """<p>The identifier of the user account.</p>"""
    user_proficiencies: "capo_connect.types.user_proficiency_disassociate_list.UserProficiencyDisassociateList"
    """<p>The proficiencies to disassociate from the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateUserProficienciesRequest) -> dict:
    out: dict = {}
    import capo_connect.types.user_proficiency_disassociate_list

    out["UserProficiencies"] = (
        capo_connect.types.user_proficiency_disassociate_list.serialize_json(
            value["user_proficiencies"]
        )
    )
    return out


def deserialize_json(data: dict) -> DisassociateUserProficienciesRequest:
    out: DisassociateUserProficienciesRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserProficiencies") is not None:
        import capo_connect.types.user_proficiency_disassociate_list

        out["user_proficiencies"] = (
            capo_connect.types.user_proficiency_disassociate_list.deserialize_json(
                data["UserProficiencies"]
            )
        )
    else:
        out["user_proficiencies"] = []
    return out
