"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DevOpsAgentInvestigation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.dev_ops_agent_confidence
    import capo_resiliencehubv2.types.dev_ops_agent_investigation_status
    import capo_resiliencehubv2.types.dev_ops_agent_verdict


class DevOpsAgentInvestigation(TypedDict, closed=True):
    verdict: NotRequired[
        "capo_resiliencehubv2.types.dev_ops_agent_verdict.DevOpsAgentVerdict"
    ]
    """<p>The investigation verdict. Valid values:</p> <ul> <li> <p>PASS - The resilience test run passed.</p> </li> <li> <p>FAIL - The resilience test run failed.</p> </li> <li> <p>INCONCLUSIVE - The investigation could not determine a clear outcome.</p> </li> </ul>"""
    confidence: NotRequired[
        "capo_resiliencehubv2.types.dev_ops_agent_confidence.DevOpsAgentConfidence"
    ]
    """<p>The confidence level of the verdict. Valid values:</p> <ul> <li> <p>HIGH - The verdict is highly reliable.</p> </li> <li> <p>MEDIUM - The verdict has moderate reliability.</p> </li> <li> <p>LOW - The verdict has low reliability.</p> </li> </ul>"""
    deep_link: NotRequired["str"]
    """<p>A deep link to the interactive DevOps Agent investigation session.</p>"""
    status: NotRequired[
        "capo_resiliencehubv2.types.dev_ops_agent_investigation_status.DevOpsAgentInvestigationStatus"
    ]
    """<p>The lifecycle status of the investigation. Valid values:</p> <ul> <li> <p>PENDING - The investigation has been created but has not started.</p> </li> <li> <p>IN_PROGRESS - The investigation is running.</p> </li> <li> <p>COMPLETED - The investigation finished successfully.</p> </li> <li> <p>FAILED - The investigation failed to complete.</p> </li> <li> <p>TIMED_OUT - The investigation did not complete within the allotted time.</p> </li> <li> <p>CANCELED - The investigation was canceled.</p> </li> </ul>"""
    summary: NotRequired["str"]
    """<p>The DevOps Agent analysis summary for the investigation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DevOpsAgentInvestigation) -> dict:
    out: dict = {}
    if "verdict" in value:
        import capo_resiliencehubv2.types.dev_ops_agent_verdict

        out["verdict"] = (
            capo_resiliencehubv2.types.dev_ops_agent_verdict.serialize_json(
                value["verdict"]
            )
        )
    if "confidence" in value:
        import capo_resiliencehubv2.types.dev_ops_agent_confidence

        out["confidence"] = (
            capo_resiliencehubv2.types.dev_ops_agent_confidence.serialize_json(
                value["confidence"]
            )
        )
    if "deep_link" in value:
        out["deepLink"] = value["deep_link"]
    if "status" in value:
        import capo_resiliencehubv2.types.dev_ops_agent_investigation_status

        out["status"] = (
            capo_resiliencehubv2.types.dev_ops_agent_investigation_status.serialize_json(
                value["status"]
            )
        )
    if "summary" in value:
        out["summary"] = value["summary"]
    return out


def deserialize_json(data: dict) -> DevOpsAgentInvestigation:
    out: DevOpsAgentInvestigation = {}  # type: ignore[typeddict-item]
    if data.get("verdict") is not None:
        import capo_resiliencehubv2.types.dev_ops_agent_verdict

        out["verdict"] = (
            capo_resiliencehubv2.types.dev_ops_agent_verdict.deserialize_json(
                data["verdict"]
            )
        )
    if data.get("confidence") is not None:
        import capo_resiliencehubv2.types.dev_ops_agent_confidence

        out["confidence"] = (
            capo_resiliencehubv2.types.dev_ops_agent_confidence.deserialize_json(
                data["confidence"]
            )
        )
    if data.get("deepLink") is not None:
        out["deep_link"] = data["deepLink"]
    if data.get("status") is not None:
        import capo_resiliencehubv2.types.dev_ops_agent_investigation_status

        out["status"] = (
            capo_resiliencehubv2.types.dev_ops_agent_investigation_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    return out
