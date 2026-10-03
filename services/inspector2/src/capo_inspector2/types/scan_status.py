"""Generated from Smithy shape ``com.amazonaws.inspector2#ScanStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.scan_status_code
    import capo_inspector2.types.scan_status_reason


class ScanStatus(TypedDict, closed=True):
    status_code: "capo_inspector2.types.scan_status_code.ScanStatusCode"
    """<p>The status code of the scan.</p>"""
    reason: "capo_inspector2.types.scan_status_reason.ScanStatusReason"
    """<p>The scan status. Possible return values and descriptions are: </p> <p> <code>ACCESS_DENIED</code> - Resource access policy restricting Amazon Inspector access. Please update the IAM policy.</p> <p> <code>ACCESS_DENIED_TO_ENCRYPTION_KEY</code> - The KMS key policy doesn't allow Amazon Inspector access. Update the key policy.</p> <p> <code>DEEP_INSPECTION_COLLECTION_TIME_LIMIT_EXCEEDED</code> - Amazon Inspector failed to extract the package inventory because the package collection time exceeding the maximum threshold of 15 minutes.</p> <p> <code>DEEP_INSPECTION_DAILY_SSM_INVENTORY_LIMIT_EXCEEDED</code> - The SSM agent couldn't send inventory to Amazon Inspector because the SSM quota for Inventory data collected per instance per day has already been reached for this instance.</p> <p> <code>DEEP_INSPECTION_NO_INVENTORY</code> - The Amazon Inspector plugin hasn't yet been able to collect an inventory of packages for this instance. This is usually the result of a pending scan, however, if this status persists after 6 hours, use SSM to ensure that the required Amazon Inspector associations exist and are running for the instance.</p> <p> <code>DEEP_INSPECTION_PACKAGE_COLLECTION_LIMIT_EXCEEDED</code> - The instance has exceeded the 5000 package limit for Amazon Inspector Deep inspection. To resume Deep inspection for this instance you can try to adjust the custom paths associated with the account.</p> <p> <code>EC2_INSTANCE_STOPPED</code> - This EC2 instance is in a stopped state, therefore, Amazon Inspector will pause scanning. The existing findings will continue to exist until the instance is terminated. Once the instance is re-started, Inspector will automatically start scanning the instance again. Please note that you will not be charged for this instance while it's in a stopped state.</p> <p> <code>EXCLUDED_BY_TAG</code> - This resource was not scanned because it has been excluded by a tag.</p> <p> <code>IMAGE_SIZE_EXCEEDED</code> - Reserved for future use.</p> <p> <code>INTEGRATION_CONNNECTION_LOST</code> - Amazon Inspector couldn't communicate with the source code management platform.</p> <p> <code>INTERNAL_ERROR</code> - Amazon Inspector has encountered an internal error for this resource. Amazon Inspector service will automatically resolve the issue and resume the scanning. No action required from the user.</p> <p> <code>NO_INVENTORY</code> - Amazon Inspector couldn't find software application inventory to scan for vulnerabilities. This might be caused due to required Amazon Inspector associations being deleted or failing to run on your resource. Please verify the status of <code>InspectorInventoryCollection-do-not-delete</code> association in the SSM console for the resource. Additionally, you can verify the instance's inventory in the SSM Fleet Manager console.</p> <p> <code>NO_RESOURCES_FOUND</code> - Reserved for future use.</p> <p> <code>NO_SCAN_CONFIGURATION_ASSOCIATED</code> - The code repository resource doesn't have an associated scan configuration.</p> <p> <code>PENDING_DISABLE</code> - This resource is pending cleanup during disablement. The customer will not be billed while a resource is in the pending disable status.</p> <p> <code>PENDING_INITIAL_SCAN</code> - This resource has been identified for scanning, results will be available soon.</p> <p> <code>RESOURCE_TERMINATED</code> - This resource has been terminated. The findings and coverage associated with this resource are in the process of being cleaned up.</p> <p> <code>SCAN_ELIGIBILITY_EXPIRED</code> - The configured scan duration has lapsed for this image.</p> <p> <code>SCAN_FREQUENCY_MANUAL</code> - This image will not be covered by Amazon Inspector due to the repository scan frequency configuration.</p> <p> <code>SCAN_FREQUENCY_SCAN_ON_PUSH</code> - This image will be scanned one time and will not new findings because of the scan frequency configuration.</p> <p> <code>SCAN_IN_PROGRESS</code> - The resource is currently being scanned.</p> <p> <code>STALE_INVENTORY</code> - Amazon Inspector wasn't able to collect an updated software application inventory in the last 7 days. Please confirm the required Amazon Inspector associations still exist and you can still see an updated inventory in the SSM console.</p> <p> <code>SUCCESSFUL</code> - The scan was successful.</p> <p> <code>UNMANAGED_EC2_INSTANCE</code> - The EC2 instance is not managed by SSM, please use the following SSM automation to remediate the issue: <a href="https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-managed-instance.html">https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-managed-instance.html</a>. Once the instance becomes managed by SSM, Inspector will automatically begin scanning this instance. </p> <p> <code>UNSUPPORTED_CODE_ARTIFACTS </code> - The function was not scanned because it has an unsupported code artifacts.</p> <p> <code>UNSUPPORTED_CONFIG_FILE</code> - Reserved for future use.</p> <p> <code>UNSUPPORTED_LANGUAGE</code> - The scan was unsuccessful because the repository contains files in an unsupported programming language.</p> <p> <code>UNSUPPORTED_MEDIA_TYPE </code>- The ECR image has an unsupported media type.</p> <p> <code>UNSUPPORTED_OS</code> - Amazon Inspector does not support this OS, architecture, or image manifest type at this time. To see a complete list of supported operating systems see: <a href=" https://docs.aws.amazon.com/inspector/latest/user/supported.html">https://docs.aws.amazon.com/inspector/latest/user/supported.html</a>.</p> <p> <code>UNSUPPORTED_RUNTIME</code> - The function was not scanned because it has an unsupported runtime. To see a complete list of supported runtimes see: <a href=" https://docs.aws.amazon.com/inspector/latest/user/supported.html">https://docs.aws.amazon.com/inspector/latest/user/supported.html</a>.</p> <p> <code>IMAGE_ARCHIVED</code> - This image has been archived in Amazon ECR and is no longer available for scanning in Amazon Inspector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ScanStatus:
    out: ScanStatus = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    else:
        raise DeserializationError("ScanStatus.status_code required")
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        raise DeserializationError("ScanStatus.reason required")
    return out
