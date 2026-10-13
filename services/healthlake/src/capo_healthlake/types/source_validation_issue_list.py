"""Generated from Smithy shape ``com.amazon.awshealthlakedatatransformationfrontendservice#SourceValidationIssueList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_healthlake.types.source_validation_issue

SourceValidationIssueList: TypeAlias = list[
    "capo_healthlake.types.source_validation_issue.SourceValidationIssue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceValidationIssueList) -> list:
    import capo_healthlake.types.source_validation_issue

    out: list = []
    for item in value:
        out.append(
            capo_healthlake.types.source_validation_issue.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SourceValidationIssueList:
    import capo_healthlake.types.source_validation_issue

    out: SourceValidationIssueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_healthlake.types.source_validation_issue.deserialize_aws_json_1_0(item)
        )
    return out


def redact_sensitive(value: SourceValidationIssueList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
