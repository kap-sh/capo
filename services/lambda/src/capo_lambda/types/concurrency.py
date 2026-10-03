"""Generated from Smithy shape ``com.amazonaws.lambda#Concurrency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.reserved_concurrent_executions


class Concurrency(TypedDict, closed=True):
    reserved_concurrent_executions: NotRequired[
        "capo_lambda.types.reserved_concurrent_executions.ReservedConcurrentExecutions"
    ]
    """<p>The number of concurrent executions that are reserved for this function. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html">Managing Lambda reserved concurrency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Concurrency) -> dict:
    out: dict = {}
    if "reserved_concurrent_executions" in value:
        out["ReservedConcurrentExecutions"] = value["reserved_concurrent_executions"]
    return out


def deserialize_json(data: dict) -> Concurrency:
    out: Concurrency = {}  # type: ignore[typeddict-item]
    if data.get("ReservedConcurrentExecutions") is not None:
        out["reserved_concurrent_executions"] = data["ReservedConcurrentExecutions"]
    return out
