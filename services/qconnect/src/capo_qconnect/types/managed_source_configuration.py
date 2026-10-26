"""Generated from Smithy shape ``com.amazonaws.qconnect#ManagedSourceConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.web_crawler_configuration


class _ManagedSourceConfiguration_webCrawlerConfiguration(TypedDict, closed=True):
    webCrawlerConfiguration: (
        "capo_qconnect.types.web_crawler_configuration.WebCrawlerConfiguration"
    )


ManagedSourceConfiguration: TypeAlias = (
    _ManagedSourceConfiguration_webCrawlerConfiguration | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ManagedSourceConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ManagedSourceConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "webCrawlerConfiguration" in value:
        import capo_qconnect.types.web_crawler_configuration

        return {
            "webCrawlerConfiguration": capo_qconnect.types.web_crawler_configuration.serialize_json(
                value["webCrawlerConfiguration"]
            )
        }
    else:
        raise SerializationError("ManagedSourceConfiguration: no variant present")


def deserialize_json(data: dict) -> ManagedSourceConfiguration:
    if data.get("webCrawlerConfiguration") is not None:
        import capo_qconnect.types.web_crawler_configuration

        return {
            "webCrawlerConfiguration": capo_qconnect.types.web_crawler_configuration.deserialize_json(
                data["webCrawlerConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ManagedSourceConfiguration: no recognized variant key"
        )


def redact_sensitive(value: ManagedSourceConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "webCrawlerConfiguration" in value:
        import capo_qconnect.types.web_crawler_configuration

        out["webCrawlerConfiguration"] = (
            capo_qconnect.types.web_crawler_configuration.redact_sensitive(
                value["webCrawlerConfiguration"]
            )
        )
    return out
