"""Generated from Smithy shape ``com.amazonaws.ses#UpdateAccountSendingEnabledRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.enabled


class UpdateAccountSendingEnabledRequest(TypedDict, closed=True):
    enabled: NotRequired["capo_ses.types.enabled.Enabled"]
    """<p>Describes whether email sending is enabled or disabled for your Amazon SES account in the current Amazon Web Services Region.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateAccountSendingEnabledRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))


def deserialize_query(el: Element) -> UpdateAccountSendingEnabledRequest:
    out: UpdateAccountSendingEnabledRequest = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
