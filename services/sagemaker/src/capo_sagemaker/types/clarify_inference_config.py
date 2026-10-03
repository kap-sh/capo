"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyInferenceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.clarify_content_template
    import capo_sagemaker.types.clarify_feature_headers
    import capo_sagemaker.types.clarify_feature_types
    import capo_sagemaker.types.clarify_features_attribute
    import capo_sagemaker.types.clarify_label_attribute
    import capo_sagemaker.types.clarify_label_headers
    import capo_sagemaker.types.clarify_label_index
    import capo_sagemaker.types.clarify_max_payload_in_mb
    import capo_sagemaker.types.clarify_max_record_count
    import capo_sagemaker.types.clarify_probability_attribute
    import capo_sagemaker.types.clarify_probability_index


class ClarifyInferenceConfig(TypedDict, closed=True):
    features_attribute: NotRequired[
        "capo_sagemaker.types.clarify_features_attribute.ClarifyFeaturesAttribute"
    ]
    """<p>Provides the JMESPath expression to extract the features from a model container input in JSON Lines format. For example, if <code>FeaturesAttribute</code> is the JMESPath expression <code>'myfeatures'</code>, it extracts a list of features <code>[1,2,3]</code> from request data <code>'{"myfeatures":[1,2,3]}'</code>.</p>"""
    content_template: NotRequired[
        "capo_sagemaker.types.clarify_content_template.ClarifyContentTemplate"
    ]
    """<p>A template string used to format a JSON record into an acceptable model container input. For example, a <code>ContentTemplate</code> string <code>'{"myfeatures":$features}'</code> will format a list of features <code>[1,2,3]</code> into the record string <code>'{"myfeatures":[1,2,3]}'</code>. Required only when the model container input is in JSON Lines format.</p>"""
    max_record_count: NotRequired[
        "capo_sagemaker.types.clarify_max_record_count.ClarifyMaxRecordCount"
    ]
    """<p>The maximum number of records in a request that the model container can process when querying the model container for the predictions of a <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-synthetic">synthetic dataset</a>. A record is a unit of input data that inference can be made on, for example, a single line in CSV data. If <code>MaxRecordCount</code> is <code>1</code>, the model container expects one record per request. A value of 2 or greater means that the model expects batch requests, which can reduce overhead and speed up the inferencing process. If this parameter is not provided, the explainer will tune the record count per request according to the model container's capacity at runtime.</p>"""
    max_payload_in_mb: NotRequired[
        "capo_sagemaker.types.clarify_max_payload_in_mb.ClarifyMaxPayloadInMB"
    ]
    """<p>The maximum payload size (MB) allowed of a request from the explainer to the model container. Defaults to <code>6</code> MB.</p>"""
    probability_index: NotRequired[
        "capo_sagemaker.types.clarify_probability_index.ClarifyProbabilityIndex"
    ]
    r"""<p>A zero-based index used to extract a probability value (score) or list from model container output in CSV format. If this value is not provided, the entire model container output will be treated as a probability value (score) or list.</p> <p> <b>Example for a single class model:</b> If the model container output consists of a string-formatted prediction label followed by its probability: <code>'1,0.6'</code>, set <code>ProbabilityIndex</code> to <code>1</code> to select the probability value <code>0.6</code>.</p> <p> <b>Example for a multiclass model:</b> If the model container output consists of a string-formatted prediction label followed by its probability: <code>'"[\'cat\',\'dog\',\'fish\']","[0.1,0.6,0.3]"'</code>, set <code>ProbabilityIndex</code> to <code>1</code> to select the probability values <code>[0.1,0.6,0.3]</code>.</p>"""
    label_index: NotRequired[
        "capo_sagemaker.types.clarify_label_index.ClarifyLabelIndex"
    ]
    r"""<p>A zero-based index used to extract a label header or list of label headers from model container output in CSV format.</p> <p> <b>Example for a multiclass model:</b> If the model container output consists of label headers followed by probabilities: <code>'"[\'cat\',\'dog\',\'fish\']","[0.1,0.6,0.3]"'</code>, set <code>LabelIndex</code> to <code>0</code> to select the label headers <code>['cat','dog','fish']</code>.</p>"""
    probability_attribute: NotRequired[
        "capo_sagemaker.types.clarify_probability_attribute.ClarifyProbabilityAttribute"
    ]
    """<p>A JMESPath expression used to extract the probability (or score) from the model container output if the model container is in JSON Lines format.</p> <p> <b>Example</b>: If the model container output of a single request is <code>'{"predicted_label":1,"probability":0.6}'</code>, then set <code>ProbabilityAttribute</code> to <code>'probability'</code>.</p>"""
    label_attribute: NotRequired[
        "capo_sagemaker.types.clarify_label_attribute.ClarifyLabelAttribute"
    ]
    """<p>A JMESPath expression used to locate the list of label headers in the model container output.</p> <p> <b>Example</b>: If the model container output of a batch request is <code>'{"labels":["cat","dog","fish"],"probability":[0.6,0.3,0.1]}'</code>, then set <code>LabelAttribute</code> to <code>'labels'</code> to extract the list of label headers <code>["cat","dog","fish"]</code> </p>"""
    label_headers: NotRequired[
        "capo_sagemaker.types.clarify_label_headers.ClarifyLabelHeaders"
    ]
    """<p>For multiclass classification problems, the label headers are the names of the classes. Otherwise, the label header is the name of the predicted label. These are used to help readability for the output of the <code>InvokeEndpoint</code> API. See the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html#clarify-online-explainability-response">response</a> section under <b>Invoke the endpoint</b> in the Developer Guide for more information. If there are no label headers in the model container output, provide them manually using this parameter.</p>"""
    feature_headers: NotRequired[
        "capo_sagemaker.types.clarify_feature_headers.ClarifyFeatureHeaders"
    ]
    """<p>The names of the features. If provided, these are included in the endpoint response payload to help readability of the <code>InvokeEndpoint</code> output. See the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html#clarify-online-explainability-response">Response</a> section under <b>Invoke the endpoint</b> in the Developer Guide for more information.</p>"""
    feature_types: NotRequired[
        "capo_sagemaker.types.clarify_feature_types.ClarifyFeatureTypes"
    ]
    """<p>A list of data types of the features (optional). Applicable only to NLP explainability. If provided, <code>FeatureTypes</code> must have at least one <code>'text'</code> string (for example, <code>['text']</code>). If <code>FeatureTypes</code> is not provided, the explainer infers the feature types based on the baseline data. The feature types are included in the endpoint response payload. For additional information see the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-invoke-endpoint.html#clarify-online-explainability-response">response</a> section under <b>Invoke the endpoint</b> in the Developer Guide for more information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClarifyInferenceConfig) -> dict:
    out: dict = {}
    if "features_attribute" in value:
        out["FeaturesAttribute"] = value["features_attribute"]
    if "content_template" in value:
        out["ContentTemplate"] = value["content_template"]
    if "max_record_count" in value:
        out["MaxRecordCount"] = value["max_record_count"]
    if "max_payload_in_mb" in value:
        out["MaxPayloadInMB"] = value["max_payload_in_mb"]
    if "probability_index" in value:
        out["ProbabilityIndex"] = value["probability_index"]
    if "label_index" in value:
        out["LabelIndex"] = value["label_index"]
    if "probability_attribute" in value:
        out["ProbabilityAttribute"] = value["probability_attribute"]
    if "label_attribute" in value:
        out["LabelAttribute"] = value["label_attribute"]
    if "label_headers" in value:
        import capo_sagemaker.types.clarify_label_headers

        out["LabelHeaders"] = (
            capo_sagemaker.types.clarify_label_headers.serialize_aws_json_1_1(
                value["label_headers"]
            )
        )
    if "feature_headers" in value:
        import capo_sagemaker.types.clarify_feature_headers

        out["FeatureHeaders"] = (
            capo_sagemaker.types.clarify_feature_headers.serialize_aws_json_1_1(
                value["feature_headers"]
            )
        )
    if "feature_types" in value:
        import capo_sagemaker.types.clarify_feature_types

        out["FeatureTypes"] = (
            capo_sagemaker.types.clarify_feature_types.serialize_aws_json_1_1(
                value["feature_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClarifyInferenceConfig:
    out: ClarifyInferenceConfig = {}  # type: ignore[typeddict-item]
    if data.get("FeaturesAttribute") is not None:
        out["features_attribute"] = data["FeaturesAttribute"]
    if data.get("ContentTemplate") is not None:
        out["content_template"] = data["ContentTemplate"]
    if data.get("MaxRecordCount") is not None:
        out["max_record_count"] = data["MaxRecordCount"]
    if data.get("MaxPayloadInMB") is not None:
        out["max_payload_in_mb"] = data["MaxPayloadInMB"]
    if data.get("ProbabilityIndex") is not None:
        out["probability_index"] = data["ProbabilityIndex"]
    if data.get("LabelIndex") is not None:
        out["label_index"] = data["LabelIndex"]
    if data.get("ProbabilityAttribute") is not None:
        out["probability_attribute"] = data["ProbabilityAttribute"]
    if data.get("LabelAttribute") is not None:
        out["label_attribute"] = data["LabelAttribute"]
    if data.get("LabelHeaders") is not None:
        import capo_sagemaker.types.clarify_label_headers

        out["label_headers"] = (
            capo_sagemaker.types.clarify_label_headers.deserialize_aws_json_1_1(
                data["LabelHeaders"]
            )
        )
    if data.get("FeatureHeaders") is not None:
        import capo_sagemaker.types.clarify_feature_headers

        out["feature_headers"] = (
            capo_sagemaker.types.clarify_feature_headers.deserialize_aws_json_1_1(
                data["FeatureHeaders"]
            )
        )
    if data.get("FeatureTypes") is not None:
        import capo_sagemaker.types.clarify_feature_types

        out["feature_types"] = (
            capo_sagemaker.types.clarify_feature_types.deserialize_aws_json_1_1(
                data["FeatureTypes"]
            )
        )
    return out
