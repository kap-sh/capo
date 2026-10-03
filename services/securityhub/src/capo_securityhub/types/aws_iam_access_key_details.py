"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamAccessKeyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_iam_access_key_session_context
    import capo_securityhub.types.aws_iam_access_key_status
    import capo_securityhub.types.non_empty_string


class AwsIamAccessKeyDetails(TypedDict, closed=True):
    user_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The user associated with the IAM access key related to a finding.</p> <p>The <code>UserName</code> parameter has been replaced with the <code>PrincipalName</code> parameter because access keys can also be assigned to principals that are not IAM users.</p>"""
    status: NotRequired[
        "capo_securityhub.types.aws_iam_access_key_status.AwsIamAccessKeyStatus"
    ]
    """<p>The status of the IAM access key related to a finding.</p>"""
    created_at: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the IAM access key was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    principal_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the principal associated with an access key.</p>"""
    principal_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of principal associated with an access key.</p>"""
    principal_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the principal.</p>"""
    account_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services account ID of the account for the key.</p>"""
    access_key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the access key.</p>"""
    session_context: NotRequired[
        "capo_securityhub.types.aws_iam_access_key_session_context.AwsIamAccessKeySessionContext"
    ]
    """<p>Information about the session that the key was used for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamAccessKeyDetails) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "status" in value:
        import capo_securityhub.types.aws_iam_access_key_status

        out["Status"] = capo_securityhub.types.aws_iam_access_key_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        out["CreatedAt"] = value["created_at"]
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    if "principal_type" in value:
        out["PrincipalType"] = value["principal_type"]
    if "principal_name" in value:
        out["PrincipalName"] = value["principal_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "access_key_id" in value:
        out["AccessKeyId"] = value["access_key_id"]
    if "session_context" in value:
        import capo_securityhub.types.aws_iam_access_key_session_context

        out["SessionContext"] = (
            capo_securityhub.types.aws_iam_access_key_session_context.serialize_json(
                value["session_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsIamAccessKeyDetails:
    out: AwsIamAccessKeyDetails = {}  # type: ignore[typeddict-item]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("Status") is not None:
        import capo_securityhub.types.aws_iam_access_key_status

        out["status"] = (
            capo_securityhub.types.aws_iam_access_key_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("CreatedAt") is not None:
        out["created_at"] = data["CreatedAt"]
    if data.get("PrincipalId") is not None:
        out["principal_id"] = data["PrincipalId"]
    if data.get("PrincipalType") is not None:
        out["principal_type"] = data["PrincipalType"]
    if data.get("PrincipalName") is not None:
        out["principal_name"] = data["PrincipalName"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("AccessKeyId") is not None:
        out["access_key_id"] = data["AccessKeyId"]
    if data.get("SessionContext") is not None:
        import capo_securityhub.types.aws_iam_access_key_session_context

        out["session_context"] = (
            capo_securityhub.types.aws_iam_access_key_session_context.deserialize_json(
                data["SessionContext"]
            )
        )
    return out
