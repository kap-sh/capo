"""Generated from Smithy shape ``com.amazonaws.entityresolution#GenerateMatchIdInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.processing_type
    import capo_entityresolution.types.record_list


class GenerateMatchIdInput(TypedDict, closed=True):
    workflow_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p> The name of the rule-based matching workflow.</p>"""
    records: "capo_entityresolution.types.record_list.RecordList"
    """<p> The records to match.</p>"""
    processing_type: NotRequired[
        "capo_entityresolution.types.processing_type.ProcessingType"
    ]
    """<p>The processing mode that determines how Match IDs are generated and results are saved. Each mode provides different levels of accuracy, response time, and completeness of results.</p> <p>If not specified, defaults to <code>CONSISTENT</code>.</p> <p> <code>CONSISTENT</code>: Performs immediate lookup and matching against all existing records, with results saved synchronously. Provides highest accuracy but slower response time.</p> <p> <code>EVENTUAL</code> (shown as <i>Background</i> in the console): Performs initial match ID lookup or generation immediately, with record updates processed asynchronously in the background. Offers faster initial response time, with complete matching results available later in S3. </p> <p> <code>EVENTUAL_NO_LOOKUP</code> (shown as <i>Quick ID generation</i> in the console): Generates new match IDs without checking existing matches, with updates processed asynchronously. Provides fastest response time but should only be used for records known to be unique. </p> <note> <p>Advanced matching workflows don't support the <code>processingType</code> field.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateMatchIdInput) -> dict:
    out: dict = {}
    import capo_entityresolution.types.record_list

    out["records"] = capo_entityresolution.types.record_list.serialize_json(
        value["records"]
    )
    if "processing_type" in value:
        import capo_entityresolution.types.processing_type

        out["processingType"] = (
            capo_entityresolution.types.processing_type.serialize_json(
                value["processing_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> GenerateMatchIdInput:
    out: GenerateMatchIdInput = {}  # type: ignore[typeddict-item]
    if data.get("records") is not None:
        import capo_entityresolution.types.record_list

        out["records"] = capo_entityresolution.types.record_list.deserialize_json(
            data["records"]
        )
    else:
        out["records"] = []
    if data.get("processingType") is not None:
        import capo_entityresolution.types.processing_type

        out["processing_type"] = (
            capo_entityresolution.types.processing_type.deserialize_json(
                data["processingType"]
            )
        )
    return out


def redact_sensitive(value: GenerateMatchIdInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "records" in value:
        import capo_entityresolution.types.record_list

        out["records"] = capo_entityresolution.types.record_list.redact_sensitive(
            value["records"]
        )
    return out
