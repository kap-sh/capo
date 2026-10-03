"""Generated from Smithy shape ``com.amazonaws.organizations#CreateAccountStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.account_id
    import capo_organizations.types.create_account_failure_reason
    import capo_organizations.types.create_account_name
    import capo_organizations.types.create_account_request_id
    import capo_organizations.types.create_account_state
    import capo_organizations.types.timestamp


class CreateAccountStatus(TypedDict, closed=True):
    id: NotRequired[
        "capo_organizations.types.create_account_request_id.CreateAccountRequestId"
    ]
    """<p>The unique identifier (ID) that references this request. You get this value from the response of the initial <a>CreateAccount</a> request to create the account.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a create account request ID string requires "car-" followed by from 8 to 32 lowercase letters or digits.</p>"""
    account_name: NotRequired[
        "capo_organizations.types.create_account_name.CreateAccountName"
    ]
    """<p>The account name given to the account when it was created.</p>"""
    state: NotRequired[
        "capo_organizations.types.create_account_state.CreateAccountState"
    ]
    """<p>The status of the asynchronous request to create an Amazon Web Services account.</p>"""
    requested_timestamp: NotRequired["capo_organizations.types.timestamp.Timestamp"]
    """<p>The date and time that the request was made for the account creation.</p>"""
    completed_timestamp: NotRequired["capo_organizations.types.timestamp.Timestamp"]
    """<p>The date and time that the account was created and the request completed.</p>"""
    account_id: NotRequired["capo_organizations.types.account_id.AccountId"]
    """<p>If the account was created successfully, the unique identifier (ID) of the new account.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for an account ID string requires exactly 12 digits.</p>"""
    gov_cloud_account_id: NotRequired["capo_organizations.types.account_id.AccountId"]
    """<p>If the account was created successfully, the ID for the new account in the Amazon Web Services GovCloud (US) Region.</p>"""
    failure_reason: NotRequired[
        "capo_organizations.types.create_account_failure_reason.CreateAccountFailureReason"
    ]
    """<p>If the request failed, a description of the reason for the failure.</p> <ul> <li> <p>ACCOUNT_LIMIT_EXCEEDED: The account couldn't be created because you reached the limit on the number of accounts in your organization.</p> </li> <li> <p>CONCURRENT_ACCOUNT_MODIFICATION: You already submitted a request with the same information.</p> </li> <li> <p>EMAIL_ALREADY_EXISTS: The account could not be created because another Amazon Web Services account with that email address already exists.</p> </li> <li> <p>FAILED_BUSINESS_VALIDATION: The Amazon Web Services account that owns your organization failed to receive business license validation.</p> </li> <li> <p>GOVCLOUD_ACCOUNT_ALREADY_EXISTS: The account in the Amazon Web Services GovCloud (US) Region could not be created because this Region already includes an account with that email address.</p> </li> <li> <p>IDENTITY_INVALID_BUSINESS_VALIDATION: The Amazon Web Services account that owns your organization can't complete business license validation because it doesn't have valid identity data.</p> </li> <li> <p>INVALID_ADDRESS: The account could not be created because the address you provided is not valid.</p> </li> <li> <p>INVALID_EMAIL: The account could not be created because the email address you provided is not valid.</p> </li> <li> <p>INVALID_PAYMENT_INSTRUMENT: The Amazon Web Services account that owns your organization does not have a supported payment method associated with the account. Amazon Web Services does not support cards issued by financial institutions in Russia or Belarus. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-general.html">Managing your Amazon Web Services payments</a>.</p> </li> <li> <p>INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Amazon Web Services Customer Support.</p> </li> <li> <p>MISSING_BUSINESS_VALIDATION: The Amazon Web Services account that owns your organization has not received Business Validation.</p> </li> <li> <p> MISSING_PAYMENT_INSTRUMENT: You must configure the management account with a valid payment method, such as a credit card.</p> </li> <li> <p>PENDING_BUSINESS_VALIDATION: The Amazon Web Services account that owns your organization is still in the process of completing business license validation.</p> </li> <li> <p>UNKNOWN_BUSINESS_VALIDATION: The Amazon Web Services account that owns your organization has an unknown issue with business license validation.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccountStatus) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "account_name" in value:
        out["AccountName"] = value["account_name"]
    if "state" in value:
        import capo_organizations.types.create_account_state

        out["State"] = (
            capo_organizations.types.create_account_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "requested_timestamp" in value:
        import capo_organizations.types.timestamp

        out["RequestedTimestamp"] = (
            capo_organizations.types.timestamp.serialize_aws_json_1_1(
                value["requested_timestamp"]
            )
        )
    if "completed_timestamp" in value:
        import capo_organizations.types.timestamp

        out["CompletedTimestamp"] = (
            capo_organizations.types.timestamp.serialize_aws_json_1_1(
                value["completed_timestamp"]
            )
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "gov_cloud_account_id" in value:
        out["GovCloudAccountId"] = value["gov_cloud_account_id"]
    if "failure_reason" in value:
        import capo_organizations.types.create_account_failure_reason

        out["FailureReason"] = (
            capo_organizations.types.create_account_failure_reason.serialize_aws_json_1_1(
                value["failure_reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAccountStatus:
    out: CreateAccountStatus = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("AccountName") is not None:
        out["account_name"] = data["AccountName"]
    if data.get("State") is not None:
        import capo_organizations.types.create_account_state

        out["state"] = (
            capo_organizations.types.create_account_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if data.get("RequestedTimestamp") is not None:
        import capo_organizations.types.timestamp

        out["requested_timestamp"] = (
            capo_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["RequestedTimestamp"]
            )
        )
    if data.get("CompletedTimestamp") is not None:
        import capo_organizations.types.timestamp

        out["completed_timestamp"] = (
            capo_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["CompletedTimestamp"]
            )
        )
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("GovCloudAccountId") is not None:
        out["gov_cloud_account_id"] = data["GovCloudAccountId"]
    if data.get("FailureReason") is not None:
        import capo_organizations.types.create_account_failure_reason

        out["failure_reason"] = (
            capo_organizations.types.create_account_failure_reason.deserialize_aws_json_1_1(
                data["FailureReason"]
            )
        )
    return out
