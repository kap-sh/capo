"""Generated from Smithy shape ``com.amazonaws.resiliencehub#CreateRecommendationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.client_token
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.recommendation_id_list
    import capo_resiliencehub.types.render_recommendation_type_list
    import capo_resiliencehub.types.tag_map
    import capo_resiliencehub.types.template_format


class CreateRecommendationTemplateRequest(TypedDict, closed=True):
    recommendation_ids: NotRequired[
        "capo_resiliencehub.types.recommendation_id_list.RecommendationIdList"
    ]
    """<p>Identifiers for the recommendations used to create a recommendation template.</p>"""
    format: NotRequired["capo_resiliencehub.types.template_format.TemplateFormat"]
    """<p>The format for the recommendation template.</p> <dl> <dt>CfnJson</dt> <dd> <p>The template is CloudFormation JSON.</p> </dd> <dt>CfnYaml</dt> <dd> <p>The template is CloudFormation YAML.</p> </dd> </dl>"""
    recommendation_types: NotRequired[
        "capo_resiliencehub.types.render_recommendation_type_list.RenderRecommendationTypeList"
    ]
    """<p>An array of strings that specify the recommendation template type or types.</p> <dl> <dt>Alarm</dt> <dd> <p>The template is an <a>AlarmRecommendation</a> template.</p> </dd> <dt>Sop</dt> <dd> <p>The template is a <a>SopRecommendation</a> template.</p> </dd> <dt>Test</dt> <dd> <p>The template is a <a>TestRecommendation</a> template.</p> </dd> </dl>"""
    assessment_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    name: "capo_resiliencehub.types.entity_name.EntityName"
    """<p>The name for the recommendation template.</p>"""
    client_token: NotRequired["capo_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""
    tags: NotRequired["capo_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""
    bucket_name: NotRequired["capo_resiliencehub.types.entity_name.EntityName"]
    """<p>The name of the Amazon S3 bucket that will contain the recommendation template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommendationTemplateRequest) -> dict:
    out: dict = {}
    if "recommendation_ids" in value:
        import capo_resiliencehub.types.recommendation_id_list

        out["recommendationIds"] = (
            capo_resiliencehub.types.recommendation_id_list.serialize_json(
                value["recommendation_ids"]
            )
        )
    if "format" in value:
        import capo_resiliencehub.types.template_format

        out["format"] = capo_resiliencehub.types.template_format.serialize_json(
            value["format"]
        )
    if "recommendation_types" in value:
        import capo_resiliencehub.types.render_recommendation_type_list

        out["recommendationTypes"] = (
            capo_resiliencehub.types.render_recommendation_type_list.serialize_json(
                value["recommendation_types"]
            )
        )
    out["assessmentArn"] = value["assessment_arn"]
    out["name"] = value["name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.serialize_json(value["tags"])
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    return out


def deserialize_json(data: dict) -> CreateRecommendationTemplateRequest:
    out: CreateRecommendationTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("recommendationIds") is not None:
        import capo_resiliencehub.types.recommendation_id_list

        out["recommendation_ids"] = (
            capo_resiliencehub.types.recommendation_id_list.deserialize_json(
                data["recommendationIds"]
            )
        )
    if data.get("format") is not None:
        import capo_resiliencehub.types.template_format

        out["format"] = capo_resiliencehub.types.template_format.deserialize_json(
            data["format"]
        )
    if data.get("recommendationTypes") is not None:
        import capo_resiliencehub.types.render_recommendation_type_list

        out["recommendation_types"] = (
            capo_resiliencehub.types.render_recommendation_type_list.deserialize_json(
                data["recommendationTypes"]
            )
        )
    if data.get("assessmentArn") is not None:
        out["assessment_arn"] = data["assessmentArn"]
    else:
        raise DeserializationError(
            "CreateRecommendationTemplateRequest.assessment_arn required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRecommendationTemplateRequest.name required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_resiliencehub.types.tag_map

        out["tags"] = capo_resiliencehub.types.tag_map.deserialize_json(data["tags"])
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    return out
