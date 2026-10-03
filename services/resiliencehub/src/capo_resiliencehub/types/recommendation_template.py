"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.boolean_optional
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.recommendation_id_list
    import capo_resiliencehub.types.recommendation_template_status
    import capo_resiliencehub.types.render_recommendation_type_list
    import capo_resiliencehub.types.s3_location
    import capo_resiliencehub.types.string500
    import capo_resiliencehub.types.tag_map
    import capo_resiliencehub.types.template_format
    import capo_resiliencehub.types.time_stamp


class RecommendationTemplate(TypedDict, closed=True):
    templates_location: NotRequired["capo_resiliencehub.types.s3_location.S3Location"]
    """<p>The file location of the template.</p>"""
    assessment_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    recommendation_ids: NotRequired[
        "capo_resiliencehub.types.recommendation_id_list.RecommendationIdList"
    ]
    """<p>Identifiers for the recommendations used in the recommendation template.</p>"""
    recommendation_types: "capo_resiliencehub.types.render_recommendation_type_list.RenderRecommendationTypeList"
    """<p>An array of strings that specify the recommendation template type or types.</p> <dl> <dt>Alarm</dt> <dd> <p>The template is an <a>AlarmRecommendation</a> template.</p> </dd> <dt>Sop</dt> <dd> <p>The template is a <a>SopRecommendation</a> template.</p> </dd> <dt>Test</dt> <dd> <p>The template is a <a>TestRecommendation</a> template.</p> </dd> </dl>"""
    format: "capo_resiliencehub.types.template_format.TemplateFormat"
    """<p>Format of the recommendation template.</p> <dl> <dt>CfnJson</dt> <dd> <p>The template is CloudFormation JSON.</p> </dd> <dt>CfnYaml</dt> <dd> <p>The template is CloudFormation YAML.</p> </dd> </dl>"""
    recommendation_template_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) for the recommendation template.</p>"""
    message: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Message for the recommendation template.</p>"""
    status: "capo_resiliencehub.types.recommendation_template_status.RecommendationTemplateStatus"
    """<p>Status of the action.</p>"""
    name: "capo_resiliencehub.types.entity_name.EntityName"
    """<p>Name for the recommendation template.</p>"""
    start_time: NotRequired["capo_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>The start time for the action.</p>"""
    end_time: NotRequired["capo_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>The end time for the action.</p>"""
    tags: NotRequired["capo_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""
    needs_replacements: NotRequired[
        "capo_resiliencehub.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates if replacements are needed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTemplate) -> dict:
    out: dict = {}
    if "templates_location" in value:
        import capo_resiliencehub.types.s3_location

        out["templatesLocation"] = capo_resiliencehub.types.s3_location.serialize_json(
            value["templates_location"]
        )
    out["assessmentArn"] = value["assessment_arn"]
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "recommendation_ids" in value:
        import capo_resiliencehub.types.recommendation_id_list

        out["recommendationIds"] = (
            capo_resiliencehub.types.recommendation_id_list.serialize_json(
                value["recommendation_ids"]
            )
        )
    import capo_resiliencehub.types.render_recommendation_type_list

    out["recommendationTypes"] = (
        capo_resiliencehub.types.render_recommendation_type_list.serialize_json(
            value["recommendation_types"]
        )
    )
    import capo_resiliencehub.types.template_format

    out["format"] = capo_resiliencehub.types.template_format.serialize_json(
        value["format"]
    )
    out["recommendationTemplateArn"] = value["recommendation_template_arn"]
    if "message" in value:
        out["message"] = value["message"]
    import capo_resiliencehub.types.recommendation_template_status

    out["status"] = (
        capo_resiliencehub.types.recommendation_template_status.serialize_json(
            value["status"]
        )
    )
    out["name"] = value["name"]
    if "start_time" in value:
        import capo_resiliencehub.types.time_stamp

        out["startTime"] = capo_resiliencehub.types.time_stamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_resiliencehub.types.time_stamp

        out["endTime"] = capo_resiliencehub.types.time_stamp.serialize_json(
            value["end_time"]
        )
    if "tags" in value:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.serialize_json(value["tags"])
    if "needs_replacements" in value:
        out["needsReplacements"] = value["needs_replacements"]
    return out


def deserialize_json(data: dict) -> RecommendationTemplate:
    out: RecommendationTemplate = {}  # type: ignore[typeddict-item]
    if data.get("templatesLocation") is not None:
        import capo_resiliencehub.types.s3_location

        out["templates_location"] = (
            capo_resiliencehub.types.s3_location.deserialize_json(
                data["templatesLocation"]
            )
        )
    if data.get("assessmentArn") is not None:
        out["assessment_arn"] = data["assessmentArn"]
    else:
        raise DeserializationError("RecommendationTemplate.assessment_arn required")
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    if data.get("recommendationIds") is not None:
        import capo_resiliencehub.types.recommendation_id_list

        out["recommendation_ids"] = (
            capo_resiliencehub.types.recommendation_id_list.deserialize_json(
                data["recommendationIds"]
            )
        )
    if data.get("recommendationTypes") is not None:
        import capo_resiliencehub.types.render_recommendation_type_list

        out["recommendation_types"] = (
            capo_resiliencehub.types.render_recommendation_type_list.deserialize_json(
                data["recommendationTypes"]
            )
        )
    else:
        raise DeserializationError(
            "RecommendationTemplate.recommendation_types required"
        )
    if data.get("format") is not None:
        import capo_resiliencehub.types.template_format

        out["format"] = capo_resiliencehub.types.template_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("RecommendationTemplate.format required")
    if data.get("recommendationTemplateArn") is not None:
        out["recommendation_template_arn"] = data["recommendationTemplateArn"]
    else:
        raise DeserializationError(
            "RecommendationTemplate.recommendation_template_arn required"
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("status") is not None:
        import capo_resiliencehub.types.recommendation_template_status

        out["status"] = (
            capo_resiliencehub.types.recommendation_template_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("RecommendationTemplate.status required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RecommendationTemplate.name required")
    if data.get("startTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["start_time"] = capo_resiliencehub.types.time_stamp.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["end_time"] = capo_resiliencehub.types.time_stamp.deserialize_json(
            data["endTime"]
        )
    if data.get("tags") is not None:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.deserialize_json(data["tags"])
    if data.get("needsReplacements") is not None:
        out["needs_replacements"] = data["needsReplacements"]
    return out
