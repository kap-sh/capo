"""Generated from Smithy shape ``com.amazonaws.textract#GetAdapterVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.adapter_id
    import capo_textract.types.adapter_version
    import capo_textract.types.adapter_version_dataset_config
    import capo_textract.types.adapter_version_evaluation_metrics
    import capo_textract.types.adapter_version_status
    import capo_textract.types.adapter_version_status_message
    import capo_textract.types.date_time
    import capo_textract.types.feature_types
    import capo_textract.types.kms_key_id
    import capo_textract.types.output_config
    import capo_textract.types.tag_map


class GetAdapterVersionResponse(TypedDict, closed=True):
    adapter_id: NotRequired["capo_textract.types.adapter_id.AdapterId"]
    """<p>A string containing a unique ID for the adapter version being retrieved.</p>"""
    adapter_version: NotRequired["capo_textract.types.adapter_version.AdapterVersion"]
    """<p>A string containing the adapter version that has been retrieved.</p>"""
    creation_time: NotRequired["capo_textract.types.date_time.DateTime"]
    """<p>The time that the adapter version was created.</p>"""
    feature_types: NotRequired["capo_textract.types.feature_types.FeatureTypes"]
    """<p>List of the targeted feature types for the requested adapter version.</p>"""
    status: NotRequired[
        "capo_textract.types.adapter_version_status.AdapterVersionStatus"
    ]
    """<p>The status of the adapter version that has been requested.</p>"""
    status_message: NotRequired[
        "capo_textract.types.adapter_version_status_message.AdapterVersionStatusMessage"
    ]
    """<p>A message that describes the status of the requested adapter version.</p>"""
    dataset_config: NotRequired[
        "capo_textract.types.adapter_version_dataset_config.AdapterVersionDatasetConfig"
    ]
    """<p>Specifies a dataset used to train a new adapter version. Takes a ManifestS3Objec as the value.</p>"""
    kms_key_id: NotRequired["capo_textract.types.kms_key_id.KMSKeyId"]
    """<p>The identifier for your AWS Key Management Service key (AWS KMS key). Used to encrypt your documents.</p>"""
    output_config: NotRequired["capo_textract.types.output_config.OutputConfig"]
    evaluation_metrics: NotRequired[
        "capo_textract.types.adapter_version_evaluation_metrics.AdapterVersionEvaluationMetrics"
    ]
    """<p>The evaluation metrics (F1 score, Precision, and Recall) for the requested version, grouped by baseline metrics and adapter version.</p>"""
    tags: NotRequired["capo_textract.types.tag_map.TagMap"]
    """<p>A set of tags (key-value pairs) that are associated with the adapter version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdapterVersionResponse) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "adapter_version" in value:
        out["AdapterVersion"] = value["adapter_version"]
    if "creation_time" in value:
        import capo_textract.types.date_time

        out["CreationTime"] = capo_textract.types.date_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "feature_types" in value:
        import capo_textract.types.feature_types

        out["FeatureTypes"] = capo_textract.types.feature_types.serialize_aws_json_1_1(
            value["feature_types"]
        )
    if "status" in value:
        import capo_textract.types.adapter_version_status

        out["Status"] = (
            capo_textract.types.adapter_version_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "dataset_config" in value:
        import capo_textract.types.adapter_version_dataset_config

        out["DatasetConfig"] = (
            capo_textract.types.adapter_version_dataset_config.serialize_aws_json_1_1(
                value["dataset_config"]
            )
        )
    if "kms_key_id" in value:
        out["KMSKeyId"] = value["kms_key_id"]
    if "output_config" in value:
        import capo_textract.types.output_config

        out["OutputConfig"] = capo_textract.types.output_config.serialize_aws_json_1_1(
            value["output_config"]
        )
    if "evaluation_metrics" in value:
        import capo_textract.types.adapter_version_evaluation_metrics

        out["EvaluationMetrics"] = (
            capo_textract.types.adapter_version_evaluation_metrics.serialize_aws_json_1_1(
                value["evaluation_metrics"]
            )
        )
    if "tags" in value:
        import capo_textract.types.tag_map

        out["Tags"] = capo_textract.types.tag_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdapterVersionResponse:
    out: GetAdapterVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    if data.get("AdapterVersion") is not None:
        out["adapter_version"] = data["AdapterVersion"]
    if data.get("CreationTime") is not None:
        import capo_textract.types.date_time

        out["creation_time"] = capo_textract.types.date_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("FeatureTypes") is not None:
        import capo_textract.types.feature_types

        out["feature_types"] = (
            capo_textract.types.feature_types.deserialize_aws_json_1_1(
                data["FeatureTypes"]
            )
        )
    if data.get("Status") is not None:
        import capo_textract.types.adapter_version_status

        out["status"] = (
            capo_textract.types.adapter_version_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("DatasetConfig") is not None:
        import capo_textract.types.adapter_version_dataset_config

        out["dataset_config"] = (
            capo_textract.types.adapter_version_dataset_config.deserialize_aws_json_1_1(
                data["DatasetConfig"]
            )
        )
    if data.get("KMSKeyId") is not None:
        out["kms_key_id"] = data["KMSKeyId"]
    if data.get("OutputConfig") is not None:
        import capo_textract.types.output_config

        out["output_config"] = (
            capo_textract.types.output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if data.get("EvaluationMetrics") is not None:
        import capo_textract.types.adapter_version_evaluation_metrics

        out["evaluation_metrics"] = (
            capo_textract.types.adapter_version_evaluation_metrics.deserialize_aws_json_1_1(
                data["EvaluationMetrics"]
            )
        )
    if data.get("Tags") is not None:
        import capo_textract.types.tag_map

        out["tags"] = capo_textract.types.tag_map.deserialize_aws_json_1_1(data["Tags"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAdapterVersionResponse) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "adapter_version" in value:
        out["AdapterVersion"] = value["adapter_version"]
    if "creation_time" in value:
        import capo_textract.types.date_time

        out["CreationTime"] = capo_textract.types.date_time.serialize_cbor(
            value["creation_time"]
        )
    if "feature_types" in value:
        import capo_textract.types.feature_types

        out["FeatureTypes"] = capo_textract.types.feature_types.serialize_cbor(
            value["feature_types"]
        )
    if "status" in value:
        import capo_textract.types.adapter_version_status

        out["Status"] = capo_textract.types.adapter_version_status.serialize_cbor(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "dataset_config" in value:
        import capo_textract.types.adapter_version_dataset_config

        out["DatasetConfig"] = (
            capo_textract.types.adapter_version_dataset_config.serialize_cbor(
                value["dataset_config"]
            )
        )
    if "kms_key_id" in value:
        out["KMSKeyId"] = value["kms_key_id"]
    if "output_config" in value:
        import capo_textract.types.output_config

        out["OutputConfig"] = capo_textract.types.output_config.serialize_cbor(
            value["output_config"]
        )
    if "evaluation_metrics" in value:
        import capo_textract.types.adapter_version_evaluation_metrics

        out["EvaluationMetrics"] = (
            capo_textract.types.adapter_version_evaluation_metrics.serialize_cbor(
                value["evaluation_metrics"]
            )
        )
    if "tags" in value:
        import capo_textract.types.tag_map

        out["Tags"] = capo_textract.types.tag_map.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> GetAdapterVersionResponse:
    out: GetAdapterVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    if data.get("AdapterVersion") is not None:
        out["adapter_version"] = data["AdapterVersion"]
    if data.get("CreationTime") is not None:
        import capo_textract.types.date_time

        out["creation_time"] = capo_textract.types.date_time.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("FeatureTypes") is not None:
        import capo_textract.types.feature_types

        out["feature_types"] = capo_textract.types.feature_types.deserialize_cbor(
            data["FeatureTypes"]
        )
    if data.get("Status") is not None:
        import capo_textract.types.adapter_version_status

        out["status"] = capo_textract.types.adapter_version_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("DatasetConfig") is not None:
        import capo_textract.types.adapter_version_dataset_config

        out["dataset_config"] = (
            capo_textract.types.adapter_version_dataset_config.deserialize_cbor(
                data["DatasetConfig"]
            )
        )
    if data.get("KMSKeyId") is not None:
        out["kms_key_id"] = data["KMSKeyId"]
    if data.get("OutputConfig") is not None:
        import capo_textract.types.output_config

        out["output_config"] = capo_textract.types.output_config.deserialize_cbor(
            data["OutputConfig"]
        )
    if data.get("EvaluationMetrics") is not None:
        import capo_textract.types.adapter_version_evaluation_metrics

        out["evaluation_metrics"] = (
            capo_textract.types.adapter_version_evaluation_metrics.deserialize_cbor(
                data["EvaluationMetrics"]
            )
        )
    if data.get("Tags") is not None:
        import capo_textract.types.tag_map

        out["tags"] = capo_textract.types.tag_map.deserialize_cbor(data["Tags"])
    return out
