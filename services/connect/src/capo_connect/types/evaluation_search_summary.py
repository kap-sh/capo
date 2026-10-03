"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSearchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.evaluation_form_title
    import capo_connect.types.evaluation_search_metadata
    import capo_connect.types.evaluation_status
    import capo_connect.types.evaluation_type
    import capo_connect.types.resource_id
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp
    import capo_connect.types.version_number


class EvaluationSearchSummary(TypedDict, closed=True):
    evaluation_id: "capo_connect.types.resource_id.ResourceId"
    """<p>A unique identifier for the contact evaluation.</p>"""
    evaluation_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the contact evaluation resource.</p>"""
    evaluation_form_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_version: "capo_connect.types.version_number.VersionNumber"
    """<p>A version of the evaluation form.</p>"""
    evaluation_form_title: NotRequired[
        "capo_connect.types.evaluation_form_title.EvaluationFormTitle"
    ]
    """<p>Title of the evaluation form.</p>"""
    metadata: "capo_connect.types.evaluation_search_metadata.EvaluationSearchMetadata"
    """<p>Summary information about the evaluation search.</p>"""
    status: "capo_connect.types.evaluation_status.EvaluationStatus"
    """<p>The status of the evaluation. </p>"""
    evaluation_type: NotRequired["capo_connect.types.evaluation_type.EvaluationType"]
    """<p>Type of the evaluation. </p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The date and time when the evaluation was created, in UTC time.</p>"""
    last_modified_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The date and time when the evaluation was modified last time, in UTC time.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSearchSummary) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    out["EvaluationArn"] = value["evaluation_arn"]
    if "evaluation_form_id" in value:
        out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormVersion"] = value["evaluation_form_version"]
    if "evaluation_form_title" in value:
        out["EvaluationFormTitle"] = value["evaluation_form_title"]
    import capo_connect.types.evaluation_search_metadata

    out["Metadata"] = capo_connect.types.evaluation_search_metadata.serialize_json(
        value["metadata"]
    )
    import capo_connect.types.evaluation_status

    out["Status"] = capo_connect.types.evaluation_status.serialize_json(value["status"])
    if "evaluation_type" in value:
        import capo_connect.types.evaluation_type

        out["EvaluationType"] = capo_connect.types.evaluation_type.serialize_json(
            value["evaluation_type"]
        )
    import capo_connect.types.timestamp

    out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    import capo_connect.types.timestamp

    out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> EvaluationSearchSummary:
    out: EvaluationSearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationId") is not None:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        raise DeserializationError("EvaluationSearchSummary.evaluation_id required")
    if data.get("EvaluationArn") is not None:
        out["evaluation_arn"] = data["EvaluationArn"]
    else:
        raise DeserializationError("EvaluationSearchSummary.evaluation_arn required")
    if data.get("EvaluationFormId") is not None:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    if data.get("EvaluationFormVersion") is not None:
        out["evaluation_form_version"] = data["EvaluationFormVersion"]
    else:
        raise DeserializationError(
            "EvaluationSearchSummary.evaluation_form_version required"
        )
    if data.get("EvaluationFormTitle") is not None:
        out["evaluation_form_title"] = data["EvaluationFormTitle"]
    if data.get("Metadata") is not None:
        import capo_connect.types.evaluation_search_metadata

        out["metadata"] = (
            capo_connect.types.evaluation_search_metadata.deserialize_json(
                data["Metadata"]
            )
        )
    else:
        raise DeserializationError("EvaluationSearchSummary.metadata required")
    if data.get("Status") is not None:
        import capo_connect.types.evaluation_status

        out["status"] = capo_connect.types.evaluation_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("EvaluationSearchSummary.status required")
    if data.get("EvaluationType") is not None:
        import capo_connect.types.evaluation_type

        out["evaluation_type"] = capo_connect.types.evaluation_type.deserialize_json(
            data["EvaluationType"]
        )
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("EvaluationSearchSummary.created_time required")
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        raise DeserializationError(
            "EvaluationSearchSummary.last_modified_time required"
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
