"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateAccountSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.account_name
    import capo_quicksight.types.authentication_method_option
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.edition
    import capo_quicksight.types.groups_list
    import capo_quicksight.types.string


class CreateAccountSubscriptionRequest(TypedDict, closed=True):
    edition: NotRequired["capo_quicksight.types.edition.Edition"]
    """<p>The edition of Amazon Quick Sight that you want your account to have. Currently, you can choose from <code>ENTERPRISE</code> or <code>ENTERPRISE_AND_Q</code>.</p> <p>If you choose <code>ENTERPRISE_AND_Q</code>, the following parameters are required:</p> <ul> <li> <p> <code>FirstName</code> </p> </li> <li> <p> <code>LastName</code> </p> </li> <li> <p> <code>EmailAddress</code> </p> </li> <li> <p> <code>ContactNumber</code> </p> </li> </ul>"""
    authentication_method: (
        "capo_quicksight.types.authentication_method_option.AuthenticationMethodOption"
    )
    """<p>The method that you want to use to authenticate your Quick Sight account.</p> <p>If you choose <code>ACTIVE_DIRECTORY</code>, provide an <code>ActiveDirectoryName</code> and an <code>AdminGroup</code> associated with your Active Directory.</p> <p>If you choose <code>IAM_IDENTITY_CENTER</code>, provide an <code>AdminGroup</code> associated with your IAM Identity Center account.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the account that you're using to create your Quick Sight account.</p>"""
    account_name: "capo_quicksight.types.account_name.AccountName"
    """<p>The name of your Amazon Quick Sight account. This name is unique over all of Amazon Web Services, and it appears only when users sign in. You can't change <code>AccountName</code> value after the Amazon Quick Sight account is created.</p>"""
    notification_email: "capo_quicksight.types.string.String"
    """<p>The email address that you want Quick Sight to send notifications to regarding your Quick Sight account or Quick Sight subscription.</p>"""
    active_directory_name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The name of your Active Directory. This field is required if <code>ACTIVE_DIRECTORY</code> is the selected authentication method of the new Quick Sight account.</p>"""
    realm: NotRequired["capo_quicksight.types.string.String"]
    """<p>The realm of the Active Directory that is associated with your Quick Sight account. This field is required if <code>ACTIVE_DIRECTORY</code> is the selected authentication method of the new Quick Sight account.</p>"""
    directory_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The ID of the Active Directory that is associated with your Quick Sight account.</p>"""
    admin_group: NotRequired["capo_quicksight.types.groups_list.GroupsList"]
    """<p>The admin group associated with your Active Directory or IAM Identity Center account. Either this field or the <code>AdminProGroup</code> field is required if <code>ACTIVE_DIRECTORY</code> or <code>IAM_IDENTITY_CENTER</code> is the selected authentication method of the new Quick Sight account.</p> <p>For more information about using IAM Identity Center in Amazon Quick Sight, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html">Using IAM Identity Center with Amazon Quick Sight Enterprise Edition</a> in the Amazon Quick Sight User Guide. For more information about using Active Directory in Amazon Quick Sight, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html">Using Active Directory with Amazon Quick Sight Enterprise Edition</a> in the Amazon Quick Sight User Guide.</p>"""
    author_group: NotRequired["capo_quicksight.types.groups_list.GroupsList"]
    """<p>The author group associated with your Active Directory or IAM Identity Center account.</p> <p>For more information about using IAM Identity Center in Amazon Quick Sight, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html">Using IAM Identity Center with Amazon Quick Sight Enterprise Edition</a> in the Amazon Quick Sight User Guide. For more information about using Active Directory in Amazon Quick Sight, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html">Using Active Directory with Amazon Quick Sight Enterprise Edition</a> in the Amazon Quick Sight User Guide.</p>"""
    reader_group: NotRequired["capo_quicksight.types.groups_list.GroupsList"]
    """<p>The reader group associated with your Active Directory or IAM Identity Center account.</p> <p>For more information about using IAM Identity Center in Amazon Quick Sight, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html">Using IAM Identity Center with Amazon Quick Sight Enterprise Edition</a> in the Amazon Quick Sight User Guide. For more information about using Active Directory in Amazon Quick Sight, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html">Using Active Directory with Amazon Quick Sight Enterprise Edition</a> in the Amazon Quick Sight User Guide.</p>"""
    admin_pro_group: NotRequired["capo_quicksight.types.groups_list.GroupsList"]
    """<p>The admin pro group associated with your Active Directory or IAM Identity Center account. Either this field or the <code>AdminGroup</code> field is required if <code>ACTIVE_DIRECTORY</code> or <code>IAM_IDENTITY_CENTER</code> is the selected authentication method of the new Quick Sight account.</p> <p>For more information about using IAM Identity Center in Amazon Quick Sight, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html">Using IAM Identity Center with Amazon Quick Sight Enterprise Edition</a> in the Amazon Quick Sight User Guide. For more information about using Active Directory in Amazon Quick Sight, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html">Using Active Directory with Amazon Quick Sight Enterprise Edition</a> in the Amazon Quick Sight User Guide.</p>"""
    author_pro_group: NotRequired["capo_quicksight.types.groups_list.GroupsList"]
    """<p>The author pro group associated with your Active Directory or IAM Identity Center account.</p> <p>For more information about using IAM Identity Center in Amazon Quick Sight, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html">Using IAM Identity Center with Amazon Quick Sight Enterprise Edition</a> in the Amazon Quick Sight User Guide. For more information about using Active Directory in Amazon Quick Sight, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html">Using Active Directory with Amazon Quick Sight Enterprise Edition</a> in the Amazon Quick Sight User Guide.</p>"""
    reader_pro_group: NotRequired["capo_quicksight.types.groups_list.GroupsList"]
    """<p>The reader pro group associated with your Active Directory or IAM Identity Center account.</p> <p>For more information about using IAM Identity Center in Amazon Quick Sight, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html">Using IAM Identity Center with Amazon Quick Sight Enterprise Edition</a> in the Amazon Quick Sight User Guide. For more information about using Active Directory in Amazon Quick Sight, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html">Using Active Directory with Amazon Quick Sight Enterprise Edition</a> in the Amazon Quick Sight User Guide.</p>"""
    first_name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The first name of the author of the Amazon Quick Sight account to use for future communications. This field is required if <code>ENTERPPRISE_AND_Q</code> is the selected edition of the new Amazon Quick Sight account.</p>"""
    last_name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The last name of the author of the Amazon Quick Sight account to use for future communications. This field is required if <code>ENTERPPRISE_AND_Q</code> is the selected edition of the new Amazon Quick Sight account.</p>"""
    email_address: NotRequired["capo_quicksight.types.string.String"]
    """<p>The email address of the author of the Amazon Quick Sight account to use for future communications. This field is required if <code>ENTERPPRISE_AND_Q</code> is the selected edition of the new Amazon Quick Sight account.</p>"""
    contact_number: NotRequired["capo_quicksight.types.string.String"]
    """<p>A 10-digit phone number for the author of the Amazon Quick Sight account to use for future communications. This field is required if <code>ENTERPPRISE_AND_Q</code> is the selected edition of the new Amazon Quick Sight account.</p>"""
    iam_identity_center_instance_arn: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the IAM Identity Center instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccountSubscriptionRequest) -> dict:
    out: dict = {}
    if "edition" in value:
        import capo_quicksight.types.edition

        out["Edition"] = capo_quicksight.types.edition.serialize_json(value["edition"])
    import capo_quicksight.types.authentication_method_option

    out["AuthenticationMethod"] = (
        capo_quicksight.types.authentication_method_option.serialize_json(
            value["authentication_method"]
        )
    )
    out["AccountName"] = value["account_name"]
    out["NotificationEmail"] = value["notification_email"]
    if "active_directory_name" in value:
        out["ActiveDirectoryName"] = value["active_directory_name"]
    if "realm" in value:
        out["Realm"] = value["realm"]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "admin_group" in value:
        import capo_quicksight.types.groups_list

        out["AdminGroup"] = capo_quicksight.types.groups_list.serialize_json(
            value["admin_group"]
        )
    if "author_group" in value:
        import capo_quicksight.types.groups_list

        out["AuthorGroup"] = capo_quicksight.types.groups_list.serialize_json(
            value["author_group"]
        )
    if "reader_group" in value:
        import capo_quicksight.types.groups_list

        out["ReaderGroup"] = capo_quicksight.types.groups_list.serialize_json(
            value["reader_group"]
        )
    if "admin_pro_group" in value:
        import capo_quicksight.types.groups_list

        out["AdminProGroup"] = capo_quicksight.types.groups_list.serialize_json(
            value["admin_pro_group"]
        )
    if "author_pro_group" in value:
        import capo_quicksight.types.groups_list

        out["AuthorProGroup"] = capo_quicksight.types.groups_list.serialize_json(
            value["author_pro_group"]
        )
    if "reader_pro_group" in value:
        import capo_quicksight.types.groups_list

        out["ReaderProGroup"] = capo_quicksight.types.groups_list.serialize_json(
            value["reader_pro_group"]
        )
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "contact_number" in value:
        out["ContactNumber"] = value["contact_number"]
    if "iam_identity_center_instance_arn" in value:
        out["IAMIdentityCenterInstanceArn"] = value["iam_identity_center_instance_arn"]
    return out


