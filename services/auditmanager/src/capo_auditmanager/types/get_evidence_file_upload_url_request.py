"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetEvidenceFileUploadUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.manual_evidence_local_file_name


class GetEvidenceFileUploadUrlRequest(TypedDict, closed=True):
    file_name: "capo_auditmanager.types.manual_evidence_local_file_name.ManualEvidenceLocalFileName"
    """<p>The file that you want to upload. For a list of supported file formats, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files">Supported file types for manual evidence</a> in the <i>Audit Manager User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvidenceFileUploadUrlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEvidenceFileUploadUrlRequest:
    out: GetEvidenceFileUploadUrlRequest = {}  # type: ignore[typeddict-item]
    return out
