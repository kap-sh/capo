"""Generated from Smithy shape ``com.amazonaws.devicefarm#ExecutionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.accounts_cleanup
    import capo_device_farm.types.app_packages_cleanup
    import capo_device_farm.types.job_timeout_minutes
    import capo_device_farm.types.skip_app_resign
    import capo_device_farm.types.video_capture


class ExecutionConfiguration(TypedDict, closed=True):
    job_timeout_minutes: NotRequired[
        "capo_device_farm.types.job_timeout_minutes.JobTimeoutMinutes"
    ]
    """<p>The number of minutes a test run executes before it times out.</p>"""
    accounts_cleanup: NotRequired[
        "capo_device_farm.types.accounts_cleanup.AccountsCleanup"
    ]
    """<p>True if account cleanup is enabled at the beginning of the test. Otherwise, false.</p>"""
    app_packages_cleanup: NotRequired[
        "capo_device_farm.types.app_packages_cleanup.AppPackagesCleanup"
    ]
    """<p>True if app package cleanup is enabled at the beginning of the test. Otherwise, false.</p>"""
    video_capture: NotRequired["capo_device_farm.types.video_capture.VideoCapture"]
    """<p>Set to true to enable video capture. Otherwise, set to false. The default is true.</p>"""
    skip_app_resign: NotRequired["capo_device_farm.types.skip_app_resign.SkipAppResign"]
    """<p>When set to <code>true</code>, for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.</p> <p>For more information about how Device Farm re-signs your apps, see <a href="http://aws.amazon.com/device-farm/faqs/">Do you modify my app?</a> in the <i>AWS Device Farm FAQs</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionConfiguration) -> dict:
    out: dict = {}
    if "job_timeout_minutes" in value:
        out["jobTimeoutMinutes"] = value["job_timeout_minutes"]
    if "accounts_cleanup" in value:
        out["accountsCleanup"] = value["accounts_cleanup"]
    if "app_packages_cleanup" in value:
        out["appPackagesCleanup"] = value["app_packages_cleanup"]
    if "video_capture" in value:
        out["videoCapture"] = value["video_capture"]
    if "skip_app_resign" in value:
        out["skipAppResign"] = value["skip_app_resign"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionConfiguration:
    out: ExecutionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("jobTimeoutMinutes") is not None:
        out["job_timeout_minutes"] = data["jobTimeoutMinutes"]
    if data.get("accountsCleanup") is not None:
        out["accounts_cleanup"] = data["accountsCleanup"]
    if data.get("appPackagesCleanup") is not None:
        out["app_packages_cleanup"] = data["appPackagesCleanup"]
    if data.get("videoCapture") is not None:
        out["video_capture"] = data["videoCapture"]
    if data.get("skipAppResign") is not None:
        out["skip_app_resign"] = data["skipAppResign"]
    return out