def deserialize_json(data: dict) -> CreateAccountSubscriptionRequest:
    out: CreateAccountSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Edition") is not None:
        import capo_quicksight.types.edition

        out["edition"] = capo_quicksight.types.edition.deserialize_json(data["Edition"])
    if data.get("AuthenticationMethod") is not None:
        import capo_quicksight.types.authentication_method_option

        out["authentication_method"] = (
            capo_quicksight.types.authentication_method_option.deserialize_json(
                data["AuthenticationMethod"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAccountSubscriptionRequest.authentication_method required"
        )
    if data.get("AccountName") is not None:
        out["account_name"] = data["AccountName"]
    else:
        raise DeserializationError(
            "CreateAccountSubscriptionRequest.account_name required"
        )
    if data.get("NotificationEmail") is not None:
        out["notification_email"] = data["NotificationEmail"]
    else:
        raise DeserializationError(
            "CreateAccountSubscriptionRequest.notification_email required"
        )
    if data.get("ActiveDirectoryName") is not None:
        out["active_directory_name"] = data["ActiveDirectoryName"]
    if data.get("Realm") is not None:
        out["realm"] = data["Realm"]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("AdminGroup") is not None:
        import capo_quicksight.types.groups_list

        out["admin_group"] = capo_quicksight.types.groups_list.deserialize_json(
            data["AdminGroup"]
        )
    if data.get("AuthorGroup") is not None:
        import capo_quicksight.types.groups_list

        out["author_group"] = capo_quicksight.types.groups_list.deserialize_json(
            data["AuthorGroup"]
        )
    if data.get("ReaderGroup") is not None:
        import capo_quicksight.types.groups_list

        out["reader_group"] = capo_quicksight.types.groups_list.deserialize_json(
            data["ReaderGroup"]
        )
    if data.get("AdminProGroup") is not None:
        import capo_quicksight.types.groups_list

        out["admin_pro_group"] = capo_quicksight.types.groups_list.deserialize_json(
            data["AdminProGroup"]
        )
    if data.get("AuthorProGroup") is not None:
        import capo_quicksight.types.groups_list

        out["author_pro_group"] = capo_quicksight.types.groups_list.deserialize_json(
            data["AuthorProGroup"]
        )
    if data.get("ReaderProGroup") is not None:
        import capo_quicksight.types.groups_list

        out["reader_pro_group"] = capo_quicksight.types.groups_list.deserialize_json(
            data["ReaderProGroup"]
        )
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    if data.get("ContactNumber") is not None:
        out["contact_number"] = data["ContactNumber"]
    if data.get("IAMIdentityCenterInstanceArn") is not None:
        out["iam_identity_center_instance_arn"] = data["IAMIdentityCenterInstanceArn"]
    return out
