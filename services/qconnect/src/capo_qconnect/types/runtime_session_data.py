"""Generated from Smithy shape ``com.amazonaws.qconnect#RuntimeSessionData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_sensitive_string
    import capo_qconnect.types.runtime_session_data_value


class RuntimeSessionData(TypedDict, closed=True):
    key: "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    """<p>The key of the data stored on the session.</p>"""
    value: "capo_qconnect.types.runtime_session_data_value.RuntimeSessionDataValue"
    """<p>The value of the data stored on the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeSessionData) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_qconnect.types.runtime_session_data_value

    out["value"] = capo_qconnect.types.runtime_session_data_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> RuntimeSessionData:
    out: RuntimeSessionData = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        import capo_qconnect.types.runtime_session_data_value

        out["value"] = capo_qconnect.types.runtime_session_data_value.deserialize_json(
            data["value"]
        )
    else:
        import capo_qconnect.types._unknown

        out["value"] = capo_qconnect.types._unknown.UnknownUnionMember("")
    return out


def redact_sensitive(value: RuntimeSessionData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key" in value:
        out["key"] = "*** Sensitive Data Redacted ***"
    if "value" in value:
        import capo_qconnect.types.runtime_session_data_value

        out["value"] = capo_qconnect.types.runtime_session_data_value.redact_sensitive(
            value["value"]
        )
    return out
