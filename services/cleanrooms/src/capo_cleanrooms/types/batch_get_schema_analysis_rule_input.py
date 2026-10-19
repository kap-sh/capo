"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetSchemaAnalysisRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.schema_analysis_rule_request_list


class BatchGetSchemaAnalysisRuleInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The unique identifier of the collaboration that contains the schema analysis rule.</p>"""
    schema_analysis_rule_requests: "capo_cleanrooms.types.schema_analysis_rule_request_list.SchemaAnalysisRuleRequestList"
    """<p>The information that's necessary to retrieve a schema analysis rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSchemaAnalysisRuleInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.schema_analysis_rule_request_list

    out["schemaAnalysisRuleRequests"] = (
        capo_cleanrooms.types.schema_analysis_rule_request_list.serialize_json(
            value["schema_analysis_rule_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetSchemaAnalysisRuleInput:
    out: BatchGetSchemaAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("schemaAnalysisRuleRequests") is not None:
        import capo_cleanrooms.types.schema_analysis_rule_request_list

        out["schema_analysis_rule_requests"] = (
            capo_cleanrooms.types.schema_analysis_rule_request_list.deserialize_json(
                data["schemaAnalysisRuleRequests"]
            )
        )
    else:
        out["schema_analysis_rule_requests"] = []
    return out
