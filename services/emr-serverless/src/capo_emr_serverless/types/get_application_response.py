"""Generated from Smithy shape ``com.amazonaws.emrserverless#GetApplicationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_serverless.types.application


class GetApplicationResponse(TypedDict, closed=True):
    application: "capo_emr_serverless.types.application.Application"
    """<p>The output displays information about the specified application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationResponse) -> dict:
    out: dict = {}
    import capo_emr_serverless.types.application

    out["application"] = capo_emr_serverless.types.application.serialize_json(
        value["application"]
    )
    return out


def deserialize_json(data: dict) -> GetApplicationResponse:
    out: GetApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("application") is not None:
        import capo_emr_serverless.types.application

        out["application"] = capo_emr_serverless.types.application.deserialize_json(
            data["application"]
        )
    else:
        raise DeserializationError("GetApplicationResponse.application required")
    return out


def redact_sensitive(value: GetApplicationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "application" in value:
        import capo_emr_serverless.types.application

        out["application"] = capo_emr_serverless.types.application.redact_sensitive(
            value["application"]
        )
    return out
