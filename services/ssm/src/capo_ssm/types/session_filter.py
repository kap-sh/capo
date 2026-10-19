"""Generated from Smithy shape ``com.amazonaws.ssm#SessionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.session_filter_key
    import capo_ssm.types.session_filter_value


class SessionFilter(TypedDict, closed=True):
    key: "capo_ssm.types.session_filter_key.SessionFilterKey"
    """<p>The name of the filter.</p>"""
    value: "capo_ssm.types.session_filter_value.SessionFilterValue"
    """<p>The filter value. Valid values for each filter key are as follows:</p> <ul> <li> <p>InvokedAfter: Specify a timestamp to limit your results. For example, specify 2024-08-29T00:00:00Z to see sessions that started August 29, 2024, and later.</p> </li> <li> <p>InvokedBefore: Specify a timestamp to limit your results. For example, specify 2024-08-29T00:00:00Z to see sessions that started before August 29, 2024.</p> </li> <li> <p>Target: Specify a managed node to which session connections have been made.</p> </li> <li> <p>Owner: Specify an Amazon Web Services user to see a list of sessions started by that user.</p> </li> <li> <p>Status: Specify a valid session status to see a list of all sessions with that status. Status values you can specify include:</p> <ul> <li> <p>Connected</p> </li> <li> <p>Connecting</p> </li> <li> <p>Disconnected</p> </li> <li> <p>Terminated</p> </li> <li> <p>Terminating</p> </li> <li> <p>Failed</p> </li> </ul> </li> <li> <p>SessionId: Specify a session ID to return details about the session.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.session_filter_key

    out["key"] = capo_ssm.types.session_filter_key.serialize_aws_json_1_1(value["key"])
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionFilter:
    out: SessionFilter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        import capo_ssm.types.session_filter_key

        out["key"] = capo_ssm.types.session_filter_key.deserialize_aws_json_1_1(
            data["key"]
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_ssm.types.session_filter_key.SessionFilterKey", ""
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
