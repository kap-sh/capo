"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchImportFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.batch_import_findings_request_finding_list


class BatchImportFindingsRequest(TypedDict, closed=True):
    findings: NotRequired[
        "capo_securityhub.types.batch_import_findings_request_finding_list.BatchImportFindingsRequestFindingList"
    ]
    """<p>A list of findings to import. To successfully import a finding, it must follow the <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html">Amazon Web Services Security Finding Format</a>. Maximum of 100 findings per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchImportFindingsRequest) -> dict:
    out: dict = {}
    if "findings" in value:
        import capo_securityhub.types.batch_import_findings_request_finding_list

        out["Findings"] = (
            capo_securityhub.types.batch_import_findings_request_finding_list.serialize_json(
                value["findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchImportFindingsRequest:
    out: BatchImportFindingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Findings") is not None:
        import capo_securityhub.types.batch_import_findings_request_finding_list

        out["findings"] = (
            capo_securityhub.types.batch_import_findings_request_finding_list.deserialize_json(
                data["Findings"]
            )
        )
    return out
