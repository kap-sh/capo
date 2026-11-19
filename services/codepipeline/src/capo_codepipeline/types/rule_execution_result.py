"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleExecutionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.error_details
    import capo_codepipeline.types.external_execution_id
    import capo_codepipeline.types.external_execution_summary
    import capo_codepipeline.types.url


class RuleExecutionResult(TypedDict, closed=True):
    external_execution_id: NotRequired[
        "capo_codepipeline.types.external_execution_id.ExternalExecutionId"
    ]
    """<p>The external ID for the rule execution.</p>"""
    external_execution_summary: NotRequired[
        "capo_codepipeline.types.external_execution_summary.ExternalExecutionSummary"
    ]
    """<p>The external provider summary for the rule execution.</p>"""
    external_execution_url: NotRequired["capo_codepipeline.types.url.Url"]
    """<p>The deepest external link to the external resource (for example, a repository URL or deployment endpoint) that is used when running the rule.</p>"""
    error_details: NotRequired["capo_codepipeline.types.error_details.ErrorDetails"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleExecutionResult) -> dict:
    out: dict = {}
    if "external_execution_id" in value:
        out["externalExecutionId"] = value["external_execution_id"]
    if "external_execution_summary" in value:
        out["externalExecutionSummary"] = value["external_execution_summary"]
    if "external_execution_url" in value:
        out["externalExecutionUrl"] = value["external_execution_url"]
    if "error_details" in value:
        import capo_codepipeline.types.error_details

        out["errorDetails"] = (
            capo_codepipeline.types.error_details.serialize_aws_json_1_1(
                value["error_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleExecutionResult:
    out: RuleExecutionResult = {}  # type: ignore[typeddict-item]
    if data.get("externalExecutionId") is not None:
        out["external_execution_id"] = data["externalExecutionId"]
    if data.get("externalExecutionSummary") is not None:
        out["external_execution_summary"] = data["externalExecutionSummary"]
    if data.get("externalExecutionUrl") is not None:
        out["external_execution_url"] = data["externalExecutionUrl"]
    if data.get("errorDetails") is not None:
        import capo_codepipeline.types.error_details

        out["error_details"] = (
            capo_codepipeline.types.error_details.deserialize_aws_json_1_1(
                data["errorDetails"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleExecutionResult) -> dict:
    out: dict = {}
    if "external_execution_id" in value:
        out["externalExecutionId"] = value["external_execution_id"]
    if "external_execution_summary" in value:
        out["externalExecutionSummary"] = value["external_execution_summary"]
    if "external_execution_url" in value:
        out["externalExecutionUrl"] = value["external_execution_url"]
    if "error_details" in value:
        import capo_codepipeline.types.error_details

        out["errorDetails"] = capo_codepipeline.types.error_details.serialize_cbor(
            value["error_details"]
        )
    return out


def deserialize_cbor(data: dict) -> RuleExecutionResult:
    out: RuleExecutionResult = {}  # type: ignore[typeddict-item]
    if data.get("externalExecutionId") is not None:
        out["external_execution_id"] = data["externalExecutionId"]
    if data.get("externalExecutionSummary") is not None:
        out["external_execution_summary"] = data["externalExecutionSummary"]
    if data.get("externalExecutionUrl") is not None:
        out["external_execution_url"] = data["externalExecutionUrl"]
    if data.get("errorDetails") is not None:
        import capo_codepipeline.types.error_details

        out["error_details"] = capo_codepipeline.types.error_details.deserialize_cbor(
            data["errorDetails"]
        )
    return out
