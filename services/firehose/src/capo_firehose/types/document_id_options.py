"""Generated from Smithy shape ``com.amazonaws.firehose#DocumentIdOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.default_document_id_format


class DocumentIdOptions(TypedDict, closed=True):
    default_document_id_format: (
        "capo_firehose.types.default_document_id_format.DefaultDocumentIdFormat"
    )
    """<p>When the <code>FIREHOSE_DEFAULT</code> option is chosen, Firehose generates a unique document ID for each record based on a unique internal identifier. The generated document ID is stable across multiple delivery attempts, which helps prevent the same record from being indexed multiple times with different document IDs.</p> <p>When the <code>NO_DOCUMENT_ID</code> option is chosen, Firehose does not include any document IDs in the requests it sends to the Amazon OpenSearch Service. This causes the Amazon OpenSearch Service domain to generate document IDs. In case of multiple delivery attempts, this may cause the same record to be indexed more than once with different document IDs. This option enables write-heavy operations, such as the ingestion of logs and observability data, to consume less resources in the Amazon OpenSearch Service domain, resulting in improved performance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentIdOptions) -> dict:
    out: dict = {}
    import capo_firehose.types.default_document_id_format

    out["DefaultDocumentIdFormat"] = (
        capo_firehose.types.default_document_id_format.serialize_aws_json_1_1(
            value["default_document_id_format"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentIdOptions:
    out: DocumentIdOptions = {}  # type: ignore[typeddict-item]
    if data.get("DefaultDocumentIdFormat") is not None:
        import capo_firehose.types.default_document_id_format

        out["default_document_id_format"] = (
            capo_firehose.types.default_document_id_format.deserialize_aws_json_1_1(
                data["DefaultDocumentIdFormat"]
            )
        )
    else:
        import typing

        out["default_document_id_format"] = typing.cast(
            "capo_firehose.types.default_document_id_format.DefaultDocumentIdFormat", ""
        )
    return out
