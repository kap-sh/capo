"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetUploadStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.arn
    import capo_iotthingsgraph.types.namespace_name
    import capo_iotthingsgraph.types.string_list
    import capo_iotthingsgraph.types.timestamp
    import capo_iotthingsgraph.types.upload_id
    import capo_iotthingsgraph.types.upload_status
    import capo_iotthingsgraph.types.version


class GetUploadStatusResponse(TypedDict, closed=True):
    upload_id: "capo_iotthingsgraph.types.upload_id.UploadId"
    """<p>The ID of the upload.</p>"""
    upload_status: "capo_iotthingsgraph.types.upload_status.UploadStatus"
    """<p>The status of the upload. The initial status is <code>IN_PROGRESS</code>. The response show all validation failures if the upload fails.</p>"""
    namespace_arn: NotRequired["capo_iotthingsgraph.types.arn.Arn"]
    """<p>The ARN of the upload.</p>"""
    namespace_name: NotRequired[
        "capo_iotthingsgraph.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the upload's namespace.</p>"""
    namespace_version: NotRequired["capo_iotthingsgraph.types.version.Version"]
    """<p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p>"""
    failure_reason: NotRequired["capo_iotthingsgraph.types.string_list.StringList"]
    """<p>The reason for an upload failure.</p>"""
    created_date: "capo_iotthingsgraph.types.timestamp.Timestamp"
    """<p>The date at which the upload was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUploadStatusResponse) -> dict:
    out: dict = {}
    out["uploadId"] = value["upload_id"]
    import capo_iotthingsgraph.types.upload_status

    out["uploadStatus"] = (
        capo_iotthingsgraph.types.upload_status.serialize_aws_json_1_1(
            value["upload_status"]
        )
    )
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "namespace_version" in value:
        out["namespaceVersion"] = value["namespace_version"]
    if "failure_reason" in value:
        import capo_iotthingsgraph.types.string_list

        out["failureReason"] = (
            capo_iotthingsgraph.types.string_list.serialize_aws_json_1_1(
                value["failure_reason"]
            )
        )
    import capo_iotthingsgraph.types.timestamp

    out["createdDate"] = capo_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
        value["created_date"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUploadStatusResponse:
    out: GetUploadStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        out["upload_id"] = ""
    if data.get("uploadStatus") is not None:
        import capo_iotthingsgraph.types.upload_status

        out["upload_status"] = (
            capo_iotthingsgraph.types.upload_status.deserialize_aws_json_1_1(
                data["uploadStatus"]
            )
        )
    else:
        import typing

        out["upload_status"] = typing.cast(
            "capo_iotthingsgraph.types.upload_status.UploadStatus", ""
        )
    if data.get("namespaceArn") is not None:
        out["namespace_arn"] = data["namespaceArn"]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    if data.get("namespaceVersion") is not None:
        out["namespace_version"] = data["namespaceVersion"]
    if data.get("failureReason") is not None:
        import capo_iotthingsgraph.types.string_list

        out["failure_reason"] = (
            capo_iotthingsgraph.types.string_list.deserialize_aws_json_1_1(
                data["failureReason"]
            )
        )
    if data.get("createdDate") is not None:
        import capo_iotthingsgraph.types.timestamp

        out["created_date"] = (
            capo_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
                data["createdDate"]
            )
        )
    else:
        import datetime

        out["created_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
