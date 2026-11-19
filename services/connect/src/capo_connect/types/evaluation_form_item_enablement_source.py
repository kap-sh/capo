"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_ai_metrics_field
    import capo_connect.types.evaluation_form_contact_attribute_key
    import capo_connect.types.evaluation_form_contact_field
    import capo_connect.types.evaluation_form_evaluation_metadata_field
    import capo_connect.types.evaluation_form_item_enablement_source_type
    import capo_connect.types.evaluation_form_segment_attribute_key
    import capo_connect.types.reference_id


class EvaluationFormItemEnablementSource(TypedDict, closed=True):
    type: "capo_connect.types.evaluation_form_item_enablement_source_type.EvaluationFormItemEnablementSourceType"
    """<p>A type of source item. Valid values:</p> <ul> <li> <p> <code>QUESTION_REF_ID</code> - The answer to another question in the evaluation form.</p> </li> <li> <p> <code>CONTACT</code> - Data from the evaluated contact.</p> </li> <li> <p> <code>EVALUATION_METADATA</code> - Metadata of the evaluation, such as the evaluation type.</p> </li> <li> <p> <code>AI_METRICS</code> - Metrics about AI agents, AI sessions, and AI tools on the contact.</p> </li> </ul>"""
    ref_id: NotRequired["capo_connect.types.reference_id.ReferenceId"]
    """<p>A referenceId of the source item. Use when <code>Type</code> is <code>QUESTION_REF_ID</code>.</p>"""
    contact_field: NotRequired[
        "capo_connect.types.evaluation_form_contact_field.EvaluationFormContactField"
    ]
    """<p>The contact field to use as the source, such as <code>CHANNEL</code>, <code>QUEUE_ARN</code>, <code>OVERALL_CUSTOMER_SENTIMENT_SCORE</code>, or <code>RECORDING_MEDIA_STREAM_TYPES</code>. Use when <code>Type</code> is <code>CONTACT</code>.</p>"""
    contact_attribute_key: NotRequired[
        "capo_connect.types.evaluation_form_contact_attribute_key.EvaluationFormContactAttributeKey"
    ]
    """<p>The key of the contact attribute to use as the source. Use when <code>Type</code> is <code>CONTACT</code>.</p>"""
    segment_attribute_key: NotRequired[
        "capo_connect.types.evaluation_form_segment_attribute_key.EvaluationFormSegmentAttributeKey"
    ]
    """<p>The key of the contact segment attribute to use as the source. Use when <code>Type</code> is <code>CONTACT</code>.</p>"""
    evaluation_metadata_field: NotRequired[
        "capo_connect.types.evaluation_form_evaluation_metadata_field.EvaluationFormEvaluationMetadataField"
    ]
    """<p>The evaluation metadata field to use as the source. Use when <code>Type</code> is <code>EVALUATION_METADATA</code>.</p>"""
    ai_metrics_field: NotRequired[
        "capo_connect.types.evaluation_form_ai_metrics_field.EvaluationFormAiMetricsField"
    ]
    """<p>The AI metrics field to use as the source. Use when <code>Type</code> is <code>AI_METRICS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementSource) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_item_enablement_source_type

    out["Type"] = (
        capo_connect.types.evaluation_form_item_enablement_source_type.serialize_json(
            value["type"]
        )
    )
    if "ref_id" in value:
        out["RefId"] = value["ref_id"]
    if "contact_field" in value:
        import capo_connect.types.evaluation_form_contact_field

        out["ContactField"] = (
            capo_connect.types.evaluation_form_contact_field.serialize_json(
                value["contact_field"]
            )
        )
    if "contact_attribute_key" in value:
        out["ContactAttributeKey"] = value["contact_attribute_key"]
    if "segment_attribute_key" in value:
        out["SegmentAttributeKey"] = value["segment_attribute_key"]
    if "evaluation_metadata_field" in value:
        import capo_connect.types.evaluation_form_evaluation_metadata_field

        out["EvaluationMetadataField"] = (
            capo_connect.types.evaluation_form_evaluation_metadata_field.serialize_json(
                value["evaluation_metadata_field"]
            )
        )
    if "ai_metrics_field" in value:
        import capo_connect.types.evaluation_form_ai_metrics_field

        out["AiMetricsField"] = (
            capo_connect.types.evaluation_form_ai_metrics_field.serialize_json(
                value["ai_metrics_field"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormItemEnablementSource:
    out: EvaluationFormItemEnablementSource = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_connect.types.evaluation_form_item_enablement_source_type

        out["type"] = (
            capo_connect.types.evaluation_form_item_enablement_source_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_connect.types.evaluation_form_item_enablement_source_type.EvaluationFormItemEnablementSourceType",
            "",
        )
    if data.get("RefId") is not None:
        out["ref_id"] = data["RefId"]
    if data.get("ContactField") is not None:
        import capo_connect.types.evaluation_form_contact_field

        out["contact_field"] = (
            capo_connect.types.evaluation_form_contact_field.deserialize_json(
                data["ContactField"]
            )
        )
    if data.get("ContactAttributeKey") is not None:
        out["contact_attribute_key"] = data["ContactAttributeKey"]
    if data.get("SegmentAttributeKey") is not None:
        out["segment_attribute_key"] = data["SegmentAttributeKey"]
    if data.get("EvaluationMetadataField") is not None:
        import capo_connect.types.evaluation_form_evaluation_metadata_field

        out["evaluation_metadata_field"] = (
            capo_connect.types.evaluation_form_evaluation_metadata_field.deserialize_json(
                data["EvaluationMetadataField"]
            )
        )
    if data.get("AiMetricsField") is not None:
        import capo_connect.types.evaluation_form_ai_metrics_field

        out["ai_metrics_field"] = (
            capo_connect.types.evaluation_form_ai_metrics_field.deserialize_json(
                data["AiMetricsField"]
            )
        )
    return out
