"""Generated from Smithy shape ``com.amazonaws.location#JobError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.job_error_code
    import capo_location.types.job_error_messages_list


class JobError(TypedDict, closed=True):
    code: "capo_location.types.job_error_code.JobErrorCode"
    """<p>Error code indicating the type of error that occurred.</p>"""
    messages: NotRequired[
        "capo_location.types.job_error_messages_list.JobErrorMessagesList"
    ]
    """<p>Error messages providing details about the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobError) -> dict:
    out: dict = {}
    out["Code"] = value["code"]
    if "messages" in value:
        import capo_location.types.job_error_messages_list

        out["Messages"] = capo_location.types.job_error_messages_list.serialize_json(
            value["messages"]
        )
    return out


def deserialize_json(data: dict) -> JobError:
    out: JobError = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    else:
        out["code"] = ""
    if data.get("Messages") is not None:
        import capo_location.types.job_error_messages_list

        out["messages"] = capo_location.types.job_error_messages_list.deserialize_json(
            data["Messages"]
        )
    return out
