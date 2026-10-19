"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#QInConnectAssistantConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.q_in_connect_assistant_arn


class QInConnectAssistantConfiguration(TypedDict, closed=True):
    assistant_arn: (
        "capo_lex_models_v2.types.q_in_connect_assistant_arn.QInConnectAssistantARN"
    )
    """<p>The assistant Arn details of the Qinconnect assistant configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QInConnectAssistantConfiguration) -> dict:
    out: dict = {}
    out["assistantArn"] = value["assistant_arn"]
    return out


def deserialize_json(data: dict) -> QInConnectAssistantConfiguration:
    out: QInConnectAssistantConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("assistantArn") is not None:
        out["assistant_arn"] = data["assistantArn"]
    else:
        out["assistant_arn"] = ""
    return out
