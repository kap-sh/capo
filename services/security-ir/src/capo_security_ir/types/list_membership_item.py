"""Generated from Smithy shape ``com.amazonaws.securityir#ListMembershipItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.aws_account_id
    import capo_security_ir.types.aws_region
    import capo_security_ir.types.membership_arn
    import capo_security_ir.types.membership_id
    import capo_security_ir.types.membership_status


class ListMembershipItem(TypedDict, closed=True):
    membership_id: "capo_security_ir.types.membership_id.MembershipId"
    """<p/>"""
    account_id: NotRequired["capo_security_ir.types.aws_account_id.AWSAccountId"]
    """<p/>"""
    region: NotRequired["capo_security_ir.types.aws_region.AwsRegion"]
    """<p/>"""
    membership_arn: NotRequired["capo_security_ir.types.membership_arn.MembershipArn"]
    """<p/>"""
    membership_status: NotRequired[
        "capo_security_ir.types.membership_status.MembershipStatus"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipItem) -> dict:
    out: dict = {}
    out["membershipId"] = value["membership_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        import capo_security_ir.types.aws_region

        out["region"] = capo_security_ir.types.aws_region.serialize_json(
            value["region"]
        )
    if "membership_arn" in value:
        out["membershipArn"] = value["membership_arn"]
    if "membership_status" in value:
        import capo_security_ir.types.membership_status

        out["membershipStatus"] = (
            capo_security_ir.types.membership_status.serialize_json(
                value["membership_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListMembershipItem:
    out: ListMembershipItem = {}  # type: ignore[typeddict-item]
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        out["membership_id"] = ""
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("region") is not None:
        import capo_security_ir.types.aws_region

        out["region"] = capo_security_ir.types.aws_region.deserialize_json(
            data["region"]
        )
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    if data.get("membershipStatus") is not None:
        import capo_security_ir.types.membership_status

        out["membership_status"] = (
            capo_security_ir.types.membership_status.deserialize_json(
                data["membershipStatus"]
            )
        )
    return out
