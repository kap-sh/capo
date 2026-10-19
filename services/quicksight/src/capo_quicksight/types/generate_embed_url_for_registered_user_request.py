"""Generated from Smithy shape ``com.amazonaws.quicksight#GenerateEmbedUrlForRegisteredUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.registered_user_embedding_experience_configuration
    import capo_quicksight.types.session_lifetime_in_minutes
    import capo_quicksight.types.string_list


class GenerateEmbedUrlForRegisteredUserRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the dashboard that you're embedding.</p>"""
    session_lifetime_in_minutes: NotRequired[
        "capo_quicksight.types.session_lifetime_in_minutes.SessionLifetimeInMinutes"
    ]
    """<p>How many minutes the session is valid. The session lifetime must be in [15-600] minutes range.</p>"""
    user_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name for the registered user.</p>"""
    experience_configuration: "capo_quicksight.types.registered_user_embedding_experience_configuration.RegisteredUserEmbeddingExperienceConfiguration"
    """<p>The experience that you want to embed. For registered users, you can embed Quick dashboards, Amazon Quick Sight visuals, the Amazon Quick Sight Q search bar, the Amazon Quick Sight Generative Q&A experience, or the entire Amazon Quick Sight console.</p>"""
    allowed_domains: NotRequired["capo_quicksight.types.string_list.StringList"]
    """<p>The domains that you want to add to the allow list for access to the generated URL that is then embedded. This optional parameter overrides the static domains that are configured in the Manage Quick Sight menu in the Amazon Quick Sight console. Instead, it allows only the domains that you include in this parameter. You can list up to three domains or subdomains in each API call.</p> <p>To include all subdomains under a specific domain to the allow list, use <code>*</code>. For example, <code>https://*.sapp.amazon.com</code> includes all subdomains under <code>https://sapp.amazon.com</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateEmbedUrlForRegisteredUserRequest) -> dict:
    out: dict = {}
    if "session_lifetime_in_minutes" in value:
        out["SessionLifetimeInMinutes"] = value["session_lifetime_in_minutes"]
    out["UserArn"] = value["user_arn"]
    import capo_quicksight.types.registered_user_embedding_experience_configuration

    out["ExperienceConfiguration"] = (
        capo_quicksight.types.registered_user_embedding_experience_configuration.serialize_json(
            value["experience_configuration"]
        )
    )
    if "allowed_domains" in value:
        import capo_quicksight.types.string_list

        out["AllowedDomains"] = capo_quicksight.types.string_list.serialize_json(
            value["allowed_domains"]
        )
    return out


def deserialize_json(data: dict) -> GenerateEmbedUrlForRegisteredUserRequest:
    out: GenerateEmbedUrlForRegisteredUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("SessionLifetimeInMinutes") is not None:
        out["session_lifetime_in_minutes"] = data["SessionLifetimeInMinutes"]
    if data.get("UserArn") is not None:
        out["user_arn"] = data["UserArn"]
    else:
        out["user_arn"] = ""
    if data.get("ExperienceConfiguration") is not None:
        import capo_quicksight.types.registered_user_embedding_experience_configuration

        out["experience_configuration"] = (
            capo_quicksight.types.registered_user_embedding_experience_configuration.deserialize_json(
                data["ExperienceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateEmbedUrlForRegisteredUserRequest.experience_configuration required"
        )
    if data.get("AllowedDomains") is not None:
        import capo_quicksight.types.string_list

        out["allowed_domains"] = capo_quicksight.types.string_list.deserialize_json(
            data["AllowedDomains"]
        )
    return out
