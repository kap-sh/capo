"""Generated from Smithy shape ``com.amazonaws.sesv2#SendBulkEmailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.bulk_email_entry_result_list


class SendBulkEmailResponse(TypedDict, closed=True):
    bulk_email_entry_results: (
        "capo_sesv2.types.bulk_email_entry_result_list.BulkEmailEntryResultList"
    )
    """<p>One object per intended recipient. Check each response object and retry any messages with a failure status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendBulkEmailResponse) -> dict:
    out: dict = {}
    import capo_sesv2.types.bulk_email_entry_result_list

    out["BulkEmailEntryResults"] = (
        capo_sesv2.types.bulk_email_entry_result_list.serialize_json(
            value["bulk_email_entry_results"]
        )
    )
    return out


def deserialize_json(data: dict) -> SendBulkEmailResponse:
    out: SendBulkEmailResponse = {}  # type: ignore[typeddict-item]
    if data.get("BulkEmailEntryResults") is not None:
        import capo_sesv2.types.bulk_email_entry_result_list

        out["bulk_email_entry_results"] = (
            capo_sesv2.types.bulk_email_entry_result_list.deserialize_json(
                data["BulkEmailEntryResults"]
            )
        )
    else:
        out["bulk_email_entry_results"] = []
    return out
