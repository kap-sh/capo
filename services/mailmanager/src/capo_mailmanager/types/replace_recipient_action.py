"""Generated from Smithy shape ``com.amazonaws.mailmanager#ReplaceRecipientAction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.recipients


class ReplaceRecipientAction(TypedDict, closed=True):
    replace_with: NotRequired["capo_mailmanager.types.recipients.Recipients"]
    """<p>This action specifies the replacement recipient email addresses to insert.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplaceRecipientAction) -> dict:
    out: dict = {}
    if "replace_with" in value:
        import capo_mailmanager.types.recipients

        out["ReplaceWith"] = capo_mailmanager.types.recipients.serialize_aws_json_1_0(
            value["replace_with"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplaceRecipientAction:
    out: ReplaceRecipientAction = {}  # type: ignore[typeddict-item]
    if data.get("ReplaceWith") is not None:
        import capo_mailmanager.types.recipients

        out["replace_with"] = (
            capo_mailmanager.types.recipients.deserialize_aws_json_1_0(
                data["ReplaceWith"]
            )
        )
    return out


def redact_sensitive(value: ReplaceRecipientAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "replace_with" in value:
        import capo_mailmanager.types.recipients

        out["replace_with"] = capo_mailmanager.types.recipients.redact_sensitive(
            value["replace_with"]
        )
    return out
