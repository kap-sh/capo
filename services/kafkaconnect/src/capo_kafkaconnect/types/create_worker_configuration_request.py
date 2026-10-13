"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CreateWorkerConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__sensitive_string
    import capo_kafkaconnect.types.__string_max1024
    import capo_kafkaconnect.types.__string_min1_max128
    import capo_kafkaconnect.types.tags


class CreateWorkerConfigurationRequest(TypedDict, closed=True):
    description: NotRequired["capo_kafkaconnect.types.__string_max1024.__stringMax1024"]
    """<p>A summary description of the worker configuration.</p>"""
    name: "capo_kafkaconnect.types.__string_min1_max128.__stringMin1Max128"
    """<p>The name of the worker configuration.</p>"""
    properties_file_content: (
        "capo_kafkaconnect.types.__sensitive_string.__sensitiveString"
    )
    """<p>Base64 encoded contents of connect-distributed.properties file.</p>"""
    tags: NotRequired["capo_kafkaconnect.types.tags.Tags"]
    """<p>The tags you want to attach to the worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkerConfigurationRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    out["propertiesFileContent"] = value["properties_file_content"]
    if "tags" in value:
        import capo_kafkaconnect.types.tags

        out["tags"] = capo_kafkaconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateWorkerConfigurationRequest:
    out: CreateWorkerConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateWorkerConfigurationRequest.name required")
    if data.get("propertiesFileContent") is not None:
        out["properties_file_content"] = data["propertiesFileContent"]
    else:
        raise DeserializationError(
            "CreateWorkerConfigurationRequest.properties_file_content required"
        )
    if data.get("tags") is not None:
        import capo_kafkaconnect.types.tags

        out["tags"] = capo_kafkaconnect.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateWorkerConfigurationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "properties_file_content" in value:
        out["properties_file_content"] = "*** Sensitive Data Redacted ***"
    return out
