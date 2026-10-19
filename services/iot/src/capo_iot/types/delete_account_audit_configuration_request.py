"""Generated from Smithy shape ``com.amazonaws.iot#DeleteAccountAuditConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.delete_scheduled_audits


class DeleteAccountAuditConfigurationRequest(TypedDict, closed=True):
    delete_scheduled_audits: NotRequired[
        "capo_iot.types.delete_scheduled_audits.DeleteScheduledAudits"
    ]
    """<p>If true, all scheduled audits are deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccountAuditConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccountAuditConfigurationRequest:
    out: DeleteAccountAuditConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
