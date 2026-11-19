"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierInputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_classifier_augmented_manifests_list
    import capo_comprehend.types.document_classifier_data_format
    import capo_comprehend.types.document_classifier_document_type_format
    import capo_comprehend.types.document_classifier_documents
    import capo_comprehend.types.document_reader_config
    import capo_comprehend.types.label_delimiter
    import capo_comprehend.types.s3_uri


class DocumentClassifierInputDataConfig(TypedDict, closed=True):
    data_format: NotRequired[
        "capo_comprehend.types.document_classifier_data_format.DocumentClassifierDataFormat"
    ]
    """<p>The format of your training data:</p> <ul> <li> <p> <code>COMPREHEND_CSV</code>: A two-column CSV file, where labels are provided in the first column, and documents are provided in the second. If you use this value, you must provide the <code>S3Uri</code> parameter in your request.</p> </li> <li> <p> <code>AUGMENTED_MANIFEST</code>: A labeled dataset that is produced by Amazon SageMaker Ground Truth. This file is in JSON lines format. Each line is a complete JSON object that contains a training document and its associated labels. </p> <p>If you use this value, you must provide the <code>AugmentedManifests</code> parameter in your request.</p> </li> </ul> <p>If you don't specify a value, Amazon Comprehend uses <code>COMPREHEND_CSV</code> as the default.</p>"""
    s3_uri: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 URI for the input data. The S3 bucket must be in the same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of input files.</p> <p>For example, if you use the URI <code>S3://bucketName/prefix</code>, if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.</p> <p>This parameter is required if you set <code>DataFormat</code> to <code>COMPREHEND_CSV</code>.</p>"""
    test_s3_uri: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p>This specifies the Amazon S3 location that contains the test annotations for the document classifier. The URI must be in the same Amazon Web Services Region as the API endpoint that you are calling. </p>"""
    label_delimiter: NotRequired["capo_comprehend.types.label_delimiter.LabelDelimiter"]
    """<p>Indicates the delimiter used to separate each label for training a multi-label classifier. The default delimiter between labels is a pipe (|). You can use a different character as a delimiter (if it's an allowed character) by specifying it under Delimiter for labels. If the training documents use a delimiter other than the default or the delimiter you specify, the labels on that line will be combined to make a single unique label, such as LABELLABELLABEL.</p>"""
    augmented_manifests: NotRequired[
        "capo_comprehend.types.document_classifier_augmented_manifests_list.DocumentClassifierAugmentedManifestsList"
    ]
    """<p>A list of augmented manifest files that provide training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.</p> <p>This parameter is required if you set <code>DataFormat</code> to <code>AUGMENTED_MANIFEST</code>.</p>"""
    document_type: NotRequired[
        "capo_comprehend.types.document_classifier_document_type_format.DocumentClassifierDocumentTypeFormat"
    ]
    """<p>The type of input documents for training the model. Provide plain-text documents to create a plain-text model, and provide semi-structured documents to create a native document model.</p>"""
    documents: NotRequired[
        "capo_comprehend.types.document_classifier_documents.DocumentClassifierDocuments"
    ]
    """<p>The S3 location of the training documents. This parameter is required in a request to create a native document model.</p>"""
    document_reader_config: NotRequired[
        "capo_comprehend.types.document_reader_config.DocumentReaderConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierInputDataConfig) -> dict:
    out: dict = {}
    if "data_format" in value:
        import capo_comprehend.types.document_classifier_data_format

        out["DataFormat"] = (
            capo_comprehend.types.document_classifier_data_format.serialize_aws_json_1_1(
                value["data_format"]
            )
        )
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "test_s3_uri" in value:
        out["TestS3Uri"] = value["test_s3_uri"]
    if "label_delimiter" in value:
        out["LabelDelimiter"] = value["label_delimiter"]
    if "augmented_manifests" in value:
        import capo_comprehend.types.document_classifier_augmented_manifests_list

        out["AugmentedManifests"] = (
            capo_comprehend.types.document_classifier_augmented_manifests_list.serialize_aws_json_1_1(
                value["augmented_manifests"]
            )
        )
    if "document_type" in value:
        import capo_comprehend.types.document_classifier_document_type_format

        out["DocumentType"] = (
            capo_comprehend.types.document_classifier_document_type_format.serialize_aws_json_1_1(
                value["document_type"]
            )
        )
    if "documents" in value:
        import capo_comprehend.types.document_classifier_documents

        out["Documents"] = (
            capo_comprehend.types.document_classifier_documents.serialize_aws_json_1_1(
                value["documents"]
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


def deserialize_aws_json_1_1(data: dict) -> DocumentClassifierInputDataConfig:
    out: DocumentClassifierInputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("DataFormat") is not None:
        import capo_comprehend.types.document_classifier_data_format

        out["data_format"] = (
            capo_comprehend.types.document_classifier_data_format.deserialize_aws_json_1_1(
                data["DataFormat"]
            )
        )
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    if data.get("TestS3Uri") is not None:
        out["test_s3_uri"] = data["TestS3Uri"]
    if data.get("LabelDelimiter") is not None:
        out["label_delimiter"] = data["LabelDelimiter"]
    if data.get("AugmentedManifests") is not None:
        import capo_comprehend.types.document_classifier_augmented_manifests_list

        out["augmented_manifests"] = (
            capo_comprehend.types.document_classifier_augmented_manifests_list.deserialize_aws_json_1_1(
                data["AugmentedManifests"]
            )
        )
    if data.get("DocumentType") is not None:
        import capo_comprehend.types.document_classifier_document_type_format

        out["document_type"] = (
            capo_comprehend.types.document_classifier_document_type_format.deserialize_aws_json_1_1(
                data["DocumentType"]
            )
        )
    if data.get("Documents") is not None:
        import capo_comprehend.types.document_classifier_documents

        out["documents"] = (
            capo_comprehend.types.document_classifier_documents.deserialize_aws_json_1_1(
                data["Documents"]
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


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentClassifierInputDataConfig) -> dict:
    out: dict = {}
    if "data_format" in value:
        import capo_comprehend.types.document_classifier_data_format

        out["DataFormat"] = (
            capo_comprehend.types.document_classifier_data_format.serialize_cbor(
                value["data_format"]
            )
        )
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "test_s3_uri" in value:
        out["TestS3Uri"] = value["test_s3_uri"]
    if "label_delimiter" in value:
        out["LabelDelimiter"] = value["label_delimiter"]
    if "augmented_manifests" in value:
        import capo_comprehend.types.document_classifier_augmented_manifests_list

        out["AugmentedManifests"] = (
            capo_comprehend.types.document_classifier_augmented_manifests_list.serialize_cbor(
                value["augmented_manifests"]
            )
        )
    if "document_type" in value:
        import capo_comprehend.types.document_classifier_document_type_format

        out["DocumentType"] = (
            capo_comprehend.types.document_classifier_document_type_format.serialize_cbor(
                value["document_type"]
            )
        )
    if "documents" in value:
        import capo_comprehend.types.document_classifier_documents

        out["Documents"] = (
            capo_comprehend.types.document_classifier_documents.serialize_cbor(
                value["documents"]
            )
        )
    if "document_reader_config" in value:
        import capo_comprehend.types.document_reader_config

        out["DocumentReaderConfig"] = (
            capo_comprehend.types.document_reader_config.serialize_cbor(
                value["document_reader_config"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DocumentClassifierInputDataConfig:
    out: DocumentClassifierInputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("DataFormat") is not None:
        import capo_comprehend.types.document_classifier_data_format

        out["data_format"] = (
            capo_comprehend.types.document_classifier_data_format.deserialize_cbor(
                data["DataFormat"]
            )
        )
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    if data.get("TestS3Uri") is not None:
        out["test_s3_uri"] = data["TestS3Uri"]
    if data.get("LabelDelimiter") is not None:
        out["label_delimiter"] = data["LabelDelimiter"]
    if data.get("AugmentedManifests") is not None:
        import capo_comprehend.types.document_classifier_augmented_manifests_list

        out["augmented_manifests"] = (
            capo_comprehend.types.document_classifier_augmented_manifests_list.deserialize_cbor(
                data["AugmentedManifests"]
            )
        )
    if data.get("DocumentType") is not None:
        import capo_comprehend.types.document_classifier_document_type_format

        out["document_type"] = (
            capo_comprehend.types.document_classifier_document_type_format.deserialize_cbor(
                data["DocumentType"]
            )
        )
    if data.get("Documents") is not None:
        import capo_comprehend.types.document_classifier_documents

        out["documents"] = (
            capo_comprehend.types.document_classifier_documents.deserialize_cbor(
                data["Documents"]
            )
        )
    if data.get("DocumentReaderConfig") is not None:
        import capo_comprehend.types.document_reader_config

        out["document_reader_config"] = (
            capo_comprehend.types.document_reader_config.deserialize_cbor(
                data["DocumentReaderConfig"]
            )
        )
    return out
