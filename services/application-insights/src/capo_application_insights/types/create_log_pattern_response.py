"""Generated from Smithy shape ``com.amazonaws.applicationinsights#CreateLogPatternResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.log_pattern
    import capo_application_insights.types.resource_group_name


class CreateLogPatternResponse(TypedDict, closed=True):
    log_pattern: NotRequired["capo_application_insights.types.log_pattern.LogPattern"]
    """<p>The successfully created log pattern.</p>"""
    resource_group_name: NotRequired[
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLogPatternResponse) -> dict:
    out: dict = {}
    if "log_pattern" in value:
        import capo_application_insights.types.log_pattern

        out["LogPattern"] = (
            capo_application_insights.types.log_pattern.serialize_aws_json_1_1(
                value["log_pattern"]
            )
        )
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLogPatternResponse:
    out: CreateLogPatternResponse = {}  # type: ignore[typeddict-item]
    if data.get("LogPattern") is not None:
        import capo_application_insights.types.log_pattern

        out["log_pattern"] = (
            capo_application_insights.types.log_pattern.deserialize_aws_json_1_1(
                data["LogPattern"]
            )
        )
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateLogPatternResponse) -> dict:
    out: dict = {}
    if "log_pattern" in value:
        import capo_application_insights.types.log_pattern

        out["LogPattern"] = capo_application_insights.types.log_pattern.serialize_cbor(
            value["log_pattern"]
        )
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    return out


def deserialize_cbor(data: dict) -> CreateLogPatternResponse:
    out: CreateLogPatternResponse = {}  # type: ignore[typeddict-item]
    if data.get("LogPattern") is not None:
        import capo_application_insights.types.log_pattern

        out["log_pattern"] = (
            capo_application_insights.types.log_pattern.deserialize_cbor(
                data["LogPattern"]
            )
        )
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    return out
