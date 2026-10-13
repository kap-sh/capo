"""Generated from Smithy shape ``com.amazonaws.glue#GetSessionEndpointResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.session_endpoint


class GetSessionEndpointResponse(TypedDict, closed=True):
    spark_connect: "capo_glue.types.session_endpoint.SessionEndpoint"
    """<p>The Spark Connect endpoint details for the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionEndpointResponse) -> dict:
    out: dict = {}
    import capo_glue.types.session_endpoint

    out["SparkConnect"] = capo_glue.types.session_endpoint.serialize_aws_json_1_1(
        value["spark_connect"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionEndpointResponse:
    out: GetSessionEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("SparkConnect") is not None:
        import capo_glue.types.session_endpoint

        out["spark_connect"] = (
            capo_glue.types.session_endpoint.deserialize_aws_json_1_1(
                data["SparkConnect"]
            )
        )
    else:
        raise DeserializationError("GetSessionEndpointResponse.spark_connect required")
    return out


def redact_sensitive(value: GetSessionEndpointResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "spark_connect" in value:
        import capo_glue.types.session_endpoint

        out["spark_connect"] = capo_glue.types.session_endpoint.redact_sensitive(
            value["spark_connect"]
        )
    return out
