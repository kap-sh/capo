"""Generated from Smithy shape ``com.amazonaws.quicksight#GetIdentityContextRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace
    import capo_quicksight.types.region
    import capo_quicksight.types.user_identifier


class GetIdentityContextRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the user whose identity context you want to retrieve is in. Currently, you use the ID for the Amazon Web Services account that contains your Quick Sight account.</p>"""
    user_identifier: "capo_quicksight.types.user_identifier.UserIdentifier"
    """<p>The identifier for the user whose identity context you want to retrieve.</p>"""
    namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The namespace of the user that you want to get identity context for. This parameter is required when the UserIdentifier is specified using Email or UserName.</p>"""
    session_expires_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which the session will expire.</p>"""
    context_region: NotRequired["capo_quicksight.types.region.Region"]
    """<p>The region in which the context is to be used. Use this parameter to obtain an identity context for cross-region use.</p> <p>The specified region must meet the following conditions:</p> <ul> <li> <p>The region must be in the same Amazon Web Services partition as the region you are calling from. Cross-partition requests are not supported. For example, you cannot specify a region in the <code>aws-cn</code> partition when calling from a region in the <code>aws</code> partition.</p> </li> <li> <p>It must be a valid Amazon QuickSight supported region.</p> </li> <li> <p>The calling customer account must be enabled in the specified context region.</p> </li> <li> <p>This parameter is not supported when calling from an opt-in region.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdentityContextRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.user_identifier

    out["UserIdentifier"] = capo_quicksight.types.user_identifier.serialize_json(
        value["user_identifier"]
    )
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "session_expires_at" in value:
        import capo_quicksight.types._prelude.timestamp

        out["SessionExpiresAt"] = (
            capo_quicksight.types._prelude.timestamp.serialize_json(
                value["session_expires_at"]
            )
        )
    if "context_region" in value:
        out["ContextRegion"] = value["context_region"]
    return out


def deserialize_json(data: dict) -> GetIdentityContextRequest:
    out: GetIdentityContextRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserIdentifier") is not None:
        import capo_quicksight.types.user_identifier

        out["user_identifier"] = capo_quicksight.types.user_identifier.deserialize_json(
            data["UserIdentifier"]
        )
    else:
        import capo_quicksight.types._unknown

        out["user_identifier"] = capo_quicksight.types._unknown.UnknownUnionMember("")
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("SessionExpiresAt") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["session_expires_at"] = (
            capo_quicksight.types._prelude.timestamp.deserialize_json(
                data["SessionExpiresAt"]
            )
        )
    if data.get("ContextRegion") is not None:
        out["context_region"] = data["ContextRegion"]
    return out


def redact_sensitive(value: GetIdentityContextRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_identifier" in value:
        import capo_quicksight.types.user_identifier

        out["user_identifier"] = capo_quicksight.types.user_identifier.redact_sensitive(
            value["user_identifier"]
        )
    return out
