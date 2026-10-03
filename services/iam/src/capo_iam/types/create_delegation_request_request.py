"""Generated from Smithy shape ``com.amazonaws.iam#CreateDelegationRequestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.account_id_type
    import capo_iam.types.boolean_type
    import capo_iam.types.delegation_permission
    import capo_iam.types.delegation_request_description_type
    import capo_iam.types.notification_channel_type
    import capo_iam.types.redirect_url_type
    import capo_iam.types.request_message_type
    import capo_iam.types.requestor_workflow_id_type
    import capo_iam.types.session_duration_type


class CreateDelegationRequestRequest(TypedDict, closed=True):
    owner_account_id: NotRequired["capo_iam.types.account_id_type.accountIdType"]
    """<p>The Amazon Web Services account ID this delegation request is targeted to.</p> <p>If the account ID is not known, this parameter can be omitted, resulting in a request that can be associated by any account. If the account ID passed, then the created delegation request can only be associated with an identity of that target account.</p>"""
    description: "capo_iam.types.delegation_request_description_type.delegationRequestDescriptionType"
    """<p>A description of the delegation request.</p>"""
    permissions: "capo_iam.types.delegation_permission.DelegationPermission"
    """<p>The permissions to be delegated in this delegation request.</p>"""
    request_message: NotRequired[
        "capo_iam.types.request_message_type.requestMessageType"
    ]
    """<p>A message explaining the reason for the delegation request.</p> <p>Requesters can utilize this field to add a custom note to the delegation request. This field is different from the description such that this is to be utilized for a custom messaging on a case-by-case basis.</p> <p>For example, if the current delegation request is in response to a previous request being rejected, this explanation can be added to the request via this field.</p>"""
    requestor_workflow_id: (
        "capo_iam.types.requestor_workflow_id_type.requestorWorkflowIdType"
    )
    """<p>The workflow ID associated with the requestor.</p> <p>This is the unique identifier on the partner side that can be used to track the progress of the request.</p> <p>IAM maintains a uniqueness check on this workflow id for each request - if a workflow id for an existing request is passed, this API call will fail.</p>"""
    redirect_url: NotRequired["capo_iam.types.redirect_url_type.redirectUrlType"]
    """<p>The URL to redirect to after the delegation request is processed.</p> <p>This URL is used by the IAM console to show a link to the customer to re-load the partner workflow.</p>"""
    notification_channel: (
        "capo_iam.types.notification_channel_type.notificationChannelType"
    )
    """<p>The notification channel for updates about the delegation request.</p> <p>At this time,only SNS topic ARNs are accepted for notification. This topic ARN must have a resource policy granting <code>SNS:Publish</code> permission to the IAM service principal (<code>iam.amazonaws.com</code>). See <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation-partner-guide.html">partner onboarding documentation</a> for more details. </p>"""
    session_duration: "capo_iam.types.session_duration_type.sessionDurationType"
    """<p>The duration for which the delegated session should remain active, in seconds.</p> <p>The active time window for the session starts when the customer calls the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_SendDelegationToken.html">SendDelegationToken</a> API.</p>"""
    only_send_by_owner: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether the delegation token should only be sent by the owner.</p> <p>This flag prevents any party other than the owner from calling <code>SendDelegationToken</code> API for this delegation request. This behavior becomes useful when the delegation request owner needs to be present for subsequent partner interactions, but the delegation request was sent to a more privileged user for approval due to the owner lacking sufficient delegation permissions. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDelegationRequestRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "owner_account_id" in value:
        pairs.append((f"{key_prefix}OwnerAccountId", str(value["owner_account_id"])))
    pairs.append((f"{key_prefix}Description", str(value["description"])))
    import capo_iam.types.delegation_permission

    capo_iam.types.delegation_permission.serialize_query(
        value["permissions"], pairs, f"{key_prefix}Permissions"
    )
    if "request_message" in value:
        pairs.append((f"{key_prefix}RequestMessage", str(value["request_message"])))
    pairs.append(
        (f"{key_prefix}RequestorWorkflowId", str(value["requestor_workflow_id"]))
    )
    if "redirect_url" in value:
        pairs.append((f"{key_prefix}RedirectUrl", str(value["redirect_url"])))
    pairs.append(
        (f"{key_prefix}NotificationChannel", str(value["notification_channel"]))
    )
    pairs.append((f"{key_prefix}SessionDuration", str(value["session_duration"])))
    pairs.append(
        (
            f"{key_prefix}OnlySendByOwner",
            "true" if value.get("only_send_by_owner", False) else "false",
        )
    )


def deserialize_query(el: Element) -> CreateDelegationRequestRequest:
    out: CreateDelegationRequestRequest = {}  # type: ignore[typeddict-item]
    child_owner_account_id = el.find("OwnerAccountId")
    if child_owner_account_id is not None:
        out["owner_account_id"] = str(child_owner_account_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    else:
        raise DeserializationError(
            "CreateDelegationRequestRequest.description required"
        )
    child_permissions = el.find("Permissions")
    if child_permissions is not None:
        import capo_iam.types.delegation_permission

        out["permissions"] = capo_iam.types.delegation_permission.deserialize_query(
            child_permissions
        )
    else:
        raise DeserializationError(
            "CreateDelegationRequestRequest.permissions required"
        )
    child_request_message = el.find("RequestMessage")
    if child_request_message is not None:
        out["request_message"] = str(child_request_message.text or "")
    child_requestor_workflow_id = el.find("RequestorWorkflowId")
    if child_requestor_workflow_id is not None:
        out["requestor_workflow_id"] = str(child_requestor_workflow_id.text or "")
    else:
        raise DeserializationError(
            "CreateDelegationRequestRequest.requestor_workflow_id required"
        )
    child_redirect_url = el.find("RedirectUrl")
    if child_redirect_url is not None:
        out["redirect_url"] = str(child_redirect_url.text or "")
    child_notification_channel = el.find("NotificationChannel")
    if child_notification_channel is not None:
        out["notification_channel"] = str(child_notification_channel.text or "")
    else:
        raise DeserializationError(
            "CreateDelegationRequestRequest.notification_channel required"
        )
    child_session_duration = el.find("SessionDuration")
    if child_session_duration is not None:
        out["session_duration"] = int(child_session_duration.text or "")
    else:
        raise DeserializationError(
            "CreateDelegationRequestRequest.session_duration required"
        )
    child_only_send_by_owner = el.find("OnlySendByOwner")
    if child_only_send_by_owner is not None:
        out["only_send_by_owner"] = (
            child_only_send_by_owner.text or ""
        ).lower() == "true"
    else:
        out["only_send_by_owner"] = False
    return out
