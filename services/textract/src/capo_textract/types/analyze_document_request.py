"""Generated from Smithy shape ``com.amazonaws.textract#AnalyzeDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_textract.errors import DeserializationError

if TYPE_CHECKING:
    import capo_textract.types.adapters_config
    import capo_textract.types.document
    import capo_textract.types.feature_types
    import capo_textract.types.human_loop_config
    import capo_textract.types.queries_config


class AnalyzeDocumentRequest(TypedDict, closed=True):
    document: "capo_textract.types.document.Document"
    """<p>The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Textract operations, you can't pass image bytes. The document must be an image in JPEG, PNG, PDF, or TIFF format.</p> <p>If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes that are passed using the <code>Bytes</code> field. </p>"""
    feature_types: "capo_textract.types.feature_types.FeatureTypes"
    """<p>A list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected form data. Add SIGNATURES to return the locations of detected signatures. Add LAYOUT to the list to return information about the layout of the document. All lines and words detected in the document are included in the response (including text that isn't related to the value of <code>FeatureTypes</code>). </p>"""
    human_loop_config: NotRequired[
        "capo_textract.types.human_loop_config.HumanLoopConfig"
    ]
    """<p>Sets the configuration for the human in the loop workflow for analyzing documents.</p> <note> <p>Amazon Textract uses Amazon Augmented AI (A2I) to run the human review workflows that you specify in <code>HumanLoopConfig</code>. A2I entered maintenance mode in July 2026 and no longer accepts new customers. If your account is not an existing A2I customer, requests fail with an <code>InvalidParameterException</code>. For more information, see <a href="https://aws.amazon.com/about-aws/whats-new/2026/06/aws-service-availability/">AWS service availability</a>. If you're an existing A2I customer but receive this error, contact AWS Support and request assistance from the A2I team.</p> </note>"""
    queries_config: NotRequired["capo_textract.types.queries_config.QueriesConfig"]
    """<p>Contains Queries and the alias for those Queries, as determined by the input. </p>"""
    adapters_config: NotRequired["capo_textract.types.adapters_config.AdaptersConfig"]
    """<p>Specifies the adapter to be used when analyzing a document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyzeDocumentRequest) -> dict:
    out: dict = {}
    import capo_textract.types.document

    out["Document"] = capo_textract.types.document.serialize_aws_json_1_1(
        value["document"]
    )
    import capo_textract.types.feature_types

    out["FeatureTypes"] = capo_textract.types.feature_types.serialize_aws_json_1_1(
        value["feature_types"]
    )
    if "human_loop_config" in value:
        import capo_textract.types.human_loop_config

        out["HumanLoopConfig"] = (
            capo_textract.types.human_loop_config.serialize_aws_json_1_1(
                value["human_loop_config"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> AnalyzeDocumentRequest:
    out: AnalyzeDocumentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Document") is not None:
        import capo_textract.types.document

        out["document"] = capo_textract.types.document.deserialize_aws_json_1_1(
            data["Document"]
        )
    else:
        raise DeserializationError("AnalyzeDocumentRequest.document required")
    if data.get("FeatureTypes") is not None:
        import capo_textract.types.feature_types

        out["feature_types"] = (
            capo_textract.types.feature_types.deserialize_aws_json_1_1(
                data["FeatureTypes"]
            )
        )
    else:
        raise DeserializationError("AnalyzeDocumentRequest.feature_types required")
    if data.get("HumanLoopConfig") is not None:
        import capo_textract.types.human_loop_config

        out["human_loop_config"] = (
            capo_textract.types.human_loop_config.deserialize_aws_json_1_1(
                data["HumanLoopConfig"]
            )
        )
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
