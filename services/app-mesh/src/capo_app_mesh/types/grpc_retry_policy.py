"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcRetryPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.duration
    import capo_app_mesh.types.grpc_retry_policy_events
    import capo_app_mesh.types.http_retry_policy_events
    import capo_app_mesh.types.max_retries
    import capo_app_mesh.types.tcp_retry_policy_events


class GrpcRetryPolicy(TypedDict, closed=True):
    per_retry_timeout: "capo_app_mesh.types.duration.Duration"
    """<p>The timeout for each retry attempt.</p>"""
    max_retries: "capo_app_mesh.types.max_retries.MaxRetries"
    """<p>The maximum number of retry attempts.</p>"""
    http_retry_events: NotRequired[
        "capo_app_mesh.types.http_retry_policy_events.HttpRetryPolicyEvents"
    ]
    """<p>Specify at least one of the following values.</p> <ul> <li> <p> <b>server-error</b> – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511</p> </li> <li> <p> <b>gateway-error</b> – HTTP status codes 502, 503, and 504</p> </li> <li> <p> <b>client-error</b> – HTTP status code 409</p> </li> <li> <p> <b>stream-error</b> – Retry on refused stream</p> </li> </ul>"""
    tcp_retry_events: NotRequired[
        "capo_app_mesh.types.tcp_retry_policy_events.TcpRetryPolicyEvents"
    ]
    """<p>Specify a valid value. The event occurs before any processing of a request has started and is encountered when the upstream is temporarily or permanently unavailable.</p>"""
    grpc_retry_events: NotRequired[
        "capo_app_mesh.types.grpc_retry_policy_events.GrpcRetryPolicyEvents"
    ]
    """<p>Specify at least one of the valid values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrpcRetryPolicy) -> dict:
    out: dict = {}
    import capo_app_mesh.types.duration

    out["perRetryTimeout"] = capo_app_mesh.types.duration.serialize_json(
        value["per_retry_timeout"]
    )
    out["maxRetries"] = value["max_retries"]
    if "http_retry_events" in value:
        import capo_app_mesh.types.http_retry_policy_events

        out["httpRetryEvents"] = (
            capo_app_mesh.types.http_retry_policy_events.serialize_json(
                value["http_retry_events"]
            )
        )
    if "tcp_retry_events" in value:
        import capo_app_mesh.types.tcp_retry_policy_events

        out["tcpRetryEvents"] = (
            capo_app_mesh.types.tcp_retry_policy_events.serialize_json(
                value["tcp_retry_events"]
            )
        )
    if "grpc_retry_events" in value:
        import capo_app_mesh.types.grpc_retry_policy_events

        out["grpcRetryEvents"] = (
            capo_app_mesh.types.grpc_retry_policy_events.serialize_json(
                value["grpc_retry_events"]
            )
        )
    return out


def deserialize_json(data: dict) -> GrpcRetryPolicy:
    out: GrpcRetryPolicy = {}  # type: ignore[typeddict-item]
    if data.get("perRetryTimeout") is not None:
        import capo_app_mesh.types.duration

        out["per_retry_timeout"] = capo_app_mesh.types.duration.deserialize_json(
            data["perRetryTimeout"]
        )
    else:
        raise DeserializationError("GrpcRetryPolicy.per_retry_timeout required")
    if data.get("maxRetries") is not None:
        out["max_retries"] = data["maxRetries"]
    else:
        out["max_retries"] = 0
    if data.get("httpRetryEvents") is not None:
        import capo_app_mesh.types.http_retry_policy_events

        out["http_retry_events"] = (
            capo_app_mesh.types.http_retry_policy_events.deserialize_json(
                data["httpRetryEvents"]
            )
        )
    if data.get("tcpRetryEvents") is not None:
        import capo_app_mesh.types.tcp_retry_policy_events

        out["tcp_retry_events"] = (
            capo_app_mesh.types.tcp_retry_policy_events.deserialize_json(
                data["tcpRetryEvents"]
            )
        )
    if data.get("grpcRetryEvents") is not None:
        import capo_app_mesh.types.grpc_retry_policy_events

        out["grpc_retry_events"] = (
            capo_app_mesh.types.grpc_retry_policy_events.deserialize_json(
                data["grpcRetryEvents"]
            )
        )
    return out
