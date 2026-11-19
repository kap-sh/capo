"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeEventTopicsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.event_topics


class DescribeEventTopicsResult(TypedDict, closed=True):
    event_topics: NotRequired["capo_directory_service.types.event_topics.EventTopics"]
    """<p>A list of Amazon SNS topic names that receive status messages from the specified Directory ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventTopicsResult) -> dict:
    out: dict = {}
    if "event_topics" in value:
        import capo_directory_service.types.event_topics

        out["EventTopics"] = (
            capo_directory_service.types.event_topics.serialize_aws_json_1_1(
                value["event_topics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventTopicsResult:
    out: DescribeEventTopicsResult = {}  # type: ignore[typeddict-item]
    if data.get("EventTopics") is not None:
        import capo_directory_service.types.event_topics

        out["event_topics"] = (
            capo_directory_service.types.event_topics.deserialize_aws_json_1_1(
                data["EventTopics"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEventTopicsResult) -> dict:
    out: dict = {}
    if "event_topics" in value:
        import capo_directory_service.types.event_topics

        out["EventTopics"] = capo_directory_service.types.event_topics.serialize_cbor(
            value["event_topics"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeEventTopicsResult:
    out: DescribeEventTopicsResult = {}  # type: ignore[typeddict-item]
    if data.get("EventTopics") is not None:
        import capo_directory_service.types.event_topics

        out["event_topics"] = (
            capo_directory_service.types.event_topics.deserialize_cbor(
                data["EventTopics"]
            )
        )
    return out
