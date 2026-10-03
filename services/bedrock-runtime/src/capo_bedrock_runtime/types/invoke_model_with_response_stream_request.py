"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithResponseStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.body
    import capo_bedrock_runtime.types.guardrail_identifier
    import capo_bedrock_runtime.types.guardrail_version
    import capo_bedrock_runtime.types.invoke_model_identifier
    import capo_bedrock_runtime.types.mime_type
    import capo_bedrock_runtime.types.performance_config_latency
    import capo_bedrock_runtime.types.request_metadata_json
    import capo_bedrock_runtime.types.service_tier_type
    import capo_bedrock_runtime.types.trace


class InvokeModelWithResponseStreamRequest(TypedDict, closed=True):
    body: NotRequired["capo_bedrock_runtime.types.body.Body"]
    """<p>The prompt and inference parameters in the format specified in the <code>contentType</code> in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html">Run inference</a> in the Bedrock User Guide.</p>"""
    content_type: NotRequired["capo_bedrock_runtime.types.mime_type.MimeType"]
    """<p>The MIME type of the input data in the request. You must specify <code>application/json</code>.</p>"""
    accept: NotRequired["capo_bedrock_runtime.types.mime_type.MimeType"]
    """<p>The desired MIME type of the inference body in the response. The default value is <code>application/json</code>.</p>"""
    model_id: "capo_bedrock_runtime.types.invoke_model_identifier.InvokeModelIdentifier"
    """<p>The unique identifier of the model to invoke to run inference.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, specify the ARN of the custom model deployment (for on-demand inference) or the ARN of your provisioned model (for Provisioned Throughput). For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>"""
    trace: NotRequired["capo_bedrock_runtime.types.trace.Trace"]
    """<p>Specifies whether to enable or disable the Bedrock trace. If enabled, you can see the full Bedrock trace.</p>"""
    guardrail_identifier: NotRequired[
        "capo_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier"
    ]
    """<p>The unique identifier of the guardrail that you want to use. If you don't provide a value, no guardrail is applied to the invocation.</p> <p>An error is thrown in the following situations.</p> <ul> <li> <p>You don't provide a guardrail identifier but you specify the <code>amazon-bedrock-guardrailConfig</code> field in the request body.</p> </li> <li> <p>You enable the guardrail but the <code>contentType</code> isn't <code>application/json</code>.</p> </li> <li> <p>You provide a guardrail identifier, but <code>guardrailVersion</code> isn't specified.</p> </li> </ul>"""
    guardrail_version: NotRequired[
        "capo_bedrock_runtime.types.guardrail_version.GuardrailVersion"
    ]
    """<p>The version number for the guardrail. The value can also be <code>DRAFT</code>.</p>"""
    performance_config_latency: (
        "capo_bedrock_runtime.types.performance_config_latency.PerformanceConfigLatency"
    )
    """<p>Model performance settings for the request.</p>"""
    service_tier: NotRequired[
        "capo_bedrock_runtime.types.service_tier_type.ServiceTierType"
    ]
    """<p>Specifies the processing tier type used for serving the request.</p>"""
    request_metadata: NotRequired[
        "capo_bedrock_runtime.types.request_metadata_json.RequestMetadataJson"
    ]
    """<p>Key-value pairs that you can use to filter invocation logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeModelWithResponseStreamRequest) -> dict:
    out: dict = {}
    if "body" in value:
        import capo_bedrock_runtime.types.body

        out["body"] = capo_bedrock_runtime.types.body.serialize_json(value["body"])
    return out


def deserialize_json(data: dict) -> InvokeModelWithResponseStreamRequest:
    out: InvokeModelWithResponseStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        import capo_bedrock_runtime.types.body

        out["body"] = capo_bedrock_runtime.types.body.deserialize_json(data["body"])
    return out
