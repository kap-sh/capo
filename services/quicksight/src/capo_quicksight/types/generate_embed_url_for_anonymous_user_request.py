"""Generated from Smithy shape ``com.amazonaws.quicksight#GenerateEmbedUrlForAnonymousUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.anonymous_user_embedding_experience_configuration
    import capo_quicksight.types.arn_list
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace
    import capo_quicksight.types.session_lifetime_in_minutes
    import capo_quicksight.types.session_tag_list
    import capo_quicksight.types.string_list


class GenerateEmbedUrlForAnonymousUserRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the dashboard that you're embedding.</p>"""
    session_lifetime_in_minutes: NotRequired[
        "capo_quicksight.types.session_lifetime_in_minutes.SessionLifetimeInMinutes"
    ]
    """<p>How many minutes the session is valid. The session lifetime must be in [15-600] minutes range.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The Amazon Quick Sight namespace that the anonymous user virtually belongs to. If you are not using an Amazon Quick custom namespace, set this to <code>default</code>.</p>"""
    session_tags: NotRequired["capo_quicksight.types.session_tag_list.SessionTagList"]
    """<p>Session tags are user-specified strings that identify a session in your application. You can use these tags to implement row-level security (RLS) controls. Before you use the <code>SessionTags</code> parameter, make sure that you have configured the relevant datasets using the <code>DataSet$RowLevelPermissionTagConfiguration</code> parameter so that session tags can be used to provide row-level security.</p> <p>When using <code>SessionTags</code> in <code>GenerateEmbedUrlForAnonymousUser</code>,</p> <ul> <li> <p>Treat <code>SessionTags</code> as security credentials. Do not expose <code>SessionTags</code> to end users or client-side code.</p> </li> <li> <p>Implement server-side controls. Ensure that <code>SessionTags</code> are set exclusively by your trusted backend services, not by parameters that end users can modify.</p> </li> <li> <p>Protect <code>SessionTags</code> from enumeration. Ensure that users in one tenant cannot discover or guess sessionTag values belonging to other tenants.</p> </li> <li> <p>Review your architecture. If downstream customers or partners are allowed to call the <code>GenerateEmbedUrlForAnonymousUser</code> API directly, evaluate whether those parties could specify sessionTag values for tenants they should not access.</p> </li> </ul> <p>Besides, these are not the tags used for the Amazon Web Services resource tagging feature. For more information, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-rls-tags.html">Using Row-Level Security (RLS) with Tags</a> in the <i>Amazon Quick User Guide</i>.</p>"""
    authorized_resource_arns: "capo_quicksight.types.arn_list.ArnList"
    """<p>The Amazon Resource Names (ARNs) for the Quick Sight resources that the user is authorized to access during the lifetime of the session.</p> <p>If you choose <code>Dashboard</code> embedding experience, pass the list of dashboard ARNs in the account that you want the user to be able to view.</p> <p>If you want to make changes to the theme of your embedded content, pass a list of theme ARNs that the anonymous users need access to.</p> <p>Currently, you can pass up to 25 theme ARNs in each API call.</p>"""
    experience_configuration: "capo_quicksight.types.anonymous_user_embedding_experience_configuration.AnonymousUserEmbeddingExperienceConfiguration"
    """<p>The configuration of the experience that you are embedding.</p>"""
    allowed_domains: NotRequired["capo_quicksight.types.string_list.StringList"]
    """<p>The domains that you want to add to the allow list for access to the generated URL that is then embedded. This optional parameter overrides the static domains that are configured in the Manage Quick Sight menu in the Amazon Quick Sight console. Instead, it allows only the domains that you include in this parameter. You can list up to three domains or subdomains in each API call.</p> <p>To include all subdomains under a specific domain to the allow list, use <code>*</code>. For example, <code>https://*.sapp.amazon.com</code> includes all subdomains under <code>https://sapp.amazon.com</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateEmbedUrlForAnonymousUserRequest) -> dict:
    out: dict = {}
    if "session_lifetime_in_minutes" in value:
        out["SessionLifetimeInMinutes"] = value["session_lifetime_in_minutes"]
    out["Namespace"] = value["namespace"]
    if "session_tags" in value:
        import capo_quicksight.types.session_tag_list

        out["SessionTags"] = capo_quicksight.types.session_tag_list.serialize_json(
            value["session_tags"]
        )
    import capo_quicksight.types.arn_list

    out["AuthorizedResourceArns"] = capo_quicksight.types.arn_list.serialize_json(
        value["authorized_resource_arns"]
    )
    import capo_quicksight.types.anonymous_user_embedding_experience_configuration

    out["ExperienceConfiguration"] = (
        capo_quicksight.types.anonymous_user_embedding_experience_configuration.serialize_json(
            value["experience_configuration"]
        )
    )
    if "allowed_domains" in value:
        import capo_quicksight.types.string_list

        out["AllowedDomains"] = capo_quicksight.types.string_list.serialize_json(
            value["allowed_domains"]
        )
    return out


def deserialize_json(data: dict) -> GenerateEmbedUrlForAnonymousUserRequest:
    out: GenerateEmbedUrlForAnonymousUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("SessionLifetimeInMinutes") is not None:
        out["session_lifetime_in_minutes"] = data["SessionLifetimeInMinutes"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    else:
        raise DeserializationError(
            "GenerateEmbedUrlForAnonymousUserRequest.namespace required"
        )
    if data.get("SessionTags") is not None:
        import capo_quicksight.types.session_tag_list

        out["session_tags"] = capo_quicksight.types.session_tag_list.deserialize_json(
            data["SessionTags"]
        )
    if data.get("AuthorizedResourceArns") is not None:
        import capo_quicksight.types.arn_list

        out["authorized_resource_arns"] = (
            capo_quicksight.types.arn_list.deserialize_json(
                data["AuthorizedResourceArns"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateEmbedUrlForAnonymousUserRequest.authorized_resource_arns required"
        )
    if data.get("ExperienceConfiguration") is not None:
        import capo_quicksight.types.anonymous_user_embedding_experience_configuration

        out["experience_configuration"] = (
            capo_quicksight.types.anonymous_user_embedding_experience_configuration.deserialize_json(
                data["ExperienceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateEmbedUrlForAnonymousUserRequest.experience_configuration required"
        )
    if data.get("AllowedDomains") is not None:
        import capo_quicksight.types.string_list

        out["allowed_domains"] = capo_quicksight.types.string_list.deserialize_json(
            data["AllowedDomains"]
        )
    return out
