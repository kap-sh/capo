"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MemberSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.member_abilities
    import capo_cleanrooms.types.ml_member_abilities
    import capo_cleanrooms.types.payment_configuration


class MemberSpecification(TypedDict, closed=True):
    account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.</p>"""
    member_abilities: "capo_cleanrooms.types.member_abilities.MemberAbilities"
    """<p>The abilities granted to the collaboration member.</p>"""
    ml_member_abilities: NotRequired[
        "capo_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
    ]
    """<p>The ML abilities granted to the collaboration member.</p>"""
    display_name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The member's display name.</p>"""
    payment_configuration: NotRequired[
        "capo_cleanrooms.types.payment_configuration.PaymentConfiguration"
    ]
    """<p>The collaboration member's payment responsibilities set by the collaboration creator. </p> <p>If the collaboration creator hasn't speciﬁed anyone as the member paying for query compute costs, then the member who can query is the default payer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberSpecification) -> dict:
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
    out["displayName"] = value["display_name"]
    if "payment_configuration" in value:
        import capo_cleanrooms.types.payment_configuration

        out["paymentConfiguration"] = (
            capo_cleanrooms.types.payment_configuration.serialize_json(
                value["payment_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemberSpecification:
    out: MemberSpecification = {}  # type: ignore[typeddict-item]
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
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("paymentConfiguration") is not None:
        import capo_cleanrooms.types.payment_configuration

        out["payment_configuration"] = (
            capo_cleanrooms.types.payment_configuration.deserialize_json(
                data["paymentConfiguration"]
            )
        )
    return out
