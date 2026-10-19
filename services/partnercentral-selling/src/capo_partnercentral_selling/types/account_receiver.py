"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AccountReceiver``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.alias
    import capo_partnercentral_selling.types.aws_account


class AccountReceiver(TypedDict, closed=True):
    alias: NotRequired["capo_partnercentral_selling.types.alias.Alias"]
    """<p>Represents the alias of the partner account receiving the Engagement Invitation, making it easier to identify and track the recipient in reports or logs.</p>"""
    aws_account_id: "capo_partnercentral_selling.types.aws_account.AwsAccount"
    """<p>Indicates the AWS account ID of the partner who received the Engagement Invitation. This is a unique identifier for managing engagements with specific AWS accounts.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountReceiver) -> dict:
    out: dict = {}
    if "alias" in value:
        out["Alias"] = value["alias"]
    out["AwsAccountId"] = value["aws_account_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountReceiver:
    out: AccountReceiver = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    if data.get("AwsAccountId") is not None:
        out["aws_account_id"] = data["AwsAccountId"]
    else:
        out["aws_account_id"] = ""
    return out


def redact_sensitive(value: AccountReceiver) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "alias" in value:
        out["alias"] = "*** Sensitive Data Redacted ***"
    if "aws_account_id" in value:
        out["aws_account_id"] = "*** Sensitive Data Redacted ***"
    return out
