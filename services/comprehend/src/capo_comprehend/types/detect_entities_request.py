"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectEntitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.customer_input_string
    import capo_comprehend.types.document_reader_config
    import capo_comprehend.types.entity_recognizer_endpoint_arn
    import capo_comprehend.types.language_code
    import capo_comprehend.types.semi_structured_document_blob


class DetectEntitiesRequest(TypedDict, closed=True):
    text: NotRequired["capo_comprehend.types.customer_input_string.CustomerInputString"]
    """<p>A UTF-8 text string. The maximum string size is 100 KB. If you enter text using this parameter, do not use the <code>Bytes</code> parameter.</p>"""
    language_code: NotRequired["capo_comprehend.types.language_code.LanguageCode"]
    """<p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. If your request includes the endpoint for a custom entity recognition model, Amazon Comprehend uses the language of your custom model, and it ignores any language code that you specify here.</p> <p>All input documents must be in the same language.</p>"""
    endpoint_arn: NotRequired[
        "capo_comprehend.types.entity_recognizer_endpoint_arn.EntityRecognizerEndpointArn"
    ]
    """<p>The Amazon Resource Name of an endpoint that is associated with a custom entity recognition model. Provide an endpoint if you want to detect entities by using your own custom model instead of the default model that is used by Amazon Comprehend.</p> <p>If you specify an endpoint, Amazon Comprehend uses the language of your custom model, and it ignores any language code that you provide in your request.</p> <p>For information about endpoints, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html">Managing endpoints</a>.</p>"""
    bytes: NotRequired[
        "capo_comprehend.types.semi_structured_document_blob.SemiStructuredDocumentBlob"
    ]
    """<p>This field applies only when you use a custom entity recognition model that was trained with PDF annotations. For other cases, enter your text input in the <code>Text</code> field.</p> <p> Use the <code>Bytes</code> parameter to input a text, PDF, Word or image file. Using a plain-text file in the <code>Bytes</code> parameter is equivelent to using the <code>Text</code> parameter (the <code>Entities</code> field in the response is identical).</p> <p>You can also use the <code>Bytes</code> parameter to input an Amazon Textract <code>DetectDocumentText</code> or <code>AnalyzeDocument</code> output file.</p> <p>Provide the input document as a sequence of base64-encoded bytes. If your code uses an Amazon Web Services SDK to detect entities, the SDK may encode the document file bytes for you. </p> <p>The maximum length of this field depends on the input document type. For details, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync.html"> Inputs for real-time custom analysis</a> in the Comprehend Developer Guide. </p> <p>If you use the <code>Bytes</code> parameter, do not use the <code>Text</code> parameter.</p>"""
    document_reader_config: NotRequired[
        "capo_comprehend.types.document_reader_config.DocumentReaderConfig"
    ]
    """<p>Provides configuration parameters to override the default actions for extracting text from PDF documents and image files.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectEntitiesRequest) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "language_code" in value:
        import capo_comprehend.types.language_code

        out["LanguageCode"] = (
            capo_comprehend.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "bytes" in value:
        import capo_comprehend.types.semi_structured_document_blob

        out["Bytes"] = (
            capo_comprehend.types.semi_structured_document_blob.serialize_aws_json_1_1(
                value["bytes"]
            )
        )
    if "document_reader_config" in value:
        import capo_comprehend.types.document_reader_config

        out["DocumentReaderConfig"] = (
            capo_comprehend.types.document_reader_config.serialize_aws_json_1_1(
                value["document_reader_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectEntitiesRequest:
    out: DetectEntitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    if data.get("LanguageCode") is not None:
        import capo_comprehend.types.language_code

        out["language_code"] = (
            capo_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    if data.get("Bytes") is not None:
        import capo_comprehend.types.semi_structured_document_blob

        out["bytes"] = (
            capo_comprehend.types.semi_structured_document_blob.deserialize_aws_json_1_1(
                data["Bytes"]
            )
        )
    if data.get("DocumentReaderConfig") is not None:
        import capo_comprehend.types.document_reader_config

        out["document_reader_config"] = (
            capo_comprehend.types.document_reader_config.deserialize_aws_json_1_1(
                data["DocumentReaderConfig"]
            )
        )
    return out
