"""Generated from Smithy shape ``com.amazonaws.glue#GetDashboardUrlResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.sensitive_url


class GetDashboardUrlResponse(TypedDict, closed=True):
    url: "capo_glue.types.sensitive_url.SensitiveUrl"
    """<p>The URL for the Spark monitoring dashboard.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDashboardUrlResponse) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDashboardUrlResponse:
    out: GetDashboardUrlResponse = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        out["url"] = ""
    return out


def redact_sensitive(value: GetDashboardUrlResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
