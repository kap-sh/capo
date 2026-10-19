"""Generated from Smithy shape ``com.amazonaws.novaact#InvokeActStepRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.call_results
    import capo_nova_act.types.uuid_string
    import capo_nova_act.types.workflow_definition_name


class InvokeActStepRequest(TypedDict, closed=True):
    workflow_definition_name: (
        "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition containing the act.</p>"""
    workflow_run_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run containing the act.</p>"""
    session_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the session containing the act.</p>"""
    act_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the act to invoke the next step for.</p>"""
    call_results: "capo_nova_act.types.call_results.CallResults"
    """<p>The results from previous tool calls that the act requested.</p>"""
    previous_step_id: NotRequired["capo_nova_act.types.uuid_string.UuidString"]
    """<p>The identifier of the previous step, used for tracking execution flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeActStepRequest) -> dict:
    out: dict = {}
    import capo_nova_act.types.call_results

    out["callResults"] = capo_nova_act.types.call_results.serialize_json(
        value["call_results"]
    )
    if "previous_step_id" in value:
        out["previousStepId"] = value["previous_step_id"]
    return out


def deserialize_json(data: dict) -> InvokeActStepRequest:
    out: InvokeActStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("callResults") is not None:
        import capo_nova_act.types.call_results

        out["call_results"] = capo_nova_act.types.call_results.deserialize_json(
            data["callResults"]
        )
    else:
        out["call_results"] = []
    if data.get("previousStepId") is not None:
        out["previous_step_id"] = data["previousStepId"]
    return out


def redact_sensitive(value: InvokeActStepRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "call_results" in value:
        import capo_nova_act.types.call_results

        out["call_results"] = capo_nova_act.types.call_results.redact_sensitive(
            value["call_results"]
        )
    return out
