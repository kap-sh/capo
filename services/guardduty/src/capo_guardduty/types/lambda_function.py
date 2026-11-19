"""Generated from Smithy shape ``com.amazonaws.guardduty#LambdaFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp


class LambdaFunction(TypedDict, closed=True):
    function_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the function.</p>"""
    function_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the function.</p>"""
    function_version: NotRequired["capo_guardduty.types.string.String"]
    """<p>The version of the function.</p>"""
    role: NotRequired["capo_guardduty.types.string.String"]
    """<p>The execution role of the function.</p>"""
    description: NotRequired["capo_guardduty.types.string.String"]
    """<p>The description of the function.</p>"""
    revision_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The revision ID of the function version.</p>"""
    updated_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the function was last updated.</p>"""
    vpc_configuration_summary: NotRequired["capo_guardduty.types.string.String"]
    """<p>A summary of the VPC configuration of the function, as a single string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaFunction) -> dict:
    out: dict = {}
    if "function_name" in value:
        out["functionName"] = value["function_name"]
    if "function_arn" in value:
        out["functionArn"] = value["function_arn"]
    if "function_version" in value:
        out["functionVersion"] = value["function_version"]
    if "role" in value:
        out["role"] = value["role"]
    if "description" in value:
        out["description"] = value["description"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "updated_at" in value:
        import capo_guardduty.types.timestamp

        out["updatedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "vpc_configuration_summary" in value:
        out["vpcConfigurationSummary"] = value["vpc_configuration_summary"]
    return out


def deserialize_json(data: dict) -> LambdaFunction:
    out: LambdaFunction = {}  # type: ignore[typeddict-item]
    if data.get("functionName") is not None:
        out["function_name"] = data["functionName"]
    if data.get("functionArn") is not None:
        out["function_arn"] = data["functionArn"]
    if data.get("functionVersion") is not None:
        out["function_version"] = data["functionVersion"]
    if data.get("role") is not None:
        out["role"] = data["role"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    if data.get("updatedAt") is not None:
        import capo_guardduty.types.timestamp

        out["updated_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("vpcConfigurationSummary") is not None:
        out["vpc_configuration_summary"] = data["vpcConfigurationSummary"]
    return out
