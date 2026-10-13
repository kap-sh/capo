"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance


class DescribeAppInstanceResponse(TypedDict, closed=True):
    app_instance: NotRequired["capo_chime_sdk_identity.types.app_instance.AppInstance"]
    """<p>The ARN, metadata, created and last-updated timestamps, and the name of the <code>AppInstance</code>. All timestamps use epoch milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceResponse) -> dict:
    out: dict = {}
    if "app_instance" in value:
        import capo_chime_sdk_identity.types.app_instance

        out["AppInstance"] = capo_chime_sdk_identity.types.app_instance.serialize_json(
            value["app_instance"]
        )
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceResponse:
    out: DescribeAppInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppInstance") is not None:
        import capo_chime_sdk_identity.types.app_instance

        out["app_instance"] = (
            capo_chime_sdk_identity.types.app_instance.deserialize_json(
                data["AppInstance"]
            )
        )
    return out


def redact_sensitive(value: DescribeAppInstanceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_instance" in value:
        import capo_chime_sdk_identity.types.app_instance

        out["app_instance"] = (
            capo_chime_sdk_identity.types.app_instance.redact_sensitive(
                value["app_instance"]
            )
        )
    return out
