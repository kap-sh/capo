"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MemberChangeSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.member_abilities
    import capo_cleanrooms.types.ml_member_abilities
    import capo_cleanrooms.types.payment_configuration


class MemberChangeSpecification(TypedDict, closed=True):
    account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the member to add to the collaboration.</p>"""
    member_abilities: "capo_cleanrooms.types.member_abilities.MemberAbilities"
    """<p>The abilities granted to the collaboration member. These determine what actions the member can perform within the collaboration.</p> <note> <p>The following values are currently not supported: <code>CAN_QUERY</code> and <code>CAN_RUN_JOB</code>. </p> <p>Set the value of <code>memberAbilities</code> to <code>[]</code> to allow a member to contribute data.</p> <p>Set the value of <code>memberAbilities</code> to <code>[CAN_RECEIVE_RESULTS]</code> to allow a member to contribute data and receive results.</p> <p>Set the value of <code>memberAbilities</code> to <code>[CAN_EXPORT_QUERY_ANALYSIS_LOG]</code> so that the member can export the analysis logs for a protected query. Having this ability isn't sufficient on its own: You can export logs only for queries that you ran or paid for.</p> </note>"""
    ml_member_abilities: NotRequired[
        "capo_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
    ]
    payment_configuration: NotRequired[
        "capo_cleanrooms.types.payment_configuration.PaymentConfiguration"
    ]
    display_name: NotRequired["capo_cleanrooms.types.display_name.DisplayName"]
    """<p>Specifies the display name that will be shown for this member in the collaboration. While this field is required when inviting new members, it becomes optional when modifying abilities of existing collaboration members. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberChangeSpecification) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_cleanrooms.types.member_abilities

    out["memberAbilities"] = capo_cleanrooms.types.member_abilities.serialize_json(
        value["member_abilities"]
    )
    if "ml_member_abilities" in value:
        import capo_cleanrooms.types.ml_member_abilities

        out["mlMemberAbilities"] = (
            capo_cleanrooms.types.ml_member_abilities.serialize_json(
                value["ml_member_abilities"]
            )
        )
    if "payment_configuration" in value:
        import capo_cleanrooms.types.payment_configuration

        out["paymentConfiguration"] = (
            capo_cleanrooms.types.payment_configuration.serialize_json(
                value["payment_configuration"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> MemberChangeSpecification:
    out: MemberChangeSpecification = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("memberAbilities") is not None:
        import capo_cleanrooms.types.member_abilities

        out["member_abilities"] = (
            capo_cleanrooms.types.member_abilities.deserialize_json(
                data["memberAbilities"]
            )
        )
    else:
        out["member_abilities"] = []
    if data.get("mlMemberAbilities") is not None:
        import capo_cleanrooms.types.ml_member_abilities

        out["ml_member_abilities"] = (
            capo_cleanrooms.types.ml_member_abilities.deserialize_json(
                data["mlMemberAbilities"]
            )
        )
    if data.get("paymentConfiguration") is not None:
        import capo_cleanrooms.types.payment_configuration

        out["payment_configuration"] = (
            capo_cleanrooms.types.payment_configuration.deserialize_json(
                data["paymentConfiguration"]
            )
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    return out
