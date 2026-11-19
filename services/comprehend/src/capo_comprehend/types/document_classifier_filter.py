"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_arn_name
    import capo_comprehend.types.model_status
    import capo_comprehend.types.timestamp


class DocumentClassifierFilter(TypedDict, closed=True):
    status: NotRequired["capo_comprehend.types.model_status.ModelStatus"]
    """<p>Filters the list of classifiers based on status.</p>"""
    document_classifier_name: NotRequired[
        "capo_comprehend.types.comprehend_arn_name.ComprehendArnName"
    ]
    """<p>The name that you assigned to the document classifier</p>"""
    submit_time_before: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Filters the list of classifiers based on the time that the classifier was submitted for processing. Returns only classifiers submitted before the specified time. Classifiers are returned in ascending order, oldest to newest.</p>"""
    submit_time_after: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Filters the list of classifiers based on the time that the classifier was submitted for processing. Returns only classifiers submitted after the specified time. Classifiers are returned in descending order, newest to oldest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_comprehend.types.model_status

        out["Status"] = capo_comprehend.types.model_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "document_classifier_name" in value:
        out["DocumentClassifierName"] = value["document_classifier_name"]
    if "submit_time_before" in value:
        import capo_comprehend.types.timestamp

        out["SubmitTimeBefore"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["submit_time_before"]
            )
        )
    if "submit_time_after" in value:
        import capo_comprehend.types.timestamp

        out["SubmitTimeAfter"] = capo_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["submit_time_after"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentClassifierFilter:
    out: DocumentClassifierFilter = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_comprehend.types.model_status

        out["status"] = capo_comprehend.types.model_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("DocumentClassifierName") is not None:
        out["document_classifier_name"] = data["DocumentClassifierName"]
    if data.get("SubmitTimeBefore") is not None:
        import capo_comprehend.types.timestamp

        out["submit_time_before"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["SubmitTimeBefore"]
            )
        )
    if data.get("SubmitTimeAfter") is not None:
        import capo_comprehend.types.timestamp

        out["submit_time_after"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["SubmitTimeAfter"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentClassifierFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_comprehend.types.model_status

        out["Status"] = capo_comprehend.types.model_status.serialize_cbor(
            value["status"]
        )
    if "document_classifier_name" in value:
        out["DocumentClassifierName"] = value["document_classifier_name"]
    if "submit_time_before" in value:
        import capo_comprehend.types.timestamp

        out["SubmitTimeBefore"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["submit_time_before"]
        )
    if "submit_time_after" in value:
        import capo_comprehend.types.timestamp

        out["SubmitTimeAfter"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["submit_time_after"]
        )
    return out


def deserialize_cbor(data: dict) -> DocumentClassifierFilter:
    out: DocumentClassifierFilter = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_comprehend.types.model_status

        out["status"] = capo_comprehend.types.model_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("DocumentClassifierName") is not None:
        out["document_classifier_name"] = data["DocumentClassifierName"]
    if data.get("SubmitTimeBefore") is not None:
        import capo_comprehend.types.timestamp

        out["submit_time_before"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["SubmitTimeBefore"]
        )
    if data.get("SubmitTimeAfter") is not None:
        import capo_comprehend.types.timestamp

        out["submit_time_after"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["SubmitTimeAfter"]
        )
    return out
