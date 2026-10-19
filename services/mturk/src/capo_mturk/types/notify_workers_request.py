"""Generated from Smithy shape ``com.amazonaws.mturk#NotifyWorkersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.customer_id_list
    import capo_mturk.types.string


class NotifyWorkersRequest(TypedDict, closed=True):
    subject: "capo_mturk.types.string.String"
    """<p>The subject line of the email message to send. Can include up to 200 characters.</p>"""
    message_text: "capo_mturk.types.string.String"
    """<p>The text of the email message to send. Can include up to 4,096 characters</p>"""
    worker_ids: "capo_mturk.types.customer_id_list.CustomerIdList"
    """<p>A list of Worker IDs you wish to notify. You can notify upto 100 Workers at a time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyWorkersRequest) -> dict:
    out: dict = {}
    out["Subject"] = value["subject"]
    out["MessageText"] = value["message_text"]
    import capo_mturk.types.customer_id_list

    out["WorkerIds"] = capo_mturk.types.customer_id_list.serialize_aws_json_1_1(
        value["worker_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotifyWorkersRequest:
    out: NotifyWorkersRequest = {}  # type: ignore[typeddict-item]
    if data.get("Subject") is not None:
        out["subject"] = data["Subject"]
    else:
        out["subject"] = ""
    if data.get("MessageText") is not None:
        out["message_text"] = data["MessageText"]
    else:
        out["message_text"] = ""
    if data.get("WorkerIds") is not None:
        import capo_mturk.types.customer_id_list

        out["worker_ids"] = capo_mturk.types.customer_id_list.deserialize_aws_json_1_1(
            data["WorkerIds"]
        )
    else:
        out["worker_ids"] = []
    return out
