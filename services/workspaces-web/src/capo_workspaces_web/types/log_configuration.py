"""Generated from Smithy shape ``com.amazonaws.workspacesweb#LogConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.s3_log_configuration


class LogConfiguration(TypedDict, closed=True):
    s3: NotRequired["capo_workspaces_web.types.s3_log_configuration.S3LogConfiguration"]
    """<p>The configuration for delivering the logs to S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogConfiguration) -> dict:
    out: dict = {}
    if "s3" in value:
        import capo_workspaces_web.types.s3_log_configuration

        out["s3"] = capo_workspaces_web.types.s3_log_configuration.serialize_json(
            value["s3"]
        )
    return out


def deserialize_json(data: dict) -> LogConfiguration:
    out: LogConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("s3") is not None:
        import capo_workspaces_web.types.s3_log_configuration

        out["s3"] = capo_workspaces_web.types.s3_log_configuration.deserialize_json(
            data["s3"]
        )
    return out


def redact_sensitive(value: LogConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "s3" in value:
        import capo_workspaces_web.types.s3_log_configuration

        out["s3"] = capo_workspaces_web.types.s3_log_configuration.redact_sensitive(
            value["s3"]
        )
    return out
