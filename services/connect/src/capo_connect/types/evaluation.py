"""Generated from Smithy shape ``com.amazonaws.connect#Evaluation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.evaluation_answers_output_map
    import capo_connect.types.evaluation_enablement_status_map
    import capo_connect.types.evaluation_item_resolution_status
    import capo_connect.types.evaluation_metadata
    import capo_connect.types.evaluation_notes_map
    import capo_connect.types.evaluation_resolved_source_list
    import capo_connect.types.evaluation_scores_map
    import capo_connect.types.evaluation_status
    import capo_connect.types.evaluation_type
    import capo_connect.types.resource_id
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp


class Evaluation(TypedDict, closed=True):
    evaluation_id: "capo_connect.types.resource_id.ResourceId"
    """<p>A unique identifier for the contact evaluation.</p>"""
    evaluation_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the contact evaluation resource.</p>"""
    metadata: "capo_connect.types.evaluation_metadata.EvaluationMetadata"
    """<p>Metadata about the contact evaluation.</p>"""
    answers: (
        "capo_connect.types.evaluation_answers_output_map.EvaluationAnswersOutputMap"
    )
    """<p>A map of question identifiers to answer value.</p>"""
    notes: "capo_connect.types.evaluation_notes_map.EvaluationNotesMap"
    """<p>A map of question identifiers to note value.</p>"""
    status: "capo_connect.types.evaluation_status.EvaluationStatus"
    """<p>The status of the contact evaluation.</p>"""
    scores: NotRequired["capo_connect.types.evaluation_scores_map.EvaluationScoresMap"]
    """<p>A map of item (section or question) identifiers to score value.</p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation was created.</p>"""
    last_modified_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation was last updated.</p>"""
    evaluation_type: NotRequired["capo_connect.types.evaluation_type.EvaluationType"]
    """<p>Type of the evaluation. </p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    item_enablement_status: NotRequired[
        "capo_connect.types.evaluation_enablement_status_map.EvaluationEnablementStatusMap"
    ]
    """<p>A map of item (section or question) identifiers to their enablement status, computed by the service from each item's conditional enablement configuration. Disabled items are excluded from scoring. Valid values: <code>ENABLED</code> | <code>DISABLED</code>.</p>"""
    source_resolution_status: NotRequired[
        "capo_connect.types.evaluation_item_resolution_status.EvaluationItemResolutionStatus"
    ]
    """<p>The aggregate status of resolving the external source data (such as Contact Lens analysis and AI metrics) that is used by conditional enablement in the evaluation. Source data is resolved asynchronously after the evaluation is started. While a source is pending or after it fails to resolve, conditions that depend on it evaluate to the item's <code>DefaultAction</code>. Valid values:</p> <ul> <li> <p> <code>PENDING</code> - One or more sources have not been resolved yet. Call <code>DescribeContactEvaluation</code> again to get updated <code>ItemEnablementStatus</code> values.</p> </li> <li> <p> <code>RESOLVED</code> - All sources have been resolved.</p> </li> <li> <p> <code>FAILED</code> - One or more sources could not be resolved. Dependent conditions use the item's <code>DefaultAction</code>.</p> </li> </ul>"""
    source_values: NotRequired[
        "capo_connect.types.evaluation_resolved_source_list.EvaluationResolvedSourceList"
    ]
    """<p>The resolved values of the external sources (such as contact data, evaluation metadata, form metadata, and AI metrics) that are used by the conditions in the evaluation form. You can use these values to evaluate the conditions against the current answers without calling <code>DescribeContactEvaluation</code> again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Evaluation) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    out["EvaluationArn"] = value["evaluation_arn"]
    import capo_connect.types.evaluation_metadata

    out["Metadata"] = capo_connect.types.evaluation_metadata.serialize_json(
        value["metadata"]
    )
    import capo_connect.types.evaluation_answers_output_map

    out["Answers"] = capo_connect.types.evaluation_answers_output_map.serialize_json(
        value["answers"]
    )
    import capo_connect.types.evaluation_notes_map

    out["Notes"] = capo_connect.types.evaluation_notes_map.serialize_json(
        value["notes"]
    )
    import capo_connect.types.evaluation_status

    out["Status"] = capo_connect.types.evaluation_status.serialize_json(value["status"])
    if "scores" in value:
        import capo_connect.types.evaluation_scores_map

        out["Scores"] = capo_connect.types.evaluation_scores_map.serialize_json(
            value["scores"]
        )
    import capo_connect.types.timestamp

    out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    import capo_connect.types.timestamp

    out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "evaluation_type" in value:
        import capo_connect.types.evaluation_type

        out["EvaluationType"] = capo_connect.types.evaluation_type.serialize_json(
            value["evaluation_type"]
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "item_enablement_status" in value:
        import capo_connect.types.evaluation_enablement_status_map

        out["ItemEnablementStatus"] = (
            capo_connect.types.evaluation_enablement_status_map.serialize_json(
                value["item_enablement_status"]
            )
        )
    if "source_resolution_status" in value:
        import capo_connect.types.evaluation_item_resolution_status

        out["SourceResolutionStatus"] = (
            capo_connect.types.evaluation_item_resolution_status.serialize_json(
                value["source_resolution_status"]
            )
        )
    if "source_values" in value:
        import capo_connect.types.evaluation_resolved_source_list

        out["SourceValues"] = (
            capo_connect.types.evaluation_resolved_source_list.serialize_json(
                value["source_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> Evaluation:
    out: Evaluation = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationId") is not None:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        out["evaluation_id"] = ""
    if data.get("EvaluationArn") is not None:
        out["evaluation_arn"] = data["EvaluationArn"]
    else:
        out["evaluation_arn"] = ""
    if data.get("Metadata") is not None:
        import capo_connect.types.evaluation_metadata

        out["metadata"] = capo_connect.types.evaluation_metadata.deserialize_json(
            data["Metadata"]
        )
    else:
        raise DeserializationError("Evaluation.metadata required")
    if data.get("Answers") is not None:
        import capo_connect.types.evaluation_answers_output_map

        out["answers"] = (
            capo_connect.types.evaluation_answers_output_map.deserialize_json(
                data["Answers"]
            )
        )
    else:
        out["answers"] = {}
    if data.get("Notes") is not None:
        import capo_connect.types.evaluation_notes_map

        out["notes"] = capo_connect.types.evaluation_notes_map.deserialize_json(
            data["Notes"]
        )
    else:
        out["notes"] = {}
    if data.get("Status") is not None:
        import capo_connect.types.evaluation_status

        out["status"] = capo_connect.types.evaluation_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connect.types.evaluation_status.EvaluationStatus", ""
        )
    if data.get("Scores") is not None:
        import capo_connect.types.evaluation_scores_map

        out["scores"] = capo_connect.types.evaluation_scores_map.deserialize_json(
            data["Scores"]
        )
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("EvaluationType") is not None:
        import capo_connect.types.evaluation_type

        out["evaluation_type"] = capo_connect.types.evaluation_type.deserialize_json(
            data["EvaluationType"]
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("ItemEnablementStatus") is not None:
        import capo_connect.types.evaluation_enablement_status_map

        out["item_enablement_status"] = (
            capo_connect.types.evaluation_enablement_status_map.deserialize_json(
                data["ItemEnablementStatus"]
            )
        )
    if data.get("SourceResolutionStatus") is not None:
        import capo_connect.types.evaluation_item_resolution_status

        out["source_resolution_status"] = (
            capo_connect.types.evaluation_item_resolution_status.deserialize_json(
                data["SourceResolutionStatus"]
            )
        )
    if data.get("SourceValues") is not None:
        import capo_connect.types.evaluation_resolved_source_list

        out["source_values"] = (
            capo_connect.types.evaluation_resolved_source_list.deserialize_json(
                data["SourceValues"]
            )
        )
    return out
