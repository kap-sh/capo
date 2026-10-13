"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsTeamMember``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_member_business_title
    import capo_partnercentral_selling.types.email
    import capo_partnercentral_selling.types.name


class AwsTeamMember(TypedDict, closed=True):
    email: NotRequired["capo_partnercentral_selling.types.email.Email"]
    """<p>Provides the Amazon Web Services team member's email address.</p>"""
    first_name: NotRequired["capo_partnercentral_selling.types.name.Name"]
    """<p>Provides the Amazon Web Services team member's first name.</p>"""
    last_name: NotRequired["capo_partnercentral_selling.types.name.Name"]
    """<p>Provides the Amazon Web Services team member's last name.</p>"""
    business_title: NotRequired[
        "capo_partnercentral_selling.types.aws_member_business_title.AwsMemberBusinessTitle"
    ]
    """<p>Specifies the Amazon Web Services team member's business title and indicates their organizational role.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsTeamMember) -> dict:
    out: dict = {}
    if "email" in value:
        out["Email"] = value["email"]
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "business_title" in value:
        import capo_partnercentral_selling.types.aws_member_business_title

        out["BusinessTitle"] = (
            capo_partnercentral_selling.types.aws_member_business_title.serialize_aws_json_1_0(
                value["business_title"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsTeamMember:
    out: AwsTeamMember = {}  # type: ignore[typeddict-item]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    if data.get("BusinessTitle") is not None:
        import capo_partnercentral_selling.types.aws_member_business_title

        out["business_title"] = (
            capo_partnercentral_selling.types.aws_member_business_title.deserialize_aws_json_1_0(
                data["BusinessTitle"]
            )
        )
    return out


def redact_sensitive(value: AwsTeamMember) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    return out
