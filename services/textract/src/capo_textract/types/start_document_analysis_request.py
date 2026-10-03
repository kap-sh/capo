"""Generated from Smithy shape ``com.amazonaws.textract#StartDocumentAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_textract.errors import DeserializationError

if TYPE_CHECKING:
    import capo_textract.types.adapters_config
    import capo_textract.types.client_request_token
    import capo_textract.types.document_location
    import capo_textract.types.feature_types
    import capo_textract.types.job_tag
    import capo_textract.types.kms_key_id
    import capo_textract.types.notification_channel
    import capo_textract.types.output_config
    import capo_textract.types.queries_config


class StartDocumentAnalysisRequest(TypedDict, closed=True):
    document_location: "capo_textract.types.document_location.DocumentLocation"
    """<p>The location of the document to be processed.</p>"""
    feature_types: "capo_textract.types.feature_types.FeatureTypes"
    """<p>A list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected form data. To perform both types of analysis, add TABLES and FORMS to <code>FeatureTypes</code>. All lines and words detected in the document are included in the response (including text that isn't related to the value of <code>FeatureTypes</code>). </p>"""
    client_request_token: NotRequired[
        "capo_textract.types.client_request_token.ClientRequestToken"
    ]
    """<p>The idempotent token that you use to identify the start request. If you use the same token with multiple <code>StartDocumentAnalysis</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidentally started more than once. For more information, see <a href="https://docs.aws.amazon.com/textract/latest/dg/api-async.html">Calling Amazon Textract Asynchronous Operations</a>.</p>"""
    job_tag: NotRequired["capo_textract.types.job_tag.JobTag"]
    """<p>An identifier that you specify that's included in the completion notification published to the Amazon SNS topic. For example, you can use <code>JobTag</code> to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).</p>"""
    notification_channel: NotRequired[
        "capo_textract.types.notification_channel.NotificationChannel"
    ]
    """<p>The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the operation to. </p>"""
    output_config: NotRequired["capo_textract.types.output_config.OutputConfig"]
    """<p>Sets if the output will go to a customer defined bucket. By default, Amazon Textract will save the results internally to be accessed by the GetDocumentAnalysis operation.</p>"""
    kms_key_id: NotRequired["capo_textract.types.kms_key_id.KMSKeyId"]
    """<p>The KMS key used to encrypt the inference results. This can be in either Key ID or Key Alias format. When a KMS key is provided, the KMS key will be used for server-side encryption of the objects in the customer bucket. When this parameter is not enabled, the result will be encrypted server side,using SSE-S3.</p>"""
    queries_config: NotRequired["capo_textract.types.queries_config.QueriesConfig"]
    adapters_config: NotRequired["capo_textract.types.adapters_config.AdaptersConfig"]
    """<p>Specifies the adapter to be used when analyzing a document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDocumentAnalysisRequest) -> dict:
    out: dict = {}
    import capo_textract.types.document_location

    out["DocumentLocation"] = (
        capo_textract.types.document_location.serialize_aws_json_1_1(
            value["document_location"]
        )
    )
    import capo_textract.types.feature_types

    out["FeatureTypes"] = capo_textract.types.feature_types.serialize_aws_json_1_1(
        value["feature_types"]
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
    if "queries_config" in value:
        import capo_textract.types.queries_config

        out["QueriesConfig"] = (
            capo_textract.types.queries_config.serialize_aws_json_1_1(
                value["queries_config"]
            )
        )
    if "adapters_config" in value:
        import capo_textract.types.adapters_config

        out["AdaptersConfig"] = (
            capo_textract.types.adapters_config.serialize_aws_json_1_1(
                value["adapters_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDocumentAnalysisRequest:
    out: StartDocumentAnalysisRequest = {}  # type: ignore[typeddict-item]
    if data.get("DocumentLocation") is not None:
        import capo_textract.types.document_location

        out["document_location"] = (
            capo_textract.types.document_location.deserialize_aws_json_1_1(
                data["DocumentLocation"]
            )
        )
    else:
        raise DeserializationError(
            "StartDocumentAnalysisRequest.document_location required"
        )
    if data.get("FeatureTypes") is not None:
        import capo_textract.types.feature_types

        out["feature_types"] = (
            capo_textract.types.feature_types.deserialize_aws_json_1_1(
                data["FeatureTypes"]
            )
        )
    else:
        raise DeserializationError(
            "StartDocumentAnalysisRequest.feature_types required"
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
    if data.get("QueriesConfig") is not None:
        import capo_textract.types.queries_config

        out["queries_config"] = (
            capo_textract.types.queries_config.deserialize_aws_json_1_1(
                data["QueriesConfig"]
            )
        )
    if data.get("AdaptersConfig") is not None:
        import capo_textract.types.adapters_config

        out["adapters_config"] = (
            capo_textract.types.adapters_config.deserialize_aws_json_1_1(
                data["AdaptersConfig"]
            )
        )
    return out
