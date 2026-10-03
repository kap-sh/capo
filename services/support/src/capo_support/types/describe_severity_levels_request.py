"""Generated from Smithy shape ``com.amazonaws.support#DescribeSeverityLevelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.language
    import capo_support.types.nullable_boolean_type


class DescribeSeverityLevelsRequest(TypedDict, closed=True):
    language: NotRequired["capo_support.types.language.Language"]
    """<p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually returning severity levels. When set to <code>true</code>, the request is validated but no severity levels are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSeverityLevelsRequest) -> dict:
    out: dict = {}
    if "language" in value:
        out["language"] = value["language"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSeverityLevelsRequest:
    out: DescribeSeverityLevelsRequest = {}  # type: ignore[typeddict-item]
    if data.get("language") is not None:
        out["language"] = data["language"]
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
