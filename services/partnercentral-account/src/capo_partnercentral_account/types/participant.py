"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#Participant``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError, SerializationError
from capo_partnercentral_account.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_account.types.account_summary
    import capo_partnercentral_account.types.partner_profile_summary
    import capo_partnercentral_account.types.seller_profile_summary


class _Participant_PartnerProfile(TypedDict, closed=True):
    PartnerProfile: "capo_partnercentral_account.types.partner_profile_summary.PartnerProfileSummary"


class _Participant_SellerProfile(TypedDict, closed=True):
    SellerProfile: (
        "capo_partnercentral_account.types.seller_profile_summary.SellerProfileSummary"
    )


class _Participant_Account(TypedDict, closed=True):
    Account: "capo_partnercentral_account.types.account_summary.AccountSummary"


Participant: TypeAlias = (
    _Participant_PartnerProfile
    | _Participant_SellerProfile
    | _Participant_Account
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Participant) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Participant: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "PartnerProfile" in value:
        import capo_partnercentral_account.types.partner_profile_summary

        return {
            "PartnerProfile": capo_partnercentral_account.types.partner_profile_summary.serialize_aws_json_1_0(
                value["PartnerProfile"]
            )
        }
    elif "SellerProfile" in value:
        import capo_partnercentral_account.types.seller_profile_summary

        return {
            "SellerProfile": capo_partnercentral_account.types.seller_profile_summary.serialize_aws_json_1_0(
                value["SellerProfile"]
            )
        }
    elif "Account" in value:
        import capo_partnercentral_account.types.account_summary

        return {
            "Account": capo_partnercentral_account.types.account_summary.serialize_aws_json_1_0(
                value["Account"]
            )
        }
    else:
        raise SerializationError("Participant: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Participant:
    if data.get("PartnerProfile") is not None:
        import capo_partnercentral_account.types.partner_profile_summary

        return {
            "PartnerProfile": capo_partnercentral_account.types.partner_profile_summary.deserialize_aws_json_1_0(
                data["PartnerProfile"]
            )
        }
    elif data.get("SellerProfile") is not None:
        import capo_partnercentral_account.types.seller_profile_summary

        return {
            "SellerProfile": capo_partnercentral_account.types.seller_profile_summary.deserialize_aws_json_1_0(
                data["SellerProfile"]
            )
        }
    elif data.get("Account") is not None:
        import capo_partnercentral_account.types.account_summary

        return {
            "Account": capo_partnercentral_account.types.account_summary.deserialize_aws_json_1_0(
                data["Account"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Participant: no recognized variant key")
