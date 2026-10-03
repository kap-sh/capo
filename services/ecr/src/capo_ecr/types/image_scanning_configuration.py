"""Generated from Smithy shape ``com.amazonaws.ecr#ImageScanningConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.scan_on_push_flag


class ImageScanningConfiguration(TypedDict, closed=True):
    scan_on_push: "capo_ecr.types.scan_on_push_flag.ScanOnPushFlag"
    """<p>The setting that determines whether images are scanned after being pushed to a repository. If set to <code>true</code>, images will be scanned after being pushed. If this parameter is not specified, it will default to <code>false</code> and images will not be scanned unless a scan is manually started with the <a href="https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_StartImageScan.html">API_StartImageScan</a> API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageScanningConfiguration) -> dict:
    out: dict = {}
    out["scanOnPush"] = value.get("scan_on_push", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageScanningConfiguration:
    out: ImageScanningConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("scanOnPush") is not None:
        out["scan_on_push"] = data["scanOnPush"]
    else:
        out["scan_on_push"] = False
    return out
