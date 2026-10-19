"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DescribeAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.assessment_identifier
    import capo_marketplace_catalog.types.catalog
    import capo_marketplace_catalog.types.describe_assessment_max_result_integer
    import capo_marketplace_catalog.types.next_token


class DescribeAssessmentRequest(TypedDict, closed=True):
    catalog: "capo_marketplace_catalog.types.catalog.Catalog"
    """<p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>"""
    assessment_identifier: (
        "capo_marketplace_catalog.types.assessment_identifier.AssessmentIdentifier"
    )
    """<p>The unique identifier of the assessment to describe. You can provide either the assessment ID (for example, <code>assessment-12345</code>) or the full assessment ARN (for example, <code>arn:aws:aws-marketplace:us-east-1::AWSMarketplace/Assessment/assessment-12345</code>).</p>"""
    max_results: NotRequired[
        "capo_marketplace_catalog.types.describe_assessment_max_result_integer.DescribeAssessmentMaxResultInteger"
    ]
    """<p>Specifies the upper limit of <code>ControlAssessment</code> elements returned on a single page. If a value isn't provided, the default value is 50. Valid values range from 1 to 100.</p>"""
    next_token: NotRequired["capo_marketplace_catalog.types.next_token.NextToken"]
    """<p>The value of the next token, if it exists. <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssessmentRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["AssessmentIdentifier"] = value["assessment_identifier"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeAssessmentRequest:
    out: DescribeAssessmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("AssessmentIdentifier") is not None:
        out["assessment_identifier"] = data["AssessmentIdentifier"]
    else:
        out["assessment_identifier"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
