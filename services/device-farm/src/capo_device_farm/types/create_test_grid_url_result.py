"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateTestGridUrlResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.date_time
    import capo_device_farm.types.sensitive_string


class CreateTestGridUrlResult(TypedDict, closed=True):
    url: NotRequired["capo_device_farm.types.sensitive_string.SensitiveString"]
    """<p>A signed URL, expiring in the time specified by the <code>CreateTestGridUrlRequest</code>, to be passed to a <code>RemoteWebDriver</code>. </p>"""
    expires: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>The number of seconds the URL stays active from creation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTestGridUrlResult) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    if "expires" in value:
        import capo_device_farm.types.date_time

        out["expires"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["expires"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTestGridUrlResult:
    out: CreateTestGridUrlResult = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("expires") is not None:
        import capo_device_farm.types.date_time

        out["expires"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["expires"]
        )
    return out


def redact_sensitive(value: CreateTestGridUrlResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
