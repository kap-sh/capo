"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#StartImportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.client_request_token
    import capo_application_discovery_service.types.import_task_name
    import capo_application_discovery_service.types.import_url


class StartImportTaskRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_application_discovery_service.types.client_request_token.ClientRequestToken"
    ]
    """<p>Optional. A unique token that you can provide to prevent the same import request from occurring more than once. If you don't provide a token, a token is automatically generated.</p> <p>Sending more than one <code>StartImportTask</code> request with the same client request token will return information about the original import task with that client request token.</p>"""
    name: "capo_application_discovery_service.types.import_task_name.ImportTaskName"
    """<p>A descriptive name for this request. You can use this name to filter future requests related to this import task, such as identifying applications and servers that were included in this import task. We recommend that you use a meaningful name for each import task.</p>"""
    import_url: "capo_application_discovery_service.types.import_url.ImportURL"
    """<p>The URL for your import file that you've uploaded to Amazon S3.</p> <note> <p>If you're using the Amazon Web Services CLI, this URL is structured as follows: <code>s3://BucketName/ImportFileName.CSV</code> </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImportTaskRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["name"] = value["name"]
    out["importUrl"] = value["import_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImportTaskRequest:
    out: StartImportTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("importUrl") is not None:
        out["import_url"] = data["importUrl"]
    else:
        out["import_url"] = ""
    return out
