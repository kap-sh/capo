"""Generated from Smithy shape ``com.amazonaws.organizations#CreateAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.create_account_status


class CreateAccountResponse(TypedDict, closed=True):
    create_account_status: NotRequired[
        "capo_organizations.types.create_account_status.CreateAccountStatus"
    ]
    """<p>A structure that contains details about the request to create an account. This response structure might not be fully populated when you first receive it because account creation is an asynchronous process. You can pass the returned <code>CreateAccountStatus</code> ID as a parameter to <a>DescribeCreateAccountStatus</a> to get status about the progress of the request at later times. You can also check the CloudTrail log for the <code>CreateAccountResult</code> event. For more information, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_incident-response.html">Logging and monitoring in Organizations</a> in the <i>Organizations User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccountResponse) -> dict:
    out: dict = {}
    if "create_account_status" in value:
        import capo_organizations.types.create_account_status

        out["CreateAccountStatus"] = (
            capo_organizations.types.create_account_status.serialize_aws_json_1_1(
                value["create_account_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAccountResponse:
    out: CreateAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("CreateAccountStatus") is not None:
        import capo_organizations.types.create_account_status

        out["create_account_status"] = (
            capo_organizations.types.create_account_status.deserialize_aws_json_1_1(
                data["CreateAccountStatus"]
            )
        )
    return out
