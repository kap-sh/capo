"""Generated from Smithy shape ``com.amazonaws.sns#PublishBatchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.publish_batch_request_entry_list
    import capo_sns.types.topic_arn


class PublishBatchInput(TypedDict, closed=True):
    topic_arn: "capo_sns.types.topic_arn.topicARN"
    """<p>The Amazon resource name (ARN) of the topic you want to batch publish to.</p>"""
    publish_batch_request_entries: (
        "capo_sns.types.publish_batch_request_entry_list.PublishBatchRequestEntryList"
    )
    """<p>A list of <code>PublishBatch</code> request entries to be sent to the SNS topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PublishBatchInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    import capo_sns.types.publish_batch_request_entry_list

    capo_sns.types.publish_batch_request_entry_list.serialize_query(
        value["publish_batch_request_entries"],
        pairs,
        f"{key_prefix}PublishBatchRequestEntries",
    )


def deserialize_query(el: Element) -> PublishBatchInput:
    out: PublishBatchInput = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    else:
        out["topic_arn"] = ""
    child_publish_batch_request_entries = el.find("PublishBatchRequestEntries")
    if child_publish_batch_request_entries is not None:
        import capo_sns.types.publish_batch_request_entry_list

        out["publish_batch_request_entries"] = (
            capo_sns.types.publish_batch_request_entry_list.deserialize_query(
                child_publish_batch_request_entries
            )
        )
    else:
        out["publish_batch_request_entries"] = []
    return out
