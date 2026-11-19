"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_arn_name
    import capo_comprehend.types.model_status
    import capo_comprehend.types.timestamp


class EntityRecognizerFilter(TypedDict, closed=True):
    status: NotRequired["capo_comprehend.types.model_status.ModelStatus"]
    """<p>The status of an entity recognizer.</p>"""
    recognizer_name: NotRequired[
        "capo_comprehend.types.comprehend_arn_name.ComprehendArnName"
    ]
    """<p>The name that you assigned the entity recognizer.</p>"""
    submit_time_before: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Filters the list of entities based on the time that the list was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in descending order, newest to oldest.</p>"""
    submit_time_after: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Filters the list of entities based on the time that the list was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in ascending order, oldest to newest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_comprehend.types.model_status

        out["Status"] = capo_comprehend.types.model_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "recognizer_name" in value:
        out["RecognizerName"] = value["recognizer_name"]
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


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerFilter:
    out: EntityRecognizerFilter = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_comprehend.types.model_status

        out["status"] = capo_comprehend.types.model_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("RecognizerName") is not None:
        out["recognizer_name"] = data["RecognizerName"]
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
def serialize_cbor(value: EntityRecognizerFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_comprehend.types.model_status

        out["Status"] = capo_comprehend.types.model_status.serialize_cbor(
            value["status"]
        )
    if "recognizer_name" in value:
        out["RecognizerName"] = value["recognizer_name"]
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


def deserialize_cbor(data: dict) -> EntityRecognizerFilter:
    out: EntityRecognizerFilter = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_comprehend.types.model_status

        out["status"] = capo_comprehend.types.model_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("RecognizerName") is not None:
        out["recognizer_name"] = data["RecognizerName"]
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
