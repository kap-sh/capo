"""Generated from Smithy shape ``com.amazonaws.workmail#ListUsersFilters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.entity_state
    import capo_workmail.types.identity_provider_user_id_prefix
    import capo_workmail.types.string
    import capo_workmail.types.user_attribute


class ListUsersFilters(TypedDict, closed=True):
    username_prefix: NotRequired["capo_workmail.types.string.String"]
    """<p>Filters only users with the provided username prefix.</p>"""
    display_name_prefix: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Filters only users with the provided display name prefix.</p>"""
    primary_email_prefix: NotRequired["capo_workmail.types.string.String"]
    """<p>Filters only users with the provided email prefix.</p>"""
    state: NotRequired["capo_workmail.types.entity_state.EntityState"]
    """<p>Filters only users with the provided state.</p>"""
    identity_provider_user_id_prefix: NotRequired[
        "capo_workmail.types.identity_provider_user_id_prefix.IdentityProviderUserIdPrefix"
    ]
    """<p>Filters only users with the ID from the IAM Identity Center.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsersFilters) -> dict:
    out: dict = {}
    if "username_prefix" in value:
        out["UsernamePrefix"] = value["username_prefix"]
    if "display_name_prefix" in value:
        out["DisplayNamePrefix"] = value["display_name_prefix"]
    if "primary_email_prefix" in value:
        out["PrimaryEmailPrefix"] = value["primary_email_prefix"]
    if "state" in value:
        import capo_workmail.types.entity_state

        out["State"] = capo_workmail.types.entity_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "identity_provider_user_id_prefix" in value:
        out["IdentityProviderUserIdPrefix"] = value["identity_provider_user_id_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsersFilters:
    out: ListUsersFilters = {}  # type: ignore[typeddict-item]
    if data.get("UsernamePrefix") is not None:
        out["username_prefix"] = data["UsernamePrefix"]
    if data.get("DisplayNamePrefix") is not None:
        out["display_name_prefix"] = data["DisplayNamePrefix"]
    if data.get("PrimaryEmailPrefix") is not None:
        out["primary_email_prefix"] = data["PrimaryEmailPrefix"]
    if data.get("State") is not None:
        import capo_workmail.types.entity_state

        out["state"] = capo_workmail.types.entity_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("IdentityProviderUserIdPrefix") is not None:
        out["identity_provider_user_id_prefix"] = data["IdentityProviderUserIdPrefix"]
    return out


def redact_sensitive(value: ListUsersFilters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name_prefix" in value:
        out["display_name_prefix"] = "*** Sensitive Data Redacted ***"
    return out
