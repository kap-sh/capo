"""Generated from Smithy shape ``com.amazon.awshealthlakedatatransformationfrontendservice#ValidateSourceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.source_format
    import capo_healthlake.types.source_validation_issue_list
    import capo_healthlake.types.validation_summary


class ValidateSourceResponse(TypedDict, closed=True):
    valid: "bool"
    """<p>Indicates whether the source file passed validation.</p>"""
    source_format: "capo_healthlake.types.source_format.SourceFormat"
    """<p>The format that was validated.</p>"""
    issues: (
        "capo_healthlake.types.source_validation_issue_list.SourceValidationIssueList"
    )
    """<p>The list of validation issues found, including errors and warnings with location details and remediation guidance.</p>"""
    summary: "capo_healthlake.types.validation_summary.ValidationSummary"
    """<p>A summary of validation results, including the count of errors and warnings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidateSourceResponse) -> dict:
    out: dict = {}
    out["Valid"] = value["valid"]
    import capo_healthlake.types.source_format

    out["SourceFormat"] = capo_healthlake.types.source_format.serialize_aws_json_1_0(
        value["source_format"]
    )
    import capo_healthlake.types.source_validation_issue_list

    out["Issues"] = (
        capo_healthlake.types.source_validation_issue_list.serialize_aws_json_1_0(
            value["issues"]
        )
    )
    import capo_healthlake.types.validation_summary

    out["Summary"] = capo_healthlake.types.validation_summary.serialize_aws_json_1_0(
        value["summary"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidateSourceResponse:
    out: ValidateSourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Valid") is not None:
        out["valid"] = data["Valid"]
    else:
        raise DeserializationError("ValidateSourceResponse.valid required")
    if data.get("SourceFormat") is not None:
        import capo_healthlake.types.source_format

        out["source_format"] = (
            capo_healthlake.types.source_format.deserialize_aws_json_1_0(
                data["SourceFormat"]
            )
        )
    else:
        raise DeserializationError("ValidateSourceResponse.source_format required")
    if data.get("Issues") is not None:
        import capo_healthlake.types.source_validation_issue_list

        out["issues"] = (
            capo_healthlake.types.source_validation_issue_list.deserialize_aws_json_1_0(
                data["Issues"]
            )
        )
    else:
        raise DeserializationError("ValidateSourceResponse.issues required")
    if data.get("Summary") is not None:
        import capo_healthlake.types.validation_summary

        out["summary"] = (
            capo_healthlake.types.validation_summary.deserialize_aws_json_1_0(
                data["Summary"]
            )
        )
    else:
        raise DeserializationError("ValidateSourceResponse.summary required")
    return out


def redact_sensitive(value: ValidateSourceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "issues" in value:
        import capo_healthlake.types.source_validation_issue_list

        out["issues"] = (
            capo_healthlake.types.source_validation_issue_list.redact_sensitive(
                value["issues"]
            )
        )
    return out
