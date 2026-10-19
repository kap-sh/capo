"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

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
    import capo_connect.types.evaluation_review_configuration
    import capo_connect.types.resource_id
    import capo_connect.types.version_number


class EvaluationFormContent(TypedDict, closed=True):
    evaluation_form_version: "capo_connect.types.version_number.VersionNumber"
    """<p>A version of the evaluation form.</p>"""
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the evaluation form resource.</p>"""
    title: "capo_connect.types.evaluation_form_title.EvaluationFormTitle"
    """<p>A title of the evaluation form.</p>"""
    description: NotRequired[
        "capo_connect.types.evaluation_form_description.EvaluationFormDescription"
    ]
    """<p>The description of the evaluation form.</p>"""
    items: "capo_connect.types.evaluation_form_items_list.EvaluationFormItemsList"
    """<p>Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section.</p>"""
    scoring_strategy: NotRequired[
        "capo_connect.types.evaluation_form_scoring_strategy.EvaluationFormScoringStrategy"
    ]
    """<p>A scoring strategy of the evaluation form.</p>"""
    auto_evaluation_configuration: NotRequired[
        "capo_connect.types.evaluation_form_auto_evaluation_configuration.EvaluationFormAutoEvaluationConfiguration"
    ]
    """<p>The configuration of the automated evaluation.</p>"""
    target_configuration: NotRequired[
        "capo_connect.types.evaluation_form_target_configuration.EvaluationFormTargetConfiguration"
    ]
    """<p>Configuration that specifies the target for this evaluation form content.</p>"""
    language_configuration: NotRequired[
        "capo_connect.types.evaluation_form_language_configuration.EvaluationFormLanguageConfiguration"
    ]
    """<p>Configuration for language settings of this evaluation form content.</p>"""
    review_configuration: NotRequired[
        "capo_connect.types.evaluation_review_configuration.EvaluationReviewConfiguration"
    ]
    """<p>Configuration for evaluation review settings of this evaluation form content.</p>"""
    ai_version: NotRequired[
        "capo_connect.types.evaluation_form_ai_version.EvaluationFormAIVersion"
    ]
    """<p>The AI version to use for the evaluation form. This specifies which AI model version is used for automated evaluations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormContent) -> dict:
    out: dict = {}
    out["EvaluationFormVersion"] = value.get("evaluation_form_version", 0)
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "auto_evaluation_configuration" in value:
        import capo_connect.types.evaluation_form_auto_evaluation_configuration

        out["AutoEvaluationConfiguration"] = (
            capo_connect.types.evaluation_form_auto_evaluation_configuration.serialize_json(
                value["auto_evaluation_configuration"]
            )
        )
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
    if "review_configuration" in value:
        import capo_connect.types.evaluation_review_configuration

        out["ReviewConfiguration"] = (
            capo_connect.types.evaluation_review_configuration.serialize_json(
                value["review_configuration"]
            )
        )
    if "ai_version" in value:
        out["AIVersion"] = value["ai_version"]
    return out


def deserialize_json(data: dict) -> EvaluationFormContent:
    out: EvaluationFormContent = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationFormVersion") is not None:
        out["evaluation_form_version"] = data["EvaluationFormVersion"]
    else:
        out["evaluation_form_version"] = 0
    if data.get("EvaluationFormId") is not None:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        out["evaluation_form_id"] = ""
    if data.get("EvaluationFormArn") is not None:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        out["evaluation_form_arn"] = ""
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Items") is not None:
        import capo_connect.types.evaluation_form_items_list

        out["items"] = capo_connect.types.evaluation_form_items_list.deserialize_json(
            data["Items"]
        )
    else:
        out["items"] = []
    if data.get("ScoringStrategy") is not None:
        import capo_connect.types.evaluation_form_scoring_strategy

        out["scoring_strategy"] = (
            capo_connect.types.evaluation_form_scoring_strategy.deserialize_json(
                data["ScoringStrategy"]
            )
        )
    if data.get("AutoEvaluationConfiguration") is not None:
        import capo_connect.types.evaluation_form_auto_evaluation_configuration

        out["auto_evaluation_configuration"] = (
            capo_connect.types.evaluation_form_auto_evaluation_configuration.deserialize_json(
                data["AutoEvaluationConfiguration"]
            )
        )
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
    if data.get("ReviewConfiguration") is not None:
        import capo_connect.types.evaluation_review_configuration

        out["review_configuration"] = (
            capo_connect.types.evaluation_review_configuration.deserialize_json(
                data["ReviewConfiguration"]
            )
        )
    if data.get("AIVersion") is not None:
        out["ai_version"] = data["AIVersion"]
    return out
