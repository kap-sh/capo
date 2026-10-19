"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateSessionDataResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.arn
    import capo_qconnect.types.runtime_session_data_list
    import capo_qconnect.types.session_data_namespace
    import capo_qconnect.types.uuid


class UpdateSessionDataResponse(TypedDict, closed=True):
    session_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    session_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the session.</p>"""
    namespace: "capo_qconnect.types.session_data_namespace.SessionDataNamespace"
    """<p>The namespace into which the session data is stored. Supported namespaces are: Custom</p>"""
    data: "capo_qconnect.types.runtime_session_data_list.RuntimeSessionDataList"
    """<p>Data stored in the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSessionDataResponse) -> dict:
    out: dict = {}
    out["sessionArn"] = value["session_arn"]
    out["sessionId"] = value["session_id"]
    out["namespace"] = value["namespace"]
    import capo_qconnect.types.runtime_session_data_list

    out["data"] = capo_qconnect.types.runtime_session_data_list.serialize_json(
        value["data"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSessionDataResponse:
    out: UpdateSessionDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        out["namespace"] = ""
    if data.get("data") is not None:
        import capo_qconnect.types.runtime_session_data_list

        out["data"] = capo_qconnect.types.runtime_session_data_list.deserialize_json(
            data["data"]
        )
    else:
        out["data"] = []
    return out


def redact_sensitive(value: UpdateSessionDataResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data" in value:
        import capo_qconnect.types.runtime_session_data_list

        out["data"] = capo_qconnect.types.runtime_session_data_list.redact_sensitive(
            value["data"]
        )
    return out
