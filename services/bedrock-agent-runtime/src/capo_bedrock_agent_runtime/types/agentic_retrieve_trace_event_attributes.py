"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveTraceEventAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_actions
    import capo_bedrock_agent_runtime.types.agentic_retrieve_failures
    import capo_bedrock_agent_runtime.types.agentic_retrieve_source_metadata_list
    import capo_bedrock_agent_runtime.types.agentic_retrieve_status
    import capo_bedrock_agent_runtime.types.agentic_retrieve_step
    import capo_bedrock_agent_runtime.types.agentic_retrieve_trace_results
    import capo_bedrock_agent_runtime.types.agentic_retrieve_warnings


class AgenticRetrieveTraceEventAttributes(TypedDict, closed=True):
    step: "capo_bedrock_agent_runtime.types.agentic_retrieve_step.AgenticRetrieveStep"
    """<p>The current step in the retrieval process.</p>"""
    status: (
        "capo_bedrock_agent_runtime.types.agentic_retrieve_status.AgenticRetrieveStatus"
    )
    """<p>The status of the current step.</p>"""
    message: "str"
    """<p>A human-readable message describing the trace event.</p>"""
    actions: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_actions.AgenticRetrieveActions"
    ]
    """<p>The list of actions taken during this step.</p>"""
    warnings: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_warnings.AgenticRetrieveWarnings"
    ]
    """<p>Warnings generated during this step.</p>"""
    failures: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_failures.AgenticRetrieveFailures"
    ]
    """<p>Failures that occurred during this step.</p>"""
    retrieval_metadata: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_source_metadata_list.AgenticRetrieveSourceMetadataList"
    ]
    """<p>Metadata about the retrieval sources used.</p>"""
    retrieval_response: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_trace_results.AgenticRetrieveTraceResults"
    ]
    """<p>The retrieval results from this step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveTraceEventAttributes) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.agentic_retrieve_step

    out["step"] = capo_bedrock_agent_runtime.types.agentic_retrieve_step.serialize_json(
        value["step"]
    )
    import capo_bedrock_agent_runtime.types.agentic_retrieve_status

    out["status"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_status.serialize_json(
            value["status"]
        )
    )
    out["message"] = value["message"]
    if "actions" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_actions

        out["actions"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_actions.serialize_json(
                value["actions"]
            )
        )
    if "warnings" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_warnings

        out["warnings"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_warnings.serialize_json(
                value["warnings"]
            )
        )
    if "failures" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_failures

        out["failures"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_failures.serialize_json(
                value["failures"]
            )
        )
    if "retrieval_metadata" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_source_metadata_list

        out["retrievalMetadata"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_source_metadata_list.serialize_json(
                value["retrieval_metadata"]
            )
        )
    if "retrieval_response" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_trace_results

        out["retrievalResponse"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_trace_results.serialize_json(
                value["retrieval_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveTraceEventAttributes:
    out: AgenticRetrieveTraceEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("step") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_step

        out["step"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_step.deserialize_json(
                data["step"]
            )
        )
    else:
        raise DeserializationError("AgenticRetrieveTraceEventAttributes.step required")
    if data.get("status") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_status

        out["status"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "AgenticRetrieveTraceEventAttributes.status required"
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "AgenticRetrieveTraceEventAttributes.message required"
        )
    if data.get("actions") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_actions

        out["actions"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_actions.deserialize_json(
                data["actions"]
            )
        )
    if data.get("warnings") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_warnings

        out["warnings"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_warnings.deserialize_json(
                data["warnings"]
            )
        )
    if data.get("failures") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_failures

        out["failures"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_failures.deserialize_json(
                data["failures"]
            )
        )
    if data.get("retrievalMetadata") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_source_metadata_list

        out["retrieval_metadata"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_source_metadata_list.deserialize_json(
                data["retrievalMetadata"]
            )
        )
    if data.get("retrievalResponse") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_trace_results

        out["retrieval_response"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_trace_results.deserialize_json(
                data["retrievalResponse"]
            )
        )
    return out


def redact_sensitive(value: AgenticRetrieveTraceEventAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "actions" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_actions

        out["actions"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_actions.redact_sensitive(
                value["actions"]
            )
        )
    return out
