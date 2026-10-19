"""Generated from Smithy shape ``com.amazonaws.directoryservice#EnableCAEnrollmentPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.pca_connector_arn


class EnableCAEnrollmentPolicyRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for which to enable the CA enrollment policy.</p>"""
    pca_connector_arn: "capo_directory_service.types.pca_connector_arn.PcaConnectorArn"
    """<p>The Amazon Resource Name (ARN) of the Private Certificate Authority (PCA) connector to use for automatic certificate enrollment. This connector must be properly configured and accessible from the directory.</p> <p>The ARN format is: <code>arn:aws:pca-connector-ad:<i>region</i>:<i>account-id</i>:connector/<i>connector-id</i> </code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableCAEnrollmentPolicyRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["PcaConnectorArn"] = value["pca_connector_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableCAEnrollmentPolicyRequest:
    out: EnableCAEnrollmentPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("PcaConnectorArn") is not None:
        out["pca_connector_arn"] = data["PcaConnectorArn"]
    else:
        out["pca_connector_arn"] = ""
    return out
