"""Generated from Smithy shape ``com.amazonaws.lambda#SelfManagedEventSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.endpoints


class SelfManagedEventSource(TypedDict, closed=True):
    endpoints: NotRequired["capo_lambda.types.endpoints.Endpoints"]
    """<p>The list of bootstrap servers for your Kafka brokers in the following format: <code>"KAFKA_BOOTSTRAP_SERVERS": ["abc.xyz.com:xxxx","abc2.xyz.com:xxxx"]</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedEventSource) -> dict:
    out: dict = {}
    if "endpoints" in value:
        import capo_lambda.types.endpoints

        out["Endpoints"] = capo_lambda.types.endpoints.serialize_json(
            value["endpoints"]
        )
    return out


def deserialize_json(data: dict) -> SelfManagedEventSource:
    out: SelfManagedEventSource = {}  # type: ignore[typeddict-item]
    if data.get("Endpoints") is not None:
        import capo_lambda.types.endpoints

        out["endpoints"] = capo_lambda.types.endpoints.deserialize_json(
            data["Endpoints"]
        )
    return out
