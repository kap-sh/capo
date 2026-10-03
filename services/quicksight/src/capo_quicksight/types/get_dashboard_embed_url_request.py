"""Generated from Smithy shape ``com.amazonaws.quicksight#GetDashboardEmbedUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.additional_dashboard_id_list
    import capo_quicksight.types.arn
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.boolean
    import capo_quicksight.types.embedding_identity_type
    import capo_quicksight.types.namespace
    import capo_quicksight.types.session_lifetime_in_minutes
    import capo_quicksight.types.short_restrictive_resource_id


class GetDashboardEmbedUrlRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the dashboard that you're embedding.</p>"""
    dashboard_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the dashboard, also added to the Identity and Access Management (IAM) policy.</p>"""
    identity_type: "capo_quicksight.types.embedding_identity_type.EmbeddingIdentityType"
    """<p>The authentication method that the user uses to sign in.</p>"""
    session_lifetime_in_minutes: NotRequired[
        "capo_quicksight.types.session_lifetime_in_minutes.SessionLifetimeInMinutes"
    ]
    """<p>How many minutes the session is valid. The session lifetime must be 15-600 minutes.</p>"""
    undo_redo_disabled: "capo_quicksight.types.boolean.Boolean"
    """<p>Remove the undo/redo button on the embedded dashboard. The default is FALSE, which enables the undo/redo button.</p>"""
    reset_disabled: "capo_quicksight.types.boolean.Boolean"
    """<p>Remove the reset button on the embedded dashboard. The default is FALSE, which enables the reset button.</p>"""
    state_persistence_enabled: "capo_quicksight.types.boolean.Boolean"
    """<p>Adds persistence of state for the user session in an embedded dashboard. Persistence applies to the sheet and the parameter settings. These are control settings that the dashboard subscriber (Amazon Quick Sight reader) chooses while viewing the dashboard. If this is set to <code>TRUE</code>, the settings are the same when the subscriber reopens the same dashboard URL. The state is stored in Amazon Quick Sight, not in a browser cookie. If this is set to FALSE, the state of the user session is not persisted. The default is <code>FALSE</code>.</p>"""
    user_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Quick user's Amazon Resource Name (ARN), for use with <code>QUICKSIGHT</code> identity type. You can use this for any Amazon Quick users in your account (readers, authors, or admins) authenticated as one of the following:</p> <ul> <li> <p>Active Directory (AD) users or group members</p> </li> <li> <p>Invited nonfederated users</p> </li> <li> <p>IAM users and IAM role-based sessions authenticated through Federated Single Sign-On using SAML, OpenID Connect, or IAM federation.</p> </li> </ul> <p>Omit this parameter for users in the third group – IAM users and IAM role-based sessions.</p>"""
    namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The Amazon Quick Sight namespace that contains the dashboard IDs in this request. If you're not using a custom namespace, set <code>Namespace = default</code>.</p>"""
    additional_dashboard_ids: NotRequired[
        "capo_quicksight.types.additional_dashboard_id_list.AdditionalDashboardIdList"
    ]
    """<p>A list of one or more dashboard IDs that you want anonymous users to have tempporary access to. Currently, the <code>IdentityType</code> parameter must be set to <code>ANONYMOUS</code> because other identity types authenticate as Quick or IAM users. For example, if you set "<code>--dashboard-id dash_id1 --dashboard-id dash_id2 dash_id3 identity-type ANONYMOUS</code>", the session can access all three dashboards.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDashboardEmbedUrlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDashboardEmbedUrlRequest:
    out: GetDashboardEmbedUrlRequest = {}  # type: ignore[typeddict-item]
    return out
