"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationRulePreviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.next_token
    import capo_compute_optimizer_automation.types.preview_results


class ListAutomationRulePreviewResponse(TypedDict, closed=True):
    preview_results: NotRequired[
        "capo_compute_optimizer_automation.types.preview_results.PreviewResults"
    ]
    """<p> The list of actions that would be taken based on the specified criteria. </p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationRulePreviewResponse) -> dict:
    out: dict = {}
    if "preview_results" in value:
        import capo_compute_optimizer_automation.types.preview_results

        out["previewResults"] = (
            capo_compute_optimizer_automation.types.preview_results.serialize_aws_json_1_0(
                value["preview_results"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationRulePreviewResponse:
    out: ListAutomationRulePreviewResponse = {}  # type: ignore[typeddict-item]
    if data.get("previewResults") is not None:
        import capo_compute_optimizer_automation.types.preview_results

        out["preview_results"] = (
            capo_compute_optimizer_automation.types.preview_results.deserialize_aws_json_1_0(
                data["previewResults"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAutomationRulePreviewResponse) -> dict:
    out: dict = {}
    if "preview_results" in value:
        import capo_compute_optimizer_automation.types.preview_results

        out["previewResults"] = (
            capo_compute_optimizer_automation.types.preview_results.serialize_cbor(
                value["preview_results"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAutomationRulePreviewResponse:
    out: ListAutomationRulePreviewResponse = {}  # type: ignore[typeddict-item]
    if data.get("previewResults") is not None:
        import capo_compute_optimizer_automation.types.preview_results

        out["preview_results"] = (
            capo_compute_optimizer_automation.types.preview_results.deserialize_cbor(
                data["previewResults"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
