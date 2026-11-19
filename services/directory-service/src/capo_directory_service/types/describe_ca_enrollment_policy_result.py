"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeCAEnrollmentPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.ca_enrollment_policy_status
    import capo_directory_service.types.ca_enrollment_policy_status_reason
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.last_updated_date_time
    import capo_directory_service.types.pca_connector_arn


class DescribeCAEnrollmentPolicyResult(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory associated with this CA enrollment policy.</p>"""
    pca_connector_arn: NotRequired[
        "capo_directory_service.types.pca_connector_arn.PcaConnectorArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Private Certificate Authority (PCA) connector that is configured for automatic certificate enrollment in this directory.</p>"""
    ca_enrollment_policy_status: NotRequired[
        "capo_directory_service.types.ca_enrollment_policy_status.CaEnrollmentPolicyStatus"
    ]
    """<p>The current status of the CA enrollment policy. This indicates if automatic certificate enrollment is currently active, inactive, or in a transitional state.</p> <p>Valid values:</p> <ul> <li> <p> <code>IN_PROGRESS</code> - The policy is being activated T</p> </li> <li> <p> <code>SUCCESS</code> - The policy is active and automatic certificate enrollment is operational</p> </li> <li> <p> <code>FAILED</code> - The policy activation or deactivation failed</p> </li> <li> <p> <code>DISABLING</code> - The policy is being deactivated</p> </li> <li> <p> <code>DISABLED</code> - The policy is inactive and automatic certificate enrollment is not available</p> </li> <li> <p> <code>IMPAIRED</code> - Network connectivity is impaired.</p> </li> </ul>"""
    last_updated_date_time: NotRequired[
        "capo_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p>The date and time when the CA enrollment policy was last modified or updated.</p>"""
    ca_enrollment_policy_status_reason: NotRequired[
        "capo_directory_service.types.ca_enrollment_policy_status_reason.CaEnrollmentPolicyStatusReason"
    ]
    """<p>Additional information explaining the current status of the CA enrollment policy, particularly useful when the policy is in an error or transitional state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCAEnrollmentPolicyResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "pca_connector_arn" in value:
        out["PcaConnectorArn"] = value["pca_connector_arn"]
    if "ca_enrollment_policy_status" in value:
        import capo_directory_service.types.ca_enrollment_policy_status

        out["CaEnrollmentPolicyStatus"] = (
            capo_directory_service.types.ca_enrollment_policy_status.serialize_aws_json_1_1(
                value["ca_enrollment_policy_status"]
            )
        )
    if "last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    if "ca_enrollment_policy_status_reason" in value:
        out["CaEnrollmentPolicyStatusReason"] = value[
            "ca_enrollment_policy_status_reason"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCAEnrollmentPolicyResult:
    out: DescribeCAEnrollmentPolicyResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("PcaConnectorArn") is not None:
        out["pca_connector_arn"] = data["PcaConnectorArn"]
    if data.get("CaEnrollmentPolicyStatus") is not None:
        import capo_directory_service.types.ca_enrollment_policy_status

        out["ca_enrollment_policy_status"] = (
            capo_directory_service.types.ca_enrollment_policy_status.deserialize_aws_json_1_1(
                data["CaEnrollmentPolicyStatus"]
            )
        )
    if data.get("LastUpdatedDateTime") is not None:
        import capo_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedDateTime"]
            )
        )
    if data.get("CaEnrollmentPolicyStatusReason") is not None:
        out["ca_enrollment_policy_status_reason"] = data[
            "CaEnrollmentPolicyStatusReason"
        ]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeCAEnrollmentPolicyResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "pca_connector_arn" in value:
        out["PcaConnectorArn"] = value["pca_connector_arn"]
    if "ca_enrollment_policy_status" in value:
        import capo_directory_service.types.ca_enrollment_policy_status

        out["CaEnrollmentPolicyStatus"] = (
            capo_directory_service.types.ca_enrollment_policy_status.serialize_cbor(
                value["ca_enrollment_policy_status"]
            )
        )
    if "last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_cbor(
                value["last_updated_date_time"]
            )
        )
    if "ca_enrollment_policy_status_reason" in value:
        out["CaEnrollmentPolicyStatusReason"] = value[
            "ca_enrollment_policy_status_reason"
        ]
    return out


def deserialize_cbor(data: dict) -> DescribeCAEnrollmentPolicyResult:
    out: DescribeCAEnrollmentPolicyResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("PcaConnectorArn") is not None:
        out["pca_connector_arn"] = data["PcaConnectorArn"]
    if data.get("CaEnrollmentPolicyStatus") is not None:
        import capo_directory_service.types.ca_enrollment_policy_status

        out["ca_enrollment_policy_status"] = (
            capo_directory_service.types.ca_enrollment_policy_status.deserialize_cbor(
                data["CaEnrollmentPolicyStatus"]
            )
        )
    if data.get("LastUpdatedDateTime") is not None:
        import capo_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_cbor(
                data["LastUpdatedDateTime"]
            )
        )
    if data.get("CaEnrollmentPolicyStatusReason") is not None:
        out["ca_enrollment_policy_status_reason"] = data[
            "CaEnrollmentPolicyStatusReason"
        ]
    return out
