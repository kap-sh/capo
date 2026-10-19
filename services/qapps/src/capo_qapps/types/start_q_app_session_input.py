"""Generated from Smithy shape ``com.amazonaws.qapps#StartQAppSessionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.app_version
    import capo_qapps.types.card_value_list
    import capo_qapps.types.instance_id
    import capo_qapps.types.tag_map
    import capo_qapps.types.uuid


class StartQAppSessionInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App to start a session for.</p>"""
    app_version: "capo_qapps.types.app_version.AppVersion"
    """<p>The version of the Q App to use for the session.</p>"""
    initial_values: NotRequired["capo_qapps.types.card_value_list.CardValueList"]
    """<p>Optional initial input values to provide for the Q App session.</p>"""
    session_id: NotRequired["str"]
    """<p>The unique identifier of the a Q App session.</p>"""
    tags: NotRequired["capo_qapps.types.tag_map.TagMap"]
    """<p>Optional tags to associate with the new Q App session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQAppSessionInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appVersion"] = value["app_version"]
    if "initial_values" in value:
        import capo_qapps.types.card_value_list

        out["initialValues"] = capo_qapps.types.card_value_list.serialize_json(
            value["initial_values"]
        )
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "tags" in value:
        import capo_qapps.types.tag_map

        out["tags"] = capo_qapps.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartQAppSessionInput:
    out: StartQAppSessionInput = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        out["app_version"] = 0
    if data.get("initialValues") is not None:
        import capo_qapps.types.card_value_list

        out["initial_values"] = capo_qapps.types.card_value_list.deserialize_json(
            data["initialValues"]
        )
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("tags") is not None:
        import capo_qapps.types.tag_map

        out["tags"] = capo_qapps.types.tag_map.deserialize_json(data["tags"])
    return out
