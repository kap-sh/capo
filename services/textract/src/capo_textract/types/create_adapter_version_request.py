"""Generated from Smithy shape ``com.amazonaws.textract#CreateAdapterVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_textract.errors import DeserializationError

if TYPE_CHECKING:
    import capo_textract.types.adapter_id
    import capo_textract.types.adapter_version_dataset_config
    import capo_textract.types.client_request_token
    import capo_textract.types.kms_key_id
    import capo_textract.types.output_config
    import capo_textract.types.tag_map


class CreateAdapterVersionRequest(TypedDict, closed=True):
    adapter_id: "capo_textract.types.adapter_id.AdapterId"
    """<p>A string containing a unique ID for the adapter that will receive a new version.</p>"""
    client_request_token: NotRequired[
        "capo_textract.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotent token is used to recognize the request. If the same token is used with multiple CreateAdapterVersion requests, the same session is returned. This token is employed to avoid unintentionally creating the same session multiple times.</p>"""
    dataset_config: (
        "capo_textract.types.adapter_version_dataset_config.AdapterVersionDatasetConfig"
    )
    """<p>Specifies a dataset used to train a new adapter version. Takes a ManifestS3Object as the value.</p>"""
    kms_key_id: NotRequired["capo_textract.types.kms_key_id.KMSKeyId"]
    """<p>The identifier for your AWS Key Management Service key (AWS KMS key). Used to encrypt your documents.</p>"""
    output_config: "capo_textract.types.output_config.OutputConfig"
    tags: NotRequired["capo_textract.types.tag_map.TagMap"]
    """<p>A set of tags (key-value pairs) that you want to attach to the adapter version. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAdapterVersionRequest) -> dict:
    out: dict = {}
    out["AdapterId"] = value["adapter_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    import capo_textract.types.adapter_version_dataset_config

    out["DatasetConfig"] = (
        capo_textract.types.adapter_version_dataset_config.serialize_aws_json_1_1(
            value["dataset_config"]
        )
    )
    if "kms_key_id" in value:
        out["KMSKeyId"] = value["kms_key_id"]
    import capo_textract.types.output_config

    out["OutputConfig"] = capo_textract.types.output_config.serialize_aws_json_1_1(
        value["output_config"]
    )
    if "tags" in value:
        import capo_textract.types.tag_map

        out["Tags"] = capo_textract.types.tag_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAdapterVersionRequest:
    out: CreateAdapterVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    else:
        out["adapter_id"] = ""
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("DatasetConfig") is not None:
        import capo_textract.types.adapter_version_dataset_config

        out["dataset_config"] = (
            capo_textract.types.adapter_version_dataset_config.deserialize_aws_json_1_1(
                data["DatasetConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAdapterVersionRequest.dataset_config required"
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
    else:
        raise DeserializationError("CreateAdapterVersionRequest.output_config required")
    if data.get("Tags") is not None:
        import capo_textract.types.tag_map

        out["tags"] = capo_textract.types.tag_map.deserialize_aws_json_1_1(data["Tags"])
    return out
