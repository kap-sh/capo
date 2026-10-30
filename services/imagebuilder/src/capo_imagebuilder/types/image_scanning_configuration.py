"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanningConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.ecr_configuration
    import capo_imagebuilder.types.image_scanning_type_list
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.scan_result_condition


class ImageScanningConfiguration(TypedDict, closed=True):
    image_scanning_enabled: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether Amazon Inspector scans for vulnerabilities when you create a new image. You must also enable image tests. For AMI output, <code>imageScanningTypes</code> sets whether Amazon Inspector scans the test instance or the output AMI. For container output, Amazon Inspector scans the container image that Image Builder pushes to the Amazon ECR repository from your <code>ecrConfiguration</code> settings.</p> <p>To use container image scans, you must activate Amazon Inspector for Amazon ECR scanning in your account. The Image Builder <code>ListImageScanFindings</code> operation returns the findings of these scans.</p>"""
    ecr_configuration: NotRequired[
        "capo_imagebuilder.types.ecr_configuration.EcrConfiguration"
    ]
    """<p>Contains Amazon ECR settings for vulnerability scans.</p>"""
    image_scanning_types: NotRequired[
        "capo_imagebuilder.types.image_scanning_type_list.ImageScanningTypeList"
    ]
    """<p>The type of vulnerability scan that Image Builder runs for AMI output when <code>imageScanningEnabled</code> is <code>true</code>. Specify a single value. If you omit <code>imageScanningTypes</code>, Image Builder uses <code>TEST_INSTANCE_CVE</code>. The scan types work as follows:</p> <ul> <li> <p>With <code>TEST_INSTANCE_CVE</code>, Amazon Inspector scans the test instance during image tests. To use this scan, you must activate Amazon Inspector for Amazon EC2 scanning in your account. The Image Builder <code>ListImageScanFindings</code> operation returns the findings.</p> </li> <li> <p>With <code>ON_DEMAND_AMI_CVE</code>, Amazon Inspector starts an on-demand scan of the output AMI during image tests. To use this scan, you must build from an image recipe, but you do not need to activate Amazon Inspector in your account. The Amazon EC2 <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetImageFindings.html">GetImageFindings</a> operation returns the findings.</p> </li> </ul>"""
    scan_result_condition: NotRequired[
        "capo_imagebuilder.types.scan_result_condition.ScanResultCondition"
    ]
    """<p>The condition that the output AMI's scan results must meet for the image to pass. You can set <code>scanResultCondition</code> only when <code>imageScanningTypes</code> is <code>ON_DEMAND_AMI_CVE</code>. If you omit it, Image Builder starts the scan but does not wait for it or use its results to pass or fail the image.</p> <p>When you set <code>scanResultCondition</code>, the test phase waits for the scan to finish. Then Image Builder checks the findings against the condition. By default, Image Builder counts only findings that have a fix available. To count every finding, set <code>fixAvailable</code> to <code>false</code>. If a counted finding exceeds <code>maximumSeverityLabel</code>, Image Builder fails the image in the test phase and does not distribute the AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanningConfiguration) -> dict:
    out: dict = {}
    if "image_scanning_enabled" in value:
        out["imageScanningEnabled"] = value["image_scanning_enabled"]
    if "ecr_configuration" in value:
        import capo_imagebuilder.types.ecr_configuration

        out["ecrConfiguration"] = (
            capo_imagebuilder.types.ecr_configuration.serialize_json(
                value["ecr_configuration"]
            )
        )
    if "image_scanning_types" in value:
        import capo_imagebuilder.types.image_scanning_type_list

        out["imageScanningTypes"] = (
            capo_imagebuilder.types.image_scanning_type_list.serialize_json(
                value["image_scanning_types"]
            )
        )
    if "scan_result_condition" in value:
        import capo_imagebuilder.types.scan_result_condition

        out["scanResultCondition"] = (
            capo_imagebuilder.types.scan_result_condition.serialize_json(
                value["scan_result_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImageScanningConfiguration:
    out: ImageScanningConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("imageScanningEnabled") is not None:
        out["image_scanning_enabled"] = data["imageScanningEnabled"]
    if data.get("ecrConfiguration") is not None:
        import capo_imagebuilder.types.ecr_configuration

        out["ecr_configuration"] = (
            capo_imagebuilder.types.ecr_configuration.deserialize_json(
                data["ecrConfiguration"]
            )
        )
    if data.get("imageScanningTypes") is not None:
        import capo_imagebuilder.types.image_scanning_type_list

        out["image_scanning_types"] = (
            capo_imagebuilder.types.image_scanning_type_list.deserialize_json(
                data["imageScanningTypes"]
            )
        )
    if data.get("scanResultCondition") is not None:
        import capo_imagebuilder.types.scan_result_condition

        out["scan_result_condition"] = (
            capo_imagebuilder.types.scan_result_condition.deserialize_json(
                data["scanResultCondition"]
            )
        )
    return out
