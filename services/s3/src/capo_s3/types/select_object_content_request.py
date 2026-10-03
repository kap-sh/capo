"""Generated from Smithy shape ``com.amazonaws.s3#SelectObjectContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.expression
    import capo_s3.types.expression_type
    import capo_s3.types.input_serialization
    import capo_s3.types.object_key
    import capo_s3.types.output_serialization
    import capo_s3.types.request_progress
    import capo_s3.types.scan_range
    import capo_s3.types.sse_customer_algorithm
    import capo_s3.types.sse_customer_key
    import capo_s3.types.sse_customer_key_md5


class SelectObjectContentRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The S3 bucket.</p>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>The object key.</p>"""
    sse_customer_algorithm: NotRequired[
        "capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm"
    ]
    """<p>The server-side encryption (SSE) algorithm used to encrypt the object. This parameter is needed only when the object was created using a checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html">Protecting data using SSE-C keys</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    sse_customer_key: NotRequired["capo_s3.types.sse_customer_key.SSECustomerKey"]
    """<p>The server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html">Protecting data using SSE-C keys</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    sse_customer_key_md5: NotRequired[
        "capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5"
    ]
    """<p>The MD5 server-side encryption (SSE) customer managed key. This parameter is needed only when the object was created using a checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html">Protecting data using SSE-C keys</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    expression: "capo_s3.types.expression.Expression"
    """<p>The expression that is used to query the object.</p>"""
    expression_type: "capo_s3.types.expression_type.ExpressionType"
    """<p>The type of the provided expression (for example, SQL).</p>"""
    request_progress: NotRequired["capo_s3.types.request_progress.RequestProgress"]
    """<p>Specifies if periodic request progress information should be enabled.</p>"""
    input_serialization: "capo_s3.types.input_serialization.InputSerialization"
    """<p>Describes the format of the data in the object that is being queried.</p>"""
    output_serialization: "capo_s3.types.output_serialization.OutputSerialization"
    """<p>Describes the format of the data that you want Amazon S3 to return in response.</p>"""
    scan_range: NotRequired["capo_s3.types.scan_range.ScanRange"]
    """<p>Specifies the byte range of the object to get the records from. A record is processed when its first byte is contained by the range. This parameter is optional, but when specified, it must not be empty. See RFC 2616, Section 14.35.1 about how to specify the start and end of the range.</p> <p> <code>ScanRange</code>may be used in the following ways:</p> <ul> <li> <p> <code><scanrange><start>50</start><end>100</end></scanrange></code> - process only the records starting between the bytes 50 and 100 (inclusive, counting from zero)</p> </li> <li> <p> <code><scanrange><start>50</start></scanrange></code> - process only the records starting after the byte 50</p> </li> <li> <p> <code><scanrange><end>50</end></scanrange></code> - process only the records within the last 50 bytes of the file.</p> </li> </ul>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""


# --- restXml ser/de ---
def serialize_xml(value: SelectObjectContentRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Expression").text = str(value["expression"])
    import capo_s3.types.expression_type

    capo_s3.types.expression_type.serialize_xml(
        value["expression_type"], el, "ExpressionType"
    )
    if "request_progress" in value:
        import capo_s3.types.request_progress

        capo_s3.types.request_progress.serialize_xml(
            value["request_progress"], el, "RequestProgress"
        )
    import capo_s3.types.input_serialization

    capo_s3.types.input_serialization.serialize_xml(
        value["input_serialization"], el, "InputSerialization"
    )
    import capo_s3.types.output_serialization

    capo_s3.types.output_serialization.serialize_xml(
        value["output_serialization"], el, "OutputSerialization"
    )
    if "scan_range" in value:
        import capo_s3.types.scan_range

        capo_s3.types.scan_range.serialize_xml(value["scan_range"], el, "ScanRange")


def deserialize_xml(el: Element) -> SelectObjectContentRequest:
    out: SelectObjectContentRequest = {}  # type: ignore[typeddict-item]
    child_expression = el.find("Expression")
    if child_expression is not None:
        out["expression"] = str(child_expression.text or "")
    else:
        raise DeserializationError("SelectObjectContentRequest.expression required")
    child_expression_type = el.find("ExpressionType")
    if child_expression_type is not None:
        import capo_s3.types.expression_type

        out["expression_type"] = capo_s3.types.expression_type.deserialize_xml(
            child_expression_type
        )
    else:
        raise DeserializationError(
            "SelectObjectContentRequest.expression_type required"
        )
    child_request_progress = el.find("RequestProgress")
    if child_request_progress is not None:
        import capo_s3.types.request_progress

        out["request_progress"] = capo_s3.types.request_progress.deserialize_xml(
            child_request_progress
        )
    child_input_serialization = el.find("InputSerialization")
    if child_input_serialization is not None:
        import capo_s3.types.input_serialization

        out["input_serialization"] = capo_s3.types.input_serialization.deserialize_xml(
            child_input_serialization
        )
    else:
        raise DeserializationError(
            "SelectObjectContentRequest.input_serialization required"
        )
    child_output_serialization = el.find("OutputSerialization")
    if child_output_serialization is not None:
        import capo_s3.types.output_serialization

        out["output_serialization"] = (
            capo_s3.types.output_serialization.deserialize_xml(
                child_output_serialization
            )
        )
    else:
        raise DeserializationError(
            "SelectObjectContentRequest.output_serialization required"
        )
    child_scan_range = el.find("ScanRange")
    if child_scan_range is not None:
        import capo_s3.types.scan_range

        out["scan_range"] = capo_s3.types.scan_range.deserialize_xml(child_scan_range)
    return out
