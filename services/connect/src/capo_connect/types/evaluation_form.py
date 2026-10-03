"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationForm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.evaluation_form_ai_version
    import capo_connect.types.evaluation_form_auto_evaluation_configuration
    import capo_connect.types.evaluation_form_description
    import capo_connect.types.evaluation_form_items_list
    import capo_connect.types.evaluation_form_language_configuration
    import capo_connect.types.evaluation_form_scoring_strategy
    import capo_connect.types.evaluation_form_target_configuration
    import capo_connect.types.evaluation_form_title
    import capo_connect.types.evaluation_form_validation_status
    import capo_connect.types.evaluation_form_version_is_locked
    import capo_connect.types.evaluation_form_version_status
    import capo_connect.types.evaluation_review_configuration
    import capo_connect.types.resource_id
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp
    import capo_connect.types.version_number


class EvaluationForm(TypedDict, closed=True):
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_version: "capo_connect.types.version_number.VersionNumber"
    """<p>A version of the evaluation form.</p>"""
    locked: "capo_connect.types.evaluation_form_version_is_locked.EvaluationFormVersionIsLocked"
    """<p>The flag indicating whether the evaluation form is locked for changes.</p>"""
    evaluation_form_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the evaluation form resource.</p>"""
    title: "capo_connect.types.evaluation_form_title.EvaluationFormTitle"
    """<p>A title of the evaluation form.</p>"""
    description: NotRequired[
        "capo_connect.types.evaluation_form_description.EvaluationFormDescription"
    ]
    """<p>The description of the evaluation form.</p>"""
    status: (
        "capo_connect.types.evaluation_form_version_status.EvaluationFormVersionStatus"
    )
    """<p>The status of the evaluation form.</p>"""
    items: "capo_connect.types.evaluation_form_items_list.EvaluationFormItemsList"
    """<p>Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section.</p>"""
    scoring_strategy: NotRequired[
        "capo_connect.types.evaluation_form_scoring_strategy.EvaluationFormScoringStrategy"
    ]
    """<p>A scoring strategy of the evaluation form.</p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation form was created.</p>"""
    created_by: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who created the evaluation form.</p>"""
    last_modified_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation form was last updated.</p>"""
    last_modified_by: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the evaluation form.</p>"""
    auto_evaluation_configuration: NotRequired[
        "capo_connect.types.evaluation_form_auto_evaluation_configuration.EvaluationFormAutoEvaluationConfiguration"
    ]
    """<p>The automatic evaluation configuration of an evaluation form.</p>"""
    review_configuration: NotRequired[
        "capo_connect.types.evaluation_review_configuration.EvaluationReviewConfiguration"
    ]
    """<p>Configuration for evaluation review settings of this evaluation form.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    target_configuration: NotRequired[
        "capo_connect.types.evaluation_form_target_configuration.EvaluationFormTargetConfiguration"
    ]
    """<p>Configuration that specifies the target for this evaluation form.</p>"""
    language_configuration: NotRequired[
        "capo_connect.types.evaluation_form_language_configuration.EvaluationFormLanguageConfiguration"
    ]
    """<p>Configuration for language settings of this evaluation form.</p>"""
    latest_validation_status: NotRequired[
        "capo_connect.types.evaluation_form_validation_status.EvaluationFormValidationStatus"
    ]
    """<p>The status of the most recent validation run for this evaluation form. Valid values: <code>IN_PROGRESS</code>, <code>COMPLETED</code>, <code>FAILED</code>.</p>"""
    last_validation_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the most recent validation was started for this evaluation form.</p>"""
    ai_version: NotRequired[
        "capo_connect.types.evaluation_form_ai_version.EvaluationFormAIVersion"
    ]
    """<p>The AI version to use for the evaluation form. This specifies which AI model version is used for automated evaluations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationForm) -> dict:
    out: dict = {}
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormVersion"] = value.get("evaluation_form_version", 0)
    out["Locked"] = value.get("locked", False)
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_connect.types.evaluation_form_version_status

    out["Status"] = capo_connect.types.evaluation_form_version_status.serialize_json(
        value["status"]
    )
    import capo_connect.types.evaluation_form_items_list

    out["Items"] = capo_connect.types.evaluation_form_items_list.serialize_json(
        value["items"]
    )
    if "scoring_strategy" in value:
        import capo_connect.types.evaluation_form_scoring_strategy

        out["ScoringStrategy"] = (
            capo_connect.types.evaluation_form_scoring_strategy.serialize_json(
                value["scoring_strategy"]
            )
        )
    import capo_connect.types.timestamp

    out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    out["CreatedBy"] = value["created_by"]
    import capo_connect.types.timestamp

    out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    out["LastModifiedBy"] = value["last_modified_by"]
    if "auto_evaluation_configuration" in value:
        import capo_connect.types.evaluation_form_auto_evaluation_configuration

        out["AutoEvaluationConfiguration"] = (
            capo_connect.types.evaluation_form_auto_evaluation_configuration.serialize_json(
                value["auto_evaluation_configuration"]
            )
        )
    if "review_configuration" in value:
        import capo_connect.types.evaluation_review_configuration

        out["ReviewConfiguration"] = (
            capo_connect.types.evaluation_review_configuration.serialize_json(
                value["review_configuration"]
            )
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "target_configuration" in value:
        import capo_connect.types.evaluation_form_target_configuration

        out["TargetConfiguration"] = (
            capo_connect.types.evaluation_form_target_configuration.serialize_json(
                value["target_configuration"]
            )
        )
    if "language_configuration" in value:
        import capo_connect.types.evaluation_form_language_configuration

        out["LanguageConfiguration"] = (
            capo_connect.types.evaluation_form_language_configuration.serialize_json(
                value["language_configuration"]
            )
        )
    if "latest_validation_status" in value:
        import capo_connect.types.evaluation_form_validation_status

        out["LatestValidationStatus"] = (
            capo_connect.types.evaluation_form_validation_status.serialize_json(
                value["latest_validation_status"]
            )
        )
    if "last_validation_time" in value:
        import capo_connect.types.timestamp

        out["LastValidationTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_validation_time"]
        )
    if "ai_version" in value:
        out["AIVersion"] = value["ai_version"]
    return out


def deserialize_json(data: dict) -> EvaluationForm:
    out: EvaluationForm = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationFormId") is not None:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        raise DeserializationError("EvaluationForm.evaluation_form_id required")
    if data.get("EvaluationFormVersion") is not None:
        out["evaluation_form_version"] = data["EvaluationFormVersion"]
    else:
        out["evaluation_form_version"] = 0
    if data.get("Locked") is not None:
        out["locked"] = data["Locked"]
    else:
        out["locked"] = False
    if data.get("EvaluationFormArn") is not None:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        raise DeserializationError("EvaluationForm.evaluation_form_arn required")
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("EvaluationForm.title required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_connect.types.evaluation_form_version_status

        out["status"] = (
            capo_connect.types.evaluation_form_version_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("EvaluationForm.status required")
    if data.get("Items") is not None:
        import capo_connect.types.evaluation_form_items_list

        out["items"] = capo_connect.types.evaluation_form_items_list.deserialize_json(
            data["Items"]
        )
    else:
        raise DeserializationError("EvaluationForm.items required")
    if data.get("ScoringStrategy") is not None:
        import capo_connect.types.evaluation_form_scoring_strategy

        out["scoring_strategy"] = (
            capo_connect.types.evaluation_form_scoring_strategy.deserialize_json(
                data["ScoringStrategy"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("EvaluationForm.created_time required")
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    else:
        raise DeserializationError("EvaluationForm.created_by required")
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        raise DeserializationError("EvaluationForm.last_modified_time required")
    if data.get("LastModifiedBy") is not None:
        out["last_modified_by"] = data["LastModifiedBy"]
    else:
        raise DeserializationError("EvaluationForm.last_modified_by required")
    if data.get("AutoEvaluationConfiguration") is not None:
        import capo_connect.types.evaluation_form_auto_evaluation_configuration

        out["auto_evaluation_configuration"] = (
            capo_connect.types.evaluation_form_auto_evaluation_configuration.deserialize_json(
                data["AutoEvaluationConfiguration"]
            )
        )
    if data.get("ReviewConfiguration") is not None:
        import capo_connect.types.evaluation_review_configuration

        out["review_configuration"] = (
            capo_connect.types.evaluation_review_configuration.deserialize_json(
                data["ReviewConfiguration"]
            )
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("TargetConfiguration") is not None:
        import capo_connect.types.evaluation_form_target_configuration

        out["target_configuration"] = (
            capo_connect.types.evaluation_form_target_configuration.deserialize_json(
                data["TargetConfiguration"]
            )
        )
    if data.get("LanguageConfiguration") is not None:
        import capo_connect.types.evaluation_form_language_configuration

        out["language_configuration"] = (
            capo_connect.types.evaluation_form_language_configuration.deserialize_json(
                data["LanguageConfiguration"]
            )
        )
    if data.get("LatestValidationStatus") is not None:
        import capo_connect.types.evaluation_form_validation_status

        out["latest_validation_status"] = (
            capo_connect.types.evaluation_form_validation_status.deserialize_json(
                data["LatestValidationStatus"]
            )
        )
    if data.get("LastValidationTime") is not None:
        import capo_connect.types.timestamp

        out["last_validation_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastValidationTime"]
        )
    if data.get("AIVersion") is not None:
        out["ai_version"] = data["AIVersion"]
    return out
