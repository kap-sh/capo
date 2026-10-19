"""Generated from Smithy shape ``com.amazonaws.inspector#GetExclusionsPreviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.list_max_results
    import capo_inspector.types.locale
    import capo_inspector.types.pagination_token
    import capo_inspector.types.uuid


class GetExclusionsPreviewRequest(TypedDict, closed=True):
    assessment_template_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN that specifies the assessment template for which the exclusions preview was requested.</p>"""
    preview_token: "capo_inspector.types.uuid.UUID"
    """<p>The unique identifier associated of the exclusions preview.</p>"""
    next_token: NotRequired["capo_inspector.types.pagination_token.PaginationToken"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the GetExclusionsPreviewRequest action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.</p>"""
    max_results: NotRequired["capo_inspector.types.list_max_results.ListMaxResults"]
    """<p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 100. The maximum value is 500.</p>"""
    locale: NotRequired["capo_inspector.types.locale.Locale"]
    """<p>The locale into which you want to translate the exclusion's title, description, and recommendation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExclusionsPreviewRequest) -> dict:
    out: dict = {}
    out["assessmentTemplateArn"] = value["assessment_template_arn"]
    out["previewToken"] = value["preview_token"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "locale" in value:
        import capo_inspector.types.locale

        out["locale"] = capo_inspector.types.locale.serialize_aws_json_1_1(
            value["locale"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExclusionsPreviewRequest:
    out: GetExclusionsPreviewRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentTemplateArn") is not None:
        out["assessment_template_arn"] = data["assessmentTemplateArn"]
    else:
        out["assessment_template_arn"] = ""
    if data.get("previewToken") is not None:
        out["preview_token"] = data["previewToken"]
    else:
        out["preview_token"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("locale") is not None:
        import capo_inspector.types.locale

        out["locale"] = capo_inspector.types.locale.deserialize_aws_json_1_1(
            data["locale"]
        )
    return out
