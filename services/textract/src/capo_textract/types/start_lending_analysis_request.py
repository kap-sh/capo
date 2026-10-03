"""Generated from Smithy shape ``com.amazonaws.textract#StartLendingAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_textract.errors import DeserializationError

if TYPE_CHECKING:
    import capo_textract.types.client_request_token
    import capo_textract.types.document_location
    import capo_textract.types.job_tag
    import capo_textract.types.kms_key_id
    import capo_textract.types.notification_channel
    import capo_textract.types.output_config


class StartLendingAnalysisRequest(TypedDict, closed=True):
    document_location: "capo_textract.types.document_location.DocumentLocation"
    client_request_token: NotRequired[
        "capo_textract.types.client_request_token.ClientRequestToken"
    ]
    """<p>The idempotent token that you use to identify the start request. If you use the same token with multiple <code>StartLendingAnalysis</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidentally started more than once. For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/api-sync.html">Calling Amazon Textract Asynchronous Operations</a>.</p>"""
    job_tag: NotRequired["capo_textract.types.job_tag.JobTag"]
    """<p>An identifier that you specify to be included in the completion notification published to the Amazon SNS topic. For example, you can use <code>JobTag</code> to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).</p>"""
    notification_channel: NotRequired[
        "capo_textract.types.notification_channel.NotificationChannel"
    ]
    output_config: NotRequired["capo_textract.types.output_config.OutputConfig"]
    kms_key_id: NotRequired["capo_textract.types.kms_key_id.KMSKeyId"]
    """<p>The KMS key used to encrypt the inference results. This can be in either Key ID or Key Alias format. When a KMS key is provided, the KMS key will be used for server-side encryption of the objects in the customer bucket. When this parameter is not enabled, the result will be encrypted server side, using SSE-S3. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartLendingAnalysisRequest) -> dict:
    out: dict = {}
    import capo_textract.types.document_location

    out["DocumentLocation"] = (
        capo_textract.types.document_location.serialize_aws_json_1_1(
            value["document_location"]
        )
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "job_tag" in value:
        out["JobTag"] = value["job_tag"]
    if "notification_channel" in value:
        import capo_textract.types.notification_channel

        out["NotificationChannel"] = (
            capo_textract.types.notification_channel.serialize_aws_json_1_1(
                value["notification_channel"]
            )
        )
    if "output_config" in value:
        import capo_textract.types.output_config

        out["OutputConfig"] = capo_textract.types.output_config.serialize_aws_json_1_1(
            value["output_config"]
        )
    if "kms_key_id" in value:
        out["KMSKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartLendingAnalysisRequest:
    out: StartLendingAnalysisRequest = {}  # type: ignore[typeddict-item]
    if data.get("DocumentLocation") is not None:
        import capo_textract.types.document_location

        out["document_location"] = (
            capo_textract.types.document_location.deserialize_aws_json_1_1(
                data["DocumentLocation"]
            )
        )
    else:
        raise DeserializationError(
            "StartLendingAnalysisRequest.document_location required"
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("JobTag") is not None:
        out["job_tag"] = data["JobTag"]
    if data.get("NotificationChannel") is not None:
        import capo_textract.types.notification_channel

        out["notification_channel"] = (
            capo_textract.types.notification_channel.deserialize_aws_json_1_1(
                data["NotificationChannel"]
            )
        )
    if data.get("OutputConfig") is not None:
        import capo_textract.types.output_config

        out["output_config"] = (
            capo_textract.types.output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if data.get("KMSKeyId") is not None:
        out["kms_key_id"] = data["KMSKeyId"]
    return out
