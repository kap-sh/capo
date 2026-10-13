"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#WorkerConfigurationRevisionDescription``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__long
    import capo_kafkaconnect.types.__sensitive_string
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.__timestamp_iso8601


class WorkerConfigurationRevisionDescription(TypedDict, closed=True):
    creation_time: NotRequired[
        "capo_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time that the worker configuration was created.</p>"""
    description: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The description of the worker configuration revision.</p>"""
    properties_file_content: NotRequired[
        "capo_kafkaconnect.types.__sensitive_string.__sensitiveString"
    ]
    """<p>Base64 encoded contents of the connect-distributed.properties file.</p>"""
    revision: "capo_kafkaconnect.types.__long.__long"
    """<p>The description of a revision of the worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerConfigurationRevisionDescription) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "properties_file_content" in value:
        out["propertiesFileContent"] = value["properties_file_content"]
    out["revision"] = value.get("revision", 0)
    return out


def deserialize_json(data: dict) -> WorkerConfigurationRevisionDescription:
    out: WorkerConfigurationRevisionDescription = {}  # type: ignore[typeddict-item]
    if data.get("creationTime") is not None:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("propertiesFileContent") is not None:
        out["properties_file_content"] = data["propertiesFileContent"]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    return out


def redact_sensitive(value: WorkerConfigurationRevisionDescription) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "properties_file_content" in value:
        out["properties_file_content"] = "*** Sensitive Data Redacted ***"
    return out
