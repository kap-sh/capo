"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MemberSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.member_abilities
    import capo_cleanrooms.types.member_status
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.ml_member_abilities
    import capo_cleanrooms.types.payment_configuration
    import capo_cleanrooms.types.uuid


class MemberSummary(TypedDict, closed=True):
    account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.</p>"""
    status: "capo_cleanrooms.types.member_status.MemberStatus"
    """<p>The status of the member. </p>"""
    display_name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The member's display name.</p>"""
    abilities: "capo_cleanrooms.types.member_abilities.MemberAbilities"
    """<p>The abilities granted to the collaboration member.</p>"""
    ml_abilities: NotRequired[
        "capo_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
    ]
    """<p>Provides a summary of the ML abilities for the collaboration member.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the member was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the member metadata was last updated.</p>"""
    membership_id: NotRequired["capo_cleanrooms.types.uuid.UUID"]
    """<p>The unique ID for the member's associated membership, if present.</p>"""
    membership_arn: NotRequired["capo_cleanrooms.types.membership_arn.MembershipArn"]
    """<p>The unique ARN for the member's associated membership, if present.</p>"""
    payment_configuration: (
        "capo_cleanrooms.types.payment_configuration.PaymentConfiguration"
    )
    """<p>The collaboration member's payment responsibilities set by the collaboration creator. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberSummary) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["status"] = value["status"]
    out["displayName"] = value["display_name"]
    import capo_cleanrooms.types.member_abilities

    out["abilities"] = capo_cleanrooms.types.member_abilities.serialize_json(
        value["abilities"]
    )
    if "ml_abilities" in value:
        import capo_cleanrooms.types.ml_member_abilities

        out["mlAbilities"] = capo_cleanrooms.types.ml_member_abilities.serialize_json(
            value["ml_abilities"]
        )
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    if "membership_id" in value:
        out["membershipId"] = value["membership_id"]
    if "membership_arn" in value:
        out["membershipArn"] = value["membership_arn"]
    import capo_cleanrooms.types.payment_configuration

    out["paymentConfiguration"] = (
        capo_cleanrooms.types.payment_configuration.serialize_json(
            value["payment_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> MemberSummary:
    out: MemberSummary = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("abilities") is not None:
        import capo_cleanrooms.types.member_abilities

        out["abilities"] = capo_cleanrooms.types.member_abilities.deserialize_json(
            data["abilities"]
        )
    else:
        out["abilities"] = []
    if data.get("mlAbilities") is not None:
        import capo_cleanrooms.types.ml_member_abilities

        out["ml_abilities"] = (
            capo_cleanrooms.types.ml_member_abilities.deserialize_json(
                data["mlAbilities"]
            )
        )
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    if data.get("paymentConfiguration") is not None:
        import capo_cleanrooms.types.payment_configuration

        out["payment_configuration"] = (
            capo_cleanrooms.types.payment_configuration.deserialize_json(
                data["paymentConfiguration"]
            )
        )
    else:
        raise DeserializationError("MemberSummary.payment_configuration required")
    return out
