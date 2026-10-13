"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#BatchCreateChannelMembershipResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.batch_channel_memberships
    import capo_chime_sdk_messaging.types.batch_create_channel_membership_errors


class BatchCreateChannelMembershipResponse(TypedDict, closed=True):
    batch_channel_memberships: NotRequired[
        "capo_chime_sdk_messaging.types.batch_channel_memberships.BatchChannelMemberships"
    ]
    """<p>The list of channel memberships in the response.</p>"""
    errors: NotRequired[
        "capo_chime_sdk_messaging.types.batch_create_channel_membership_errors.BatchCreateChannelMembershipErrors"
    ]
    """<p>If the action fails for one or more of the memberships in the request, a list of the memberships is returned, along with error codes and error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateChannelMembershipResponse) -> dict:
    out: dict = {}
    if "batch_channel_memberships" in value:
        import capo_chime_sdk_messaging.types.batch_channel_memberships

        out["BatchChannelMemberships"] = (
            capo_chime_sdk_messaging.types.batch_channel_memberships.serialize_json(
                value["batch_channel_memberships"]
            )
        )
    if "errors" in value:
        import capo_chime_sdk_messaging.types.batch_create_channel_membership_errors

        out["Errors"] = (
            capo_chime_sdk_messaging.types.batch_create_channel_membership_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchCreateChannelMembershipResponse:
    out: BatchCreateChannelMembershipResponse = {}  # type: ignore[typeddict-item]
    if data.get("BatchChannelMemberships") is not None:
        import capo_chime_sdk_messaging.types.batch_channel_memberships

        out["batch_channel_memberships"] = (
            capo_chime_sdk_messaging.types.batch_channel_memberships.deserialize_json(
                data["BatchChannelMemberships"]
            )
        )
    if data.get("Errors") is not None:
        import capo_chime_sdk_messaging.types.batch_create_channel_membership_errors

        out["errors"] = (
            capo_chime_sdk_messaging.types.batch_create_channel_membership_errors.deserialize_json(
                data["Errors"]
            )
        )
    return out


def redact_sensitive(value: BatchCreateChannelMembershipResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "batch_channel_memberships" in value:
        import capo_chime_sdk_messaging.types.batch_channel_memberships

        out["batch_channel_memberships"] = (
            capo_chime_sdk_messaging.types.batch_channel_memberships.redact_sensitive(
                value["batch_channel_memberships"]
            )
        )
    return out
