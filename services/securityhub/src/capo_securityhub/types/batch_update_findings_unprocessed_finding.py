"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsUnprocessedFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_security_finding_identifier
    import capo_securityhub.types.non_empty_string


class BatchUpdateFindingsUnprocessedFinding(TypedDict, closed=True):
    finding_identifier: NotRequired[
        "capo_securityhub.types.aws_security_finding_identifier.AwsSecurityFindingIdentifier"
    ]
    """<p>The identifier of the finding that was not updated.</p>"""
    error_code: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The code associated with the error. Possible values are:</p> <ul> <li> <p> <code>ConcurrentUpdateError</code> - Another request attempted to update the finding while this request was being processed. This error may also occur if you call <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html"> <code>BatchUpdateFindings</code> </a> and <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html"> <code>BatchImportFindings</code> </a> at the same time.</p> </li> <li> <p> <code>DuplicatedFindingIdentifier</code> - The request included two or more findings with the same <code>FindingIdentifier</code>.</p> </li> <li> <p> <code>FindingNotFound</code> - The <code>FindingIdentifier</code> included in the request did not match an existing finding.</p> </li> <li> <p> <code>FindingSizeExceeded</code> - The finding size was greater than the permissible value of 240 KB.</p> </li> <li> <p> <code>InternalFailure</code> - An internal service failure occurred when updating the finding.</p> </li> <li> <p> <code>InvalidInput</code> - The finding update contained an invalid value that did not satisfy the <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html">Amazon Web Services Security Finding Format</a> syntax.</p> </li> </ul>"""
    error_message: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The message associated with the error. Possible values are:</p> <ul> <li> <p> <code>Concurrent finding updates detected</code> </p> </li> <li> <p> <code>Finding Identifier is duplicated</code> </p> </li> <li> <p> <code>Finding Not Found</code> </p> </li> <li> <p> <code>Finding size exceeded 240 KB</code> </p> </li> <li> <p> <code>Internal service failure</code> </p> </li> <li> <p> <code>Invalid Input</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsUnprocessedFinding) -> dict:
    out: dict = {}
    if "finding_identifier" in value:
        import capo_securityhub.types.aws_security_finding_identifier

        out["FindingIdentifier"] = (
            capo_securityhub.types.aws_security_finding_identifier.serialize_json(
                value["finding_identifier"]
            )
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateFindingsUnprocessedFinding:
    out: BatchUpdateFindingsUnprocessedFinding = {}  # type: ignore[typeddict-item]
    if data.get("FindingIdentifier") is not None:
        import capo_securityhub.types.aws_security_finding_identifier

        out["finding_identifier"] = (
            capo_securityhub.types.aws_security_finding_identifier.deserialize_json(
                data["FindingIdentifier"]
            )
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
