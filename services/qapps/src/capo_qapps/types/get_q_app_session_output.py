"""Generated from Smithy shape ``com.amazonaws.qapps#GetQAppSessionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.app_version
    import capo_qapps.types.card_status_map
    import capo_qapps.types.execution_status
    import capo_qapps.types.session_name


class GetQAppSessionOutput(TypedDict, closed=True):
    session_id: "str"
    """<p>The unique identifier of the Q App session.</p>"""
    session_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the Q App session.</p>"""
    session_name: NotRequired["capo_qapps.types.session_name.SessionName"]
    """<p>The name of the Q App session.</p>"""
    app_version: NotRequired["capo_qapps.types.app_version.AppVersion"]
    """<p>The version of the Q App used for the session.</p>"""
    latest_published_app_version: NotRequired["capo_qapps.types.app_version.AppVersion"]
    """<p>The latest published version of the Q App used for the session.</p>"""
    status: "capo_qapps.types.execution_status.ExecutionStatus"
    """<p>The current status of the Q App session.</p>"""
    card_status: "capo_qapps.types.card_status_map.CardStatusMap"
    """<p>The current status for each card in the Q App session.</p>"""
    user_is_host: NotRequired["bool"]
    """<p>Indicates whether the current user is the owner of the Q App data collection session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQAppSessionOutput) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["sessionArn"] = value["session_arn"]
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    if "app_version" in value:
        out["appVersion"] = value["app_version"]
    if "latest_published_app_version" in value:
        out["latestPublishedAppVersion"] = value["latest_published_app_version"]
    import capo_qapps.types.execution_status

    out["status"] = capo_qapps.types.execution_status.serialize_json(value["status"])
    import capo_qapps.types.card_status_map

    out["cardStatus"] = capo_qapps.types.card_status_map.serialize_json(
        value["card_status"]
    )
    if "user_is_host" in value:
        out["userIsHost"] = value["user_is_host"]
    return out


def deserialize_json(data: dict) -> GetQAppSessionOutput:
    out: GetQAppSessionOutput = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    if data.get("sessionName") is not None:
        out["session_name"] = data["sessionName"]
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    if data.get("latestPublishedAppVersion") is not None:
        out["latest_published_app_version"] = data["latestPublishedAppVersion"]
    if data.get("status") is not None:
        import capo_qapps.types.execution_status

        out["status"] = capo_qapps.types.execution_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_qapps.types.execution_status.ExecutionStatus", ""
        )
    if data.get("cardStatus") is not None:
        import capo_qapps.types.card_status_map

        out["card_status"] = capo_qapps.types.card_status_map.deserialize_json(
            data["cardStatus"]
        )
    else:
        out["card_status"] = {}
    if data.get("userIsHost") is not None:
        out["user_is_host"] = data["userIsHost"]
    return out
