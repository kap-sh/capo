"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.date_time_timestamp
    import capo_imagebuilder.types.image_build_version_arn
    import capo_imagebuilder.types.image_pipeline_arn
    import capo_imagebuilder.types.inspector_score_details
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.non_negative_double
    import capo_imagebuilder.types.package_vulnerability_details
    import capo_imagebuilder.types.remediation


class ImageScanFinding(TypedDict, closed=True):
    aws_account_id: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services account ID that's associated with the finding.</p>"""
    image_build_version_arn: NotRequired[
        "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image build version that's associated with the finding.</p>"""
    image_pipeline_arn: NotRequired[
        "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image pipeline that's associated with the finding.</p>"""
    type: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The type of the finding. Image Builder looks for findings of the type <code>PACKAGE_VULNERABILITY</code> that apply to output images, and excludes other types.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the finding.</p>"""
    title: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The title of the finding.</p>"""
    remediation: NotRequired["capo_imagebuilder.types.remediation.Remediation"]
    """<p>An object that contains the details about how to remediate the finding.</p>"""
    severity: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The severity of the finding. For more information, see <a href="https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html">Severity levels for Amazon Inspector findings</a> in the <i>Amazon Inspector User Guide</i>.</p>"""
    first_observed_at: NotRequired[
        "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time when the finding was first observed.</p>"""
    updated_at: NotRequired[
        "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp when the finding was last updated.</p>"""
    inspector_score: NotRequired[
        "capo_imagebuilder.types.non_negative_double.NonNegativeDouble"
    ]
    """<p>The score that Amazon Inspector assigned for the finding.</p>"""
    inspector_score_details: NotRequired[
        "capo_imagebuilder.types.inspector_score_details.InspectorScoreDetails"
    ]
    """<p>An object that contains details of the Amazon Inspector score.</p>"""
    package_vulnerability_details: NotRequired[
        "capo_imagebuilder.types.package_vulnerability_details.PackageVulnerabilityDetails"
    ]
    """<p>An object that contains the details of a package vulnerability finding.</p>"""
    fix_available: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Details about whether a fix is available for any of the packages that are identified in the finding through a version update. Valid values include:</p> <ul> <li> <p> <code>YES</code> – A fix is available for all of the packages identified in the finding.</p> </li> <li> <p> <code>NO</code> – No fix is available.</p> </li> <li> <p> <code>PARTIAL</code> – A fix is available for some, but not all, of the packages identified in the finding.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanFinding) -> dict:
    out: dict = {}
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    if "image_pipeline_arn" in value:
        out["imagePipelineArn"] = value["image_pipeline_arn"]
    if "type" in value:
        out["type"] = value["type"]
    if "description" in value:
        out["description"] = value["description"]
    if "title" in value:
        out["title"] = value["title"]
    if "remediation" in value:
        import capo_imagebuilder.types.remediation

        out["remediation"] = capo_imagebuilder.types.remediation.serialize_json(
            value["remediation"]
        )
    if "severity" in value:
        out["severity"] = value["severity"]
    if "first_observed_at" in value:
        import capo_imagebuilder.types.date_time_timestamp

        out["firstObservedAt"] = (
            capo_imagebuilder.types.date_time_timestamp.serialize_json(
                value["first_observed_at"]
            )
        )
    if "updated_at" in value:
        import capo_imagebuilder.types.date_time_timestamp

        out["updatedAt"] = capo_imagebuilder.types.date_time_timestamp.serialize_json(
            value["updated_at"]
        )
    if "inspector_score" in value:
        out["inspectorScore"] = (
            "NaN"
            if value["inspector_score"] != value["inspector_score"]
            else "Infinity"
            if value["inspector_score"] == float("inf")
            else "-Infinity"
            if value["inspector_score"] == float("-inf")
            else value["inspector_score"]
        )
    if "inspector_score_details" in value:
        import capo_imagebuilder.types.inspector_score_details

        out["inspectorScoreDetails"] = (
            capo_imagebuilder.types.inspector_score_details.serialize_json(
                value["inspector_score_details"]
            )
        )
    if "package_vulnerability_details" in value:
        import capo_imagebuilder.types.package_vulnerability_details

        out["packageVulnerabilityDetails"] = (
            capo_imagebuilder.types.package_vulnerability_details.serialize_json(
                value["package_vulnerability_details"]
            )
        )
    if "fix_available" in value:
        out["fixAvailable"] = value["fix_available"]
    return out


def deserialize_json(data: dict) -> ImageScanFinding:
    out: ImageScanFinding = {}  # type: ignore[typeddict-item]
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    if data.get("imageBuildVersionArn") is not None:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    if data.get("imagePipelineArn") is not None:
        out["image_pipeline_arn"] = data["imagePipelineArn"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("remediation") is not None:
        import capo_imagebuilder.types.remediation

        out["remediation"] = capo_imagebuilder.types.remediation.deserialize_json(
            data["remediation"]
        )
    if data.get("severity") is not None:
        out["severity"] = data["severity"]
    if data.get("firstObservedAt") is not None:
        import capo_imagebuilder.types.date_time_timestamp

        out["first_observed_at"] = (
            capo_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["firstObservedAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_imagebuilder.types.date_time_timestamp

        out["updated_at"] = (
            capo_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if data.get("inspectorScore") is not None:
        out["inspector_score"] = float(data["inspectorScore"])
    if data.get("inspectorScoreDetails") is not None:
        import capo_imagebuilder.types.inspector_score_details

        out["inspector_score_details"] = (
            capo_imagebuilder.types.inspector_score_details.deserialize_json(
                data["inspectorScoreDetails"]
            )
        )
    if data.get("packageVulnerabilityDetails") is not None:
        import capo_imagebuilder.types.package_vulnerability_details

        out["package_vulnerability_details"] = (
            capo_imagebuilder.types.package_vulnerability_details.deserialize_json(
                data["packageVulnerabilityDetails"]
            )
        )
    if data.get("fixAvailable") is not None:
        out["fix_available"] = data["fixAvailable"]
    return out
